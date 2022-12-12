from flask import Flask, render_template, render_template_string
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/Chainsaw_Man") #1
def chainsaw_man():
    return render_template("chainsaw_man.html")

@app.route("/86_Eighty_Six") #2
def eighty_six():
    return render_template("86 Eighty Six.html")

@app.route("/Black_Clover") #3
def black_clover():
    return render_template("Black Clover.html")

@app.route("/Bleach") #4
def bleach():
    return render_template("Bleach.html")

@app.route("/Dr._Stone") #5 
def dr_stone():
    return render_template("Dr. Stone.html")

@app.route("/Fire_Force") #6
def fire_force():
    return render_template("Fire Force.html")

@app.route("/Fullmetal_Alchemist_Brotherhood") #7 
def fullmetal_alchemist_brotherhood():
    return render_template("Fullmetal Alchemist Brotherhood.html")

@app.route("/Kaguya-sama_wa_Kokurasetai") #8
def kaguya_sama_wa_kokurasetai():
    return render_template("Kaguya-sama wa Kokurasetai.html")

@app.route("/Made_in_Abyss") #9
def made_in_abyss():
    return render_template("Made in Abyss.html")

@app.route("/Mononoke_Hime") #10
def mononoke_hime():
    return render_template("Mononoke Hime.html")

@app.route("/Mushishi_Zoku_Shou") #11 
def mushishi_zoku_shou():
    return render_template("Mushishi Zoku Shou.html")

@app.route("/Mushoku_Tensei") #12
def mushoku_tensei():
    return render_template("Mushoku Tensei.html")

@app.route("/Nichijou") #13
def nichijou():
    return render_template("Nichijou.html")

@app.route("/Platinum_End") #14 
def platinum_end():
    return render_template("Platinum End.html")

@app.route("/Spy_x_Family") #15
def spy_x_family():
    return render_template("Spy x Family.html")

@app.route("/Steins;Gate") #16
def steins_gate():
    return render_template("Steins;Gate.html")

@app.route("/Cross_Game") #17
def cross_game():
    return render_template("cross_game.html")

@app.route("/Grand_Blue") #18
def grand_blue():
    return render_template("grand_blue.html")

@app.route("/Haikyu") #19
def haikyu():
    return render_template("haikyu.html")

@app.route("/Kimitsu_No_Yaiba") #20
def kimitsu_no_yaiba():
    return render_template("kimitsu no yaiba.html")

@app.route("/Owarimonogatari") #21
def owarimonogatari():
    return render_template("owarimonogatari.html") 

@app.route("/Hunter_x_Hunter") #22
def hunter_x_hunter():
    return render_template("Hunter x Hunter.html") 

@app.route("/Jujutsu_Kaisen") #23
def jujutsu_kaisen():
    return render_template("Jujutsu Kaisen.html") 

@app.route("/Koe_no_Katachi") #24
def koe_no_katachi():
    return render_template("Koe no Katachi.html") 

@app.route("/Legend_of_the_Galactic_Heroes") #25 
def legend_of_the_galactic_heroes():
    return render_template("Legend of the Galactic Heroes.html") 

@app.route("/Natsume_Yuujinchou_Roku") #26
def natsume_yuujinchou_roku():
    return render_template("Natsume Yuujinchou Roku.html") 
    
@app.route("/Ookami_Kodomo_no_Ame_to_Yuki") #27 
def ookami_kodomo_no_ame_to_yuki():
    return render_template("Ookami Kodomo no Ame to Yuki.html") 

@app.route("/Shigatsu_wa_Kimi_no_Uso") #28
def shigatsu_wa_kimi_no_uso():
    return render_template("Shigatsu wa Kimi no Uso.html") 

@app.route("/Summertime_Render") #29
def summertime_render():
    return render_template("Summertime Render.html") 

@app.route("/Suzumiya_Haruhi_no_Shoushitsu") #30 
def suzumiya_haruhi_no_shoushitsu():
    return render_template("Suzumiya.html") 

@app.route("/Tengen_Toppa_Gurren_Lagann") #31
def tengen_toppagurren_lagann():
    return render_template("Tengen Toppa Gurren Lagann.html") 

@app.route("/Uchuu_kyoudai") #32
def uchuu_kyoudai():
    return render_template("Uchuu_kyoudai.html") 

@app.route("/Zoku_Natsume_Yuujinchou") #33 
def zoku_natsume_yuujinchou():
    return render_template("Zoku Natsume Yuujinchou.html") 

@app.route("/Aria_The_Origination") #34
def aria_the_origination():
    return render_template("aria_the_origination.html") 

@app.route("/Banana_Fish") #35
def banana_fish():
    return render_template("banana_fish.html") 

@app.route("/Deathnote") #36
def deathnote():
    return render_template("deathnote.html") 
       
@app.route("/Code_Geass") #37
def cpde_geass():
    return render_template("Code_Geass.html") 

@app.route("/Hotaru_no_Haka") #38
def hotaru_no_haka():
    return render_template("Hotaru no Haka.html") 
       
@app.route("/Kimi_no_Na_Wa") #39
def kimi_no_na_wa():
    return render_template("Kimi_no_Na_Wa.html") 

@app.route("/Violet_Evergarden_Movie") #40
def violet_evergarden_movie():
    return render_template("Violet_Evergarden_Movie.html") 

@app.route("/Yakusoku_no_Neverland") #41
def yakusoku_no_neverland():
    return render_template("Yakusoku no Neverland.html") 

@app.route("/Perfect_Blue") #42
def perfect_blue():
    return render_template("Perfect Blue.html") 

@app.route("/One_Punch_Man") #43
def one_punch_mna():
    return render_template("One Punch Man.html") 

@app.route("/Slam_Dunk") #44
def slam_dunk():
    return render_template("Slam Dunk.html") 

@app.route("/Samurai_Champloo") #45
def samurai_champloo():
    return render_template("Samurai Champloo.html") 

@app.route("/Sora_yori_mo_Tooi_Basho") #46
def sora_yori_mo_tooi_basho():
    return render_template("Sora yori mo Tooi Basho.html") 

@app.route("/Kenpuu_Denki_Berserk") #47
def kenpuu_denki_berserk():
    return render_template("Kenpuu Denki Berserk.html") 

@app.route("/Gintama") #48
def gintama():
    return render_template("Gintama.html") 

@app.route("/Attack_on_Titan") #49
def attack_on_titan():
    return render_template("Attack on Titan.html") 

@app.route("/Kimi_no_Suizou_wo_Tabetai") #50
def kimi_no_suizou_wo_tabetai():
    return render_template("Kimi no Suizou wo Tabetai.html") 

@app.route("/Sci-Fi") #random scifi
def sci_fi():
    return render_template("sci_fi.html") 

@app.route("/Fantasy") #random fantasy
def fantasy():
    return render_template("fantasy.html") 

@app.route("/Action") #random action
def action():
    return render_template("action.html") 

@app.route("/Mystery") #random horror
def mystery():
    return render_template("mytery.html") 

@app.route("/Drama") #random drama
def drama():
    return render_template("drama.html") 

@app.route("/Super_Natural") #random super natural
def super_natural():
    return render_template("super natural.html") 

@app.route("/Comedy") #random comedy
def comedy():
    return render_template("comedy.html") 

@app.route("/Sports") #random sports
def sports():
    return render_template("sports.html") 

@app.route("/Adventure") #random adventure
def adventures():
    return render_template("adventure.html") 

@app.route("/Romance") #random romance
def romance():
    return render_template("romance.html") 

@app.route("/Slice_Of_Life") #random slice of life
def slice_of_life():
    return render_template("slice_of_life.html") 
