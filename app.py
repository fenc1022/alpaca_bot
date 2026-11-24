import alpaca_markets as alpaca
import datetime

symbols = ["AAPL", "NVDA"]
max_number_of_candles = 1000
timeframe = "1hour"

def auto_run_trading_bot():
    """
    Function to run the trading bot
    """
    print("Welcome to your very own trading bot")

    end_date = datetime.datetime.now() - datetime.timedelta(days=1)
    start_date = end_date - datetime.timedelta(days=365)

    for symbol in symbols:
        symbol_text = symbol
        symbol = [symbol]
        symbol_historical_data = alpaca.get_historic_bars(
            symbols=symbol,
            timeframe=timeframe,
            start_date=start_date,
            end_date=end_date,
            limit=max_number_of_candles
        )

        print(symbol_historical_data)

if __name__ == '__main__':
    auto_run_trading_bot()