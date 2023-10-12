class Voiture:
    voitures_crees = 0
    def __init__(self, marque) -> None:
        Voiture.voitures_crees +=1
        self.marque = marque

voiture_01 = Voiture("Lamborghini")
voiture_02 = Voiture("Porsche")

print(Voiture.voitures_crees)