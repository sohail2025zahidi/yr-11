#docstring-Sohail Zahidi- 3d printer database application

#imports
import sqlite3

#contants and varaibles
Database = "3DPRINTER.DB"


#functions
def print_all_printer():
    '''prints all the 3dprinter data nicely'''
    db = sqlite3.connect("3DPRINTER.DB")
    cursor = db.cursor()
    sql = "SELECT * FROM PRINTER_3D;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('Printer_name                  Brand          Type           Price          Weight         Nozzle_Diaeter')
    for printer in results:
        print(f"{printer[1]:<30}{printer[2]:<15}{printer[3]:<15}{printer[4]:<15}{printer[5]:<15}{printer[6]:<15}")
    #loop is finished here
    db.close()


#main code
while True:
    user_input = input("\nWhat would you like to do.\n1. Print all 3D printers\n2.Exit\n")
    if user_input == '1':
        print_all_printer()
    if user_input == '2':
        break
    else:
        print('Not an option little bro')
