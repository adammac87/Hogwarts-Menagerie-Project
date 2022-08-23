from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet
import repositories.vet_repository as vet_repository 

def save_pet(pet):
    sql = "INSERT INTO pets (name, breed, gender,birthday,owner_name, contact_details, notes,checked_in, vet_id) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s) RETURNING *"
    values = [pet.name, pet.breed, pet.gender, pet.birthday, pet.owner_name,pet.contact_details, pet.notes, pet.checked_in,pet.vet.id]
    results = run_sql(sql , values)
    id = results[0]["id"]
    pet.id = id
    return pet 

def delete_all_pets():
    sql = "DELETE FROM pets"
    run_sql(sql)

def delete_pet(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql ,values)


def update_pet(pet):
    sql = "UPDATE pets SET (name, breed, gender, birthday, owner_name,contact_details, notes,checked_in, vet_id) = (%s,%s,%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [pet.name, pet.breed, pet.gender, pet.birthday, pet.owner_name, pet.contact_details, pet.notes,pet.checked_in, pet.vet.id, pet.id]
    run_sql(sql, values)




def select_all_pets():
    pets = []
    sql = "SELECT * FROM pets"
    results= run_sql(sql)
    for row in results:
        vet = vet_repository.select_vet(row["vet_id"])
        pet = Pet(row["name"], row ["breed"], row ["gender"], row ["birthday"],row ["owner_name"], row ["contact_details"], row["notes"],row["checked_in"], vet , row ["id"])
        pets.append(pet)
    return pets

def select_pet(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = vet_repository.select_vet(result["vet_id"])
        pet = Pet(result["name"], result["breed"], result["gender"], result["birthday"], result["owner_name"], result["contact_details"], result["notes"] ,result["checked_in"],vet, result["id"])
    return pet 


# def show_all_vet_pets(pet):
#     pets = []
#     sql = "SELECT * FROM pets WHERE vet_id = %s"
#     results = run_sql(sql)
#     for row in results:
#         vet = vet_repository.select_vet(row["vet_id"])
#         pet = Pet(row["name"], row["breed"], row["gender"], row["birthday"], row["owner_name"],
#                 row["contact_details"], row["notes"], row["checked_in"], vet, row["id"])
#         pets.append(pet)
#     return pets




def search_by_petname(almost_name):
    pet_list = []
    sql = """SELECT * FROM pets
    WHERE lower(name) like %s"""
    values = ['%'+almost_name+'%']
    results = run_sql(sql, values)
    for row in results:
        vet = vet_repository.select_vet(row["vet_id"])
        pet = Pet(row["name"], row["breed"], row["gender"], row["birthday"], row["owner_name"]
                ,row["contact_details"], row["notes"], row["checked_in"], vet, row["id"])
        pet_list.append(pet)
    return pet_list


def show_all_vet_pets(vet_id):
    pet_list =[]
    sql = "SELECT * FROM pets WHERE vet_id =%s "
    values = [vet_id]
    results = run_sql(sql,values)
    for row in results:
        vet = vet_repository.select_vet(row["vet_id"])
        pet = Pet(row["name"], row["breed"], row["gender"], row["birthday"], row["owner_name"],
                row["contact_details"], row["notes"], row["checked_in"], vet, row["id"])
        pet_list.append(pet)
    return pet_list
