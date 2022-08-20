from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet
import repositories.vet_repository as vet_repository 

def save(pet):
    sql = "INSERT INTO pets (name, breed, gender,birthday,owner_name, contact_details, notes, vet_id) VALUES (%s, %s, %s,%s,%s,%s,%s,%s) RETURNING *"
    values = [pet.name, pet.breed, pet.gender, pet.birthday, pet.owner_name,pet.contact_details, pet.notes, pet.vet.id]
    results = run_sql(sql , values)
    id = results[0]["id"]
    pet.id = id
    return pet 

def delete_all_pets():
    sql = "DELETE FROM pets"
    run_sql(sql)