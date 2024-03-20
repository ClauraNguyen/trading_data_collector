# This is the MT5 class for making intergral from MT5 requests with internal projects

import MetaTrader5 as mt
import datetime as dt
import pandas as pd
from .trading_interface import TradingInterface


GRANURITY_MAPPING = {
        "M15": mt.TIMEFRAME_M15,
        "H1": mt.TIMEFRAME_H1,
        "H4": mt.TIMEFRAME_H4,
        "D1": mt.TIMEFRAME_D1
    }


class MT5(TradingInterface):
    
    def __init__(self, login, server, password):
        #local_dir = os.path.dirname(__file__)
        if not mt.initialize(login=login, server=server,password=password):
            print(f"\nCan't connect with mt5, errors: {mt.last_error()}")
            mt.shutdown()
        else:
            print("\nConnect with mt5 successful")
   
    
    def get_account_instruments(self):
        return mt.symbols_get()

    
    def get_account_instruments_df(self) -> pd.DataFrame:
        return super().get_account_instruments_df()
    
    
    def get_candles(self, symbol, date_f, date_t, granularity):        
        if granularity not in GRANURITY_MAPPING.keys():
            raise ValueError("Invalid granularity. Must be one of: {}".format(GRANURITY_MAPPING.keys()))
        
        candle = mt.copy_rates_range(symbol, GRANURITY_MAPPING.get(granularity),date_f,date_t)
        return candle

    
    def get_candles_df(self, symbol, date_f: dt.datetime, date_t: dt.datetime, granularity) -> pd.DataFrame:
        """Return OHLC, Volume and Spread of Symbol with DataFrame form,
        save it if nead."""
        df_candles = super().get_candles_df(symbol, date_f, date_t, granularity)
        df_candles['time'] = pd.to_datetime(df_candles['time'], unit='s')
        return df_candles