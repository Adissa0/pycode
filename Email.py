
# # ask for email
# mails = input("What's your name? ").split('@')

# # checkout of input
# for mail in mails:
#       if mail.isalnum():
#print(mail[0:-1])
 


# variables
mails = ["bouraima", "antif"]
username = ""
# conversion to username & verification
while username not in mails:
      mail = input("What's your mail? ").strip().split('@')
      username = [i[0:-1] for i in mail if i.isalnum()]
      if username==[] or username[0] not in mails:
            print(username)
      #       continue
      # else:
      #       break
      
      # elif :
      #       print("Found error !!!")
            

      


 
