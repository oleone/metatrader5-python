import account_info
from dotenv import load_dotenv
import os
from datetime import datetime

def main():
    load_dotenv()
    
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')
    SERVER = os.getenv('SERVER')

    account_info.dispatch()

    from_date=datetime(2019,1,1)
    to_date=datetime.now()

    mt5 = account_info.init_meta_trader_4(LOGIN, PASSWORD, SERVER)

    print(mt5.positions_get())

    # print(account_info.history_orders_total(date_from = from_date, date_to = to_date))

    # print("\n", mt5.history_orders_get(date_from=from_date, date_to=to_date, group="P*"))


if __name__ == "__main__":
    main()