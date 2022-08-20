from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import vet_repository
from repositories import pet_repository
from models.pet import Pet

vets_blueprint = Blueprint("vets",__name__)


@vets_blueprint.route("/vets")
def show_all_vets():
    vets = vet_repository.select_all_vets()
    return render_template('vets/index.html', all_vets=vets)


@vets_blueprint.route("/vets/<id>", methods=['GET'])
def show_vet(id):
    vet = vet_repository.select_vet(id)
    return render_template('vets/show.html', vet=vet)
