from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def admin(name=None):
    return render_template('pawan-projects-welcome.html')

@app.route('/weather')
def weather(name=None):
    return render_template('weather-app-sunny.html')

@app.route('/student', methods=['GET', 'POST'])
def student(name=None):
    return render_template('student.html')
@app.route('/saiveera',methods=['GET','POST'])
def saiveera(name=None):
    return render_template('saiveera.html')

@app.route('/Aboutme')
def Aboutme(name=None):
    return render_template('aboutme.html')



#this is a login page where user can login with username and password. If the username and password are correct, the user will be redirected to the True_Caffeine.html page. If the username and password are incorrect, the user will be shown an error message.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'pawan' and password == 'Pawan@2025':
            # return "welcome %s" % username
            return render_template('options.html', username=username)
        # else:
        #     return "Invalid username or password"
        return "Invalid username or password"
    return render_template('login.html')


# @app.route('/Aboutme', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if username == 'pawan' and password == 'Pawan@2025':
#             # return "welcome %s" % username
#             return render_template('Aboutme.html', username=username)
        # else:
        #     return "Invalid username or password"
    #     return "Invalid username or password"
    # return render_template('login.html')


# @app.route('/Aboutme',methods=['GEST','POST'])
# def Aboutme():
#     if request.method== 'POST':
#         if Aboutme == Aboutme:
#             return render_template('Aboutme',username=Aboutme)

if __name__ == '__main__':
    app.run(debug=True)