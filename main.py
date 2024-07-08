from faker import Faker

fake = Faker('pt-BR')

# Gera um nome completo
name = fake.name()

# Usa o nome para criar um e-mail mais realista
# Exemplo: pega o primeiro nome e o último nome, remove espaços e adiciona um domínio
first_name = name.split()[0].lower()
last_name = name.split()[-1].lower()
email = f"{first_name}.{last_name}@exemplo.com"

# Gera outros dados
user = fake.user_name()
password = fake.password()
bio = fake.paragraph(nb_sentences=3)

# Exibe os dados gerados
print(f'Nome: {name}')
print(f'E-mail: {email}')
print(f'Usuário: {user}')
print(f'Senha: {password}')
print(f'Bio: {bio}')
