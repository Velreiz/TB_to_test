import config
import data_manager
import strategy
import trader
import utils
import time
from datetime import datetime
import MetaTrader5 as mt5

logger = utils.setup_logger('bot', 'log/bot.log') #создаем логгер

def main():
   utils.log_message(logger, logging.INFO, "Starting bot") #записываем в лог
   if not data_manager.initialize_mt5(config.SERVER,config.LOGIN, config.PASSWORD): #инициализируем mt5
      utils.log_message(logger,logging.ERROR,"Can't connect to MT5")
      return False

   while True:
      for symbol in config.SYMBOLS: #торгуем по каждому символу
        data = data_manager.get_quotes(symbol, mt5.TIMEFRAME_M15, 100) #получаем исторические данные
        if data is not None:
            signals = strategy.generate_signals(data, config.MA_FAST, config.MA_SLOW, config.RSI_OVERBOUGHT, config.RSI_OVERSOLD, 14) #генерируем сигналы
            if signals is not None and len(signals) > 0:
               if signals[-1] == 1:
                   utils.log_message(logger,logging.INFO, f"Buy signal for {symbol} at {datetime.now()}")
                   trader.execute_order(symbol, mt5.ORDER_TYPE_BUY, config.POSITION_SIZE, mt5.symbol_info_tick(symbol).ask, 12345, 3, 0, 0)
               if signals[-1] == 2:
                   utils.log_message(logger,logging.INFO, f"Sell signal for {symbol} at {datetime.now()}")
                   trader.execute_order(symbol, mt5.ORDER_TYPE_SELL, config.POSITION_SIZE, mt5.symbol_info_tick(symbol).bid, 12345, 3, 0, 0)
            else:
                utils.log_message(logger,logging.WARNING, f"Signals are None or empty for {symbol} at {datetime.now()}")

        else:
            utils.log_message(logger,logging.ERROR, f"Can't get quotes for {symbol} at {datetime.now()}")

      time.sleep(60) #спим минуту

if __name__ == "__main__":
   main()