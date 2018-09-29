from flask import Flask
from student_manage.student_list import student_list
from student_manage.student_add import student_add
from student_manage.student_edit import student_edit
from student_manage.student_del import student_del


app = Flask(__name__)
app.register_blueprint(student_list.studentlist)
app.register_blueprint(student_add.studentadd)
app.register_blueprint(student_edit.studentedit)
app.register_blueprint(student_del.studentdel)



if __name__ == '__main__':
    app.run('127.0.0.1',9527,debug=True)

#备注，进来先修改数据库配置文件
# http://127.0.0.1:9527/student/list