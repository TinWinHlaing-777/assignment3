from database import Database
from product import Product
from catagory import Catagory
from add import Display


def addNewProduct():
    product=Product()
    product.id=input("Please eneter the id of product: ")
    product.product_name=input("Enter the name of product: ")
    product.price=input("Please enter the price of product: ")
    product.catagory_id=input("Enter the catagory id of product: ")
    product.save()

def displayAllProduct():
    products=Product.get()
    for product in products:
        product.display()

def addNewCatagory():
    catagory=Catagory()
    catagory.catagory_name=input("Please enter the catagory name: ")
    catagory.save()

def displayAllCatagories():
    catagory_list=Catagory.get()
    for catagory in catagory_list:
        catagory.display()

def displayByCatagory():
    id=input("Enter the id of catagory id: ")
    catagory=Catagory.find(id)
    print(catagory)

def displayWholeTable():
    add_list=Display.displayAll()
    for display in add_list:
        display.displayAll()

def viewMenu():
    try:
        option=input(
            f'Shop Inventory App\n'
            f'[1] Add Catagories\n'
            f'[2] Add Products\n'
            f'[3] View Catagories\n'
            f'[4] View Products\n'
            f'[5] View by Catagory Id\n'
            f'[6] View Overall Table\n'
            f'Press any Key to exit from the program\n'
            f'Please Enter your choice:\n'
        )
        if (option=='1'):
            addNewCatagory()
        elif (option=='2'):
            addNewProduct()
        elif (option=='3'):
            displayAllCatagories()
        elif (option=='4'):
            displayAllProduct()
        elif (option=='5'):
            displayByCatagory()
        elif (option=='6'):
            displayWholeTable()
        choice=input("Do you want to do again?y/n\n")
        if choice=='y':
            viewMenu()
        else:
            print("Bye Bye")
    except KeyboardInterrupt:
        print("Bye Bye")

viewMenu()