from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import vet_repository
from repositories import pet_repository
from models.pet import Pet

pets_blueprint = Blueprint("pets",__name__)

@pets_blueprint.route("/pets")
def show_all_pets():
    pets = pet_repository.select_all_pets()
    return render_template('pets/index.html', all_pets= pets)


@pets_blueprint.route("/pets/<id>", methods=['GET'])
def show_pet(id):
    pet = pet_repository.select_pet(id)
    return render_template('pets/show.html', pet=pet)
