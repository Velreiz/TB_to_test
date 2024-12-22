import data_manager
import strategy
import trader
import config
import MetaTrader5 as mt5
import pytest
def test_initialize_mt5():
   assert data_manager.initialize_mt5("demo", 12345, "password") == False #проверяем на неправильные данные
   assert data_manager.initialize_mt5("real", 12345, "password") == False
def test_get_quotes():
   data = data_manager.get_quotes('EURUSD',mt5.TIMEFRAME_M15,100)
   assert data is not None #проверяем, что данные не пустые
def test_calculate_ma():
   data = data_manager.get_quotes('EURUSD',mt5.TIMEFRAME_M15,100)
   if data is not None:
     ma_values = strategy.calculate_ma(data, config.MA_FAST)
     assert ma_values is not None
def test_calculate_rsi():
   data = data_manager.get_quotes('EURUSD',mt5.TIMEFRAME_M15,100)
   if data is not None:
     rsi_values = strategy.calculate_rsi(data, 14)
     assert rsi_values is not None
def test_generate_signals():
  data = data_manager.get_quotes('EURUSD',mt5.TIMEFRAME_M15,100)
  if data is not None:
     signals = strategy.generate_signals(data,config.MA_FAST, config.MA_SLOW, config.RSI_OVERBOUGHT, config.RSI_OVERSOLD, 14)
     assert signals is not None
     assert len(signals) > 0
def test_execute_order():
    assert trader.execute_order("EURUSD",mt5.ORDER_TYPE_BUY, 0.1, 1.1000, 12345, 3, 0, 0) == False