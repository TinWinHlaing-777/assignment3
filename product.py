from database import Database

class Product: 
    id=None
    product_name=None
    price=None
    catagory_id=None

    def __init__(self,tuple=None):
        if(tuple):
            self.id=tuple[0]
            self.product_name=tuple[1]
            self.price=tuple[2]
            self.catagory_id=tuple[3]

    def display(self):
        print(f'[{self.id}] - {self.product_name} - {self.price} - {self.catagory_id}')

    def save(self):
        Database.cursor.execute('insert into products set id=%s, product_name=%s, price=%s, catagory_id=%s',[self.id, self.product_name, self.price, self.catagory_id])
        Database._data.commit()
        self.id=Database.cursor.lastrowid
        self.catagory=Catagory.find(self.catagory_id)
        self.display()

    @staticmethod
    def find():
        Database.cursor.execute("Select * from products where catagory_id = %s ", )
        result=Database.cursor.fetchone()
        return Product(result)
        
    @staticmethod
    def get():
        Database.cursor.execute('Select * from products')
        product_list=[]
        for productTuple in Database.cursor.fetchall():
            product=Product(productTuple)
            product_list.append(product)
        return product_list