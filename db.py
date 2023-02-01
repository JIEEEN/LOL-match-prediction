import pymysql
from data.progamer_info import ProGamer as PG


class DB:
    def __init__(self,con,cur):
        con = pymysql.connect(host='localhost', user='root', password='2835',
                        db='lmp_db', charset='utf8', autocommit=True,
                        cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()
        cur.execute("select * from progamer")

    def db_insert():
        sql_query = "insert into progamer values(%s)"
        for data in PG.progamer_list:
            val = (data)
            cur(sql_query, val)
    
    