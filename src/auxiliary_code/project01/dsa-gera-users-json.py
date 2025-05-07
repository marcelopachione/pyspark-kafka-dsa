# Projeto 1 - Pipeline PySpark Para Extrair, Transformar e Carregar Arquivos JSON em Banco de Dados

# Imports
import os
import random
import json
import uuid
from datetime import datetime, timedelta

# Generate random CPF
def generate_cpf():
    return f"{random.randint(100,999)}.{random.randint(100,999)}.{random.randint(100,999)}-{random.randint(10,99)}"

# Generate date of birth
def generate_birth_date(age):
    today = datetime.today()
    birth_date = today.replace(year=today.year - age) - timedelta(days=random.randint(0, 364))
    return birth_date.strftime("%d/%m/%Y")

# Generate random phone number
def generate_phone():
    ddd = random.choice(['11', '21', '31', '41', '51', '61', '71', '81', '84', '85', '98', '95'])
    number = f"{random.randint(90000, 99999)}-{random.randint(1000, 9999)}"
    return f"+55 {ddd} {number}"

# Generate full name and nationality
def generate_full_name_and_nationality():
    brazilian_first_names = [
        "Lucas", "Mariana", "Thiago", "Fernanda", "Paulo", "Amanda",
        "Miguel", "Isabela", "Matheus", "Camila", "Gabriel", "Laura", "Enzo", "Helena"
    ]
    international_first_names = [
        "Liam", "Emma", "Noah", "Olivia", "Ethan", "Sophia", "Ava", "James", "Isabella", "John", "Alice", "Carol", "Grace", "Hank", "Ivy", "Jack"
    ]
    last_names = [
        "Silva", "Souza", "Oliveira", "Costa", "Santos", "Pereira", "Lima", "Carvalho",
        "Martins", "Almeida", "Gomes", "Rodrigues", "Barbosa", "Fernandes", "Dias",
        "Ribeiro", "Freitas", "Moreira", "Castro", "Melo", "Vieira", "Moura", "Rezende"
    ]

    if random.random() < 0.7:
        first_name = random.choice(brazilian_first_names)
        nationality = "Brazilian"
    else:
        first_name = random.choice(international_first_names)
        nationality = random.choice(["American", "British", "Canadian", "German", "French"])

    last_name = random.choice(last_names)
    return f"{first_name} {last_name}", nationality

# Updated main function to include UUID
def generate_user_data(num_records):
    
    cities = [
        "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Curitiba", "Florianópolis",
        "Recife", "Salvador", "Fortaleza", "Natal", "João Pessoa", "Aracaju", "Palmas", "Teresina",
        "Manaus", "Belém", "Macapá", "Boa Vista", "Porto Velho", "Rio Branco", "Brasília", "Cuiabá", "Goiânia", "Campo Grande"
    ]
    
    professions = [
        "Systems Analyst", "Software Engineer", "Project Manager", "Finance Director", "Support Technician",
        "HR Coordinator", "Data Scientist", "Backend Developer", "Frontend Developer", "Solutions Architect",
        "Doctor", "Nurse", "Lawyer", "Teacher", "Graphic Designer", "Accountant", "Salesperson", "Driver",
        "Administrative Assistant", "Business Consultant", "Psychologist", "Pharmacist", "Civil Engineer", "Architect", "Nutritionist"
    ]
    
    marital_statuses = ["Single", "Married", "Divorced", "Widowed"]
    genders = ["Male", "Female", "Other"]

    for _ in range(num_records):
        user_id = str(uuid.uuid4())
        name, nationality = generate_full_name_and_nationality()
        age = random.randint(20, 60)
        birth_date = generate_birth_date(age)
        cpf = generate_cpf()
        phone = generate_phone()
        email = f"{name.split()[0].lower()}@dsa.com"
        salary = random.randint(3000, 20000)
        city = random.choice(cities)
        profession = random.choice(professions)
        marital_status = random.choice(marital_statuses)
        gender = random.choice(genders)
        is_active = random.choice([True, False])

        yield {
            "uuid": user_id,
            "name": name,
            "age": age,
            "birth_date": birth_date,
            "cpf": cpf,
            "nationality": nationality,
            "email": email,
            "phone": phone,
            "salary": salary,
            "city": city,
            "profession": profession,
            "marital_status": marital_status,
            "gender": gender,
            "active": is_active
        }

# Generate 1000 user records
sample_data = list(generate_user_data(1000))

# Output file path
# output_file_path = '../../../storage/dsa-usuarios.json'
output_file_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'storage', 'dsa-usuarios.json')
output_file_path = os.path.abspath(output_file_path)

# Write data to JSON file, one record per line
with open(output_file_path, 'w') as file:
    for record in sample_data:
        json.dump(record, file)
        file.write('\n')


