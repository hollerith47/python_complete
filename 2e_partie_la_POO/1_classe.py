class Voiture:
  marque = "Lamborghini"
  couleur = "rouge"
voiture_01 = Voiture()
voiture_02 = Voiture()
# print(Voiture.marque)
# print(Voiture)
# print(Voiture.couleur)
Voiture.marque ="Porsche"
voiture_01.marque = "Peugeolt"
voiture_02.marque = "Volkswagen"

print(Voiture.marque)
print(voiture_01.marque)
print(voiture_02.marque)

class Employee():
    first_name = 'John'
    last_name ='Smith'
employee_01 = Employee()
employee_02 = Employee()
