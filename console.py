from models.pet import Pet
from models.vet import Vet
import repositories.pet_repository as pet_repo
import repositories.vet_repository as vet_repo



# vet_repo.delete_all_vets()
# pet_repo.delete_all_pets()



vet1 = Vet("bill", "ross", "Cats")
vet_repo.save(vet1)
vet2 = Vet("anna", "mitchell", "dogs")
vet_repo.save(vet2)

pet1 = Pet("fido", "lab", "m", "15.11.87", "adam", "0132525" , "sdgsdgdsgsdgsdgdgs", vet1)
pet_repo.save(pet1)
pet1 = Pet("loki", "moggy", "m", "20.12.19","adam", "01352353" , "s32566236gsdgdgs", vet1)
pet_repo.save(pet1)
pet1 = Pet("navi", "moggy", "m", "01.23.87","adam", "0132525" , "ffhfddfhsdgsdgdgs", vet2)
pet_repo.save(pet1)

