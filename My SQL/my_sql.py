# 0157CY221126
# Shiksha Jaiswal

import mysql.connector as sql
import colorama
import os
import sys
import time
import random

def clear_lines(num_lines):
    for _ in range(num_lines):
        sys.stdout.write("\033[F")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear the line
    sys.stdout.flush()

def clear():
    if os.name == 'nt':
        _ = os.system('cls')

db = sql.connect(
    host = "localhost",
    user = "root",
    password = "@shiksha04",
    database = "shiksha"
)

cur = db.cursor()

#global values
logged_in = False
user = ''
uid = 0

#results printer
def print_table(data):
    headers = ["Subject Name", "Score", "Grade", "Date of Performance"]
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data, headers)]
    boundary = "+".join("-" * (width + 2) for width in col_widths)
    boundary = f"+{boundary}+"
    header_row = "|".join(f" {header.ljust(width)} " for header, width in zip(headers, col_widths))
    header_row = f"|{header_row}|"
    print(boundary)
    print(header_row)
    print(boundary)
    
    for row in data:
        row_str = "|".join(f" {str(item).ljust(width)} " for item, width in zip(row, col_widths))
        row_str = f"|{row_str}|"
        print(row_str)
        print(boundary)


def register():
    clear()
    print("Register")
    print()
    print("Enter your following information")
    print()
    name = input("Enter you full name : ")
    while name == "":
        name = input("Enter you full name (not empty): ")

    city = input("Enter you city : ")
    while city == "":
        city = input("Enter you city (not empty): ")

    mobile_no = input("Enter your mobile number : ")
    while len(mobile_no) != 10:
        clear_lines(1)
        mobile_no = input("Enter your mobile number (10 digit only): ")
        if len(mobile_no) == 10 and mobile_no.isdecimal():
            break
    
    qry = "select username from users"
    cur.execute(qry)
    lst = [row[0] for row in cur.fetchall()]
    username = input("Enter your username : ")
    while True:
        if username not in lst and username != "":
            password = input("Enter your password : ")
            break
        else:
            clear_lines(1)
            username = input("Enter your username (unique one): ")
    
    qry = "insert into users(name, city, mobile_no, username, password) value(%s, %s, %s, %s, %s)"
    val = (name, city, mobile_no, username, password)
    cur.execute(qry, val)
    db.commit()


def login():
    global logged_in, user, uid
    clear()
    print("Login")
    print()
    print("Enter your following information")
    print()
    username = input("Enter your username : ")
    i = 2
    while True:
        qry = "select uid,password from users where username = %s"
        val = (username,)
        cur.execute(qry, val)
        lst = cur.fetchall()
        if len(lst) != 0:
            password = input("Enter your password : ")
            if lst[0][1] == password:
                logged_in = True
                user = username
                uid = lst[0][0]
                break
            else:
                if i == 2:
                    clear_lines(2)
                    i += 1
                else:
                    clear_lines(3)
                    
                print("Incorrect password !!")
                username = input("Enter your username : ")
        else:
            clear_lines(1)
            username = input("Enter your username (correct one): ")


def quiz_initiator():
    global logged_in, user, uid
    i = 0
    while(True):
        clear()
        if(logged_in):
            print(colorama.Fore.CYAN + f"Current Logged In User : {user} !!" + colorama.Style.RESET_ALL)
            print()
        print("Welcome to quiz !!")
        print()
        print("Please select anyone operation : ")
        print("1 : Start Quiz")
        print("2 : Main mnenu")
        print("3 : Logout")
        print()
        if i == 0:
            ch = input("Enter your choice : ")
        else:
            ch = input("Enter your choice (Invalid choice): ")
        if(ch == ""):
            continue

        if(ch == '1'):
            a = quiz()
            if(a == "BREAK"):
                return
        elif(ch == '2'):
            print()
            print("Thank you for playing !!")
            break
        elif(ch == '3'):
            print()
            print("Logged out successfully !!")
            logout()
            break
        else:
            i += 1

