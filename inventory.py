from tabulate import tabulate


# ========The beginning of the class==========
class Shoe:  # shoe class

    def __init__(self, country, code, product, cost, quantity): # attributes of 'Shoe"
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # 'get_cost' method that returns the cost of the shoes
    def get_cost(self):
        return self.cost

    # 'get_quantity' method that returns the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # returns the string representation of the shoe class
    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


# =============Shoe list===========
# an empty list to store the inventory and newly added inventory
shoe_list = []


# ==========Functions outside the class==============
# opens the inventory txt file, splits the lines with commas and
# then stores the data in 'shoe_list'
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as file:
            next(file) # skip line.. chegg helped with this line
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoe_list.append(shoe)
            print("Shoe inventory has been read!\n")
    except FileExistsError:
        print("The file you entered can not be found.\n")
    return shoe_list


# a function to capture new shoes to the inventory
# we ask for the country, code,product, cost, and quantity
# then  append this data to 'shoe-list'
def capture_shoes():
    cap_country = input("\nPlease enter country: ")
    cap_code = (input("Please enter code: "))
    cap_product = input("Please enter the product: ")
    cap_cost = float(input("Please enter the cost of the shoe: "))
    cap_quantity = int(input("Please enter the quantity of the shoe: "))

    shoe = Shoe(cap_country, cap_code, cap_product, cap_cost, cap_quantity)
    shoe_list.append(shoe)
    print("The shoe has been captured!\n")


# a function to view all the stock in the inventory
# we iterate over the 'shoe_list' and print the details of the shoe inventory
# in a table like format
def view_all():
    table = []  # empty list to store our shoe inventory details in table format
    for shoe in shoe_list:
        table.append([shoe.country, shoe.code, shoe.product, f"R{shoe.cost}", shoe.quantity])
        header = ["Country", "Code", "Product", "Cost", "Quantity"]  # headings of the inventory
        print(tabulate(table, headers=header))
    print("These are all the shoes we have in inventory!\n")


# a function to view the shoe with the lowest stock
# we loop through 'shoe_list' to find a shoe with minimun quantity
# if one is found, it will print the product and ask if you want to restock it
# if yes, the user inputs the new quantity of the shoe
def re_stock():
    min_qty = None
    min_shoe = None
    for shoe in shoe_list:
        if min_qty is None or shoe.quantity < min_qty:
            min_qty = shoe.quantity
            min_shoe = shoe
    if min_shoe:
        choice = input(f"The shop is low on {min_shoe.product} stock? Restock? Yes/No: ").lower()
        if choice == "yes":
            new_qty = int(input("Enter the updated stock quantity: \n"))
            min_shoe.quantity = new_qty
            with open('inventory.txt', 'r') as file:
                lines = file.readlines()
            with open('inventory.txt', 'a') as add:
                for line in lines:
                    data = line.strip().split(",")
                    if data[1] == min_shoe.code:
                        data[-1] = str(min_shoe.quantity)
                        line = ",".join(data) + "\n"
                        add.write(line)
            print("Shoe quantity updated. Thank you! :)\n")
    else:
        if choice == "no":
            print("cool :)\n")


# a function to find a shoe in the inventory by searching the code
# ask the user for the shoe code they want to search
# if the code the user enters matches one from the inventory text file found
# the shoe is printed
def search_shoe():
    search = input("Please enter the code of the shoe to search: ")
    found = []
    for shoe in shoe_list:
        if shoe.code == search:
            found.append(shoe)
            return found


# a function to find the value of each shoe
# we get the value of all the shoes one by one
def value_per_item():
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity  # for each shoe, this calulation will be used and diplayed as below
        print(f"Product {shoe.product} ({shoe.code}) has a value of: R{value}")


# a function to find the shoe with the highest quantity
# we loop through 'shoe_list' to find the shoe with the highest quantity
def highest_qty():
    high_qty = None
    max_shoe = None
    for shoe in shoe_list:
        if high_qty is None or shoe.quantity > high_qty:
            high_qty = shoe.quantity
            max_shoe = shoe
    if max_shoe:
        print(f"The highest quantity shoe is : {max_shoe.product}, code : {max_shoe.code}\n")

# ==========Main Menu=============
# a menu for the user to interact with
# where all the functions above will be used


shoe_list = read_shoes_data()


while True:
    print("^^^^^Welcome to Autumn Inventory System^^^^^^")
    print("1. Enter new shoe into system")
    print("2. View all inventory")
    print("3. Restock shoes")
    print("4. Search shoe")
    print("5. Value of each shoe")
    print("6. Highest shoe quantity")
    print("7. Exit")

# user enters a number that corresponds with what the user wants to do
    select = int(input("\nWhat do you want to do? Please enter number 1 - 7: "))

    if select == 1:
        capture_shoes()
    elif select == 2:
        view_all()
    elif select == 3:
        re_stock()
    elif select == 4:
        found = search_shoe()
        if found:
            print("\nFound the shoe: ")
            for shoe in found:
                print(shoe)
    elif select == 5:
        value_per_item()
    elif select == 6:
        highest_qty()
    elif select == 7:
        break
    else:
        print("Sorry. You have entered an invalid number. Please try again!")

# got some help from chegg
