print("Login")
MAX_ATTEMPTS = 3
username="sims"
user_age="35"
for MAX_ATTEMPTS in range(1,MAX_ATTEMPTS, +1):
    user=input("Enter Username: ")
    age=input("Enter Age: ")
    if user== username and age==user_age:
        print("Login Successful")
        break
    else:
        print("Login Failed, you have", MAX_ATTEMPTS, "attempts remaining")
else:
    print("Sorry you ran out of attempts ")



