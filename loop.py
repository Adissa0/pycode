
def name():
      name = ""
      while name == "":
            name = input("Entrer un name? ")
      return name
# if loop
def age(person):
      age = 0
      while age == 0:
            age_str = input(person + ": Entrer votre age? ")
            try:
                  age = int(age_str)
            except:
                  print("Erreur!!!")
      return age

def taille(name):
      taille = 0
      while taille == 0:
            taille = input(name + ": Votre taille? ")
      if taille != 0:
            print(f"J'ai {taille} m")
      return taille

def info(name, age, taille):
      print(name + ": Vous avez {} ans et l'an prochain vous aurez {} ans".format(age, age+1))
      print()
for i in range(1, 4):
      print(i, end=" ")
      name0 = name()
      age0 = age(name0)
      taille0 = taille(name0)
      info(name0, age0, taille0)


      