def quiz():
    global logged_in, user, uid
    i = 0
    while(True):
        clear()
        if(logged_in):
            print(colorama.Fore.CYAN + f"Current Logged In User : {user} !!" + colorama.Style.RESET_ALL)
            print()
        print("Please select anyone subject for quiz: ")
        print("1 : Operating System")
        print("2 : Dbms")
        print("3 : Computer Networks")
        print()
        print("4 : Main menu")
        print()
        
        a=""
        if i == 0:
            ch = input("Enter your choice : ")
        else:
            ch = input("Enter your choice (Invalid choice): ")

        if(ch == ""):
            continue
    
        if(ch == '1'):
            a = test("os")
            i = 0
        elif(ch == '2'):
            a = test("dbms")
            i = 0
        elif(ch == '3'):
            a = test("cn")
            i = 0
        elif(ch == '4'):
            a = "BREAK"
            i = 0
        else:
            i += 1
        
        if(a == "BREAK"):
            return "BREAK"

def test(subject):
    global logged_in, user, uid
    score = 0
    qry = f"select * from {subject}_question_table"
    cur.execute(qry)
    lst = cur.fetchall()
    qt = random.sample(lst, 5)
    i = 1

    for q in qt:
        clear()
        if(logged_in):
            print(colorama.Fore.CYAN + f"Current Logged In User : {user} !!" + colorama.Style.RESET_ALL)
            print()
        print(f"Question {i} : {q[0]}")
        print(f"{q[1]}\n{q[2]}\n{q[3]}\n{q[4]}")
        print()
        ans = input("Enter your answer : ").lower()
        print()
        if ans not in ['a','b','c','d']:
            print("You have entered the wrong option. So it is considered as", end=" ")
        if(ans == q[5]):
            print(colorama.Fore.GREEN + "Correct answer !!" + colorama.Style.RESET_ALL)
            time.sleep(0.5)
            score += 1
        else:
            print(colorama.Fore.RED + "Incorrect answer !!" + colorama.Style.RESET_ALL + f"\nCorrect answer is : {q[5]}")
            time.sleep(0.5)
        i += 1
    
    i = 1
    clear()
    if(logged_in):
        print(colorama.Fore.CYAN + f"Current Logged In User : {user} !!" + colorama.Style.RESET_ALL)
        print()
    print(f"Your score is : {score}")
    grade = chr(70-score)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    qry = "insert into results value(%s, %s, %s, %s, %s)"
    val = (uid, subject, score, grade, current_time)
    cur.execute(qry, val)
    db.commit()
    print()
    print("Do you want to still continue !! [y/n]")
    ch = input("Enter your choice : ").lower()
    if(ch == 'y'):
        return
    else:
        return "BREAK"


def view_result():
    global logged_in, user, uid
    clear()
    if(logged_in):
        print(colorama.Fore.CYAN + f"Current Logged In User : {user} !!" + colorama.Style.RESET_ALL)
        print()
    
    qry = "select subject, marks, grade, time from results where uid = %s"
    val = (uid,)
    cur.execute(qry, val)
    lst = cur.fetchall()
    if len(lst) == 0:
        print("No record found !!")
    else:
        print_table(lst)
    
    print()
    ch = input("Press enter key........").lower()


def view_profile():
    global logged_in, user, uid
    qry = "select name, city, mobile_no, username from users where uid = %s"
    val = (uid,)
    cur.execute(qry, val)
    lst = cur.fetchall()
    clear()
    if(logged_in):
        print(colorama.Fore.CYAN + f"Current Logged In User : {user} !!" + colorama.Style.RESET_ALL)
        print()
    print("Profile Information")
    print()
    print(f"Name : {lst[0][0]}")
    print(f"City : {lst[0][1]}")
    print(f"Mobile No. : {lst[0][2]}")
    print(f"Username : {lst[0][3]}")

    print()
    ch = input("Press enter key........").lower()


