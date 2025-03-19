import random

print('Witaj oto gra "Guesser" Miłej gry!')

lista = []


random_number = random.randint(1, 100)

while True:
  try:
    number = int(input("Zgadnij liczbę:  "))
  except ValueError:
    print('ERROR! - Wpisz liczbe!')
    break

  if random_number == number:
    lista.append(number)
    print(f'Brawo! Oto historia twoich odpowiedzi: {lista}')
    break
  elif number > random_number:
    lista.append(number)
    print('Twoja liczba jest za duża!')
  elif number < random_number:
    lista.append(number)
    print('Twoja liczba jest za mała!')
