from models.pet import Pet
from models.vet import Vet
import repositories.pet_repository as pet_repo
import repositories.vet_repository as vet_repo

vet1 = Vet("bill", "one", "dogs")
vet_repo.save(vet1)