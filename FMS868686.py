import re
import random
import maskpass
import datetime
from datetime import *
import mysql.connector as db
from prettytable import from_db_cursor

class Tab:
    def __init__(self):

        # connect to database
        # self.mydb=db.connect(host="localhost",user="dbuser",password="Squ@d123",database="BasicDB")
        # self.cursor=self.mydb.cursor()
         
        self.mydb=db.connect(host="localhost",user="dbuser",password="1234",database="BasicDB")
        self.cursor=self.mydb.cursor()

        self.name = "FLIGHT MANAGEMENT SYSTEM"

        query=("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50),
                password VARCHAR(255),
                email varchar(50) unique
            )
        """)
        self.cursor.execute(query)
        
        query=("""
            CREATE TABLE IF NOT EXISTS passenger (
                passenger_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) not null, 
                address VARCHAR(255),
                mobile_number varchar(100),
                booking_date_time datetime,
                rdate date 
                )            
            """)
        self.cursor.execute(query)

        query=("""
            CREATE TABLE IF NOT EXISTS tclass (
                cls_Srno INT PRIMARY KEY,
                class_type varchar(30),
                Amount int(10)
                )
            """)
        self.cursor.execute(query)

        try:
            query='''Insert into tclass values(1,"Business class", "9999"),
            (2,"First class","5999"),
            (3,"Economy class" ,"3999")
            '''
            self.cursor.execute(query)
            self.mydb.commit()
        except:
            print(" ")

        query=("""
            CREATE TABLE IF NOT EXISTS food (
                food_id INT AUTO_INCREMENT PRIMARY KEY,
                FOODSname VARCHAR(50) Unique,
                price INT(100)
            )
        """)
        self.cursor.execute(query)

        try:
            query='''Insert into food(FOODSname,price) values("SAMOSA & CHAI","250"),
                ("BLACK FOREST PASTRY", "299"),
                ("PROTEIN SALAD VEG" ,"500"),
                ("PROTEIN SALAD NON-VEG" ,"500"),
                ("TANDOORI PANEER CROISSANT SANDWICH VEG" ,"500"),
                ("TANDOORI PANEER CROISSANT SANDWICH NON-VEG" ,"500"),
                ("CELEBRATION CAKE","750")
                '''
            self.cursor.execute(query)
            self.mydb.commit()
        except:
            print("")

        query=("""
            CREATE TABLE IF NOT EXISTS Ordered (
                food_id INT,
                passenger_id INT,
                name varchar(100),
                FOODSname VARCHAR(50),
                price INT(100),
                FOREIGN KEY (food_id) REFERENCES food(food_id),
                FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id)
            )
        """)
        self.cursor.execute(query)

        query=("""
            CREATE TABLE IF NOT EXISTS flights (
                Srno INT(50) Unique ,
                Airlines_name varchar(100) , 
                Sorce varchar(100),
                Destination varchar(100) ,
                Flight_no varchar(100) PRIMARY KEY ,
                Time_of_Airline time,
                Routine varchar(100)
                ) 
            """)
        self.cursor.execute(query)

        try:
            query='''
            Insert into flights (Srno,Airlines_name,Sorce,Destination,Flight_no,Time_of_Airline,Routine) values('1',"Spicejet" ,"mumbai","jaipur" ,"SG-818"  ,'08:50:00',"Daily"),
                ("2","Vistara", "mumbai" ,"Jodhpur" , "UK-879" , "09:10:00","Daily"),
                ("3","AirINDIA" ,"mumbai"  , "surat"  ,"G8-395"  ,  "19:00:00","Daily"),
                ("4","AixConnect" ,"mumbai" ,"pune" , "AI-802"  ,  "02:00:00","Daily"),
                ("5",'IndiGO'  ,'mumbai'  , 'nashik'  ,'GK-591' ,  "07:15:00","Daily"),
                ("6",'GoFirst' ,'mumbai' ,'goa' , 'AI-852' , '02:00:00',"Daily"),
                ("7",'GoINDIA' ,'mumbai' ,'Delhi' , 'AI-822'  ,  '01:00:00',"Daily"),
                ("8",'Alliance Air' , 'mumbai' , 'bangalore'  , 'SG-819' , '08:50:00',"Daily"),
                ('9','AirExpress'  ,'mumbai'  , 'tamil nadu'  ,'GK-551', '02:15:00',"Daily"),
                ('10','GoAir' ,'mumbai' ,'kerala' , 'AI-8702'  , '05:00:00',"Daily"),
                ('11','JetAirways' ,'mumbai' ,'Andhra pradesh' , 'AI-885' , '02:00:00',"Daily"),
                ('12','AirIndiaExpress' ,'mumbai' ,'Bhopal' , 'kj-752' , '11:00:00',"Daily"),
                ("13",'TruJet' ,'mumbai' ,'odisha' , 'FG-875' , '10:00:00',"Daily"),
                ('14','Indian Airlines' ,'mumbai' ,'ranchi' , 'SA-452' , '09:00:00',"Daily"),
                ('15','Emirates' ,'mumbai' ,'bihar' , 'YJ-152' , '08:00:00',"Daily"),
                ('16','JetLite' ,'mumbai' ,'lucknow' , 'PK-752' , '07:00:00',"Daily"),
                ('17','No1Air' ,'mumbai' ,'punjab' , 'WE-352' , '06:00:00',"Daily"),
                ('18','Gulf Air' ,'mumbai' ,'haryana' , 'IJ-002' , '05:00:00',"Daily"),
                ('19','Star Air' ,'mumbai' ,'uttarakhand' , 'PO-352' , '04:00:00',"Daily"),
                ('20','SingAirlines' ,'mumbai' ,'himachal' , 'DF-625' , '03:00:00',"Daily"),
                ('21','Air Costa' ,'mumbai' ,'jammu and kashmir' , 'HG-452' , '01:00:00',"Daily"),
                ('22','CathayPaci' ,'mumbai' ,'bhopal' , 'AI-444' , '02:00:00',"Daily"),
                ('23',"Spicejet" ,"jaipur" ,'mumbai' ,"SG-81118"  ,'08:50:00',"Daily"),
                ('24',"Vistara" ,"Jodhpur" ,'mumbai', "UK-87009" , "09:10:00","Daily"),
                ('25',"AirINDIA"   , "surat" ,'mumbai' ,"G8-39525"  ,  "19:00:00","Daily"),
                ('26',"xConnect" ,"pune" ,'mumbai', "AI-80002"  ,  "02:00:00","Daily"),
                ('27','IndiGO'   , 'nashik'  ,'mumbai','GK-59142' ,  "07:15:00","Daily"),
                ('28','GoFirst'  ,'goa' , 'mumbai','AI-82552' , '02:00:00',"Daily"),
                ('29','GoINDIA' ,'Delhi' ,'mumbai', 'AI-8486522'  ,  '01:00:00',"Daily"),
                ('30','Alliance Air'  , 'bengaluru','mumbai' , 'S-818629' , '08:50:00',"Daily"),
                ('31','AirExpress'   , 'tamilnadu','mumbai'  ,'GK-594561', '02:15:00',"Daily"),
                ('32','JetAirways' ,'Andhra pradesh' ,'mumbai', 'AI-88865' , '02:00:00',"Daily"),
                ('33','AirIndiaExpress' ,'hariyana' ,'mumbai', 'kj-73252' , '11:00:00',"Daily"),
                ('34','TruJet' ,'odisha','mumbai' , 'FG-81275' , '10:00:00',"Daily"),
                ('35','Indian Airlines'  ,'ranchi','mumbai' , 'SA-45852' , '09:00:00',"Daily"),
                ('36','Emirates' ,'bihar','mumbai', 'PK-182' , '08:00:00','Daily'),
                ('37','JetLite' ,'mumbai' ,'lucknow' , 'PK-3752' , '07:00:00',"Daily"),
                ('38','No1Air'  ,'punjab' ,'mumbai', 'WE-3527' , '06:00:00',"Daily"),
                ('39','Gulf Air'  ,'haryan Uniquea','mumbai' , 'IJ-82452' , '05:00:00',"Daily"),
                ('40','Star Air'  ,'uttarakhand' ,'mumbai','PO-38552' , '04:00:00',"Daily"),
                ('41','SingAirlines' ,'himachal' ,'mumbai' , 'DF-6254' , '03:00:00',"Daily"),
                ('42','Air Costa'  ,'jammu and kashmir' ,'mumbai', 'HG-4592' , '01:00:00',"Daily"),
                ('43','CathayPaci'  ,'bhopal','mumbai' , 'AI-55654' , '02:00:00',"Daily")
                '''
            self.cursor.execute(query)
            self.mydb.commit()              
        except:
            print(" ")

        query=("""
            CREATE TABLE IF NOT EXISTS payment (
                passenger_id INT,
                name VARCHAR(255) not null, 
                address VARCHAR(255),
                mobile_number varchar(100) unique,
                Sorce varchar(233),
                Destination varchar(255),
                Airlines_name varchar(100),
                Flight_no varchar(100), 
                cls_Srno INT(10),
                class_type varchar(100),
                booking_date_time datetime,
                rdate date,
                Amount int(100),
                FOREIGN KEY (cls_Srno) REFERENCES tclass(cls_Srno),
                FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id),
                FOREIGN KEY (Flight_no) REFERENCES flights(Flight_no)
                )            
            """) 
        self.cursor.execute(query)


    def user_register(self):
        try:
            var=input("\n\nEnter your name to register --> ")
            email=input("Enter your E-mail --> \t")
            pattern='^[a-z]+[._]?[a-z0-9]+[@][a-z0-9_]+[.][a-z0-9_]{2,3}$'
            if re.search(pattern,email): 
                    password=input("Create password --> \t")
                    data=(var,password,email)
                    query='insert into users(username,password,email) values (%s,%s,%s)'
                    self.cursor.execute(query,data)
                    self.mydb.commit()
                    print("--->>-->| Your Registration Completed Successfully |<--<<---")
            else:
                print("-->>--->>-->| Enter valid Email |<--<<---<<---   ")
        except:
            print("\n Duplicate Entry.....")


    def Admin_login(self):
        self.var1=input("\n\nEnter your name --> \t")
        if self.var1=="admin":
            self.passwd=maskpass.askpass("Enter Your Password --> ",mask='*')
            if  self.passwd=="1234":
                while(True):
                    print("\nx-x-x-x ---=--=-=-=-=-=-=-=-=-=-=-==--=-=---  x-x-x-x \n")
                    print("[1] Display Flights \n[2] Book Reservation \n[3] Show All passenger Details \n[4] Show Single passenger Details \n[5] Show food menu \n[6] Add New food in Menu \n[7] Ordered Food \n[8] Delete Food Item if No More Available  \n[9] Delete Passenger Details \n[10] Users \n[11] exit ")   
                    print("\nx-x-x-x ---=--=-=-=-=-=-=-=-=-=-=-==--=-=---  x-x-x-x \n")
                    choice=input("Enter your choice --> \t")
                    if choice=="1":
                        self.Display_Flights()
                    elif choice=="2":
                        self.Reservation()
                        while True:
                            print("\n\n Do You want to do Reseve ticket's more..?")
                            var=input("y/n --> \t")
                            if var=="y":
                                self.Reservation()
                            else: 
                                break
                    elif choice=="3":
                        self.Display_ALL_Reservation()
                        while True:
                            print("\n\n Do you want to Display Again?")
                            var=input("y/n --> \t")
                            if var=="y":
                                self.Display_ALL_Reservation()
                            else: 
                                break
                    elif choice=="4":
                            self.Admin_show_single_Reservation()
                            while True:
                                print("\n\n Do You want to Display again Passenger Details..?")
                                var=input("y/n --> \t")
                                if var=="y":
                                    self.Admin_show_single_Reservation()
                                else: 
                                    break
                    elif choice=="5":
                        self.showfoodmenu()
                    elif choice=="6":
                        self.add_food()
                        while True:
                            print("\n\nwant to add more?")
                            var=input("y/n --> \t")
                            if var=="y":
                                self.add_food()
                            else: 
                                break
                    elif choice=="7":
                        self.ord_food()
                        while True:
                            print("\n\nwant to odered food more?")
                            var=input("y/n -->")
                            if var=="y":
                                self.ord_food()
                            else: 
                                break
                    elif choice=="8":
                        self.delete_food()
                        while True:
                            print("\n\nwant to delete more?")
                            var=input("y/n -->")
                            if var=="y":
                                self.delete_food()
                            else: 
                                break
                    elif choice=="9":
                        self.delete_passenger_Admin()
                        while True:
                            print("\n\nwant to delete more?")
                            var=input("y/n -->")
                            if var=="y":
                                self.delete_passenger_Admin()
                            else: 
                                break
                    elif choice=="10":
                        self.var3=input("\n\n Enter User Id -->\t")
                        query="select * from users where user_id=%s"
                        data=(self.var3,)
                        self.cursor.execute(query,data)
                        table=from_db_cursor(self.cursor)
                        print(table)

                    elif choice=="11":
                        print(" -->>-->>-->>| Thank You |<<--<<--<<-- ")
                        fms.main()          
            else:
                print("  -->>-->>-->>|  Incorrect Password |<<--<<--<<-- ")      
        else:
            print("  -->>-->>-->>|  Enter valid name  |<<--<<--<<-- ")


    def user_login(self):
        try:
            self.var2=input("\nEnter your name -->  ")
            self.email=input("Enter your E-mail --> \t")
            self.pattern='^[a-z]+[._]?[a-z0-9]+[@][a-z0-9_]+[.][a-z0-9_]{2,3}$'
            if re.search(self.pattern,self.email):             
                self.password=maskpass.askpass("Enter Your Password --> ",mask='*')
                query='select * from users where username=%s and email=%s and password=%s'
                data=(self.var2,self.email,self.password)
                self.cursor.execute(query,data)
                count=0
                for i in self.cursor:
                    count+=1
                if count==1:
                    while(True):      
                        print("\nx-x-x-x ---=--=-=-=-=-=-=-=-=-=-=-==--=-=---  x-x-x-x \n")
                        print("\n[1] Display Flights Details \n[2] Book Your Reservation Seat \n[3] Show your Ticket \n[4] Show FOODs Menu.\n[5] Ordered FOOD \n[6] Cancle your Reservation \n[7] Exit ")
                        print("\nx-x-x-x ---=--=-=-=-=-=-=-=-=-=-=-==--=-=---  x-x-x-x\n ")
                        choice1=(input("Enter your choice --> \t ") )
                        if choice1=="1":
                            self.Display_Flights()
                        elif choice1=="2":
                                self.Reservation()
                                while True:
                                    print("\n\n Do you want to Reseve ticket's more.?")
                                    var=input("\y/n --> \t")
                                    if var=="y":
                                        self.Reservation()
                                    else: 
                                        break
                        elif choice1=="3":
                                self.show_your_Reservation()
                        elif choice1=="4":
                                self.showfoodmenu()
                        elif choice1=="5":
                                self.ord_food()
                                while True:
                                    print("\n\n Do you want to Ordered more?")
                                    var=input("y/n --->\t")
                                    if var=="y":
                                        self.ord_food()
                                    else: 
                                        break        
                        elif choice1=="6":
                                self.delete_passenger1_User()
                                while True:
                                    print("\n\n Do you want to cancle more?")
                                    var=input("y/n -->\t")
                                    if var=="y":
                                        self.delete_passenger1_User()
                                    else: 
                                        break        
                        elif choice1=="7":
                            print("\n-->>-->>-->>| Thank you for visiting the AIRLINES |<<--<<--<<--  ")
                            print("x-x-x-x ---=--=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-==--=-=--- \n\n x-x-x-x ")
                            break 
                        else:
                            print("  -->>-->>-->>|  Enter valid choice |<<--<<--<<--    ")          
                else:
                    print(" -->>-->>-->>| Enter valid username and password |<<--<<--<<--   ")  
            else:
                print("-->>-->>-->>|  Enter valid Your Email |<<--<<--<<-")
        except :
              print("\nEnter valid choice ..")   
            
            



    def Display_Flights(self):
        print("\n------>---->--->---->---->---->|                                     |<-----<-----<-----<---<-----<-------")
        print("------>---->--->---->---->---->| Welcome To",self.name,"|<-----<-----<-----<----<-----<------")
        print("------>---->--->---->---->---->|                                     |<-----<-----<-----<----<-----<------")
        query="select * from flights ORDER BY Srno ASC"
        self.cursor.execute(query)
        table=from_db_cursor(self.cursor)
        print(table)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        


    def Reservation(self):
        self.rname=input("\n\nEnter Your Name --> ")
        if self.rname.isalpha():
            self.raddress=input("\nEnter Your Address --> ")

            n=1
            while n<4:
                self.bmobile=input("\nEnter Your Mobile No --> ")
                if self.bmobile.isdigit() and re.match('^[6-9]\d{9}$',self.bmobile):
                    self.cdate=datetime.now()
                    t=1
                    while t<4:    
                        self.bdate=input("\nEnter Your Reservation Date as (YYYY-MM-DD) --> ")
                        if datetime.strptime(self.bdate,'%Y-%m-%d')>self.cdate:
                            print(f"\n\n->->->->-Booked Your Reservation on {self.cdate},  ->->->-> THANK YOU!!!->->->->\n\n ")
                            try:
                                self.lst1=[(self.rname,self.raddress,self.bmobile,self.cdate,self.bdate)]  
                                self.cursor.executemany('''insert into passenger(name,address,mobile_number,booking_date_time,rdate) values(%s,%s,%s,%s,%s)''',self.lst1)
                                self.mydb.commit()
                                self.data1=(self.bmobile,)
                                query ='Select * from passenger where mobile_number = %s'              
                                self.cursor.execute(query,self.data1)
                                self.mytab=from_db_cursor(self.cursor)
                                print(self.mytab)

                            except :
                                print("\n\nQuery Not Updated , Please Try After Sometime")

                            print("\n\nRedirecting to the Flight Searching Page And Payment Page........")
                            fms.payment()
                            break
                        else:
                            print("\nCheck Your format.")
                            if t==3:
                                print("Too many attempts. Invalid Date.")
                                break
                            t+=1

                else: 
                    print("\nEnter a Valid Mobile No. -->")
                    if n==3:
                        print("-->>Too many attempts. Invalid Mobile Number<<--")
                        exit()
                    n+=1  
                    
        else:
            print("\nPlease Enter a Valid Name.")



    def Display_ALL_Reservation(self):
        query ='Select * from payment'              
        self.cursor.execute(query)
        self.mytab=from_db_cursor(self.cursor)
        print(self.mytab)


    def show_your_Reservation(self):
        self.var=input("Enter your Mobile No.--> ")
        self.data1=[(self.var)]
        query ='Select * from payment where mobile_number = %s'              
        self.cursor.execute(query,self.data1)
        self.mytab=from_db_cursor(self.cursor)
        print(self.mytab)


    def Admin_show_single_Reservation(self):
        self.var=input("Enter your Passenger ID --> \t")
        self.data1=[(self.var)]
        query ='Select * from payment where passenger_id = %s'              
        self.cursor.execute(query,self.data1)
        self.mytab=from_db_cursor(self.cursor)
        print(self.mytab)


    def delete_passenger_Admin(self):
        query ='Select * from payment'              
        self.cursor.execute(query)
        self.mytab=from_db_cursor(self.cursor)
        print(self.mytab)
        var=input("Enter Passenger ID which one you want you delete Passenger diteal --> \t")
        self.cursor.executemany("delete from payment where passenger_id=%s;",[(var,)])
        self.cursor.execute("select * from payment ")
        mytable1=from_db_cursor(self.cursor)
        print(mytable1)
        print("\n\n--->>-->>-->>-->>-Record Deleted-<<--<<--<<--<<---")



    def delete_passenger1_User(self):
        self.data1=input("Enter Your Mobile Number --> \t")
        self.data2=(self.data1,)
        query1 ='delete from payment where mobile_number=%s;'
        self.cursor.execute(query1,self.data2)
        print("\n\n--->>-->>-->>-->>-Record Deleted-<<--<<--<<--<<---")
        



    def payment(self):
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            self.payid=input("\nEnter Your Mobile No. -->")
            self.source=input("\nEnter Your Source --> ")        
            self.destination=input("\nEnter Your Destination --> ")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            self.cls=input("\n[1]--Business class--\n[2]--First class--\n[3]--Economy class-- \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nEnter your choice --> \t")        
            
            self.cursor.execute("select passenger_id,name,address,booking_date_time,rdate from passenger where mobile_number=%s ",(self.payid,))
            prow=self.cursor.fetchone()
            
            self.cursor.execute("select Airlines_name,Flight_no from flights where Sorce=%s and Destination=%s",(self.source,self.destination))
            frow=self.cursor.fetchone()

            self.cursor.execute("select  class_type,Amount from tclass where cls_Srno= %s ",(self.cls,))
            ctyperow=self.cursor.fetchone()
 
            print("\n\nFetching Details, Please wait-->->>->>>")

            try:
                query='''insert into payment(passenger_id,name,address,mobile_number,Sorce,Destination,Airlines_name,Flight_no,cls_Srno,class_type,booking_date_time,rdate,Amount) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''' 
                self.cursor.execute(query,(prow[0],prow[1],prow[2],self.payid,self.source,self.destination,frow[0],frow[1],self.cls,ctyperow[0],prow[3],prow[4],ctyperow[1]))
                self.mydb.commit()
                self.data1=(self.payid,)
                query1 ='Select * from payment where mobile_number = %s'
                self.cursor.execute(query1,self.data1)
                self.mytab=from_db_cursor(self.cursor)
                print(self.mytab)
        
            except:
                print("\n\n-->>->>- Sorry this flight Not Available -<<-<<--")
                print("\n>>>>>>> Please Check the Flight details <<<<<<<<<<")
                fms.payment()  

            print("\n\nFetching Details, Please wait-->->>->>>")
                        
            self.upi=input("\n\nEnter Your UPI Id --> ")
            self.upi_condition='[a-zA-Z0-9.\-_]{2,256}@[a-zA-Z]{2,8}'
                        
            u=0	
            if re.search(self.upi_condition, self.upi):
                n=0
                while n<4:
                    print("\n\nPlease Enter the otp given below ")
                    self.otpgen=random.randint(1000,10000)
                    print(f"\n\t\t [ {self.otpgen} ]")
                    self.inpotp=input("\n\tENTER OTP HERE--> \t")
                    if str(self.otpgen)==self.inpotp:
                        print(f"\n\t\t~~~~~~~~~~~~~~||Payment Successful Thank you||~~~~~~~~~~~~~~~~\n\t\t~~~~~~~~~~~~~~~~~~||   HAPPY JOURNEY SAFE JOURNEY  ||~~~~~~~~~~~~~~~~")
                        break
                    else:
                        print("\n\n-->>-->>| Invalid Otp |<<--<<--")
                        n+=1
            else:
                print("\n\nEnter a valid upi id --> \t")
                u+=1
                if u==4:
                    print("-->>-->>-Wrong UPI Id entered many times-<<--<<--")
                else:
                    fms.payment()
            

    def showfoodmenu(self):
        print("-->>-->>-->>-->>-->>-| All FOOD ITEMSs Available |-<<--<<--<<--<<--<<--*\n\n")
        query="select * from food"
        self.cursor.execute(query)
        table=from_db_cursor(self.cursor)                   
        print(table)



    def add_food(self):
        try:
            query="select * from food"
            self.cursor.execute(query)
            table1=from_db_cursor(self.cursor)
            print(table1)  

            itemname=input("Enter a FOODname -->")
            price=int(input("Enter Price Of Food Item Per Piece -->\t"))
            Val =[(itemname,price)]
            
            self.cursor.executemany("insert into food(FOODSname,price) values (%s,%s)",Val)
            self.mydb.commit()
            print("--->>-->>-->>-->>-->>-| Adding New FOOD ITEMSs in Menu |-<<--<<--<<--<<--<<---")
            self.cursor.execute("select * from food")
            mytable = from_db_cursor(self.cursor)
            print(mytable)
                        
        except:
            print("Already Exist in Food Menu")



    def delete_food(self):
        try:
            print("**--**--**--**--| Before any changes in FOOD Menu |--**--**--**--**\n")
            c1=self.mydb.cursor()
            c1.execute("select food_id,FOODSname,price from food")
            mytable = from_db_cursor(c1)
            print(mytable)
        
            b=input("\n\nEnter food name which one you want you delete in menu -->  \t")
            mc=self.mydb.cursor()
            mc.executemany("delete from food where FOODSname=%s;",[(b,)])
            mc.execute("select * from food ")
            mytable1=from_db_cursor(mc)
            print(mytable1)
            print("\n\n--->>-->>-->>-->>| Record Deleted |<<--<<--<<--<<---")
        except:
            print("Already Deleted in Food Menu")



    def ord_food(self):
        self.pid = int(input("ENTER PASSENGER ID --> \t"))
        self.name = input("Enter your Name:")
        query='select * from passenger where passenger_id=%s and name=%s'
        data=(self.pid,self.name)
        self.cursor.execute(query,data)
        count=0
        for i in self.cursor:
            count+=1
        if count==1:
            self.cursor.execute("select * from food ")
            mytable1=from_db_cursor(self.cursor)
            print(mytable1)
            self.foodid = int(input("\n\nEnter Food ID --> \t"))
            
            self.cursor.execute("select FOODSname,price from food where food_id= %s ",(self.foodid,))
            frow=self.cursor.fetchone()

            try:
                query='''insert into Ordered(food_id,passenger_id,name,FOODSname,price) values(%s,%s,%s,%s,%s)''' 
                self.cursor.execute(query,(self.foodid,self.pid,self.name,frow[0],frow[1]))
                self.mydb.commit()
                self.data1=(self.foodid,)

                query1 ='Select * from Ordered where food_id = %s'
                self.cursor.execute(query1,self.data1)
                self.mytab=from_db_cursor(self.cursor)
                print(self.mytab)
            
            except :
                print("\n\nNo such Food Id found.")
                fms.ord_food()
        else:
            print("\n -->>-->>-->>| Enter valid name and Passenger Id |<<--<<--<<--  ")
            fms.ord_food()



    def main(self):
        print("\n\n\n-->>-->| Welcome to",self.name,"|<--<<--")
        while(True):
            print("\nx-x-x-x---=--=-=-=-=-=-=-=-=-=-=-==--=-=---x-x-x-x \n\n")
            print("\t[1]--Admin Login--\n\t[2]--User Register-- \n\t[3]--User login-- \n\t[4]--Exit--")
            print("\nx-x-x-x---=--=-=-=-=-=-=-=-=-=-=-==--=-=---x-x-x-x \n\n")
            choice=(input("\nEnter your choice --> \t"))
            if choice=="1":
                self.Admin_login()    
            elif choice=="2":
                self.user_register()
            elif choice=="3":
                self.user_login()
            elif choice==".":
                query='''Drop tables Ordered,payment'''
                self.cursor.execute(query)
            elif choice=="4":
                print("\n-->>-->>-->>| Thank you for Visiting the AIRLINES |<<--<<--<<-- \n\n")
                break
            else:
                print("-->>-->>-->>| Enter valid choice |<<--<<--<<-  ")
                  

    

fms=Tab()
fms.main()


