from flask import Flask, render_template, request, url_for, redirect, session, send_from_directory
import random
from flask_wtf import Form, FlaskForm
from wtforms import Form, TextField, BooleanField, validators, PasswordField, SelectField, SubmitField
#Imports from local files
from goodies import pick_hero
from schemes import schemes
from baddies import masterminds, henchmen, villains
from paired_baddies import bad_pair
from baddies_spec import hench_no_rand
from paired_villains import paired_villains
import pymysql.cursors

app = Flask(__name__)

def split_line(text):
    # split the text
    words = text.split()

num_players = [('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
class Players(Form):
    num_play = SelectField(label = "Choose the Number of Players", choices = num_players)

class Playing(Form):
    num_play = SelectField(label = "Choose the Number of Players", choices = num_players)

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        form = Players(request.form)

        if request.method == "POST":
            num_play = form.num_play.data

            pick_scheme, scheme_hero, scheme_att = schemes()

            # #Picks a Mastermind and their sidekick NEED TO PAIR MASTERS AND VILLAINS
            pick_master = masterminds()
            pick_sidekick = villains()

            #Picks another Villain based on sidekick value
            alt_villain_text = 'Spider-Infected or Doombot Rolled, Villain is:'
            if pick_sidekick == 'Spider-Infected':
                alt_villain = villains()
            elif pick_sidekick == 'Doombot Legion':
                alt_villain = villains()
            else:
                alt_villain = None

            #Chooses another mastermind if conditions met
            alt_master2_text = 'Dark Alliance or Secret Wars Rolled, Mastermind 2 is:'
            if pick_scheme == 'Dark Alliance':
                pick_master2 = masterminds()
            elif pick_scheme == 'Secret Wars':
                pick_master2 = masterminds()
            else:
                pick_master2 = None

            #Picks a Villain
            if int(num_play) > 1:
                pick_villain1 = villains()

            #Picks a second Villain if more than 2 players
            villain2_text = 'The Second Villain is:'
            if int(num_play) > 2:
                pick_villain2 = villains()
            elif int(num_play) <= 2:
                pick_villain2 = None

            #If players more than 4 pick another villain
            villain3_text = 'The Third Villain is:'
            if int(num_play) > 4:
                pick_villain3 = villains()
            elif int(num_play) <= 4:
                pick_villain3 = None

            #Picks the first henchmen if the conditions are met
            pick_hench1_text = 'Henchmen is:'
            if pick_villain1 != 'Spider-Infected':
                pick_hench1 = henchmen()
            elif pick_villain1 != 'Doombot Legion':
                pick_hench1 = henchmen()
            else:
                pick_hench1 = None

            # #Picks a second henchmen if the players are more than 3
            hench2_text = 'Henchmen is:'
            if int(num_play) > 3:
                pick_hench2 = henchmen()
            elif int(num_play) <= 3:
                pick_hench2 = None

            #Picks the 3rd henchman depending on conditions
            hench3_text = 'Henchmen is:'
            if pick_scheme == 'Predict Future Crime':
                pick_hench3 = henchmen()
            elif pick_scheme == 'Change the Outcome of WWII':
                pick_hench3 = henchmen()
            elif pick_scheme == 'Deadlands Hordes Charge the Wall':
                pick_hench3 = henchmen()
            elif pick_scheme == 'Steal the Weaponized Plutonium':
                pick_hench3 = henchmen()
            elif pick_scheme == 'Smash Two Dimensions Together':
                pick_hench3 = henchmen()
            else:
                pick_hench3 = None

            #Picks Four default heros
            samples = random.sample(pick_hero(), 5)
            hero_1, hero_1_att = samples[0]
            hero_2, hero_2_att = samples[1]
            hero_3, hero_3_att = samples[2]
            hero_4, hero_4_att = samples[3]

            # #If more than 2 players and scheme is Super hero Civil War picks another hero
            hero5_text = 'The fifth hero is:'
            if int(num_play) == 2 and pick_scheme == 'Super Hero Civil War':
                hero_5, hero_5_att = ssamples[4]
            else:
                hero_5 = None
                hero_5_att = None

            #If players = 5 picks another hero
            hero6_text = 'The last hero is:'
            if int(num_play) == 5:
                hero_6, hero_6_att = pick_hero()
            else:
                hero_6 = None
                hero_6_att = None

            # #Sets the number of Bystanders
            bystand = 0
            if pick_scheme == "Replace Earth's Leaders with Killbots":
                bystand = 18
            elif pick_scheme == 'Midtown Bank Robbery':
                bystand = 12
            elif int(num_play) == 2:
                bystand = 2
            elif int(num_play) == 3:
                bystand = 8
            elif int(num_play) == 4:
                bystand = 8
            elif int(num_play) == 5:
                bystand = 12

            return render_template('results.html', form = form, pick_scheme = pick_scheme, pick_master = pick_master, alt_villain_text = alt_villain_text,
                                pick_sidekick = pick_sidekick, pick_villain1 = pick_villain1, pick_villain2 = pick_villain2, alt_master2_text = alt_master2_text,
                                pick_villain3 = pick_villain3, pick_hench1 = pick_hench1, pick_hench2 = pick_hench2, hero_1 = hero_1, hero_2 = hero_2, hero_3 = hero_3,
                                villain2_text = villain2_text, villain3_text = villain3_text, pick_hench1_text = pick_hench1_text, hench2_text = hench2_text,
                                hench3_text = hench3_text, hero5_text = hero5_text, hero6_text = hero6_text, hero_1_att = hero_1_att, hero_2_att = hero_2_att,
                                hero_3_att = hero_3_att, hero_4_att = hero_4_att, hero_5_att = hero_5_att, hero_6_att = hero_6_att,
                                hero_4 = hero_4, bystand = bystand, hero_5 = hero_5, hero_6 = hero_6, pick_master2 = pick_master2, pick_hench3 = pick_hench3, alt_villain = alt_villain)
        return render_template('index.html', form = form)
    except Exception as e:
        return(str(e))

        try:
            form = playing(request.form)

            if request.method == "POST":
                num_play = form.num_play.data

                pick_scheme, scheme_hero, scheme_attribute = schemes()

                master1, who_led, oppenent = bad_pair()
                oppenent, oppenent_att = oppenent

                #Picks another Villain based on sidekick value
                alt_villain_text = 'Spider-Infected or Doombot Legion Rolled, Villain is:'
                if who_led == 'Spider-Infected':
                    alt_villain = villains()
                elif who_led == 'Doombot Legion':
                    alt_villain = villains()
                else:
                    alt_villain = None

                #Chooses another mastermind if conditions met
                pick_master2_text = 'Dark Alliance or Secret Wars Rolled, Mastermind two is:'
                if pick_scheme == 'Dark Alliance':
                    pick_master2 = masterminds()
                elif pick_scheme == 'Secret Wars':
                    pick_master2 = masterminds()
                else:
                    pick_master2 = None

                #Picks a Villain
                if int(num_play) > 1:
                    pick_villain1, vill_hero1 = paired_villains()
                    vill_hero1, vill_hero1_att = vill_hero1

                #Picks a second Villain if more than 2 players
                pick_villain2_text = 'Villain Three is:'
                if int(num_play) > 2:
                    pick_villain2 = villains()
                elif int(num_play) <= 2:
                    pick_villain2 = None

                #If players more than 4 pick another villain
                pick_villain3_text = 'Last Villain is:'
                if int(num_play) > 4:
                    pick_villain3 = villains()
                elif int(num_play) <= 4:
                    pick_villain3 = None

                #Picks the first henchmen if the conditions are met
                pick_hench1_text = 'Henchmen is:'
                if pick_villain1 != 'Spider-Infected':
                    pick_hench1 = henchmen()
                elif pick_villain1 != 'Doombot Legion':
                    pick_hench1 = henchmen()
                else:
                    pick_hench1 = None

                # #Picks a second henchmen if the players are more than 3
                pick_hench2_text = 'Henchmen is:'
                pick_hench2_hero_text = 'Next hero is:'
                if int(num_play) > 3:
                    pick_hench2, pick_hero_hench2 = hench_no_rand()
                    pick_hero_hench2, pick_hero_hench2_att = pick_hero_hench2
                elif int(num_play) <= 3:
                    pick_hench2 = None
                    pick_hero_hench2 = None
                    pick_hero_hench2_att = None

                #Picks the 3rd henchman depending on conditions
                pick_hench3_text = 'Last Henchmen is:'
                if pick_scheme == 'Predict Future Crime':
                    pick_hench3 = henchmen()
                elif pick_scheme == 'Change the Outcome of WWII':
                    pick_hench3 = henchmen()
                elif pick_scheme == 'Deadlands Hordes Charge the Wall':
                    pick_hench3 = henchmen()
                elif pick_scheme == 'Steal the Weaponized Plutonium':
                    pick_hench3 = henchmen()
                elif pick_scheme == 'Smash Two Dimensions Together':
                    pick_hench3 = henchmen()
                else:
                    pick_hench3 = None

                #Picks Four default heros
                hero_4 = pick_hero()
                hero_4, hero_4_att = hero_4

                # #If more than 2 players and scheme is Super hero Civil War picks another hero
                hero_5_text = 'The fifth hero is:'
                if int(num_play) == 2 and pick_scheme == 'Super Hero Civil War':
                    hero_5 = pick_hero()
                    hero_5, hero_5_att = hero_5
                else:
                    hero_5 = None
                    hero_5_att = None

                my_hero_list_6 = []
                #If players = 5 picks another hero
                if int(num_play) == 5:
                    hero_6, hero_6_att = pick_hero()
                    hero_6_att = split_line(hero_6_att)
                    hero_6_att.append(my_hero_list_6)
                    hero_6_att = my_hero_list_6

                else:
                    hero_6 = None
                    hero_6_att = None

                bystand = 0
                if pick_scheme == "Replace Earth's Leaders with Killbots":
                    bystand = 18
                elif pick_scheme == 'Midtown Bank Robbery':
                    bystand = 12
                elif int(num_play) == 2:
                    bystand = 2
                elif int(num_play) == 3:
                    bystand = 8
                elif int(num_play) == 4:
                    bystand = 8
                elif int(num_play) == 5:
                    bystand = 12

                return render_template('ordered.html', form = form, bystand = bystand, master1 = master1, who_led = who_led, alt_villain_text = alt_villain_text,
                                    oppenent = oppenent, alt_villain = alt_villain, pick_master2 = pick_master2, pick_master2_text = pick_master2_text,
                                    pick_scheme = pick_scheme, scheme_hero = scheme_hero, scheme_attribute = scheme_attribute, pick_villain2_text = pick_villain2_text,
                                    pick_hench2 = pick_hench2, pick_hero_hench2 = pick_hero_hench2, pick_villain1 = pick_villain1, pick_hench1_text = pick_hench1_text,
                                    vill_hero1 = vill_hero1, pick_villain2 = pick_villain2, pick_villain3 = pick_villain3, pick_villain3_text = pick_villain3_text,
                                    pick_hench1 = pick_hench1, pick_hench3 = pick_hench3, hero_4 = hero_4, hero_5 = hero_5, pick_hero_hench2_att = pick_hero_hench2_att,
                                    hero_6 = hero_6, pick_hench2_hero_text = pick_hench2_hero_text, pick_hench2_text = pick_hench2_text, pick_hench3_text = pick_hench3_text,
                                    oppenent_att = oppenent_att, vill_hero1_att = vill_hero1_att, hero_4_att = hero_4_att, hero_5_text = hero_5_text, hero_5_att = hero_5_att,
                                    hero_6_att = hero_6_att)
            return render_template('index.html', form = form)
        except Exception as e:
            return(str(e))

@app.route("/heroes_win")
def heroes_win():
    return render_template('heroes_win.html')

@app.route("/villains_win")
def villains_win():
    return render_template('villains_win.html')

@app.route("/vote_hero_page", methods=["GET", "POST"])
def vote_hero():
    conn = pymysql.connect(host='legendarydb.cnmjscz500v8.us-east-1.rds.amazonaws.com', user='jouwstrab', passwd='Asl33p12!', db='legendaryroller')
    try:
        if request.method == "POST":
            with conn.cursor() as cursor:
                sql = "INSERT INTO `voting` (`hero`) VALUES (%s)"
                cursor.execute(sql, (1))
                conn.commit()
                conn.close()
        return redirect(url_for('heroes_win'))
    except Exception as e:
        return(str(e))

@app.route("/vote_villain_page", methods=["GET", "POST"])
def vote_villain():
    conn = pymysql.connect(host='legendarydb.cnmjscz500v8.us-east-1.rds.amazonaws.com', user='jouwstrab', passwd='Asl33p12!', db='legendaryroller')
    try:
        if request.method == "POST":
            with conn.cursor() as cursor:
                sql = "INSERT INTO `voting` (`villain`) VALUES (%s)"
                cursor.execute(sql, (1))
                conn.commit()
                conn.close()
        return redirect(url_for('villains_win'))
    except Exception as e:
        return(str(e))

@app.route("/results", methods=["GET", "POST"])
def results():
    try:
        form = Players(request.form)

        if request.method == "POST":
            num_play = form.num_play.data

            pick_scheme, scheme_hero, scheme_att = schemes()

            # #Picks a Mastermind and their sidekick NEED TO PAIR MASTERS AND VILLAINS
            pick_master = masterminds()
            pick_sidekick = villains()

            #Picks another Villain based on sidekick value
            alt_villain_text = 'Spider-Infected or Doombot Rolled, Villain is:'
            if pick_sidekick == 'Spider-Infected':
                alt_villain = villains()
            elif pick_sidekick == 'Doombot Legion':
                alt_villain = villains()
            else:
                alt_villain = None

            #Chooses another mastermind if conditions met
            alt_master2_text = 'Dark Alliance or Secret Wars Rolled, Mastermind 2 is:'
            if pick_scheme == 'Dark Alliance':
                pick_master2 = masterminds()
            elif pick_scheme == 'Secret Wars':
                pick_master2 = masterminds()
            else:
                pick_master2 = None

            #Picks a Villain
            if int(num_play) > 1:
                pick_villain1 = villains()

            #Picks a second Villain if more than 2 players
            villain2_text = 'The Second Villain is:'
            if int(num_play) > 2:
                pick_villain2 = villains()
            elif int(num_play) <= 2:
                pick_villain2 = None

            #If players more than 4 pick another villain
            villain3_text = 'The Third Villain is:'
            if int(num_play) > 4:
                pick_villain3 = villains()
            elif int(num_play) <= 4:
                pick_villain3 = None

            #Picks the first henchmen if the conditions are met
            pick_hench1_text = 'Henchmen is:'
            if pick_villain1 != 'Spider-Infected':
                pick_hench1 = henchmen()
            elif pick_villain1 != 'Doombot Legion':
                pick_hench1 = henchmen()
            else:
                pick_hench1 = None

            # #Picks a second henchmen if the players are more than 3
            hench2_text = 'Henchmen is:'
            if int(num_play) > 3:
                pick_hench2 = henchmen()
            elif int(num_play) <= 3:
                pick_hench2 = None

            #Picks the 3rd henchman depending on conditions
            hench3_text = 'Henchmen is:'
            if pick_scheme == 'Predict Future Crime':
                pick_hench3 = henchmen()
            elif pick_scheme == 'Change the Outcome of WWII':
                pick_hench3 = henchmen()
            elif pick_scheme == 'Deadlands Hordes Charge the Wall':
                pick_hench3 = henchmen()
            elif pick_scheme == 'Steal the Weaponized Plutonium':
                pick_hench3 = henchmen()
            elif pick_scheme == 'Smash Two Dimensions Together':
                pick_hench3 = henchmen()
            else:
                pick_hench3 = None

            #Picks Four default heros
            hero_1, hero_1_att = pick_hero()
            hero_2, hero_2_att = pick_hero()
            hero_3, hero_3_att = pick_hero()
            hero_4, hero_4_att = pick_hero()

            # #If more than 2 players and scheme is Super hero Civil War picks another hero
            hero5_text = 'The fifth hero is:'
            if int(num_play) == 2 and pick_scheme == 'Super Hero Civil War':
                hero_5, hero_5_att = pick_hero()
            else:
                hero_5 = None
                hero_5_att = None

            #If players = 5 picks another hero
            hero6_text = 'The last hero is:'
            if int(num_play) == 5:
                hero_6, hero_6_att = pick_hero()
            else:
                hero_6 = None
                hero_6_att = None

            # #Sets the number of Bystanders
            bystand = 0
            if pick_scheme == "Replace Earth's Leaders with Killbots":
                bystand = 18
            elif pick_scheme == 'Midtown Bank Robbery':
                bystand = 12
            elif int(num_play) == 2:
                bystand = 2
            elif int(num_play) == 3:
                bystand = 8
            elif int(num_play) == 4:
                bystand = 8
            elif int(num_play) == 5:
                bystand = 12

            return render_template('results.html', form = form, pick_scheme = pick_scheme, pick_master = pick_master, alt_villain_text = alt_villain_text,
                                pick_sidekick = pick_sidekick, pick_villain1 = pick_villain1, pick_villain2 = pick_villain2, alt_master2_text = alt_master2_text,
                                pick_villain3 = pick_villain3, pick_hench1 = pick_hench1, pick_hench2 = pick_hench2, hero_1 = hero_1, hero_2 = hero_2, hero_3 = hero_3,
                                villain2_text = villain2_text, villain3_text = villain3_text, pick_hench1_text = pick_hench1_text, hench2_text = hench2_text,
                                hench3_text = hench3_text, hero5_text = hero5_text, hero6_text = hero6_text, hero_1_att = hero_1_att, hero_2_att = hero_2_att,
                                hero_3_att = hero_3_att, hero_4_att = hero_4_att, hero_5_att = hero_5_att, hero_6_att = hero_6_att,
                                hero_4 = hero_4, bystand = bystand, hero_5 = hero_5, hero_6 = hero_6, pick_master2 = pick_master2, pick_hench3 = pick_hench3, alt_villain = alt_villain)
        return render_template('results.html', form = form)
    except Exception as e:
        return(str(e))


class OrderedPlay(Form):
    num_play = SelectField(label = "Choose the Number of Players", choices = num_players)

@app.route("/ordered", methods=["GET", "POST"])
def ordered():
    try:
        form = OrderedPlay(request.form)

        if request.method == "POST":
            num_play = form.num_play.data

            pick_scheme, scheme_hero, scheme_attribute = schemes()

            master1, who_led, oppenent = bad_pair()
            oppenent, oppenent_att = oppenent

            #Picks another Villain based on sidekick value
            alt_villain_text = 'Spider-Infected or Doombot Legion Rolled, Villain is:'
            if who_led == 'Spider-Infected':
                alt_villain = villains()
            elif who_led == 'Doombot Legion':
                alt_villain = villains()
            else:
                alt_villain = None

            #Chooses another mastermind if conditions met
            pick_master2_text = 'Dark Alliance or Secret Wars Rolled, Mastermind two is:'
            if pick_scheme == 'Dark Alliance':
                pick_master2 = masterminds()
            elif pick_scheme == 'Secret Wars':
                pick_master2 = masterminds()
            else:
                pick_master2 = None

            #Picks a Villain
            if int(num_play) > 1:
                pick_villain1, vill_hero1 = paired_villains()
                vill_hero1, vill_hero1_att = vill_hero1

            #Picks a second Villain if more than 2 players
            pick_villain2_text = 'Villain Three is:'
            if int(num_play) > 2:
                pick_villain2 = villains()
            elif int(num_play) <= 2:
                pick_villain2 = None

            #If players more than 4 pick another villain
            pick_villain3_text = 'Last Villain is:'
            if int(num_play) > 4:
                pick_villain3 = villains()
            elif int(num_play) <= 4:
                pick_villain3 = None

            #Picks the first henchmen if the conditions are met
            pick_hench1_text = 'Henchmen is:'
            if pick_villain1 != 'Spider-Infected':
                pick_hench1 = henchmen()
            elif pick_villain1 != 'Doombot Legion':
                pick_hench1 = henchmen()
            else:
                pick_hench1 = None

            # #Picks a second henchmen if the players are more than 3
            pick_hench2_text = 'Henchmen is:'
            pick_hench2_hero_text = 'Next hero is:'
            if int(num_play) > 3:
                pick_hench2, pick_hero_hench2 = hench_no_rand()
                pick_hero_hench2, pick_hero_hench2_att = pick_hero_hench2
            elif int(num_play) <= 3:
                pick_hench2 = None
                pick_hero_hench2 = None
                pick_hero_hench2_att = None

            #Picks the 3rd henchman depending on conditions
            pick_hench3_text = 'Last Henchmen is:'
            if pick_scheme == 'Predict Future Crime':
                pick_hench3 = henchmen()
            elif pick_scheme == 'Change the Outcome of WWII':
                pick_hench3 = henchmen()
            elif pick_scheme == 'Deadlands Hordes Charge the Wall':
                pick_hench3 = henchmen()
            elif pick_scheme == 'Steal the Weaponized Plutonium':
                pick_hench3 = henchmen()
            elif pick_scheme == 'Smash Two Dimensions Together':
                pick_hench3 = henchmen()
            else:
                pick_hench3 = None

            #Picks Four default heros
            hero_4 = pick_hero()
            hero_4, hero_4_att = hero_4

            # #If more than 2 players and scheme is Super hero Civil War picks another hero
            hero_5_text = 'The fifth hero is:'
            if int(num_play) == 2 and pick_scheme == 'Super Hero Civil War':
                hero_5 = pick_hero()
                hero_5, hero_5_att = hero_5
            else:
                hero_5 = None
                hero_5_att = None

            #If players = 5 picks another hero
            if int(num_play) == 5:
                hero_6, hero_6_att = pick_hero()
            else:
                hero_6 = None
                hero_6_att = None

            bystand = 0
            if pick_scheme == "Replace Earth's Leaders with Killbots":
                bystand = 18
            elif pick_scheme == 'Midtown Bank Robbery':
                bystand = 12
            elif int(num_play) == 2:
                bystand = 2
            elif int(num_play) == 3:
                bystand = 8
            elif int(num_play) == 4:
                bystand = 8
            elif int(num_play) == 5:
                bystand = 12

            return render_template('ordered.html', form = form, bystand = bystand, master1 = master1, who_led = who_led, alt_villain_text = alt_villain_text,
                                oppenent = oppenent, alt_villain = alt_villain, pick_master2 = pick_master2, pick_master2_text = pick_master2_text,
                                pick_scheme = pick_scheme, scheme_hero = scheme_hero, scheme_attribute = scheme_attribute, pick_villain2_text = pick_villain2_text,
                                pick_hench2 = pick_hench2, pick_hero_hench2 = pick_hero_hench2, pick_villain1 = pick_villain1, pick_hench1_text = pick_hench1_text,
                                vill_hero1 = vill_hero1, pick_villain2 = pick_villain2, pick_villain3 = pick_villain3, pick_villain3_text = pick_villain3_text,
                                pick_hench1 = pick_hench1, pick_hench3 = pick_hench3, hero_4 = hero_4, hero_5 = hero_5, pick_hero_hench2_att = pick_hero_hench2_att,
                                hero_6 = hero_6, pick_hench2_hero_text = pick_hench2_hero_text, pick_hench2_text = pick_hench2_text, pick_hench3_text = pick_hench3_text,
                                oppenent_att = oppenent_att, vill_hero1_att = vill_hero1_att, hero_4_att = hero_4_att, hero_5_text = hero_5_text, hero_5_att = hero_5_att,
                                hero_6_att = hero_6_att)
        return render_template('ordered.html', form = form)
    except Exception as e:
        return(str(e))

@app.route("/questions", methods=["GET", "POST"])
def questions():
    return render_template('questions.html')

@app.route("/random_FAQ", methods=["GET", "POST"])
def randomFAQ():
    return render_template('random_FAQ.html')

@app.route("/ordered_FAQ", methods=["GET", "POST"])
def ordered_FAQ():
    return render_template('ordered_FAQ.html')

if __name__ == "__main__":
    app.run(debug=True)
