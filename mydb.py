import pymysql
import os
from data.progamer_info import ProGamer as Pro
from dotenv import load_dotenv

load_dotenv()

class DB:
    def db_con(self):
        DB.con = pymysql.connect(host=os.environ.get('DB_HOST'), user=os.environ.get('DB_USER'), password=os.environ.get('DB_PASSWORD'),
                        db=os.environ.get('DB_DATABASE'), charset='utf8', autocommit=True,
                        cursorclass=pymysql.cursors.DictCursor)
        DB.cur = DB.con.cursor()


    def db_insert(self):
        pg = Pro()
        sql_query = "insert ignore into progamer2023(id, total_winrate) values(%s, %s)"

        for pro_id, total_wr in zip(pg.progamer_list, pg.winrate_list):
            if total_wr.get_text()[0:4] == '50%': 
                value = (pro_id.get_text(), 50.0)
            else: value = (pro_id.get_text(), float(total_wr.get_text()[0:4]))
            DB.cur.execute(sql_query, value)
        # sql_query = "insert ignore into progamer2023(id) values(%s)"
        # for pro_id in pg.progamer_list:
        #     value = (pro_id.get_text())
        #     DB.cur.execute(sql_query, value)

        DB.con.commit()


    def update_winrate(self):
        pg = Pro()
        DB.cur.execute("select id from progamer2023")
        res = DB.cur.fetchmany(40)

        for pro_id in res:
            pg.winRate(pro_id['id'], "LCK2023")

