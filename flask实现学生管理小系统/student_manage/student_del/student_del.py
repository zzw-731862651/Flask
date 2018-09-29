from flask import Blueprint,render_template,redirect,request
from student_manage.sqlhelp import delete_one

studentdel = Blueprint('studentdel',__name__)


@studentdel.route('/student/del/<int:id>',methods=['GET'])
def student_del(id):
    sql = 'delete from student where id=%s'
    row = delete_one(sql,id)
    return redirect('/student/list')
