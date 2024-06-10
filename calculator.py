
def main():
      while not (n1.isdigit() and n2.isdigit()):
            a = input("What is a? ")
            b = input("What is b? ")
      print(f"{a} + {b} equal {sum(a, b)}")
      

def sum(n1, n2):
      return int(n1)+int(n2)


main()
 

