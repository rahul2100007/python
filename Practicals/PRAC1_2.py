import datetime as dt
full_name = input("Enter your full name: ")
dob = input("Enter your date of birth: ")
email = input("Enter your email address: ")
phone = input("Enter your phone number: ")
course = input("course in which you are study: ")
submit = input("Do you want to submit? (Y/N): ")

if submit == "Y" or submit == "y":
    time_stamp = dt.datetime.now()
    f_name=print("\nEntered Details : ")
    print("\tName: ", full_name)
    print("\tBirth Date: ", dob)
    print("\tEmail: ", email)
    print("\tPhone: ", phone)
    print("\tCourse: ", course)
    print("\tSubmitted Time: ", time_stamp)
    print("\nsubmitted successfully")

elif submit == "N" or submit == "n":
    print("Cancelled the submission")

else:
    print("Cancelled the submission due to invalid input")
