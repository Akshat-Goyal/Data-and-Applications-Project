import subprocess as sp
import pymysql
import pymysql.cursors
from adminFunctions import *


def admin(con, cur):
	while(True):
		tmp = sp.call('clear',shell=True)
		print("Do you want to enter:")
		print("1. Passenger Table")
		print("2. Port Table")
		print("3. Ship Table")
		print("4. Cargo Ship Table")
		print("5. Passenger Ship Table")
		print("6. Booking Agent Table")
		print("7. Route Table")
		print("8. Ticket Table")
		print("9. Department Table")
		print("10. Employee Table")
		print("11. Security Table")
		print("12. Drivers Table")
		print("13. Other Staff Table")
		print("14. Employee Dependents Table")
		print("15. Passenger PhoneNumber; Table")
		print("16. Passenger EmailID Table")
		print("17. Employee PhoneNumber Table")
		print("18. Employee EmailID Table")
		print("19. Employee Dependent Phone No Table")
		print("20. Employee Dependent EmailID Table")
		print("21. State_Country Table")
		print("22. Logout")
		ch = int(input("Enter choice> "))
		tmp = sp.call('clear',shell=True)
		if ch == 1:
			passenger(con, cur)
		elif ch == 2:
			port(con, cur)
		elif ch == 3:
			ship(con, cur)
		elif ch == 4:
			cargoShip(con, cur)
		elif ch == 5:
			passengerShip(con, cur)
		elif ch == 6:
			agent(con, cur)
		elif ch == 7:
			route(con, cur)
		elif ch == 8:
			ticket(con, cur)
		elif ch == 9:
			department(con, cur)
		elif ch == 10:
			employee(con, cur)
		elif ch == 11:
			security(con, cur)
		elif ch == 12:
			driver(con, cur)
		elif ch == 13:
			otherStaff(con, cur)
		elif ch == 14:
			employeeDependent(con, cur)
		elif ch == 15:
			passPNo(con, cur)
		elif ch == 16:
			passEmail(con, cur)
		elif ch == 17:
			empPNo(con, cur)
		elif ch == 18:
			empEmail(con, cur)
		elif ch == 19:
			empDepPNo(con, cur)
		elif ch == 20:
			empDepEmail(con, cur)
		elif ch == 21:
			stateCountry(con, cur)
		elif ch == 22:
			return 1
		else:
			print("Please choose the correct option")

def user(id, con, cur):
	while(True):
		print("Do you want to:")
		print("1. Book Ticket")
		print("2. Logout")
		ch = int(input("Enter choice> "))
		if ch == 1:
			return 1
		elif ch == 2:
			return 1
		else:
			print("Please choose the correct option")

def login(con, cur):
	try:
		info = {}
		info["ID"] = int(input("Passenger_ID: "))
		query = "SELECT * FROM Passenger WHERE Passenger_ID = '%d'" %(info["ID"]);
		cur.execute()
		row = cur.fetchone()
		if row == None:
			print("You are not registered.")
			return
		tmp = sp.call('clear',shell=True)
		print("You are logged in.\n")
		user(info["ID"], con, cur)
	except Exception as er:
		print(er)

def register(con, cur):
	try:
		info = {}
		info["ID"] = int(input("Passenger_ID: "))
		query = "SELECT * FROM Passenger WHERE Passenger_ID = '%d'" %(info["ID"]);
		cur.execute()
		row = cur.fetchone()
		if row != None:
			print("Passenger_ID already exists.")
			return
		info["Fname"], info["Mname"], info["Lname"] = (input("Name (Fname Minit Lname): ")).split(' ')	
		info["DOB"] = input("DOB (YYYY-MM-DD): ")
		info["Gender"] = input("Gender (Male, Female, Others): ")
		info["Address"] = input("Address : ")
		info["Pin Code"] = int(input("Pin Code : "))
		info["State"] = input("State : ")
		query = "INSERT INTO Passenger(Passenger_ID, First_Name, Middle_Name, Last_Name, DOB, Gender, Address, PinCode, State) VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s')" %(info["ID"], info["Fname"], info["Mname"], info["Lname"], info["DOB"], info["Gender"], info["Address"], info["Pin Code"], info["State"]);
		cur.execute(query)
		con.commit()
		info["PNo1"] = input("Phone Number1 : ")
		info["PNo2"] = input("Phone Number2 : ")
		info["E1"] = input("Email ID1 : ")
		info["E2"] = input("Email ID2 : ")
		query = "INSERT INTO Passenger_PhoneNumber(Passenger_ID, PhoneNumber) VALUES('%d', '%s')" %(info["ID"], info["PNo1"]);
		cur.execute(query)
		con.commit()
		query = "INSERT INTO Passenger_EmailID(Passenger_ID, EmailID) VALUES('%d', '%s')" %(info["ID"], info["E1"]);
		cur.execute(query)
		con.commit()
		if info["PNo2"] != "":
			query = "INSERT INTO Passenger_PhoneNumber(Passenger_ID, PhoneNumber) VALUES('%d', '%s')" %(info["ID"], info["PNo2"]);
			cur.execute(query)
			con.commit()
		if info["E2"] != "":
			query = "INSERT INTO Passenger_EmailID(Passenger_ID, EmailID) VALUES('%d', '%s')" %(info["ID"], info["E2"]);
			cur.execute(query)
			con.commit()
		tmp = sp.call('clear',shell=True)
		print("\nSuccessfully Registered. You are logged in.\n")
		user(info["ID"], con, cur)
	except Exception as er:
		con.rollback()
		print("Failed to insert into database")
		print(">>>>>>>>>", er)


if __name__ == '__main__':
	run = 1
	while(run):
		tmp = sp.call('clear',shell=True)
		# username = input("Username: ")
		# password = input("Password: ")
		
		try:
			con = pymysql.connect(host='localhost',
					user='user',
					password='password',
					db='SHIP_MANAGEMENT_SYSTEM',
					cursorclass=pymysql.cursors.DictCursor)
			tmp = sp.call('clear',shell=True)

			if(con.open):
				print("Connected")
			else:
				print("Failed to connect")

			tmp = input("Press ENTER key to CONTINUE>")

			with con:
				cur = con.cursor()
				while(1):
					tmp = sp.call('clear',shell=True)
					print("Do you want to:")
					print("1. Register as User")
					print("2. Login as User")
					print("3. Login as Admin")
					print("4. Exit the system")
					ch = int(input("Enter choice> "))
					if ch == 1:
						register(con, cur)
						tmp = input("Press ENTER to CONTINUE>")
					elif ch == 2:
						login(con, cur)
						tmp = input("Press ENTER to CONTINUE>")
					elif ch == 3:
						while(True):
							tmp = input("Enter the password to CONTINUE> ")
							sp.call('clear',shell=True)
							if tmp == 'admin':
								print("Successfully logged in.\n")
								input("Press ENTER to CONTINUE>")
								admin(con, cur)
								break
							else:
								print("Wrong password. Do you want to:")
								print("1. Login")
								print("2. Go back")
								ch = int(input("Enter choice> "))
								if ch != 1:
									break
					elif ch == 4:
						run = 0
						break
					else:
						print("Please choose the correct option")
						tmp = input("Press ENTER to CONTINUE>")

		except:
			tmp = sp.call('clear',shell=True)
			print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
			tmp = input("Press ENTER to CONTINUE>")
