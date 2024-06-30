mails = ["bou", "antif"]
while True:
     mail = input("What's your email? ").strip().split('@')
     print(mail)
     print(len(mail))
     if not mail == []:
          get_usn = [i[0:-1] for i in mail if i.isalnum()]
          print(get_usn)
          print(len(get_usn))
          
     else:
          continue
     

     """
     
while True:
     mail = 
     if mail == "":
          continue
     else:
          
          usn = get_usn[0]
          if usn in mails:
               print("Good")
               break
     """

      


 
