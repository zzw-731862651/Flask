from flask import Blueprint,render_template,request,redirect
from student_manage.sqlhelp import select_one,update_one

studentedit= Blueprint('studentedit',__name__,template_folder='edit_template')

@studentedit.route('/student/edit/<int:id>',methods=['GET','POST'])
def student_edit(id):

    if request.method == 'GET':
        sql = 'select * from student where id=%s '%(id)
        row = select_one(sql,id)

        return render_template('student_edit.html',row=row)
    if request.method == 'POST':
        # sid = request.form.get('id')
        sname = request.form.get('name')
        sage = request.form.get('age')
        sgender = request.form.get('gender')
        sql = 'update student set name="%s",age="%s",gender="%s" where id="%s"' %(sname,sage,sgender,id)
        row = update_one(sql,id)

        return redirect('/student/list')
