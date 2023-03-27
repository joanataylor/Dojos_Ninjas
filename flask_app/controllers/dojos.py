from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app import app


@app.route("/")
@app.route("/dojos")
def dojo():
    results = Dojo.get_all()
    return render_template('dojos.html', results=results)


@app.route("/dojo_create", methods=["POST"])
def old_ninja():
    Dojo.save(request.form)
    return redirect("/dojos")


@app.route('/ninjas/<int:id>')
def display_ninjas(id):
    data = {
        "id": id
    }
    ninjas = Dojo.onedojo(data)
    return render_template("dojo1.html", ninjas=ninjas)


# @app.route('/dojos/destroy/<int:id>')
# def destroy(id):
#     data = {
#         'id': id
#     }
#     Dojo.destroy(data)
#     return redirect('/dojos')
