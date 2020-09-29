import pickle  # "Pickle" library for file management,


class Food:  # Class Food some contains the inventory of the pantry.

    def products(self, name, quantity, unit):  # Constructor for food.
        self.name = name
        self.quantity = quantity
        self.unit = unit
        print("Food has been added to the pantry: ", self.name)

    def __str__(self):
        return "{} {} {}".format(self.name, self.quantity, self.unit)


class ListFood:  # Class some contain the list of the food.
    foods = []  # List for food in the pantry.

    def __init__(self):  # Open a file for save the inventory.
        listOfFood = open("file", "ab+")
        listOfFood.seek(0)
        try:
            self.foods = pickle.load(listOfFood)
            print("Loaded {} products of the file".format(len(self.foods)))
        except:
            print("File is empty")
        finally:
            listOfFood.close()  # Close the file.
            del(listOfFood)

    def addFood(self, f):  # Function for add food.
        f = Food()  # Variable F some will be an object.
        f.name = input("Food to add: ")  # Here the user add the products.
        while True:
            try:
                f.quantity = float(input("Amount of the product: "))
            except ValueError:
                print("Sorry, you have to give the amount in number.")
                continue
            else:
                break
        f.unit = input("Unit of the product? (for example st, kg, etc.): ")
        self.foods.append(f)  # Will add the objetct to the list.
        self.saveFood()  # Call the method for save food.

    def showFood(self):  # Function for show the food.
        for f in self.foods:  # For for read all in the food list.
            print(f)

    def saveFood(self):  # Function for save the food.
        listOfFood = open("file", "wb")  # Open file in write mode.
        pickle.dump(self.foods, listOfFood)  # Add the list to the file.
        listOfFood.close()  # Close file.
        del(listOfFood)

    def showInfoFood(self):  # Function for show the food.
        print("Inventory contains: ")
        for f in self.foods:  # Read all the items in the list.
            print(f)


def saveRecept():  # Function for save receips.
    recetary = {}  # One dictionary.
    continue1 = 1  # Input of the data and exception for errors.
    while continue1 == 1:
        name = input("Name for the receipe: ")
        continue2 = 1
        while True:
            try:
                portion = int(input("How many portions: "))
            except ValueError:
                print("Sorry, you have to give a number of portions.")
                continue
            else:
                break
        recipes = []  # List for save the data inside of dict.
        while continue2 == 1:
            ingredient = input("Ingredient: ")
            while True:
                try:
                    quantity = int(input("Amount of the ingredient: "))
                except ValueError:
                    print("Sorry, you have to give the amount in number.")
                    continue
                else:
                    break
            unit = input("what unit is the ingredient(for example kg, st): ")
            indication = input("Add a description to the recip: ")
            recipes.append((ingredient, quantity, unit, indication))
            while True:
                try:
                    continue2 = int(input("For add other ingredient press 1 or press to 2 to finish[1/2]: "))
                except ValueError:
                    print("Wrong option.")
                    continue
                else:
                    break
        recetary[name, portion] = recipes  # Save the information.
        while True:
            try:
                continue1 = int(input("For add other receip press 1 or press to 2 to finish[1/2]: "))
            except ValueError:
                print("Wrong option.")
                continue
            else:
                break
    return recetary


def showRecipes(recetary):  # Function for show recipes with parameter "recetary".
    print("Recipes saved")
    for name in recetary:  # Read all the dict.
        print("Recipe:", name)
        for ingredient, quantity, unit, indication in recetary[name]:
            print(ingredient, quantity, unit, indication)


def saveReceip(recetary):  # Function for save recipes with parameter "recetary".
    r_file = open("recei.txt", "ab")  # File for save the data.
    pickle.dump(recetary, r_file)  # Add the data to the file.
    r_file.close()  # Close the file.
    del(r_file)


def fileIn():  # Function some receive the information.
    recipesSaved = []  # A List some will save the read of the file.
    with (open("recei.txt", "rb")) as openfile:  # Read the file.
        while True:
            try:
                recipesSaved.append(pickle.load(openfile))
            except EOFError:
                break
    print(recipesSaved)
    openfile.close()  # Close the File.


myList = ListFood()  # Variable some will be an object of ListFood.

while True:  # Menu
    try:
        print("------Menu------")
        print("1.- Add food to the pantry")
        print("2.- Add Receips ")
        print("3.- Show food in the pantry")
        print("4.- Show saved receips")
        print("5.- Exit")

        option = int(input("What do you want to do: "))
    except ValueError:
        print("Please write a valid option")
    else:
        if option < 0 or option > 5:
            print("Is not a valid option")
            continue
    if option == 1:  # Options of the menu.
        food = Food()
        myList.addFood(food)
    elif option == 2:
        recetary = saveRecept
        saveReceip(recetary)
    elif option == 3:
        myList.showInfoFood()
    elif option == 4:
        fileIn()
    elif option == 5:
        break
    else:
        print("Invalid option")
print("Thnaks for use this program of pantry")
# In case the user put a wrong option in the input.