def edit_profile():
    global logged_in, user, uid
    qry = "select name, city, mobile_no from users where uid = %s"
    val = (uid,)
    cur.execute(qry, val)
    lst = cur.fetchall()
    clear()
    if(logged_in):
        print(colorama.Fore.CYAN + f"Current Logged In User : {user} !!" + colorama.Style.RESET_ALL)
        print()
    print("If you don't want to change the field leave blank !!")
    name = input(f"Enter your new name (previous : {lst[0][0]}): ")
    if name != "":
        qry = "update users set name = %s where uid = %s"
        val = (name, uid)
        cur.execute(qry, val)
    
    city = input(f"Enter your new city (previous : {lst[0][1]}): ")
    if city != "":
        qry = "update users set city = %s where uid = %s"
        val = (city, uid)
        cur.execute(qry, val)
    
    mobile_no = input(f"Enter your new mobile number (previous : {lst[0][2]}): ")
    if mobile_no != "":
        while len(mobile_no) != 10:
            clear_lines(1)
            mobile_no = input(f"Enter your new mobile number (previous : {lst[0][2]} , 10 digit only): ")
            if len(mobile_no) == 10 and mobile_no.isdecimal():
                break
        
        qry = "update users set mobile_no = %s where uid = %s"
        val = (mobile_no, uid)
        cur.execute(qry, val)
    
    db.commit()
    print()
    print("All changes are stored !!")
    print()
    ch = input("Press enter key........").lower()


def change_pass():
    global logged_in, user, uid
    qry = "select password from users where uid = %s"
    val = (uid,)
    cur.execute(qry, val)
    lst = cur.fetchall()
    clear()
    if(logged_in):
        print(colorama.Fore.CYAN + f"Current Logged In User : {user} !!" + colorama.Style.RESET_ALL)
        print()
    
    cur_pass = input("Enter your current password : ")
    if(cur_pass == lst[0][0]):
        i = 2
        while True:
            password = input("Enter your new password : ")
            rpassword = input("Re-enter your new password : ")
            if(password == rpassword):
                qry = "update users set password = %s where uid = %s"
                val = (password, uid)
                cur.execute(qry, val)
                break
            else:
                if i == 2:
                    clear_lines(2)
                    i += 1
                else:
                    clear_lines(3)
                print("Password not matching !!")
    
        db.commit()
        print()
        print("Password changed !!")
    else:
        print()
        print("Permission denied !!")

    print()
    ch = input("Press enter key........").lower()

    
def del_ac():
    global logged_in, user, uid
    clear()
    if(logged_in):
        print(colorama.Fore.CYAN + f"Current Logged In User : {user} !!" + colorama.Style.RESET_ALL)
        print()
    
    ch = input("Are you sure to delete your account (y/n): ").lower()
    if ch == 'y':
        qry = "delete from users where uid = %s"
        val = (uid,)
        cur.execute(qry, val)
        db.commit()
        print("Account Deleted !!")
        logout()
    else:
        print()
        print("Account deletion terminated !!")
    ch = ch = input("Press enter key........").lower()

def logout():
    global logged_in, user, uid
    logged_in = False
    user = ""
    uid = 0
    


def main():
    global logged_in, user, uid
    i = 0
    while True:
        clear()
        if logged_in:
            print(colorama.Fore.CYAN + f"Current Logged In User : {user} !!" + colorama.Style.RESET_ALL)
            print()
            print("Please select anyone operation : ")
            print("1 : Take Quiz")
            print("2 : View Result")
            print("3 : View Profile")
            print("4 : Edit Profile")
            print("5 : Change Password")
            print("6 : Delete Account")
            print("7 : Logout")
            print("8 : Exit")
        else:
            print("Quiz Application")
            print()
            print("Please select anyone operation : ")
            print("1 : Register")
            print("2 : Login")
            print("3 : Exit")

        print()
        if i == 0:
            ch = input("Enter your choice : ")
        else:
            ch = input("Enter your choice (Invalid choice): ")
        if ch == '':
            continue

        if logged_in:
            if ch == '1':
                quiz_initiator()
                i = 0
            elif ch == '2':
                view_result()
                i = 0
            elif ch == '3':
                view_profile()
                i = 0
            elif ch == '4':
                edit_profile()
                i = 0
            elif ch == '5':
                change_pass()
                i = 0
            elif ch == '6':
                del_ac()
                i = 0
            elif ch == '7':
                logout()
                i = 0
            elif ch == '8':
                break
            else:
                i += 1
        else:
            if ch == '1':
                register()
                i = 0
            elif ch == '2':
                login()
                i = 0
            elif ch == '3':
                print("Thanks for using it !!")
                break
            else:
                i += 1

if __name__ == '__main__':
    main()
