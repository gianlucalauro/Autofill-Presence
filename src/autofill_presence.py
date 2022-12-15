import sys
from utils import driver
from utils import login
from utils import insert_asa_and_submit
from utils import insert_smart_permission

driver.get("https://example.com")

login()

driver.get("https://example.com/profile")

if sys.argv[1] == "Presenza":
    insert_asa_and_submit()
elif sys.argv[1] == "Smart":
    insert_smart_permission()

driver.close()
