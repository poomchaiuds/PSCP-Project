from flask import Flask, render_template, render_template_string
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/Chainsaw Man") #1
def chainsaw_man():
    return render_template("chainsaw_man.html")

@app.route("/86 Eighty Six") #2
def eighty_six():
    return render_template("86 Eighty Six.html")

@app.route("/Black Clover") #3
def black_clover():
    return render_template("Black Clover.html")

@app.route("/Bleach") #4
def bleach():
    return render_template("Bleach.html")

@app.route("/Dr. Stone") #5 
def dr_stone():
    return render_template("Dr. Stone.html")

@app.route("/Fire Force") #6
def fire_force():
    return render_template("Fire Force.html")

@app.route("/Fullmetal Alchemist Brotherhood") #7 
def fullmetal_alchemist_brotherhood():
    return render_template("Fullmetal Alchemist Brotherhood.html")

@app.route("/Kaguya-sama wa Kokurasetai") #8
def kaguya_sama_wa_kokurasetai():
    return render_template("Kaguya-sama wa Kokurasetai.html")

@app.route("/Made in Abyss") #9
def made_in_abyss():
    return render_template("Made in Abyss.html")

@app.route("/Mononoke Hime") #10
def mononoke_hime():
    return render_template("Mononoke Hime.html")

@app.route("/Mushishi Zoku Shou") #11 
def mushishi_zoku_shou():
    return render_template("Mushishi Zoku Shou.html")

@app.route("/Mushoku Tensei") #12
def mushoku_tensei():
    return render_template("Mushoku Tensei.html")

@app.route("/Nichijou") #13
def nichijou():
    return render_template("Nichijou.html")

@app.route("/Platinum End") #14 
def platinum_end():
    return render_template("Platinum End.html")

@app.route("/Spy x Family") #15
def spy_x_family():
    return render_template("Spy x Family.html")

@app.route("/Steins;Gate") #16
def steins_gate():
    return render_template("Steins;Gate.html")

@app.route("/Cross Game") #17
def cross_game():
    return render_template("cross_game.html")

@app.route("/Grand Blue") #18
def grand_blue():
    return render_template("grand_blue.html")

@app.route("/Haikyu") #19
def haikyu():
    return render_template("haikyu.html")

@app.route("/Kimitsu No Yaiba") #20
def kimitsu_no_yaiba():
    return render_template("kimitsu no yaiba.html")

@app.route("/Owarimonogatari") #21
def owarimonogatari():
    return render_template("owarimonogatari.html") 

@app.route("/Hunter x Hunter") #22
def owarimonogatari():
    return render_template("Hunter x Hunter.html") 

@app.route("/Jujutsu Kaisen") #23
def owarimonogatari():
    return render_template("Jujutsu Kaisen.html") 

@app.route("/Koe no Katachi") #24
def owarimonogatari():
    return render_template("Koe no Katachi.html") 

@app.route("/Legend of the Galactic Heroes") #25 
def owarimonogatari():
    return render_template("Legend of the Galactic Heroes.html") 

@app.route("/Natsume Yuujinchou Roku") #26
def owarimonogatari():
    return render_template("Natsume Yuujinchou Roku.html") 
    
@app.route("/Ookami Kodomo no Ame to Yuki") #27 
def owarimonogatari():
    return render_template("Ookami Kodomo no Ame to Yuki.html") 

@app.route("/Shigatsu wa Kimi no Uso") #28
def owarimonogatari():
    return render_template("Shigatsu wa Kimi no Uso.html") 

@app.route("/Summertime Render") #29
def owarimonogatari():
    return render_template("Summertime Render.html") 

@app.route("/Suzumiya Haruhi no Shoushitsu") #30 
def owarimonogatari():
    return render_template("Suzumiya.html") 

@app.route("/Tengen Toppa Gurren Lagann") #31
def owarimonogatari():
    return render_template("Tengen Toppa Gurren Lagann.html") 

@app.route("/Uchuu kyoudai") #32
def owarimonogatari():
    return render_template("Uchuu_kyoudai.html") 

@app.route("/Summertime Render") #33 
def owarimonogatari():
    return render_template("Summertime Render.html") 

@app.route("/Aria The Origination") #34
def owarimonogatari():
    return render_template("aria_the_origination.html") 

@app.route("/Banana Fish") #35
def owarimonogatari():
    return render_template("banana_fish.html") 

@app.route("/Deathnote") #36
def owarimonogatari():
    return render_template("deathnote.html") 
       
