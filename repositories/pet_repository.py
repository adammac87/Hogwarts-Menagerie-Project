from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet
import repositories.vet_repository as vet_repository 

def save(pet):
    sql = "INSERT INTO pets (name, breed, vet_id) VALUES (%s, %s, %s) RETURNING *"
    values = [pet.name, pet.breed, pet.vet.id]
    results = run_sql(sql , values)
    id = results[0]["id"]
    pet.id = id
    return pet 

def delete_all_pets():
    sql = "DELETE FROM pets"
    run_sql(sql)