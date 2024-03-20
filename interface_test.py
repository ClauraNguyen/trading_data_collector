import json
from trading_interface import *
from infrastructure.collect_candle import run_collect


def load_config(path, sector):
    filename = f"{path}/config.json"
    with open(filename,"r") as f:
        config = {}
        data = json.loads(f.read())
        for k, v in data[sector].items():
            config[k]= v
        f.close()
    return config


def run():
    authority = load_config(".","mt5")    
    api = MT5(**authority)
    data = load_config(".","data")
    output = load_config(".","output")
    run_collect(** data, output=output, api=api)
    

if __name__ == "__main__":
    run()

