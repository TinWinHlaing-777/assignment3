from database import Database
from product import Product
from catagory import Catagory

class Display:
    id=None
    product_name=None
    price=None
    catagory_id=None
    catagory_name=None

    def __init__(self,tuple=None):
        if(tuple):
            self.id=tuple[0]
            self.product_name=tuple[1]
            self.price=tuple[2]
            self.catagory_id=tuple[3]
            self.catagory_name[4]

    @staticmethod
    def displayAll():
        Database._cursor.execute('Select * from products left joine catagories on products.catagory_id=catagories.id')
        add_list=[]
        for addTuple in Database._cursor.fetchall():
            add=Product(addTuple)
            add_list.append(add)
        return add_list