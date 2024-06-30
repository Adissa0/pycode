# variables
mails = ["bouraima", "antif"]
username = ""
# conversion to username & verification
while username not in mails:
      mail = input("What's your mail? ").split('@')
      try:
            username = [i[0:-1] for i in mail if i.isalnum()]
      except IndexError as err:
            print(err, "Error found !!!")
            continue
      else:
            if username[0] not in mails:
                  print(username)
                  continue
            
