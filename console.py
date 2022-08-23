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
vet5 = Vet("Rubeus", "Hagrid", "Dragons")
vet_repo.save_vet(vet5)
vet5 = Vet("Albus", "Dumbledoew", "Magical Birds")
vet_repo.save_vet(vet5)

pet1 = Pet("Fang", "Hound", "Male", "23.04.19", "Hagrid", "01532152" , "Good doggo",True, vet1)
pet_repo.save_pet(pet1)
pet1 = Pet("Scabbers", "Rat", "Male", "20.12.20", "Percy", "01322534",  "Bad Rat", True, vet1)
pet_repo.save_pet(pet1)
pet1 = Pet("Hedwig", "Owl", "Female", "28.07.21","Harry", "013225425" , "Snowy Owl", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Nagini", "Snake", "Female", "01.09.21","Tom", "013252545" , "Crazy Snake", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Buckbeak", "Gryphon", "Male", "11.06.21","Hagrid", "013182525" , "Remember to bow", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Fawkes", "Phoenix", "Male", "16.09.21","ALbus", "013251225" , "Ever living Bird", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Mrs Norris", "Cat", "Female", "11.09.21","Filch", "013258925" , "Mean Cat", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Norbert", "Dragon", "Male", "015.06.14","Hagrid", "013332525" , "Big ol Dragon", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Fluffy", "Cerebus", "Male", "01.09.21","Hagrid", "013429525" , "Three headed dog", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Aragog", "Spider", "Male", "15.04.13","Hagrid", "013295275" , "Horrible ,horrible spider", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Trevor", "Toad", "Male", "11.02.18","Neville", "014325425" , "Slimey", True, vet2)
pet_repo.save_pet(pet1)
pet1 = Pet("Errol", "Owl", "Male", "14.11.13","Bill", "013225525" , "Tiny Owl", True, vet2)
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


