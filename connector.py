import mysql.connector

def connect():
    Inventory=mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor=Inventory.cursor()
    cursor.execute('create database if not exists inventoryshop')
    cursor.execute('use inventoryshop')
    cursor.execute('create table if not exists products(id int auto_increment, product_name text, price int, catagory_id int, primary key(id))')
    cursor.execute('create table if not exists catagories (id int auto_increment, catagory_name text, primary key(id))')
    return cursor, Inventory
