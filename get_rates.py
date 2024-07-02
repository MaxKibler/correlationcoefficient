import pandas as pd
from datetime import datetime, timedelta
import MetaTrader5 as mt5
import pytz

class GetRates:

    def __init__(self):

        mt5.initialize()
        #enter credentials
        mt5.login(login=, password='', server='')
        self.local_tz = pytz.timezone('EET')
        self.utc_offset = timedelta(hours=-3)
        self.timeframe = mt5.TIMEFRAME_M1

    def get_rates(self, symbol):
        from_date_local = datetime.now(self.local_tz)
        from_date = from_date_local - self.utc_offset
        ticks = mt5.symbol_info(symbol)
        ticks_frame = pd.DataFrame(ticks)
        return ticks
