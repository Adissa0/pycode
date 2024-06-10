


# cinetic energy
# E = m*c**2
def main():
      m = int(input("m: "))
      print("E: ", energy(m))
      

def energy(mass, c=300000000):
      return mass*c**2

main()

