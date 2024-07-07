from flask import Flask,render_template,redirect,url_for,request,session

app = Flask(__name__)
app.secret_key = "situu#"

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for("designs"))
    return render_template("home.html")


@app.route("/designs")
def designs():
    return render_template("designs.html")

@app.route("/checktemplate",methods=['POST'])
def checktemplate():
    temp = request.form['button']
    session['template'] = temp
    return redirect(url_for('form'))

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        template = session.get('template',None)

        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        phone = request.form.get('phone')
        mail = request.form.get('mail')

        designation = request.form.get('designation')
        location = request.form.get('location')

        company = request.form.get('company')
        work = request.form.get('work')
        education = request.form.get('education')
        college = request.form.get('college')

        skill1 = request.form.get('skill1')
        skill2 = request.form.get('skill2')
        skill3 = request.form.get('skill3')
        skill4 = request.form.get('skill4')
        about = request.form.get('about')
        

        if template == 'template1':
            return render_template("template1.html",firstname=firstname,lastname=lastname,designation=designation,location=location,company=company,work=work,education=education,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,about=about,college=college,phone=phone,mail=mail)

        elif template == 'template2':
            return render_template("template2.html",firstname=firstname,lastname=lastname,designation=designation,location=location,company=company,work=work,education=education,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,about=about,college=college,phone=phone,mail=mail)
        elif template == 'template3':
            return render_template("template3.html",firstname=firstname,lastname=lastname,designation=designation,location=location,company=company,work=work,education=education,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,about=about,college=college,phone=phone,mail=mail)
        elif template == 'template4':
            return render_template("template4.html",firstname=firstname,lastname=lastname,designation=designation,location=location,company=company,work=work,education=education,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,about=about,college=college,phone=phone,mail=mail)
        elif template == 'template5':
            return render_template("template5.html",firstname=firstname,lastname=lastname,designation=designation,location=location,company=company,work=work,education=education,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,about=about,college=college,phone=phone,mail=mail)
        elif template == 'template6':
            return render_template("template6.html",firstname=firstname,lastname=lastname,designation=designation,location=location,company=company,work=work,education=education,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,about=about,college=college,phone=phone,mail=mail)
    return render_template("form.html")


@app.route("/test")
def test():
    return render_template("template5.html")
app.run(debug=True)