from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import vet_repository
from repositories import pet_repository
from models.pet import Pet
from models.vet import Vet

vets_blueprint = Blueprint("vets",__name__)


@vets_blueprint.route("/vets")
def show_all_vets():
    vets = vet_repository.select_all_vets()
    return render_template('vets/index.html', all_vets=vets)


@vets_blueprint.route("/vets/<id>", methods=['GET'])
def show_vet(id):
    vet = vet_repository.select_vet(id)
    return render_template('vets/show.html', vet=vet)


@vets_blueprint.route("/vets/new", methods=['GET'])
def new_vet():
    vets = vet_repository.select_all_vets()
    return render_template("vets/new.html", all_vets=vets)


@vets_blueprint.route("/vets", methods=['POST'])
def create_vet():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    speciality = request.form['speciality']

    new_vet = Vet(first_name, last_name, speciality)
    vet_repository.save_vet(new_vet)
    return redirect('/vets')


@vets_blueprint.route('/vets/delete/<id>', methods=['POST'])
def delete(id):
    vet_repository.delete_vet(id)
    return redirect('/vets')


@vets_blueprint.route("/vets/<id>/edit", methods=['GET'])
def edit_vet(id):
    vet = vet_repository.select_vet(id)
    return render_template('vets/edit.html', vet=vet)


@vets_blueprint.route("/vets/<id>", methods=['POST'])
def update_vet(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    speciality = request.form['speciality']
    new_vet = Vet(first_name, last_name, speciality, id)
    vet_repository.update_vet(new_vet)
    return redirect('/vets')
