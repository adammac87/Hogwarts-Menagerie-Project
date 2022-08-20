from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet

def save(vet):
    sql = "INSERT INTO vets (first_name, last_name, speciality) VALUES (%s,%s,%s) RETURNING *"
    values = [vet.first_name, vet.last_name, vet.speciality]
    results = run_sql (sql,values)
    id = results[0]["id"]
    vet.id = id
    return vet 

def delete_all_vets():
    sql = "DELETE FROM vets"
    run_sql(sql)