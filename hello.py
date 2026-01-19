print("Hello world")
print("Login successful")

try:
    Username = input("Enter username: ")
except EOFError:
    Username = "jenkins_default"


