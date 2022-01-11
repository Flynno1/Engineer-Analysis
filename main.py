
from website import create_app

app = create_app()


# def retrieve():
#     token = input("please enter your github user token: ")
#     gh = Github(token)
#     usr = gh.get_user()
#     print("your username is: " + usr.login)


if __name__ == '__main__':
    app.run(debug=True)
    # retrieve()
