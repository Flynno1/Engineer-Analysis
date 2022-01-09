import requests

def retrieve():
    name = input("please enter the username you wish to search: ")
    string = "https://api.github.com/users/" + name
    response = requests.get(string)
    print(response.json())


if __name__ == '__main__':
    retrieve()
