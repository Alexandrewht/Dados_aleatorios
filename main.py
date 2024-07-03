from faker import Faker

fake = Faker(locale='pt-BR')

nome = fake.name()
email = fake.email()
usuario = fake.user_name()
endereco = fake.address()

print(f'Nome: {nome}')
print(f'E-mail: {email}')
print(f'Usuário: {usuario}')
print(f'Endereço: {endereco}')