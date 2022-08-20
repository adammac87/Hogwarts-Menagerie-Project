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

pet1 = Pet("fido", "lab", vet1)
pet_repo.save(pet1)
pet2 = Pet("loki", "moggy", vet1)
pet_repo.save(pet2)
pet3= Pet("navi", "moggy", vet2)
pet_repo.save(pet3)


