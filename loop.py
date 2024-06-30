# request for username: bank account

mails = ["bou", "antif"]
while True:
     mail = input("What's your email? ").strip().split('@')
     if mail == []:
          continue
     else:
          get_usn = [i[0:-1] for i in mail if i.isalnum()]
          usn = get_usn[0]
          if usn in mails:
               print("Good")
               break
               
     
     