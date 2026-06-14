import time

print("VPS Config")
time.sleep(3)
print("Before entering, please  enter your special admin keys")

api_insert = input("Enter your admin keys/api keys from the admin")

if api_insert == "kPh798o2":
  print("Api correct, Welcome User")
  time.sleep(3)
  print("""Please select
  1. Check internal storage
  2. Check Ping server
  3. Delete server
  4. Current DDoS attack""")
  user_select = input("Select from 1-4")

  if user_select == "1":
    print("""Internal Storage:
    Storage = 250GB had been used from 2TB
    RAM = 5GB had been used from 128GB""")

  elif user_select == "2":
    print("Current Ping: 12ms")

  elif user_select == "3":
    print("Deleting server starting....")
    time.sleep(10)
    print("Server has been deleted.")

  elif user_select == "4":
    print("""Here is the current DDoS Attack:
    1. DDoS Attack from 128.267.78.9
    2. DDoS Attack from 136.666.66.6""")
  else:
    print("invalid input")

else:
  print("API Invalid")
