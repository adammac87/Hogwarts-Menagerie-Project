from models.pet import Pet
from models.vet import Vet
import repositories.pet_repository as pet_repo
import repositories.vet_repository as vet_repo



# vet_repo.delete_all_vets()
# pet_repo.delete_all_pets()



vet1 = Vet("Sirius", "Black", "Dogs")
vet_repo.save_vet(vet1)
vet2 = Vet("Hermoine", "Granger", "Cats")
vet_repo.save_vet(vet2)
vet3 = Vet("Harry", "Potter", "Owls")
vet_repo.save_vet(vet3)
vet4 = Vet("Ron ", "Weasley", "Rats")
vet_repo.save_vet(vet4)
vet5 = Vet("Neville", "Longbottom", "Toads")
vet_repo.save_vet(vet5)

pet1 = Pet("Fang", "Hound", "Male", "23.04.19", "Hagrid", "0153252" , "Good doggo",True, vet1)
pet_repo.save_pet(pet1)
pet1 = Pet("Scabbers", "Rat", "Male", "20.12.20", "Percy", "0132534",  "Big Kitty", True, vet1)
pet_repo.save_pet(pet1)
pet1 = Pet("Hedwig", "Owl", "Female", "01.09.21","Harry", "0132525" , "Small Kitty", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Nagini", "Snake", "Female", "01.09.21","Tom", "0132525" , "Small Kitty", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Buckbeak", "Gryphon", "Male", "01.09.21","Hagrid", "0132525" , "Small Kitty", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Fawkes", "Phoenix", "Male", "01.09.21","ALbus", "0132525" , "Small Kitty", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Mrs Norris", "Cat", "Female", "01.09.21","Filch", "0132525" , "Small Kitty", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Aragog", "Spider", "Male", "01.09.21","hagrid", "0132525" , "Small Kitty", True, vet2)
pet_repo.save_pet(pet1)


# print(vet_repo.select_vet(1).__dict__)
# print(pet_repo.select_pet(1).__dict__)

# print(pet_repo.select_pet(1).vet.__dict__) 
# -goes into vet object

# pet = Pet("1","2","3","4","5","6","7",vet2,2)
# pet_repo.update_pet(pet)
# # ---updates a pet

# vet = Vet("1","2","3",1 )
# vet_repo.update_vet(vet)   
# ---updates a vet

# vet_repo.delete_vet(1)


# print(vet_repo.select_vet(2).__dict__)


# for pet in pet_repo.select_all_pets():
#     print(pet.__dict__)


# for vet in vet_repo.select_all_vets():
#     print(vet.__dict__)


