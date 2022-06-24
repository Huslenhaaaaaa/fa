import re
from flask import Flask, render_template, request, redirect, session
from DBConnection import Db

import matplotlib.pyplot as plt

from nbclass import predict_fun
from predictionn import train_model, prediction_result

from similarity import similaritycheck

import datetime as dt

app = Flask(__name__)
app.secret_key = "abc"
@app.route('/ab')
def hello_world():
    return 'Hello World!'

@app.route('/')
def mainhome():
    return render_template("mainhome.html")

@app.route('/login',methods = ['get','post'])
def login():
    db = Db()
    if request.method == "POST" :
        username = request.form['username']
        password = request.form['password']
        res = db.selectOne(" select * from login where username = '"+username+"' and password = '"+password+"' ")
        print(res)
        if res is not None :
            #creating session
            # session['lid'] = res['loginid']
            # print(session['lid'])
            session['log'] = 'log'
            if res['user_type'] == "admin" :
                return redirect('/adminhome')
            elif res['user_type'] == "std":
                session['lid'] = res['loginid']
                return redirect('/home')
            else:
                return '''<script>alert("student doesn't exist!!");window.location = "/"</script>'''
        else:
            return '''<script>alert("student doesn't exist!!");window.location = "/"</script>'''
    else :
        return render_template("loginform.html")

@app.route('/user_registration', methods = ['get','post'])
def registration():
    db = Db()
    if request.method == "POST":
        print(request.form)
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        place = request.form['place']
        phoneno = request.form['phone']
        fmly_stat = request.form['famly']
        quali = request.form['qualification']
        stream = request.form['stream']
        interest = request.form['interest']
        mark = request.form['mark']
        skill1= request.form['skillone']
        skill2 = request.form['skilltwo']
        skill3 = request.form['skillthree']
        skillfour = request.form['skillfour']
        email = request.form['email']
        password = request.form['password']
        cnpassword = request.form['cnpassword']
        phoneno = request.form['phone']
        place = request.form['place']
        result = db.selectOne("select * from login where username='"+email+"'")
        if result is not None:
            return '''<script>alert("User already exists!!");window.location = "/user_registration"</script>'''
        else:
            if  password == cnpassword :
                res = db.insert("insert into login values('','"+email+"','"+cnpassword+"','std')")
                req = db.insert("insert into student values('','"+ str(res) +"','" + name + "','" + age + "','" + gender + "','" + place + "','" + phoneno + "','"+quali+"','" + email + "')")
                db.insert("insert into std_required values('"+ str(req) +"','"+fmly_stat+"','" + stream + "','"+interest+"','"+mark+"','"+skill1+"','"+skill2+"','"+skill3+"','"+skillfour+"')")
                return '''<script>alert("Registration successfully completed!!");window.location = "/login"</script>'''
            else:
                return '''<script>alert("Password mismatch!!");window.location = "/login"</script>'''
    else:
        return render_template("registerform.html")

@app.route('/student_home')
def stdhome():
    if session['log'] == "log":

        return render_template("studenthome.html")
        # if session['log'] == "log":
        #     return render_template("studenthome.html")
    else:
            return redirect('/login')

@app.route('/home')
def home():
    if session['log'] == "log":
        db = Db()
        res = db.selectOne("select * from student where std_id = '"+str(session['lid'])+"'")
        return render_template("home.html",data = res['name'])
    else:
        return redirect('/login')

@app.route('/view_profile')
def profile():
    if session['log'] == "log":
        db = Db()
        res = db.selectOne("SELECT * FROM student,std_required WHERE student.id = std_required.std_id AND std_required.std_id='"+str(session['lid'])+"'")
        return render_template("viewprofile.html",data = res)
    else:
        return redirect('/login')





@app.route('/view_profile1')
def view_profile1():
    if session['log'] == "log":
        db = Db()
        res = db.selectOne("SELECT * FROM student,std_required WHERE student.id = std_required.std_id AND std_required.std_id='"+str(session['lid'])+"'")
        return render_template("registerformview.html",data = res)
    else:
        return redirect('/login')




@app.route('/about')
def about():
    return render_template("firm-profile.html")



@app.route('/logout')
def logout():
    session['log'] = ""
    return redirect('/')


