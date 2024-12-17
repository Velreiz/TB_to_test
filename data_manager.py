import MetaTrader5 as mt5
import pandas as pd
import numpy as np

def initialize_mt5(server, login, password):
    if not mt5.initialize():
         print("initialize() failed")
         mt5.shutdown()
         return False
    if not mt5.login(login, password, server):
          print(f'Не удалось подключиться к MT5, login:{login}')
          mt5.shutdown()
          return False
    return True

def get_quotes(symbol, timeframe, count):
       rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, count) #получаем данные от mt5
       if rates is None or len(rates) == 0:
           return None
       df = pd.DataFrame(rates) #преобразуем данные в pandas
       df['time'] = pd.to_datetime(df['time'], unit='s') #конвертируем время
       df.set_index('time',inplace = True) #устанавливаем время в качестве индекса
       return df
   
def get_account_info():
         account = mt5.account_info() #получаем инфо о счете
         if account is None:
          return None
         return  {
                    'balance': account.balance,
                    'equity' : account.equity,
                    'margin': account.margin
                    }