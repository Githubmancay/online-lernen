from flask import Flask, render_template, url_for, request
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template ("home.html")

@app.route("/about")
def about():
    return render_template ("about.html")

@app.route("/Deutsch")
def Deutsch():
    return render_template ("Deutsch.html")

@app.route("/Englisch")
def Englisch():
    return render_template ("Englisch.html")

#Deutsch-Subpages
@app.route("/Grammatik")
def Grammatik():
    return render_template ("Grammatik.html")





#Englisch-Subpages
@app.route("/grammar")
def grammar():
    return render_template ("grammar.html")



@app.route("/tenses")
def tenses():
    return render_template ("tenses.html")

@app.route("/vocab")
def vocab():
    return render_template ("vocab.html")


@app.route("/adverbs")
def adverbs():
    return render_template ("grammar/adverbs.html")

@app.route("/fail")
def fail():
    return render_template ("fail.html")






# grammar/ adverbs --> forms
@app.route("/grammar/forms", methods=["POST"])
def forms():
    gap1 = request.form.get ("gap1")
    
    
    if not gap1:
        error_statement = "Holy guacamoly! Try again, pal!"
        return render_template ("/grammar/adverbs.html", error_statement= error_statement)
    
    title="Huch!"
    return render_template ("grammar/forms.html", gap1=gap1)

    if request.method == "POST":
        name=gap1 = request.form["name"]
        return render_template ("/grammar/adverbs.html")
    else:
        error_statement = "Holy guacamoly! Try again, pal!"
        return render_template ("/grammar/adverbs.html", error_statement= error_statement)

if __name__=="__main__":
    app.run(debug=True)