@app.route('/questions',methods = ['get','post'])
def iqtest():
    if session['log'] == "log":

        db= Db()
        print(request.method,"======")
        list1=[5,5,10,10,5,5,10,20,10,20]
        if request.method == "POST" :
            a = str(session['a'])
            a = a.split('+')[0]
            # a = a+".0"
            print(a)
            b = dt.datetime.now()
            print(a, type(a))
            print(b, type(b))
            format = "%Y-%m-%d %H:%M:%S"
            a = dt.datetime.strptime(a,format)
            timediff = ( ( b - a ).total_seconds() ) / 60
            print(timediff,"*********")
            q1 = request.form['q1']
            aq1 = request.form['aq1']
            q2 = request.form['q2']
            aq2 = request.form['aq2']
            q3 = request.form['q3']
            aq3 = request.form['aq3']
            q4 = request.form['q4']
            aq4 = request.form['aq4']
            q5 = request.form['q5']
            aq5 = request.form['aq5']
            q6 = request.form['q6']
            aq6 = request.form['aq6']
            q7 = request.form['q7']
            aq7 = request.form['aq7']
            q8 = request.form['q8']
            aq8 = request.form['aq8']
            q9 = request.form['q9']
            aq9 = request.form['aq9']
            q10 = request.form['q10']
            aq10 = request.form['aq10']
            tm = 40
            if q1 == aq1 :
                tm = tm + list1[0]
            if q2 == aq2 :
                tm = tm + list1[1]
            if q3 == aq3 :
                tm = tm + list1[2]
            if q4 == aq4 :
                tm = tm + list1[3]
            if q5 == aq5 :
                tm = tm + list1[4]
            if q6 == aq6 :
                tm = tm + list1[5]
            if q7 == aq7 :
                tm = tm + list1[6]
            if q8 == aq8 :
                tm = tm + list1[7]
            if q9 == aq9 :
                tm = tm + list1[8]
            if q10 == aq10 :
                tm = tm + list1[9]
            if tm!=50:
                if timediff <2:
                    tm = tm+10
                elif timediff<4:
                    tm = tm +8
                elif timediff < 6:
                    tm = tm + 6
                elif timediff < 8:
                    tm = tm + 4
                elif timediff <10:
                    tm = tm+ 2
                elif timediff <15:
                    tm = tm - 5
                elif timediff < 20:
                    tm = tm - 10
            db.insert("insert into iqmark values('"+str(session['lid'])+"','"+str(tm)+"','"+str(timediff)+"')")
            return '''<script>alert("Successfully Completed");window.location = "/testresult"</script>'''
        else:
            a = dt.datetime.now()
            session['a'] = a
            ss = db.selectOne("select * from iqmark where std_id = '" + str(session['lid']) + "'")
            print(ss, "====")
            if ss is not None:
                return "<script>alert('You Already Completed your test!!!');window.location='/testresult'</script>"
            return render_template("questions2.html")
    return redirect('/login')

@app.route('/testresult',methods = ['get','post'])
def testresult() :
    if session['log'] == "log":

            try:
                db = Db()
                res = db.selectOne("select * from eqscore where std_id='" + str(session['lid']) + "'")
                abc = db.selectOne("select * from iqmark where std_id ='"+str(session['lid'])+"'")
                #assigning table data into a set
                data = {'extraversion': int(res['extroversion']), 'agreeableness': int(res['agreeableness']), 'conscientiousness': int(res['conscientiousness']),
                        'neuroticism': int(res['neuroticism']), 'openness': int(res['openess'])}
                courses = list(data.keys())
                values = list(data.values())
                print("cc",courses)
                print("val",values)

                fig = plt.figure(figsize=(10,4))
                # mylabels = ["Extroversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openess", "IQ"]
                # myexplode = [0, 0, 0, 0, 0, 0.2]
                #
                # plt.pie(values, labels=mylabels, explode=myexplode)
                # plt.legend()
                # plt.show()

                # creating the bar plot
                plt.bar(courses, values, color='green',
                        width=0.3)

                plt.xlabel("Big Five Factors")
                plt.ylabel("Score")
                # 'iqmark': int(abc['mark'])
                plt.title("EQ Test Score")
                plt.savefig(r"C:\Users\HP\Downloads\career_prediction\career_prediction\sample.jpg")
                return render_template("testresult.html",iq=abc['mark'],iqt=abc['time'])
            except Exception as e:
                print(e)
                return '''<script>alert("Please Complete Your Test");window.location = "/home"</script>'''
    else:
        return redirect('/login')

     # ques = ['1) ________ is the basic unit of all living things?','2) The square root of 81 is?','3) After how many years Olympic Games are held?' ,'4) A 180 degree angle is called?','5) When was Microsoft established?',
     #         '6) In which direction a fan rotates?','7) A group of wolves is called?','8) How water is written scientifically?','9) What number should logically replace the question mark ; 26,34,41,46,56,?',
     #         '10) 7*9 - (3*4) +10 = X : What is the value of X?','11)V. Sindhu is associated with which game?']
     #
     # if request.method == "GET":
     #     session['ans'] = ""
     #     session['cnt'] = 0
     #     cnt = 0
     #     return render_template("questions.html", qstn=ques[cnt], ln=len(ques), cnt=cnt)
     # else:
     #     btn=request.form['button']
     #     if btn == "Next":
     #         ans = request.form['textarea2']
     #         session['ans']=session['ans']+"#"+ans
     #         # ans_list.append(ans)
     #         session['cnt'] = session['cnt'] + 1
     #         return render_template("questions.html", qstn=ques[session['cnt']], ln=len(ques), cnt=session['cnt'])
     #     else:
     #         ans = request.form['textarea2']
     #         session['ans'] = session['ans'] + "#" + ans
     #         ans_list=session["ans"].split("#")
     #         print("Answers    ", ans_list[1:])
     #         return "Over"

