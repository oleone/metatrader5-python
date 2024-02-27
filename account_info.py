import MetaTrader5 as mt5
from dotenv import load_dotenv
import os

def init_meta_trader_4(login, password, server):
    if not mt5.initialize():
        print("MetaTrader5 package is not started!\n")
        mt5.shurtdown()
    else:
        print("MetaTrader5 started!\n")

    timeout = 500

    if mt5.login(login=int(login), password=password, server=server, timeout=timeout):
        print("MetaTrader logged!\n","Server: ",server," Account: ",login)
        print(mt5.account_info())
        return mt5
    else:
        dispatch()
        raise ValueError('MetaTrader is not logged!')

def dispatch():
    mt5.shutdown()

def main():
    load_dotenv()

    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')
    SERVER = os.getenv('SERVER')

    init_meta_trader_4(LOGIN, PASSWORD, SERVER)

if __name__ == "__main__":
    main()