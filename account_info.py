import MetaTrader5 as mt5

def init_meta_trader_4(login, password, server):
    if not mt5.initialize():
        print("MetaTrader5 package is not initialized!\n")
        mt5.shurtdown()
    else:
        print("MetaTrader5 started!\n")

    timeout = 500

    if mt5.login(login=login, password=password, server=server, timeout=timeout):
        print("MetaTrader logged!\n","Server: ",server," Account: ",login)
        print(mt5.account_info())
        return mt5

def dispatch():
    mt5.shurtdown()

def main():
    init_meta_trader_4(3166686, "lp.12!@.LP", "XPMT5-PRD")

if __name__ == "__main__":
    main()