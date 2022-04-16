mainlist=[ 'place','data']
def group():
    print(Fore.GREEN+('''How would you like to group-
1.Lower than average levels of air pollution in India
2.Greater than average levels of air pollution in India
3.Lower than average levels of air pollution in Asia
4.Greater than average levels of air pollution in Asia
5.Lower than average levels of air pollution in World
6.Greater than average levels of air pollution in World
7.Top 3 with maximum levels
8.Bottom 3 with minimum levels
9.Go back
'''))
    ast=int(input())
    if ast==1:
        l=[]
        print(Fore.RED+('The average level of air pollution (AQI) in India is 83.2 microgram/cubic metre'))
        sql26=" SELECT * FROM pollution_data where data<83.2 group by data"
        mycur.execute(sql26)
        mycon.commit()
        rows= mycur.fetchall()
        for x in rows:
            l.append(x)
        print(Fore.CYAN+(tabulate(l,headers=[mainlist[0],mainlist[1]],tablefmt='fancy_grid', showindex=range(1,len(l)+1))))
        group()
    elif ast==2:
        l=[]
        print(Fore.RED+('The average level of air pollution (AQI) in India is 83.2 microgram/cubic metre'))
        sql2=" SELECT * FROM pollution_data where data>83.2 GROUP BY data"
        mycur.execute(sql2)
        mycon.commit()
        rows= mycur.fetchall()
        for x in rows:
            l.append(x)
        print((Fore.CYAN+(tabulate(l,headers=[mainlist[0],mainlist[1]],tablefmt='fancy_grid', showindex=range(1,len(l)+1)))))
        group()
    elif ast==3:
            l=[]
            print(Fore.RED+('The average level of air pollution (AQI) in Asia is 99 microgram/cubic metre'))
            sql26="SELECT * FROM pollution_data WHERE data<99 GROUP BY data"
            mycur.execute(sql26)
            mycon.commit()
            rows= mycur.fetchall()
            for x in rows:
                l.append(x)
            print(Fore.CYAN+(tabulate(l,headers=[mainlist[0],mainlist[1]],tablefmt='fancy_grid', showindex=range(1,len(l)+1))))
            group()
    elif ast==4:
        l=[]
        print(Fore.RED+('The average level of air pollution (AQI) in Asia is 99 microgram/cubic metre'))
        sql26="SELECT * FROM pollution_data WHERE data>99 GROUP BY data"
        mycur.execute(sql26)
        mycon.commit()
        rows= mycur.fetchall()
        for x in rows:
            l.append(x)
        print(Fore.CYAN+(tabulate(l,headers=[mainlist[0],mainlist[1]],tablefmt='fancy_grid', showindex=range(1,len(l)+1))))
        group()
    elif ast==5:
        l=[]
        print(Fore.RED+('The average level of air pollution (AQI) in the World is 54 microgram/cubic metre'))
        sql26="SELECT * FROM pollution_data WHERE data<54 GROUP BY data "
        mycur.execute(sql26)
        mycon.commit()
        rows= mycur.fetchall()
        for x in rows:
            l.append(x)
        print(Fore.CYAN+(tabulate(l,headers=[mainlist[0],mainlist[1]],tablefmt='fancy_grid', showindex=range(1,len(l)+1))))
        group()
    elif ast==6:
        l=[]
        print(Fore.RED+('The average level of air pollution (AQI) in the World is 54 microgram/cubic metre'))
        sql26="SELECT * FROM pollution_data WHERE data>54 GROUP BY data"
        mycur.execute(sql26)
        mycon.commit()
        rows= mycur.fetchall()
        for x in rows:
            l.append(x)
        print(Fore.CYAN+(tabulate(l,headers=[mainlist[0],mainlist[1]],tablefmt='fancy_grid', showindex=range(1,len(l)+1))))
        group()
    elif ast==7:
        l=[]
        print(Fore.RED+('Top 3 countries with Maximum Air Pollution (AQI)'))
        sql26="SELECT * FROM pollution_data ORDER BY data DESC"
        mycur.execute(sql26)
        mycon.commit()
        rows= mycur.fetchmany(3)
        for x in rows:
            l.append(x)
        print(Fore.CYAN+(tabulate(l,headers=[mainlist[0],mainlist[1]],tablefmt='fancy_grid', showindex=range(1,len(l)+1))))
        group()
    elif ast==8:
        l=[]
        print(Fore.RED+('Bottom 3 countries with Minimum Air Pollution (AQI)'))
        sql26="SELECT * FROM pollution_data ORDER BY data ASC"
        mycur.execute(sql26)
        mycon.commit()
        rows= mycur.fetchmany(3)
        for x in rows:
            l.append(x)
        print(Fore.CYAN+(tabulate(l,headers=[mainlist[0],mainlist[1]],tablefmt='fancy_grid', showindex=range(1,len(l)+1))))
        group()
    elif ast==9:
        stats()
    else:
        print(Fore.RED+('You enterd an appropiate key'))
        group()
