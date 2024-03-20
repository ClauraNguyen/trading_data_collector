import pandas as pd
import datetime as dt

class TradingInterface:
    """The class for all trading interface, get and make request with brokers"""
    def __init__(self):
        return None

    
    def get_account_summary(self):
        return None

    
    def get_account_instruments(self) :
        return None           

    
    def get_account_instruments_df(self) -> pd.DataFrame:        
        instrumnents = self.get_account_instruments()
        
        attributes = dir(instrumnents[0]) 
        attributes = [attr for attr in attributes if not attr.startswith('_')]
        instruments_dict = {}        

        for i in instrumnents:
            key = i.name
            instruments_dict[key] = {k: getattr(i,k) for k in attributes}
        df_instruments = pd.DataFrame.from_dict(instruments_dict, orient='index')
        for k in ['name','Symbol', 'pairname']:
            if k in df_instruments.columns:
                df_instruments['symbol'] = df_instruments[f"{k}"]            
        return df_instruments
    
    
    def get_candles(self):
        return None

    
    def get_candles_df(self, symbol, date_f: dt.datetime, date_t:dt.datetime, granularity) -> pd.DataFrame:
        candles = self.get_candles(symbol, date_f, date_t, granularity)
        df_candles = pd.DataFrame(candles)
        return df_candles