import MetaTrader5 as mt5
def execute_order(symbol, order_type, volume, price, magic_number, slippage, stop_loss, take_profit):
   request = {
           "action": mt5.TRADE_ACTION_DEAL,
           "symbol": symbol,
           "type": order_type,
           "volume": volume,
           "price": price,
           "magic": magic_number,
           "sl": stop_loss,
           "tp": take_profit,
           "deviation": slippage
           }
   result = mt5.order_send(request) #размещение ордера
   if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:
          print(f"Ошибка отправки ордера: {result}")
          return False
   return True