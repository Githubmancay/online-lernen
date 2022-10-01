from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'smlNYpzwsdtriccrpc2FSAFGbdjwkofr'


@app.route("/")
def home():
    return render_template("home.html")

########################################### Home-Subpages ##########################################

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/Deutsch")
def Deutsch():
    return render_template("Deutsch.html")

@app.route("/Englisch")
def Englisch():
    return render_template("Englisch.html")

####################################################################################################



######################################### Deutsch-Subpages ######################################### 

@app.route("/Deutsch/Grammatik")
def Grammatik():
    return render_template("Deutsch/Grammatik.html")


####################################################################################################



######################################## Englisch-Subpages #########################################

@app.route("/Englisch/grammar")
def grammar():
    return render_template("Englisch/grammar.html")

################ grammar-Subpages #################

class AdverbForm1(FlaskForm):
    gap1 = StringField("She cries", validators=[DataRequired()])
    submit1 = SubmitField('Submit')

class AdverbForm2(FlaskForm):
    gap2 = StringField("Mike is quite", validators=[DataRequired()])
    submit2 = SubmitField('Submit')

# just a helper function to reduce code
def check_gap(input, expected):
    if input == expected:
        return "Nice work!"
    else:
        return "Holy guacamoly! Try again, pal!"

@app.route("/Englisch/grammar/adverbs", methods=("GET", "POST"))
def adverbs():
    form1 = AdverbForm1()
    message1 = ""
    if form1.validate_on_submit():
        message1 = check_gap(form1.gap1.data, "loud")
    form2 = AdverbForm2()
    message2 = ""
    if form2.validate_on_submit():
        message2 = check_gap(form2.gap2.data, "quiet")
        
    return render_template("Englisch/grammar/adverbs.html", 
                        form1=form1, message1=message1, 
                        form2=form2, message2=message2)



###################################################

@app.route("/Englisch/tenses")
def tenses():
    return render_template("Englisch/tenses.html")

@app.route("/Englisch/vocab")
def vocab():
    return render_template("Englisch/vocab.html")

@app.route("/Englisch/fail")
def fail():
    return render_template("Englisch/fail.html")

####################################################################################################

if __name__=="__main__":
    app.run(debug=True)