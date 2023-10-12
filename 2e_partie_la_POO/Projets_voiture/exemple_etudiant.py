class Voiture:
    essence = 100

    def afficher_reservoir(self):
        if self.essence <= 10:
            print("Vous n'avez bientôt plus d'essence")
        print(f"La voiture contient {self.essence}L d'essence")

    def faire_le_plein(self):
        if self.essence == 100:
            print("Vous avez déjà le plein")
        else:
            self.essence = 100
            self.afficher_reservoir()

    def roule(self, km):
        essence_necessaire = (km * 5) / 100
        if self.essence == 0:
            print("Vous n'avez plus d'essence, faites le plein")
        elif essence_necessaire > self.essence:
            print("Vous n'avez pas assez d'essence pour parcourir cette distance")
        else:
            self.essence -= essence_necessaire
            self.afficher_reservoir()