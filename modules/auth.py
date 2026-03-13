def login(user_name, password):
    logo = ["╭━━━┳╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮","┃╭━╮┃┃╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃","┃╰━━┫╰━┳━━┳━╯┣━━┳╮╭╮╭╮╰╮╭╋━━┳━┳╮╭┳┳━╮╭━━┫┃","╰━━╮┃╭╮┃╭╮┃╭╮┃╭╮┃╰╯╰╯┃╱┃┃┃┃━┫╭┫╰╯┣┫╭╮┫╭╮┃┃","┃╰━╯┃┃┃┃╭╮┃╰╯┃╰╯┣╮╭╮╭╯╱┃╰┫┃━┫┃┃┃┃┃┃┃┃┃╭╮┃╰╮","╰━━━┻╯╰┻╯╰┻━━┻━━╯╰╯╰╯╱╱╰━┻━━┻╯╰┻┻┻┻╯╰┻╯╰┻━╯"]
    name = input("Enter your name:\n")
    while name != user_name:
        name = input("Name invalid, pls try again\n").strip()

    passwd = input("Enter your password\n" ).strip()
    if passwd == password:
        for line in logo:
            print(f"{line}")
    else:
        print(f"U dont know passwd?)"", Bye bye")
        exit()


if __name__ == "__main__":
    user_name = "admin"
    password = "secret"
    print(f"Right now u in shadod terminal\n")
    login(user_name, password)