@app.route('/eqques',methods = ['get' , 'post'])
def eqtest():
    if session['log'] == "log":

        if request.method == "POST":
            print(request.form)
            q1 = request.form['q1']
            q2 = request.form['q2']
            q3 = request.form['q3']
            q4 = request.form['q4']
            q5 = request.form['q5']
            q6 = request.form['q6']
            q7= request.form['q7']
            q8 = request.form['q8']
            q9 = request.form['q9']
            q10= request.form['q10']
            q11 = request.form['q11']
            q12 = request.form['q12']
            q13 = request.form['q13']
            q14 = request.form['q14']
            q15 = request.form['q15']
            q16 = request.form['q16']
            q17 = request.form['q17']
            q18 = request.form['q18']
            q19 = request.form['q19']
            q20 = request.form['q20']
            q21 = request.form['q21']
            q22 = request.form['q22']
            q23 = request.form['q23']
            q24 = request.form['q24']
            q25 = request.form['q25']

            #calculating fivefactor scores

            E = int(q1) + int(q6)+ int(q11) + int(q16) + int(q21)
            A =int(q2) + int(q7) + int(q12) + int(q17) + int(q22)
            C =int(q3) + int(q8) + int(q13) + int(q18) + int(q23)
            N = int(q4) + int(q9) + int(q14) + int(q19) + int(q24)
            O = int(q5) + int(q10) + int(q15) + int(q20) + int(q25)
            db = Db()

            db.insert(
                "insert into eqscore VALUES('','" + str(session['lid']) + "','" + str(E) + "','" + str(A) + "','" + str(
                    C) + "','" + str(N) + "','" + str(O) + "')")

            # res =db.selectOne("select * from student where std_id = '"+str(session['lid'])+"'")
            # age =res['age']
            # gender = res['gender']
            #
            # if gender=='male':
            #
            #
            #     model = train_model()
            #     model.train()
            #     pred = prediction_result(('1', str(age),str(E) ,str(A),str(C),str(N),str(O)))
            #     # print("Hellooo  ")
            #     # aa = str(pred)
            #     # print(aa)
            #
            #     l=str(pred)
            #     l1 = re.sub('[^A-Za-z]+', '', l)
            #     # print(l1)
            #     # inserting values into the score table
            #     ss = db.insert("insert into eqscore VALUES('','"+str(session['lid'])+"','"+str(E)+"','"+str(A)+"','"+str(C)+"','"+str(N)+"','"+str(O)+"','" +l1+"')")
            #     return render_template('testresult.html',value=l1)
            # else:
            #     model = train_model()
            #     model.train()
            #     pred = prediction_result(('0', str(age), str(E), str(A), str(C), str(N), str(O)))
            #     l = str(pred)
            #     l1 = re.sub('[^A-Za-z]+', '', l)
            #     # print(l1)
            #     # print("Hiiii   ")
            #     # print(type(pred))
            #
            #     ss = db.insert("insert into eqscore VALUES('','"+str(session['lid'])+"','"+str(E)+"','"+str(A)+"','"+str(C)+"','"+str(N)+"','"+str(O)+"','" +l1+"')")
            #     return render_template('testresult.html',value=l1)
            return '''<script>alert("Successfully Completed");window.location = "/questions"</script>'''
        else:
            db = Db()
            ss = db.selectOne("select * from eqscore where std_id = '"+str(session['lid'])+"'")
            print(ss,"====")
            if ss is not None:
                return "<script>alert('You Already Completed your test!!!');window.location='/questions'</script>"
            return render_template("questionnaire.html")
    else:
        return redirect('/login')

