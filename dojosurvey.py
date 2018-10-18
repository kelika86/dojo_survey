from flask import Flask, render_template, request, redirect, session
app= Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("dojosurvey1.html")

@app.route('/users', methods=['POST'])
def result():
    print(request.form)
    session ['name']= request.form ['name']
    session ['location']= request.form ['location']
    session ['language']= request.form['language']
    session ['comment']= request.form ['comment']
    return redirect ('/show')

@app.route('/show')
def show_user():
    return render_template('dojosurvey2.html', name=session ['name'], location=session ['location'], language= session ['language'], comment=session ['comment'])
    

@app.route('/danger')
def danger():
    print('user tried to enter dangerzone')
    return redirect ('/')



app.run(debug=True)