def sort():
    print(Fore.MAGENTA+('''Select-
1.Sort by Ascending order of data
2.Sort by Descending order of data
'''))
    ask=int(input())
    try:
        if ask==1:
             l=[]
             sql = "SELECT * FROM pollution_data ORDER BY data ASC"
             mycur.execute(sql)
             mycon.commit()
             rows= mycur.fetchall()
             for x in rows:
                l.append(x)
             print(Fore.CYAN+(tabulate(l,headers=[mainlist[0],mainlist[1]],tablefmt='fancy_grid', showindex=range(1,len(l)+1))))
             stats()
        elif ask==2:
             l=[]
             sql = "SELECT * FROM pollution_data order by data DESC"
             mycur.execute(sql)
             mycon.commit()
             rows= mycur.fetchall()
             for x in rows:
                l.append(x)
             print(Fore.CYAN+(tabulate(l,headers=[mainlist[0],mainlist[1]],tablefmt='fancy_grid', showindex=range(1,len(l)+1))))
             stats()
        else:
            stats()
    except:
        print(Fore.RED+'Error Occured')
        stats()

def display():
    l=[]
    sql11="select * from pollution_data"
    mycur.execute(sql11)
    mycon.commit()
    rows= mycur.fetchall()
    for x in rows:
        l.append(x)
    print(Fore.CYAN+(tabulate(l,headers=[mainlist[0],mainlist[1]],tablefmt='fancy_grid', showindex=range(1,len(l)+1))))
    stats()
def add ():
    try:
        print(Fore.GREEN+("Enter name of the new {}: ".format(mainlist[0])))
        n=input()
        d=input("Enter Data of {}: ".format(n))
        sql6="insert into pollution_data values ('"+n+"','"+d+"')"
        mycur.execute(sql6)
        mycon.commit()
        print(Fore.BLUE+("Row Added Successfully"))
    except:
        print(Fore.RED+('Error occured.'))
        stats()
    display()
   
def update():
    try:
        print(Fore.GREEN+("Enter {} name-".format(mainlist[0])))
        s=input()
        q=input("Enter the new value for {}-".format(s))
        query="update pollution_data set data='"+q+"' where place = '"+s+"'"
        mycur.execute(query)
        mycon.commit()
        print(Fore.RED+("Row Updated Successfully"))
        display()
    except:
        print(Fore.RED+('Error Occured.'))
        stats()
def delete():
    try:
        print(Fore.GREEN+("Enter {} name - ".format(mainlist[0])))
        s=input()
        query="delete from pollution_data where place='"+s+"'"
        mycur.execute(query)
        mycon.commit()
        print(Fore.RED+("Row Deleted Successfully"))
        display()
    except:
        print(Fore.RED+('Error occured.'))
        stats()
def dataanalytics():
    print(Fore.MAGENTA+('''Select-
1.Sorting
2.Grouping
'''))
    s=int(input())
    if s==1:
        sort()
    elif s==2:
        group()
    else:
        stats()
def stats():
    print(Fore.MAGENTA+('''What would you like to do with the table ?
1.Add a record
2.Update a record
3.Delete a record
4.Do data analytics
5.Display the data
6.Go back to menu
'''))
    c=int(input())
    if c==1:
        add()
    elif c==2:
        update()
    elif c==3:
        delete()
    elif c==4:
        dataanalytics()
    elif c==5:
        display()
    elif c==6:
        print(Fore.BLUE+('Going back will delete your data'))
        print('Do you want to go back to menu? (y/n)')
        apt=input()
        if apt=='y'or apt=='Y':
            print(Fore.RED+('table deleted'))
            sql12="drop table pollution_data"
            mycur.execute(sql12)
            mycon.commit()
            menu()
    
    elif apt=='n' or apt=='N':
            stats()
    else:
            print(Fore.RED+('You entered inappropiate key'))
            stats()
           
def insertdata():
    try:
        placename=input('Enter place name -')
        data=input('Enter the data of {}-'.format(placename))
        sql6="insert into pollution_data values('"+placename+"','"+data+"')"
        mycur.execute(sql6)
        mycon.commit()
        print(Fore.BLUE+('row inserted successfully'))
    except:
        print(Fore.RED+('Error occured. Redirected to menu'))
        print(Fore.RED+('No data saved '))
        sql5='drop pollution_data'
        mycur.execute(sql5)
        mycon.commit()
        menu()
       
