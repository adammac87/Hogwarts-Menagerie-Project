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
    print("this is request.form",request.form)
    name = request.form['name']
    breed = request.form['breed']
    gender = request.form['gender']
    birthday = request.form['birthday']
    owner_details = request.form['owner_details']
    contact_details = request.form['contact_details']
    notes = request.form['notes']
    if "checked_in" in request.form.keys():
        checked_in = True
    else:
        checked_in = False  
    
    print(checked_in)
    vet = vet_repository.select_vet(request.form['vet_id'])
    new_pet = Pet(name,breed, gender,birthday, owner_details , contact_details, notes,checked_in,  vet)
    pet_repository.save_pet(new_pet)
    return redirect('/pets')

@pets_blueprint.route('/pets/delete/<id>', methods = ['POST'])
def delete(id):
    pet_repository.delete_pet(id)
    return redirect('/pets')

@pets_blueprint.route("/pets/<id>/edit", methods = ['GET'])
def edit_pet(id):
    pet = pet_repository.select_pet(id)
    vet = vet_repository.select_all_vets()
    return render_template('pets/edit.html', pet=pet, all_vets= vet )

@pets_blueprint.route("/pets/<id>", methods=['POST'])
def update_pet(id):
    name = request.form['name']
    breed = request.form['breed']
    gender = request.form['gender']
    birthday = request.form['birthday']
    owner_details = request.form['owner_details']
    contact_details = request.form['contact_details']
    notes = request.form['notes']
    if "checked_in" in request.form.keys():
        checked_in = True
    else:
        checked_in = False  
    vet = vet_repository.select_vet(request.form['vet_id'])
    new_pet = Pet(name,breed, gender,birthday, owner_details , contact_details,notes,checked_in, vet ,id)
    pet_repository.update_pet(new_pet)
    return redirect('/pets')



@pets_blueprint.route("/pets/<id>/notes", methods=['GET'])
def get_notes(id):
    pet = pet_repository.select_pet(id)
    return render_template('pets/notes.html', pet=pet)


@pets_blueprint.route("/pets/<id>/notes_edit", methods=['POST'])
def update_notes(id):
    notes = request.form['notes']
    pet =pet_repository.select_pet(id)
    pet.notes = notes
    pet_repository.update_pet(pet)
    return redirect('/pets')


@pets_blueprint.route("/pets/<id>/notes_edit", methods=['GET'])
def get_notes_get(id):
    pet = pet_repository.select_pet(id)
    return render_template('pets/note_edit.html', pet=pet)


@pets_blueprint.route("/pets/search", methods=['POST'])
def search_by_petname():
    almost_name =request.form['search']
    pet_list = pet_repository.search_by_petname(almost_name)
    return render_template('pets/index.html', all_pets=pet_list)



