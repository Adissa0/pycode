def main():
      number = get_number()
      mean(number)
      

def get_number():
      while True:
            n = int(input("What is n? "))
            if n > 0:
                  return n

      
def mean(n):
      for _ in range(n):
            print("mean")
            
main()