@app.route('/predict')
def predict():
    if session['log'] == "log":

    # try:
        try :
            db = Db()
            res = db.selectOne("select * from std_required where std_id = '"+str(session['lid'])+"'")
            abc = db.selectOne("select * from eqscore where std_id = '"+str(session['lid'])+"'")
            se = db.selectOne("select * from iqmark where std_id = '" + str(session['lid']) + "'")

            lis0 = ['average', 'middle', 'low']
            lis1 = ['science', 'commerce', 'humanities']
            lis2 = ['building', 'technology', 'healthcare', 'volunteering', 'coding', 'business', 'management', 'law', 'arts']

            lis14 = ['Engineering', 'Medical', 'CA_and_IT', 'Enterpricing_and_management', 'Law', 'Entertainment']
            lis15 = ['Engineering', 'Medical','Computer Application and IT','Enterpricing and Management','Law','Media and Arts']
            row = []
            row.append(lis0.index(res['fmly']))
            row.append(lis1.index(res['stream']))
            row.append(lis2.index(res['interest']))
            row.append(int(res['mark']))
            row.append(int(res['skill_1']))
            row.append(int(res['skill_2']))
            row.append(int(res['skill_3']))
            row.append(int(res['skill_4']))

            row.append(int(abc['extroversion']))
            row.append(int(abc['agreeableness']))
            row.append(int(abc['conscientiousness']))
            row.append(int(abc['neuroticism']))
            row.append(int(abc['openess']))

            row.append(int(se['mark']))

            res = predict_fun([row])

            result = lis15[res]

            dic = {"0": row[0], "1":row[1],"2":row[2],"3":row[3],"4":row[4],"5":row[5],"6":row[6],"7":row[7],"8":row[8],"9":row[9],"10":row[10],"11":row[11],"12":row[12],"13":row[13]}
            out, sim = similaritycheck(res,dic)
            print(out,"=========================")
            print(sim,"=============================")
            largevalue1 = 0
            largevalueindex = -1
            secondlargevalue = 0
            second_large_value_index = -1
            for i in range(0,len(out)):
                if lis15[out[i]] != result :
                    if sim[i] > largevalue1 :
                        secondlargevalue =  largevalue1
                        second_large_value_index = largevalueindex
                        largevalue1 = sim[i]
                        largevalueindex = i
                    elif sim[i] > secondlargevalue :
                        secondlargevalue = sim[i]
                        second_large_value_index = i

            result1 = lis15[out[largevalueindex]]
            result2 = lis15[out[second_large_value_index]]



            return  render_template("viewresult.html", r = result, r1 = result1, r2 = result2)
        except Exception as e:
            print(e)
            return '''<script>alert("Please Complete Your Test");window.location = "/home"</script>'''
    else:
        return redirect('/login')
@app.route('/feedback',methods = ['get','post'])
def feedback():
    if session['log'] == "log":

        db = Db()
        if request.method == "POST":
            fd = request.form['textarea1']
            db.insert("insert into feedback VALUES ('"+str(session['lid'])+"','"+fd+"')")
            return '''<script>alert("Your Feedback Successfuly send");window.location = "/feedback"</script>'''
        return render_template("feedback.html")
    return redirect('/login')

@app.route('/adminhome')
def adminhome():
    if session['log'] == "log":

        db = Db()

        return render_template("admin_home.html")
    else:
        return redirect('/login')

@app.route('/viewfdbck')
def view_fdbck():
    if session['log'] == 'log':

        db=Db()
        res = db.select("select * from feedback ")
        return render_template("viewfeedback.html",data=res)
    else:
        return redirect('/adminhome')


@app.route('/view_std')
def viewstd():
    if session['log'] == 'log':
        db = Db()
        res = db.select("select * from student,std_required,iqmark,eqscore where student.std_id =std_required.std_id and student.std_id = iqmark.std_id and student.std_id=eqscore.std_id  ")
        print(res)
        res1 = db.select("SELECT * FROM `student` WHERE `student`.`std_id` NOT IN (SELECT `std_id` FROM `eqscore`)AND  `student`.`std_id` NOT IN (SELECT `std_id` FROM `iqmark` )")
        print(res)

        return render_template("viewstudents.html",data=res,data1=res1)
    else:
        return redirect('/adminhome')



@app.route('/prediction')
def prediction():
    if session['log'] == "log":

        id=request.args.get('id')
        db=Db()
        res = db.select("SELECT * FROM `eqscore` WHERE `std_id`='"+str(id)+"' ")
        res1 = db.select("SELECT * FROM `iqmark` WHERE `std_id`='"+str(id)+"' ")

        return render_template("eq.html",data=res,data1=res1)
    else:
        return redirect('/login')


if __name__ == '__main__':
    app.run(debug = "true")
