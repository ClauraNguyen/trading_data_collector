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

def load_interface():
    interface = input("Which source do you want to retrieve data from? (MT5/OpenFX/OANDA): ")
    while interface not in ["MT5", "OpenFX", "OANDA"]:
        interface = input("Please type again. Source must be one in MT5/OpenFX/OANDA: ")
    authority = load_config(".",f"{interface}") 
    if interface == "MT5":
        api = MT5(**authority)
    elif interface == "OpenFX":
        api = ApiOpenFx(**authority)
    elif interface == "OANDA":
        api = ApiOanda(**authority)
    return api

def check_requirement(symbols, timeframes, start_date, end_date, format, destination):
    agree = input(f"\nDo you really want to collect: "
                f"\n - List of symbols: {symbols},"
                f"\n - With list of timeframes: {timeframes},"
                f"\n - From {start_date} to {end_date}"
                f"\n - To {format} file in {destination}? (y/n):")
    while agree not in ["y", "n"]:
        agree = input("\nPlease select:"
                      '\n - "y" if you agree with the configuration,'
                      '\n - "n" if the configuration does not meet your requirements:')
    
    return agree
    
def run():
    api = load_interface()
    data = load_config(".","data")
    output = load_config(".","output")    
    agree = check_requirement (**data, **output)
    
    if agree == "n":
        print("\nPlease reset the config.json file with your requirements and run again.")
        pass
    elif agree == "y":
        run_collect(**data, output=output, api=api)

if __name__ == "__main__":
    run()