from ligo.scald.io import influx
from ligo.scald import utils
import pandas as pd
import configparser

class CalFetcher:

    def __init__(self, config_file):
   
        # initialize backend
        backend = self._init_backend(config_file)
        self.backend = backend
        self.consumer = influx.Consumer(hostname=backend['hostname'], db=backend['db'],
                                        auth=backend['auth'], https=backend['https'],
                                        check_certs=backend['check_certs'])

    def _init_backend(self, config_file):

        config = configparser.ConfigParser()

        # Read backend
        config.read(config_file)

        # Backend will contain hostname and db
        backend = config['Backend']
        
        # Convert to dict so we can store bools
        backend = dict(backend)
        backend['auth'] = config.getboolean('Backend', 'auth')
        backend['https'] = config.getboolean('Backend', 'https')
        backend['check_certs'] = config.getboolean('Backend', 'check_certs')
        return backend

    def _format_influx_query(self, gps_start_time, gps_end_time, meas, fields, conditions=None):

        # Format measurements
        meas = ['"{item}"'.format(item=item) for item in meas]

        # Filter on GPS times
        # FIXME: a little clunky right now
        time_range = influx._format_influxql_conditions(start=gps_start_time, end=gps_end_time)
        if conditions is not None:
            conditions_suffix = ' AND '.join(conditions)
            all_conditions = time_range + ' AND ' + conditions_suffix
        else:
            all_conditions = time_range
        query = 'SELECT ' + ', '.join(fields) + ' FROM ' + ', '.join(meas) + ' {conditions}'.format(meas=meas, conditions=all_conditions)

        return query

    def fetch_data(self, gps_start_time, gps_end_time, meas, fields, conditions=None):
        """
        Fetches data from influxDB for a given time range, measurement, and associated fields.

        Parameters
        ----------
        gps_start_time: int
            Starting GPS time of the desired data segment
        gps_end_time: int
            Ending GPS time of the desired data segment
        meas: str
            Name of measurement to pull data for ('TF_mag', 'TF_phase', etc.). Must be an existing measurement 
            in the database specified during configuration.
        fields: str or list
            Name or names of fields associated with measurement meas to pull from influxDB. Field keys must be 
            associated with meas.
        conditions: str or list
            List of additional filters/conditions to apply to query. NOTE: STRINGS MUST BE PASSED AS TRIPLE QUOTE STRINGS 
            TO ACCORD WITH INFLUXDB FORMATTING.

        Returns
        -------
        dataframe: Pandas DataFrame
            Pandas DataFrame object with fields and meas as columns and time values as rows.
        """

        # Generate query
        query = self._format_influx_query(gps_start_time, gps_end_time, meas, fields, conditions=conditions)

        cols, data = influx._query_influx_data(self.consumer.client, self.backend['db'], query)

        # Construct pandasDF
        dataframe = pd.DataFrame(data, columns=cols)

        if 'oscillator_frequency' in dataframe.columns:
            dataframe['oscillator_frequency'].replace({'_':'.'}, inplace=True, regex=True)
            dataframe['oscillator_frequency'] = pd.to_numeric(dataframe['oscillator_frequency'])

        return dataframe

