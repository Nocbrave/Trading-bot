# Trading-bot
A simple  automated trading bot that executes trades based on predefined strategies and market conditions.
-------------------------

Please note that To use the code, make sure you have the ccxt library installed. You can install it using the following command:
```
pip install ccxt
```

In the python code, i created a TradingBot object, connect to the Binance exchange using API keys, and specify the symbol (BTC/USDT). We then run the strategy, which fetches recent candlestick data, calculates the SMA, and executes a buy or sell order based on the predefined conditions.


 -  ``` __init__ ```: Initializes the bot with the exchange and symbol.
 -  ``` get_recent_candles```: Fetches recent candlestick data for the specified symbol and timeframe.
 -  ```calculate_sma```: Calculates the Simple Moving Average (SMA) based on the candlestick data.
 -  ```execute_trade```: Executes a market order for the specified symbol and side (buy or sell) with the specified quantity.
 -  ```run_strategy```: Implements the trading strategy based on predefined conditions (in this example, a simple SMA crossover strategy).
   
