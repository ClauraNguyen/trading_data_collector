# Trading Data Collector

This project aims to collect trading data from various trading interfaces such as the MetaTrader 5 (MT5) platform, OpenFX API, and OANDA API. The collected data can be used for analysis, backtesting trading strategies, and generating insights into financial markets.

## Features

- **Data Collection**: Retrieve historical and real-time trading data from multiple sources.
- **Flexibility**: Compatible with MT5 platform, OpenFX API, and OANDA API, allowing for diverse data collection options.
- **Customization**: Easily configurable to collect specific data types and timeframes.
- **Export**: Export data to various formats for further analysis or integration with other systems.

## Installation

1. Clone the repository:
```git clone https://github.com/yourusername/trading-data-collector.git```


2. Install dependencies: 
```pip install -r requirements.txt```

## Usage

1. Configure the settings in `config.json` file according to your preferences.
2. Run the main script: ```python main.py```
4. Follow the prompts to start collecting data.

## Configuration

In the `config.json` file, you can specify various settings including:

- API credentials for MT5, OpenFX, and OANDA.
- Data collection parameters such as instruments, timeframes, and date ranges.
  + `end_date` parameters will receive utc present time if it is emtry string 
- Output format and destination for collected data.

Example `config.json`:

```json
{
  "mt5": {
    "server": "demo",
    "account": "123456",
    "password": "your_password"
  },
  "openfx": {
    "api_key": "your_api_key",
    "secret_key": "your_secret_key"
  },
  "oanda": {
    "api_key": "your_api_key",
    "account_id": "your_account_id"
  },
  "data": {
    "instruments": ["EURUSD", "GBPUSD"],
    "timeframes": ["M1", "H1", "D1"],
    "start_date": "2022-01-01",
    "end_date": "2022-12-31"
  },
  "output": {
    "format": "csv",
    "destination": "./data"
  }
}
```
## Contributing

Contributions are welcome! If you have any ideas for improvements or find any issues, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Thanks to the developers of MetaTrader 5, OpenFX API, and OANDA API for providing access to trading data.
Inspiration for this project came from the need to easily collect and analyze trading data for research and strategy development purposes.

Feel free to customize it further based on your specific project requirements and guidelines.
