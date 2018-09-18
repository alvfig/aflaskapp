#!/usr/bin/python


import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField, validators


app = Flask(__name__)
#app.config["SECRET_KEY"] = "Klassified"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", default="Klassified")
csrf = CSRFProtect(app)


class AnyForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired()])
    phone = StringField("Phone", [validators.InputRequired(), validators.Regexp(r"^\d{4,13}$")])
    email = StringField("Email", [validators.InputRequired(), validators.Email()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def home():
    #form = AnyForm(request.form)
    #if request.method == "POST" and form.validate():
    form = AnyForm()
    if form.validate_on_submit():
        pass
    return render_template("home.html", form=form, msg="Register")


if __name__ == "__main__":
    #app.secret_key = "Klassified"
    app.run()
