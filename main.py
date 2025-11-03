# main.py
from utils import greet_user

def main():
    #name = "GitHub Actions"
    name = "GitHub Actions - Version 2"
    message = greet_user(name)
    print(message)

if __name__ == "__main__":
    main()
