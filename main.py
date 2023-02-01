from db import DB
from data.progamer_info import ProGamer as PG

if __name__ == '__main__':
    DB.db_insert()
    for i in PG.progamer_list:
        print(i.get_text())