def enterdata():
    print(Fore.BLUE+('How many rows you want to enter?'))
    n=int(input())
    print(Fore.BLUE+('Since this a comparitive study program you can only enter numeric values in 2nd column'))
    for i in range(1,n+1):
        print('Row-',i)
        insertdata()
    print(Fore.BLUE+('Table made successfully'))
    display()
def createdatabase():
    try:
        print(Fore.BLUE+(''' This a one time use program for comparitive study.You may use microgram per cubic metre as criteria to enter your data .This program compares annual average Air Quality Index (AQI) of asian countries .You may follow the same citeria for the better study.'''))
        yn=input('Do you want to go ahead and create database ?(y/n)')
        if yn=='y' or yn=='Y':
            print(Fore.YELLOW+'database created.')
            createtable()
        else:
            menu()
    except:
        print(Fore.RED+('''Some Error Generated.
No data saved.
'''))
        sql12="drop table pollution_data"
        mycur.execute(sql12)
        mycon.commit()
        menu()
       
def createtable():
    try:
        sql="create table pollution_data (place varchar (30),data int)"
        mycur.execute(sql)
        mycon.commit()
        print(Fore.YELLOW+('Table with 2 columns created'))
        enterdata()
       
    except:
        sql12="drop table pollution_data"
        mycur.execute(sql12)
        mycon.commit()
        menu()
       
from colorama import init
init()
from colorama import Fore,Style,Back
from tabulate import tabulate
import pymysql
mycon=pymysql.connect(host='localhost',user='root',password='hirnikaoberoi7')
mycur=mycon.cursor()
def menu():
    print(Fore.YELLOW+Style.BRIGHT+Back.RESET+('''What would you like to do-
1. View the latest ranking for asian countries
2. Create your own data base for statistics
3. Check how clean the air around you is
4. Exit
'''))
    choice=int(input())
    if choice==1:
        try:
            sql12="use pollution"
            mycur.execute(sql12)
            mycon.commit()
            l=[]
            sql11="select * from Pollutionchart"
            mycur.execute(sql11)
            mycon.commit()
            rows= mycur.fetchall()
            for x in rows:
              l.append(x)
            print(Fore.CYAN+(tabulate(l,headers=['Sno','Country','Worldwide Rank','Year 2020 (during lockdown)','Year 2019','Year 2018'],tablefmt='fancy_grid')))
            menu()
        except:
            print(Fore.RED+('Errored occured'))
            menu()
    elif choice==2:
        sql12="use pollution"
        mycur.execute(sql12)
        mycon.commit()
        createdatabase()
    elif choice==3:
        aqi=int(input('Enter the AQI of the area around you (put a numeric value):'))
        if 0<=aqi<=50:
            print(Fore.GREEN+('GOOD'))
        elif 51<=aqi<=100:
            print(Fore.YELLOW+('MODERATE'))
        elif 101<=aqi<=150:
            print(Fore.CYAN+('UNHEALTHY FOR PEOPLE WITH RESPIRATORY DISEASES'))
        elif 151<=aqi<=200:
            print(Fore.BLUE+('UNHEALTHY'))
        elif 201<=aqi<=300:
            print(Fore.RED+('VERY UNHEALTHY'))
        elif 301<=aqi<=500:
            print(Fore.MAGENTA+('HAZARDOUS'))
        else:
            print(Fore.RED+('You entered a wrong value'))
            menu()
        l1=[('301-500','HAZARDOUS'),('201-300','VERY UNHEALTHY'),('151-200','UNHEALTHY'),('101-150','UNHEALTHY FOR PEOLPLE WITH RESPIRATORY DISEASES'),('51-100','MODERATE'),('0-50','GOOD')]
        print(Fore.CYAN+((tabulate(l1,headers=['AQI','PARAMETERS'],tablefmt='fancy_grid'))))
        menu()
    elif choice==4:
        print(Fore.GREEN+('Thankyou'))
        print('Program ended')
    elif choice==' ':
        print(Fore.RED+('You didnt enter correct key'))
    else:
        print(Fore.RED+('You didnt enter correct key'))
        pass
print (Fore.GREEN+Style.BRIGHT+('''
                                  AIR POLLUTION LEVEL DATA STATISTICS
                                 '''))
print('Welcome to air pollution level data statistics program ')
menu()
mycon.close()