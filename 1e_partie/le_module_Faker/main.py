from faker import Faker
import time

fake = Faker(locale="ru-RU")
# for i in range(10):
    # print(fake.numerify(text= "%%%-#-%%%%-%%%%-##"))
    # print(fake.bothify(text= "Product number: ????-#######-$$ "))

while True:
    print(fake.name())
    print(fake.job())
    print(fake.credit_card_number(), fake.credit_card_expire(), fake.credit_card_security_code())
    print(fake.numerify(text= "%%%-#-%%%%-%%%%-##"))
    print(fake.bothify(text= "Product number: ????-#######"))
    print("*"*70)
    time.sleep(2)
    
# on peut meme generer le couleur avec faker
    """fonction faker
    fake.rgb_color()
    fake.hex_color()
    ??? pour obtenir de lettre aleatoire de A-Z
    ### nombre aleatoire de 1-9
    
    """
    