from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet

def save_vet(vet):
    sql = "INSERT INTO vets (first_name, last_name, speciality) VALUES (%s,%s,%s) RETURNING *"
    values = [vet.first_name, vet.last_name, vet.speciality]
    results = run_sql (sql,values)
    id = results[0]["id"]
    vet.id = id
    return vet 

def delete_all_vets():
    sql = "DELETE FROM vets"
    run_sql(sql)

def select_all_vets():
    vets =[]
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row["first_name"], row["last_name"],row["speciality"], row["id"])
        vets.append(vet)
    return vets

def select_vet(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id =%s"
    values = [id]
    result = run_sql(sql , values)[0]

    if result is not None:
        vet = Vet(result["first_name"], result["last_name"], result["speciality"] ,result["id"])
    return vet

def delete_vet(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update_vet(vet):
    sql = "UPDATE vets SET (first_name, last_name, speciality) = (%s,%s,%s) WHERE id =%s"
    values = [vet.first_name, vet.last_name, vet.speciality, vet.id]
    run_sql(sql, values)