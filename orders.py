import account_info
from dotenv import load_dotenv
import os

load_dotenv()

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
SERVER = os.getenv('SERVER')

mt5 = account_info.init_meta_trader_4(LOGIN, PASSWORD, SERVER)
print(mt5.orders_total())