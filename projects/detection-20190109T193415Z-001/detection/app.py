import functools
import os

import cv2
import mysql.connector
from flask import Flask, redirect, render_template, request, url_for, session, flash
from flask.json import jsonify
from mysql.connector import errorcode

import matching
import dataset
import training

app = Flask(__name__)
# connecting to Database
db = mysql.connector.connect(host="localhost", user="root", passwd="", db="detection")
cur = db.cursor()


@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (name, password))

        myresult = cur.fetchone()
        print(myresult)
        # print("got usertype ", myresult[3])

        session['user_type'] = myresult[3]
        session['user_id'] = myresult[0]
        session['user_name'] = myresult[1]

        if cur.rowcount > 0:
            if myresult[3] == 'Guard':
                    return redirect(url_for("guard"))
                # return render_template("guard.html")
            elif myresult[3] == 'Admin':
                    return redirect(url_for("admin"))
                # return render_template("adminedit.html")
            else:
                return render_template("no-account.html")
        else:
            return render_template("no-account.html")

        # return "here"
    else:
        return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        userid = request.form["userid"]
        name = request.form["username"]
        password = request.form["password"]
        usertype = request.form["usertype"]

        cur.execute("INSERT INTO users (UserID, Username, Password, Usertype) VALUES (%s, %s, %s, %s)",
                    (userid, name, password, usertype))
        db.commit()

        print(cur.rowcount, "record inserted.")

        # return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/logout")
def logout():
    session.pop('user_type', None)
    # return jsonify({'result': 'success'})
    return render_template("index.html")


@app.route("/goback")
def goback():
    if session['user_type'] == 'Admin':
        return render_template("adminedit.html")
    elif session['user_type'] == 'Guard':
        return render_template("guard.html")
    else:
        return render_template("no-account.html")


@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")


@app.route("/guard_dashboard")
def guard_dashboard():
    return render_template("guard_dashboard.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/guard")
def guard():
    return render_template("guard.html")


@app.route("/register_student")
def registerstudent():
    return render_template("registerstudent.html")


@app.route("/student_details", methods=["GET", "POST"])
def studentdetails():
    try:
        if request.method == "POST":
            StudentID = request.form["studentid"]
            Name = request.form["name"]

            cur.execute("SELECT * FROM students WHERE StudentID = %s AND Name = %s", (StudentID, Name))
            myresult = cur.fetchone()
            print(myresult)

            if cur.rowcount == 1:
                flash("STUDENT ALREADY EXISTS!!!")
                return "STUDENT ALREADY EXISTS!!!"
            else:
                cur.execute("INSERT INTO students(StudentID, Name) VALUES(%s,%s)", (StudentID, Name))
                db.commit()
                flash("Thank you for registering!")
                print(cur.rowcount, "record inserted.")

                session['current_student_id'] = cur.lastrowid
                session['current_student_name'] = Name

                # return "STUDENT HAS BEEN REGISTERED!!! KINDLY GO BACK SO AS TO TAKE THEIR IMAGES!!"
                return redirect(url_for("studentdetails"))
        return render_template("registerstudent.html")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("STH IS WRONG WITH YOUR USERNAME OR PASSWORD")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("DATABASE DOES NOT EXIST")
        else:
            print(err)


@app.route("/take_images", methods=["GET", "POST"])
def takeimages():
    print(request.method)
    # if request.method == "GET" and session['current_student']:
    StudentID = session['current_student_id']
    Studentname = session['current_student_name']
    # StudentID = request.form["studentid"]
    # Studentname = request.form["name"]

    dataset.faceID(StudentID, Studentname)
    if session['user_type'] == 'Admin':
        return render_template("adminedit.html")
    elif session['user_type'] == 'Guard':
        return render_template("guard.html")
    else:
        return render_template("no-account.html")


@app.route("/train_page")
def train_function():
    training.train()
    if session['user_type'] == 'Admin':
        return render_template("adminedit.html")
    elif session['user_type'] == 'Guard':
        return render_template("guard.html")
    else:
        return render_template("no-account.html")


@app.route("/match_page")
def match_function():
    flash("MATCHING FACE IN PROGRESS!!!!")
    UserID = session['user_id']
    UserWorking = session['user_name']
    print(UserID, UserWorking)

    cur.execute("INSERT INTO logs(UserID, UserWorking) VALUES(%s,%s)", (UserID, UserWorking))
    db.commit()

    matching.match()
    if session['user_type'] == 'Admin':
        return render_template("adminedit.html")
    elif session['user_type'] == 'Guard':
        return render_template("guard.html")
    else:
        return render_template("no-account.html")


@app.route("/adminedit")
def adminedit():
    return render_template("adminedit.html")


@app.route("/students")
def students():
    return render_template("students.html")


@app.route("/userguard")
def users():
    return render_template("userguard.html")


@app.route("/deletestudent", methods=["GET", "POST"])
def deletestudent():
    if request.method == "GET":
        StudentID = session['current_student_id']
        Studentname = session['current_student_name']

        # cur.execute("SELECT * FROM students WHERE StudentID = %s ", StudentID)
        # myresult = cur.fetchone()
        # print(myresult)

        # if cur.rowcount == 1:
        cur.execute("DELETE FROM students WHERE StudentID = ", StudentID)
        db.commit()
        print(cur.rowcount, "record(s) deleted")
    else:
        return "STUDENT DOES NOT EXIST!!!"

    # return render_template("students.html")
    return "hello"


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)
