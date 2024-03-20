import pandas as pd
import time
import datetime as dt
from dateutil.parser import parse
from trading_interface import *


def save_data(format, destination, df: pd.DataFrame, filename):
    file_path = f"{destination}/{filename}"
    if format == "pickle":
        df.to_pickle(f"{file_path}.pkl")        
    elif format == "csv":
        df.to_csv(f"{file_path}.csv")        
    elif format == "json":
        df.to_json(f"{file_path}.json")
    else:
        print("\nWrong output format, please adjust config file")
        pass
    print(f"***Saved {filename} to {destination}***")
        

def fetch_candle(symbol, date_f, date_t, timeframe, api: TradingInterface):   
    candles = api.get_candles_df(symbol, date_f, date_t, timeframe)
    str = f"Loading candles of {symbol} in {timeframe} from {date_f} to {date_t}"
    print (f"\n{str} --> {candles.shape[0]} candles loaded")
    return candles


def run_collect(symbols, timeframes, start_date, end_date, output, api: TradingInterface):
    date_f = parse(start_date)
    if end_date == "":
        date_t = dt.datetime.utcnow()
    else:
        date_t = parse(end_date)
    for symbol in symbols:
        for timeframe in timeframes:
            filename = f"{symbol}_{timeframe}"
            df = fetch_candle(symbol, date_f, date_t, timeframe, api)        
            save_data(**output, df=df, filename=filename)
            time.sleep(10)
    print("---> FINISHED <---")