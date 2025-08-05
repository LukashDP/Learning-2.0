first_password = input("Input first password: ")
second_password = input("Enter password again: ")
assert first_password == second_password, "passwords do not match "

print("Password match")