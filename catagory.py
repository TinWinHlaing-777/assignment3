from database import Database

class Catagory:
    id=None
    name=None

    def __init__ (self,tuple_data=None):
        if(tuple_data):
            self.id=tuple_data[0]
            self.name=tuple_data[1]

    def save(self):
        Database.cursor.execute('insert into catagories(catagory_name) values(%s)', [self.name])
        Database._data.commit()
        self.id=Database.cursor.lastrowid
        self.display()

    def display(self):
        print(f'[{self.id}] -{self.name}')

    @staticmethod
    def find():
        Database.cursor.execute("Select * from products where catagory_id = %s ", )
        result=Database.cursor.fetchone()
        return Catagory(result)

    @staticmethod
    def get():
        Database.cursor.execute('Select * from catagories')
        catagory_list=[]
        for catagoryTuple in Database.cursor.fetchall():
            catagory=Catagory(catagoryTuple)
            catagory_list.append(catagory)
        return catagory_list
