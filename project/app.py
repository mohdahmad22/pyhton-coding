from flask import Flask,render_template,request
import os
from Studentdbs import StudentDatabase
app=Flask(__name__)#flask object
@app.route('/index') #homepage address
def index():    #function that will run when homepage starts 
    data=list (range(0,100,2))
    return render_template('index.html',num=data)

@app.route('/',methods=['GET','POST'])
def daily():
    msg=""
    if request.method=="POST":
        stddb=StudentDatabase()
        #stddb.create_table()
        studentname=request.form.get('Student')
        batch=request.form.get('Batch')
        roll=request.form.get('roll')
        address=request.form.get('address')
        status=stddb.addstudent(studentname,batch,roll,address)
        records=stddb.view()
        print(records)
        if status:
            msg="saved succesfully"
        else:
            msg='failed to save'
    return render_template('dailyform.html',msg=msg)

"""
@app.route('/',methods=['GET','POST']) #homepage address
def expenses():    #function that will run when homepage starts 
    msg=""
    records=""
    if request.method=="POST":
        db=Database()
        db.create_table()
        name=request.form.get('item')
        price=request.form.get('price')
        status=db.add(name,price)
        records=db.view()
        if status:
            msg="saved succesfully"
        else:
            msg="error saving data"

        for data in request.form.items():
            print(data)

            
    print(records)
    return render_template('expense.html')
"""
if __name__=="__main__":
    app.run(debug=True)#starts the web server when we run  the app