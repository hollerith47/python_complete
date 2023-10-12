import re
import string

class User:
	def __init__(self, first_name: str, last_name: str, phone_number: str = "", address: str = ""):
		self.first_name = first_name
		self.last_name = last_name
		self.phone_number = phone_number
		self.address = address
	
	# on va ici definir une fonction de la facon dont on va representer notre fonction
	def __repr__(self):
		return f"User({self.first_name}, {self.last_name})"
	
	def __str__(self):
		return f"{self.full_name}\n{self.phone_number}\n{self.address}"
	
	# 	on va utiliser une proprietee dynamique pour generer le fullname
	@property
	def full_name(self):
		return f'{self.first_name} {self.last_name}'
	
	def _checks(self):
		self._check_phone_number()
		self._check_names()
		
	def _check_phone_number(self):
		phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
		if len(phone_number) < 10 or not phone_number.isdigit():
			raise ValueError(f"Numéro de téléphone {self.phone_number} invalide.")
		# print(phone_number)
	
	def _check_names(self):
		if not (self.first_name and self.last_name):
			raise ValueError("Le prénom et le nom de famille ne doivent pas être vides.")
		caractere_special = string.punctuation + string.digits
		# print(caractere_special)
		for character in self.first_name+self.last_name:
			if character in caractere_special:
				raise ValueError(f"Nom invalide {self.full_name}.")

if __name__ == "__main__":
	from faker import Faker
	fake = Faker(locale="fr_FR")
	for _ in range(10):
		user = User(first_name=fake.first_name(),
					last_name=fake.last_name(),
					phone_number=fake.phone_number(),
					address=fake.address())
		print(user)
		user._checks()
		"""print(user.full_name)
		user._check_phone_number()
		user._check_names()
		#grace a la methode checks on n'a plus besoin d'ecrire toute ses fonctions
		"""
		print("--" * 25)
