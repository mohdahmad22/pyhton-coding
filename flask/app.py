
from flask import Flask,render_template,request
import os
from Database import Database
app=Flask(__name__)#flask object
@app.route('/index') #homepage address
def index():    #function that will run when homepage starts 
    data=list (range(0,100,2))
    return render_template('index.html',num=data)
@app.route('/about') #homepage address
def about():    #function that will run when homepage starts 
    return render_template('about.html')
@app.route('/',methods=['GET','POST']) #homepage address
def expenses():    #function that will run when homepage starts 
    msg=""
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

if __name__=="__main__":
    app.run(debug=True)#starts the web server when we run  the appb