import random
import os 
import string 
from datetime import datetime

Current_file = "current_password.txt"
Archive_file = "archieve_password.txt"

length = int(input("Enter password length:"))

chars = string.ascii_letters + string.digits + string.punctuation
new_password = ""

for i in range(length):
    new_password += random.choice(chars)

if os.path.exists(Current_file):
    with open(Current_file,"r") as f:
        old_password = f.read().strip()

    if old_password:
        with open(Archive_file,"a") as af:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            af.write(f"{timestamp} | {old_password}\n")

with open(Current_file,"w") as f:
    f.write(new_password)

print("New Password Generated:",new_password)
print("Previous password archived successfully ")            