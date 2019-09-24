import MySQLdb

def insert_inf(result_list):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='dragonfly',
        charset='utf8',
    )

    cur = conn.cursor()
    # 插入一条数据
    for result in result_list:
        sql = 'insert into information (`in_title`,`in_time`,`in_site`,`in_introduce`) values(%s,%s,%s,%s)'
        cur.execute(sql,[result[0],result[1],result[2],result[3]])

    cur.close()
    conn.commit()
    conn.close()
    print('插入成功！')