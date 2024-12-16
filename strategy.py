import numpy as np
import talib

def calculate_ma(data, window):
    # Проверяем, что данные не пусты
     if data is None or len(data) == 0:
        return None

     close_prices = data['close'].values
     return talib.SMA(close_prices, timeperiod=window)

def calculate_rsi(data, period):
     if data is None or len(data) == 0:
         return None
     close_prices = data['close'].values
     return talib.RSI(close_prices, timeperiod=period)

def generate_signals(data, ma_fast, ma_slow, rsi_overbought, rsi_oversold, rsi_period):
      ma_fast_values = calculate_ma(data, ma_fast)
      ma_slow_values = calculate_ma(data, ma_slow)
      rsi_values = calculate_rsi(data, rsi_period)
      if ma_fast_values is None or ma_slow_values is None or rsi_values is None:
        return None
      signals = []
      for i in range(len(data)):
            signal = 0 #по умолчанию не делаем ничего
            if ma_fast_values[i] > ma_slow_values[i] and rsi_values[i] < rsi_oversold:
                signal = 1 #buy
            if ma_fast_values[i] < ma_slow_values[i] and rsi_values[i] > rsi_overbought:
                signal = 2 #sell
            signals.append(signal)
      return signals
