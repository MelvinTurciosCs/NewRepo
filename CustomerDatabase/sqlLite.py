import sqlite3
from Customers import Customers


conn = sqlite3.connect('Customer.db')

c = conn.cursor()

c.execute("""CREATE TABLE customers (
            first text,
            last text,
            email text,
            phone text
    )""")

def insert_emp(custs):
    with conn:
        c.execute("INSERT INTO customers VALUES (:first, :last, :email, :phone)", {'first': custs.first, 'last': custs.last, 'email': custs.email, 'phone': custs.phone})

def get_custs_by_name(lastname):
    c.execute("SELECT + FROM customers WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_email(custs, email):
    with conn:
        c.execute("""UPDATE customers SET email = :email
                    WHERE first = :first AND last = :last""",
                    {'first': custs.first, 'last': custs.last, 'email': custs.email})

def remove_emp(custs):
    with conn:
        c.execute("DELETE from customers WHERE first = :first AND last = :last",
                    {'first': custs.first, 'last': custs.last})


cust_1 = ('John', 'Doe', 'john@gmail.com', '832-232-1111')
cust_2 = ('charles', 'Doe', 'charles@gmail.com', '713-222-1111')


insert_emp(cust_1)
insert_emp(cust_2)

conn.commit()

custs = get_custs_by_name('Doe')
print(custs)

conn.close()