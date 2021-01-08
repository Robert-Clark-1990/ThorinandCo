import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

"""
import os standard python library, flask class & render_template function
"""
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

"""
storing it in a variable called app.
first argument of the Flask class is the application's module - our package
as its a single module, we use __name__ which is a built in python variable
decorator "/"browses the root directory & triggers the function underneath
"""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        flash(
            "Thanks {}, we have received your message!".format(
                request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)


"""
if name is equal to main the we run our app with the following arguments
__main__ is the name of default module in python
using os library we get the IP environment if it exists or default if not found
it will be the same as PORT but we're casting it as an int with default of 5000
specify debug as true because it allows us to debuy our code much easier

DO NOT HAVE debug=True in a product application or project submission
As this can allow arbitrary code to be run, which is a security flaw
only have it on while testing in development
"""
