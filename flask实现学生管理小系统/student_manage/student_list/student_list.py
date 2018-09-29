from flask import Blueprint,render_template,Markup
from student_manage.sqlhelp import select_all

studentlist = Blueprint('studentlist',__name__,
                         template_folder='list_template'
                         )

# 连接数据库连接池创建数据库连接
# def func():
#     conn = POOL.connection()
#     cursor = conn.cursor(pymysql.cursors.DictCursor)
#     cursor.execute('select * from student')
#     ret = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return ret


@studentlist.route('/student/list')
def student_list():
    btn = '<a href="/student/add">添加</a>'
    btn = Markup(btn)
    # row = func()
    sql = 'select * from student'
    row = select_all(sql)
    print(row)              #[{'id': 2, 'name': '粟裕', 'gender': '男', 'age': 22}, {'id': 7, 'name': '聂荣臻', 'gender': '男', 'age': 18}, {'id': 8, 'name': '林彪', 'gender': '男', 'age': 18}, {'id': 9, 'name': '王必成', 'gender': '男', 'age': 22}, {'id': 10, 'name': '那英', 'gender': '女', 'age': 22}, {'id': 11, 'name': '韩红', 'gender': '女', 'age': 18}]
    return render_template('student_list.html',row=row,btn=btn)