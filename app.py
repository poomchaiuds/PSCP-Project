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
       
@app.route("/Code Geass") #37
def owarimonogatari():
    return render_template("Code_Geass.html") 

@app.route("/Hotaru no Haka") #38
def owarimonogatari():
    return render_template("Hotaru no Haka.html") 
       
@app.route("/Kimi no Na Wa") #39
def owarimonogatari():
    return render_template("Kimi_no_Na_Wa.html") 

@app.route("/Violet Evergarden Movie") #40
def owarimonogatari():
    return render_template("Violet_Evergarden_Movie.html") 

@app.route("/Yakusoku no Neverland") #41
def owarimonogatari():
    return render_template("Yakusoku no Neverland.html") 

@app.route("/Perfect Blue") #42
def owarimonogatari():
    return render_template("Perfect Blue.html") 

@app.route("/One Punch Man") #43
def owarimonogatari():
    return render_template("One Punch Man.html") 

@app.route("/Slam Dunk") #44
def owarimonogatari():
    return render_template("Slam Dunk.html") 

@app.route("/Samurai Champloo") #45
def owarimonogatari():
    return render_template("Samurai Champloo.html") 

@app.route("/Sora yori mo Tooi Basho") #46
def owarimonogatari():
    return render_template("Sora yori mo Tooi Basho.html") 

@app.route("/Kenpuu Denki Berserk") #47
def owarimonogatari():
    return render_template("Kenpuu Denki Berserk.html") 

@app.route("/Slam Dunk") #48
def owarimonogatari():
    return render_template("Slam Dunk.html") 

@app.route("/Slam Dunk") #49
def owarimonogatari():
    return render_template("Slam Dunk.html") 

@app.route("/Slam Dunk") #50
def owarimonogatari():
    return render_template("Slam Dunk.html") 

@app.route("/Sci-Fi") #random scifi
def owarimonogatari():
    return render_template("scifi.html") 

@app.route("/Fantasy") #random fantasy
def owarimonogatari():
    return render_template("fantasy.html") 

@app.route("/Action") #random action
def owarimonogatari():
    return render_template("action.html") 

@app.route("/Horror") #random horror
def owarimonogatari():
    return render_template("Slam Dunk.html") 

@app.route("/Drama") #random drama
def owarimonogatari():
    return render_template("Slam Dunk.html") 

@app.route("/Super Natural") #random super natural
def owarimonogatari():
    return render_template("super natural.html") 

@app.route("/Comedy") #random comedy
def owarimonogatari():
    return render_template("comedy.html") 

@app.route("/Sports") #random sports
def owarimonogatari():
    return render_template("sports.html") 

@app.route("/Adventure") #random adventure
def owarimonogatari():
    return render_template("adventure.html") 

@app.route("/Romance") #random romance
def owarimonogatari():
    return render_template("romance.html") 

@app.route("/Slice Of Life") #random slice of life
def owarimonogatari():
    return render_template("slice_of_life.html") 
