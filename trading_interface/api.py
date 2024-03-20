import datetime as dt
import pandas as pd
from .trading_interface import TradingInterface

class Api(TradingInterface):
    def __init__(self):
        super().__init__()
    
    def make_request(self):
        pass
    
    
    def get_account_instruments(self):
        return super().get_account_instruments()
    

    def get_account_instruments_df(self) -> pd.DataFrame:
        return super().get_account_instruments_df()
    

    def get_candles(self):
        return super().get_candles()
    
    
    def get_candles_df(self, symbol, date_f: dt.datetime, date_t: dt.datetime, granularity) -> pd.DataFrame:
        return super().get_candles_df(symbol, date_f, date_t, granularity)