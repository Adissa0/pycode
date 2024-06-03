
# code
# calculator
# calculate a+b
def sum():
      a = b = ""
      while not (a.isdigit() and b.isdigit()):
            a = input("0. Entrez? ")
            b = input("1. Entrez? ")
      print(f"La somme de {a}+{b} est {int(a) + int(b)}")

sum()


