DROP TABLE pets;
DROP TABLE vets;

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR (255),
    speciality VARCHAR (255)
);

CREATE TABLE pets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    breed VARCHAR(255),
    gender VARCHAR(255),
    birthday VARCHAR(255),
    owner_name VARCHAR(255),
    contact_details VARCHAR(255),
    notes VARCHAR(255),
    vet_id INT NOT NULL REFERENCES vets(id) ON DELETE CASCADE
);