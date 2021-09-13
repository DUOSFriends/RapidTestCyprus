import random
import time

# Title
print("Rapid Test Maker")

# Random Numbers
random_id = random.randint(231, 897)
random_special_id = random.randint(4200000, 4260000)

# Variables Questions
name = input("What is your name?: ")
surname = input("What is your last name?: ")
date_of_birth = input("What is your date of birth? (DD/MM/YY): ")
today_date = input("Enter today's date (DD/MM/YY): ")
current_time = input("Enter current time: ")

# Your Test
print("Your new rapid test:")

# Result
print(name[0] + "." + surname[0] + ".(AΔT/ID xxx" + str(random_id) + ")" + "(HM.ΓEN./DOB: " + date_of_birth + ")" + " TO AΠOTEΛEΣMA THΣ EΞETAΣHΣ ΣAΣ ΣTIΣ " + today_date + "," + current_time + " ΓIA TH NOΣO COVID-19 EINAI APNHTIKO.https://bit.ly/37lU6Dv YOUR TEST RESULT ON " + today_date + "," + current_time + " FOR COVID-19 IS NEGATIVE. https://bit.ly/3mhDil9 UNIQUE ID:" + str(random_special_id) + ", MINISTRY OF HEALTH, CY")


while True:
    time.sleep(5)
