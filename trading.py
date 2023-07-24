import ccxt

class TradingBot:
    def __init__(self, exchange, symbol):
        self.exchange = exchange
        self.symbol = symbol

    def get_recent_candles(self, timeframe, limit):
        try:
            candles = self.exchange.fetch_ohlcv(self.symbol, timeframe=timeframe, limit=limit)
            return candles
        except ccxt.ExchangeError as e:
            print("Error fetching candles:", e)
            return []

    def calculate_sma(self, candles, period):
        closes = [candle[4] for candle in candles]
        sma = sum(closes[-period:]) / period
        return sma

    def execute_trade(self, side, quantity):
        try:
            order = self.exchange.create_market_order(symbol=self.symbol, side=side, quantity=quantity)
            print("Trade executed successfully.")
            return order
        except ccxt.ExchangeError as e:
            print("Error executing trade:", e)
            return None

    def run_strategy(self):
        # Fetch recent candles:
        candles = self.get_recent_candles("1h", 20)

        if not candles:
            return

        # Calculate Simple Moving Average (SMA)
        sma = self.calculate_sma(candles, 10)

        # Implement strategy logic
        current_price = candles[-1][4]
        last_price = candles[-2][4]

        if current_price > sma and last_price < sma:
            # Place a buy order
            order = self.execute_trade("buy", 0.1)
            if order:
                # Set stop-loss at 2% below entry price
                stop_loss_price = order['price'] * 0.98
                print("Stop-loss set at:", stop_loss_price)

        elif current_price < sma and last_price > sma:
            # Place a sell order
            order = self.execute_trade("sell", 0.1)
            if order:
                # Set take-profit at 2% above entry price
                take_profit_price = order['price'] * 1.02
                print("Take-profit set at:", take_profit_price)

# Example usage:
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_API_SECRET',
    'enableRateLimit': True
})

symbol = 'BTC/USDT'

bot = TradingBot(exchange, symbol)
bot.run_strategy()
