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


@pets_blueprint.route("/pets/new", methods = ['GET'])
def new_pet():
    vets = vet_repository.select_all_vets()
    return render_template("pets/new.html", all_vets=vets)




@pets_blueprint.route("/pets", methods = ['POST'])
def create_pet():
    name = request.form['name']
    breed = request.form['breed']
    gender = request.form['gender']
    birthday = request.form['birthday']
    owner_details = request.form['owner_details']
    contact_details = request.form['contact_details']
    notes = request.form['notes']
    vet = vet_repository.select_vet(request.form['vet_id'])
    new_pet = Pet(name,breed, gender,birthday, owner_details , contact_details, notes, vet)
    pet_repository.save_pet(new_pet)
    return redirect('/pets')

@pets_blueprint.route('/pets/delete/<id>', methods = ['POST'])
def delete(id):
    pet_repository.delete_pet(id)
    return redirect('/pets')