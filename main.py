from mydb import DB
from data.progamer_info import ProGamer as Pro


def init():
    lmp_db.db_con()
    lmp_db.update_winrate()
    lmp_db.db_insert()


if __name__ == '__main__':
    progamer_info = Pro()
    lmp_db = DB()
    init()


    