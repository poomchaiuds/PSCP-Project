from flask import Flask, render_template, render_template_string
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/Chainsaw Man") #test ใช้ไม่ได้
def chainsaw_man():
    return render_template("chainsaw_man.html")

@app.route("/86 Eighty Six") 
def eighty_six():
    return render_template("86 Eighty Six.html")

@app.route("/Black Clover") 
def black_clover():
    return render_template("Black Clover.html")

@app.route("/Bleach") 
def bleach():
    return render_template("Bleach.html")

@app.route("/Dr. Stone") 
def dr_stone():
    return render_template("Dr. Stone.html")

@app.route("/Fire Force") 
def fire_force():
    return render_template("Fire Force.html")

@app.route("/Fullmetal Alchemist Brotherhood") 
def fullmetal_alchemist_brotherhood():
    return render_template("Fullmetal Alchemist Brotherhood.html")

@app.route("/Kaguya-sama wa Kokurasetai") 
def kaguya_sama_wa_kokurasetai():
    return render_template("Kaguya-sama wa Kokurasetai.html")

@app.route("/Made in Abyss") 
def made_in_abyss():
    return render_template("Made in Abyss.html")

@app.route("/Mononoke Hime") 
def mononoke_hime():
    return render_template("Mononoke Hime.html")

@app.route("/Mushishi Zoku Shou") 
def mushishi_zoku_shou():
    return render_template("Mushishi Zoku Shou.html")

@app.route("/Mushoku Tensei") 
def mushoku_tensei():
    return render_template("Mushoku Tensei.html")

@app.route("/Nichijou") 
def nichijou():
    return render_template("Nichijou.html")

@app.route("/Platinum End") 
def platinum_end():
    return render_template("Platinum End.html")

@app.route("/Spy x Family") 
def spy_x_family():
    return render_template("Spy x Family.html")

@app.route("/Steins;Gate") 
def steins_gate():
    return render_template("Steins;Gate.html")

@app.route("/Cross Game") 
def cross_game():
    return render_template("cross_game.html")

@app.route("/Grand Blue") 
def grand_blue():
    return render_template("grand_blue.html")

@app.route("/Haikyu") 
def haikyu():
    return render_template("haikyu.html")

@app.route("/Kimitsu No Yaiba") 
def kimitsu_no_yaiba():
    return render_template("kimitsu no yaiba.html")

@app.route("/Owarimonogatari") 
def owarimonogatari():
    return render_template("owarimonogatari.html") 

