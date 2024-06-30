
# ask user for their name
def name():
      while True:
            name = input("What's your name? ").strip()
            lstr = [i.isdigit() for i in name]
            if not (True in lstr or lstr == []):
                  print("Good")
                  break
            else:
                  print("Digit number found or Enter is emphy")

            
name()

# ask user for their age

# ask user for their size

# infoperson()
