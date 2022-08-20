from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet
import repositories.vet_repository as vet_repository 

def save_pet(pet):
    sql = "INSERT INTO pets (name, breed, gender,birthday,owner_name, contact_details, notes, vet_id) VALUES (%s, %s, %s,%s,%s,%s,%s,%s) RETURNING *"
    values = [pet.name, pet.breed, pet.gender, pet.birthday, pet.owner_name,pet.contact_details, pet.notes, pet.vet.id]
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
    sql = "UPDATE pets SET (name, breed, gender, birthday, owner_name,contact_details, notes, vet_id) = (%s,%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [pet.name, pet.breed, pet.gender, pet.birthday, pet.owner_name, pet.contact_details, pet.notes, pet.vet.id, pet.id]
    run_sql(sql, values)




def select_all_pets():
    pets = []
    sql = "SELECT * FROM pets"
    results= run_sql(sql)
    for row in results:
        vet = vet_repository.select_vet(row["vet_id"])
        pet = Pet(row["name"], row ["breed"], row ["gender"], row ["birthday"],row ["owner_name"], row ["contact_details"], row["notes"], vet , row ["id"])
        pets.append(pet)
    return pets

def select_pet(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = vet_repository.select_vet(result["vet_id"])
        pet = Pet(result["name"], result["breed"], result["gender"], result["birthday"], result["owner_name"], result["contact_details"], result["notes"] ,vet, result["id"])
    return pet 