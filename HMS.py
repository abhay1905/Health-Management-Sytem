Clients = ['Abhay', 'Ankit', 'Shiwani', 'Bunny']

def getdate():
    import datetime
    return datetime.datetime.now()

print(getdate())

def entryfood(name):
    with open(f"{name}_food.txt", "a") as file:
        file.write(f"[{getdate()}]: {f}\n")


def entryex(name):
    with open(f"{name}_ex.txt", "a") as file:
        file.write(f"{e}\n")


def getfood(name):
    with open(f"{name}_food.txt", "r") as file:
        for line in file:
            print(line)

def getex(name):
    with open(f"{name}_ex.txt", "r") as file:
        for line in file:
            print(line)

while True:
    print("What do you want do?")
    print("Choose an option")
    print("Choose 1 to log entry")
    print("Choose 2 to retieve entries")

    o1 = int(input())


    print("Enter the name of client:")
    print("Abhay, Shiwani, Ankit, Bunny")

    name = input().capitalize()
    while True:
        if name in Clients:
            print("choose 1 for food")
            print("choose 2 for exercise")
            o2 = int(input())

        else:
            print("Invalid Input")
            break

            

        if o1==1 and o2==1:
            print("Enter Food")
            f = input()
            entryfood(name)

        elif o1==1 and o2==2:
            print("Enter Exercise")
            e = input()
            entryex(name)

        elif o1==2 and o2==1:
            getfood(name)

        else:
            getex(name)
        print("exit?")
        choice=input("y/n\n")
        if choice == "y":
            break

    break
