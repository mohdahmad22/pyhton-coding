from flask import Flask,render_template,request
import os
app=Flask(__name__)#flask object
@app.route('/index') #homepage address
def index():    #function that will run when homepage starts 
    data=list (range(0,100,2))
    return render_template('index.html',num=data)

@app.route('/')
def daily():
    return render_template('captureform.html')

if __name__=="__main__":
    app.run(debug=True)#starts the web server when we run  the app