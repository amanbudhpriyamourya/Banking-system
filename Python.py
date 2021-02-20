import sqlite3
from datetime import datetime # date aur time ke liye check notes
import sys


def create_table(cur):
    cur.execute ("""create table if not exists bank (
    id integer primary key autoincrement,
    name text not null,
    date_of_creation text,
    amount integer default 0
    )""") # agr table nhi hai toh bnn jayega else ignore

def choice(cur):
    choice = int(input("""Enter Choice:\n1. add_cust\n2. change_name
3. check_balance\n4. update_balance\nto exit press any other key\n"""))# multi line string mein agr enter daalo toh vo reflect hoga
    if choice == 1:
        add_cust(cur)
        choice(cur)
    if choice == 2 :
        change_name(cur)
        choice(cur)
    if choice == 3:
        check_balance(cur)
        choice(cur)
    if choice == 4:
        update_balance(cur)
        choice(cur)
    else:
        sys.exit()

def add_cust(cur):
    now = datetime.now()
    date=now.strftime("%d/%m/%Y %H:%M:%S")
    name=input("Please enter the customer name \n")
    amount=int(input("What is the initial amount deposited by the customer? \n"))
    cur.execute ("""insert into bank (name,amount,date_of_creation)
                    values (?,?,?)""",(name,amount,date,))
    cur.execute("select id from bank where date_of_creation=?",(date,))
    row=cur.fetchone()
    print("The customer id of "+name+" is "+str(row[0]))

def change_name(cur):
    id=int(input("Enter customer id:\n"))
    name=input("Enter new customer name")
    cur.execute("""update bank set name = ? where id = ?""",(name,id))

def check_balance(cur):
    id=int(input("Enter customer id:\n"))
    cur.execute("select name,amount from bank where id=?",(id,)) #last id ke baad comma jruri hai else parameter are of unsupported type error aa jata hai in case of select statement
    row=cur.fetchone()
    print("The customer "+str(row[0])+" have amount "+str(row[1]))

def update_balance(cur):
    id=int(input("Enter customer id:\n"))
    amount=int(input("What is the new amount? \n"))
    cur.execute("""update bank set amount = ? where id = ?""",(amount,id))

def main ():

    conn = sqlite3.connect('bank_db.sqlite')
    cur = conn.cursor()
    choice(cur)

    conn.commit() #save data


if __name__ == '__main__':
    main()
