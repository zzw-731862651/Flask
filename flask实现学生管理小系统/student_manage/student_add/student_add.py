from flask import Blueprint,render_template,request,redirect
from student_manage.sqlhelp import insert_one

studentadd = Blueprint('studentadd',__name__,template_folder='add_template')


@studentadd.route('/student/add',methods=['GET','POST'])#这个studentadd是上面的studentadd
def student_add():
    if request.method == 'GET':
        render_template('student_add.html')
    if request.method == 'POST':
        # sid = request.form.get('id')
        sname = request.form.get('name')
        sage = request.form.get('age')
        sgender = request.form.get('gender')

        # sql语句
        sql = 'insert into student(name,age,gender) values (%s,%s,%s)'
        row = insert_one(sql,(sname,sage,sgender))
        return redirect('/student/list')

    return render_template('student_add.html')

