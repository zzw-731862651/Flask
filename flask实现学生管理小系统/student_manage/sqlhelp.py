from student_manage.utils import POOL
import pymysql

def create_conn():
    conn = POOL.connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn,cursor

def close_conn(conn,cursor):
    conn.close()
    cursor.close()

def select_one(sql,args):
    conn,cursor = create_conn()
    cursor.execute(sql)
    ret = cursor.fetchone()
    close_conn(conn,cursor)
    return ret

def select_all(sql):
    conn,cursor = create_conn()
    cursor.execute(sql)
    ret = cursor.fetchall()
    close_conn(conn,cursor)
    return ret

def insert_one(sql,args):
    conn,cursor = create_conn()
    ret = cursor.execute(sql,args)
    conn.commit()
    close_conn(conn,cursor)
    return ret

def update_one(sql,args):
    conn,cursor = create_conn()
    ret = cursor.execute(sql)
    conn.commit()
    close_conn(conn,cursor)
    return ret

def delete_one(sql,id):
    conn,cursor = create_conn()
    ret = cursor.execute(sql,id)
    conn.commit()
    close_conn(conn,cursor)
    return ret

