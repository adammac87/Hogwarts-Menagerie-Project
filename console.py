from models.pet import Pet
from models.vet import Vet
import repositories.pet_repository as pet_repo
import repositories.vet_repository as vet_repo



# vet_repo.delete_all_vets()
# pet_repo.delete_all_pets()



vet1 = Vet("Bill", "Ross", "Cats")
vet_repo.save_vet(vet1)
vet2 = Vet("Anna", "Mitchell", "Dogs")
vet_repo.save_vet(vet2)

pet1 = Pet("Fido", "Lab", "Male", "23.04.19", "Adam", "0153252" , "Good doggo", vet1)
pet_repo.save_pet(pet1)
pet1 = Pet("Loki", "Moggy", "Male", "20.12.20","Adam", "0132534" , "Big Kitty", vet1)
pet_repo.save_pet(pet1)
pet1 = Pet("Navi", "Moggy", "Female", "01.09.21","Adam", "0132525" , "Small Kitty", vet2)
pet_repo.save_pet(pet1)


# print(vet_repo.select_vet(1).__dict__)
# print(pet_repo.select_pet(1).__dict__)

# print(pet_repo.select_pet(1).vet.__dict__) 
# -goes into vet object

pet = Pet("1","2","3","4","5","6","7",vet2,2)
pet_repo.update_pet(pet)
# ---updates a pet

# vet = Vet("1","2","3",1 )
# vet_repo.update_vet(vet)   
# ---updates a vet

# vet_repo.delete_vet(1)


# print(vet_repo.select_vet(2).__dict__)


# for pet in pet_repo.select_all_pets():
#     print(pet.__dict__)


# for vet in vet_repo.select_all_vets():
#     print(vet.__dict__)


