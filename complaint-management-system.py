import mysql.connector
        
def residentlogin():
    x=int(input("\nroomno: "))
    y=input("\nname:  ")
    z=input("\ngender: ")
    print('\n\n')  
    accountexistfun(x,y,z) 
        
def accountexistfun(x,y,z):
    try:
        conn= mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="2580",
                    database="resident"
                    )
        cur=conn.cursor()
        query="select *from residents where roomno={} and name='{}' and gender='{}'".format(x,y,z)
        cur.execute(query)
        data=cur.fetchall()
        if len(data)==0:
            print('account not exist')
        else:
            signinmenuchoice()
    finally:
        conn.close()
        return 0


def signinmenuchoice():
    print('\n1.file complaints')
    print('\n2.see previous complaints/resposes')
    print('\n3.exit')
    print('\n\n')
    choice = int(input('Enter your choice ...: '))            
    if choice ==1:
        accountexistfun1()
    if choice ==2:
        prevcomp()
    if choice == 3:
        exit
        
        
def accountexistfun1():
    try:
        conn= mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="2580",
                    database="newcomp"
                    )
        x=int(input("\nroomno: "))
        y=input("\nname:  ")
        z=input("\ngender: ")
        q=input("\nenter complaint/comments: ")
        print('\n\n') 
        sql="INSERT INTO newcomps VALUES ({}, '{}', '{}', '{}');".format(x,y,z,q)   
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
    finally:
        signinmenuchoice()
        conn.close()
        return 0      



def prevcomp():
    x=int(input("\nroomno: "))
    print('\n\n')  
    accountexistfun2(x) 
        
def accountexistfun2(x):
    try:
        conn= mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="2580",
                    database="prevcom"
                    )
        cur=conn.cursor()
        query="select *from prevcoms where roomno={} ".format(x)
        cur.execute(query)
        data=cur.fetchall()
        print(data)  
    finally:
        signinmenuchoice()
        conn.close()
        return 0      


def adminloginmenu():
    x=int(input("\nloginid: "))
    y=input("\npassword:  ")
    print('\n\n')  
    adminmenu(x,y) 

def adminmenu(x,y):
    try:
        conn= mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="2580",
                    database="admin"
                    )
        cur=conn.cursor()
        query="select *from adminids where loginid={} and password={}".format(x,y)
        cur.execute(query)
        data=cur.fetchall()
        if len(data)==0:
            print('account not exist')
        else:
            adminmenuchoice()
    finally:
        conn.close()
        return 0


def adminmenuchoice():
    print('\n1.new compaints/add resposes')
    print('\n2.remove new complaints')
    print('\n3.see previous complaints/resposes')
    print('\n4.exit')
    print('\n\n')
    choice = int(input('Enter your choice ...: '))            
    if choice ==1:
        allnewcomp()
    if choice==2:
        delnewcom()
    if choice ==3:
        allprevcomp()
    if choice == 4:
        exit


        
def allnewcomp():
    try:
        conn= mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="2580",
                    database="newcomp"
                    )
        cur=conn.cursor()
        query="select *from newcomps"
        cur.execute(query)
        data=cur.fetchall()
        print(data)     
    finally:   
        print("\n1. to insert resposes")
        print("\n2. exit")
        print('\n\n')
        choice=int(input())
        if choice==1:
            response()
        if choice==2:
            adminmenuchoice()   
        conn.close()
        return 0    
        
def response():
    try:
        conn= mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="2580",
                    database="prevcom"
                    )
        x=int(input("\nroomno: "))
        y=input("\nname:  ")
        z=input("\nregading issue: ")
        q=input("\nenter response: ")
        print('\n\n') 
        sql="INSERT INTO prevcoms VALUES ({}, '{}', '{}', '{}');".format(x,y,z,q)   
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
    finally:
        adminmenuchoice()
        conn.close()
        return 0 

def delnewcom():
    x=int(input("\nroomno: "))
    print('\n\n')  
    delnewcomfun(x)         


def delnewcomfun(x):
    try:
        conn= mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="2580",
                    database="newcomp"
                    )
        cur=conn.cursor()
        query="delete from newcomps where roomno={}".format(x)
        cur.execute(query)
        conn.commit()
        print("deleted successfully")
        print("\n")
    finally:
        adminmenuchoice()
        conn.close()
        return 0           


        
        
def allprevcomp():
    try:
        conn= mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="2580",
                    database="prevcom"
                    )
        cur=conn.cursor()
        query="select *from prevcoms"
        cur.execute(query)
        data=cur.fetchall()
        print(data)  
    finally:
        adminmenuchoice()
        conn.close()
        return 0           


def main_menu():
    while True:
        print(' Main Menu')
        print("\n1. resident login")
        print('\n2. admin login')
        print('\n3.  quit')
        print('\n\n')
        choice = int(input('Enter your choice ...:'))
        if choice == 1:
            residentlogin()
        if choice == 2:
            adminloginmenu()
        if choice == 3:
            break
            

if __name__ == "__main__":
    main_menu()
            