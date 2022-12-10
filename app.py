from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/chainsaw man") #test ใช้ไม่ได้
def chainsaw_man("/chainsaw man"):
    return render_template("chainsaw_man.html")
