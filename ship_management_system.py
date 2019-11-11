import subprocess as sp
import pymysql
import pymysql.cursors
from adminFunctions import *

def passengerShip(con, cur):
	while(True):
		print("Do you want to:")
		print("1. See all entries")
		print("2. Add new entry")
		print("3. Modify the entry")
		print("4. Delete the entry")
		print("5. Go back")
		ch = int(input("Enter choice> "))
		if ch == 1:
			try:
				query = 'SELECT * FROM PassengerShip;'
				cur.execute(query)
				rows = cur.fetchall()
				for row in rows:
					print(row)
				print("")
			except Exception as er:
				print("Failed to show entries")
				print(">>>>>>>>>", er)
		elif ch == 2:
			try:
				info = {}
				info["ID"] = int(input("Ship_ID: "))
				info["Capacity"] = float(input("Capacity (TEU) : "))
				info["Facilities"] = input("Facilities : ")
				query = "INSERT INTO PassengerShip(Ship_ID, Capacity(TEU), Facilities) VALUES('%d', '%f', '%s')" %(info["ID"], info["Capacity"], info["Facilities"]);
				cur.execute(query)
				con.commit()
				print("Successfully Added\n")
			except Exception as er:
				con.rollback()
				print("Failed to insert into database")
				print(">>>>>>>>>", er)
		elif ch == 3:
			try:
				info = {}
				ID = int(input("Enter Ship_ID to modify: "))
				query = "SELECT * FROM PassengerShip where Ship_ID = '%d'" %(ID);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Ship_ID: ")
				if info["ID"] != "":
					row["Ship_ID"] = int(info["ID"])
				info["Capacity"] = input("Capacity (TEU) : ")	
				if info["Capacity"] != "":
					row["Capacity(TEU)"] = float(info["Capacity"])
				info["Facilities"] = input("Facilities : ")
				if info["Facilities"] != "":
					row["Facilities"] = info["Facilities"]
				query = "UPDATE PassengerShip SET Ship_ID = '%d', Capacity(TEU) = '%f', Facilities = '%s' WHERE Ship_ID = '%d'" %(row["Ship_ID"], row["Capacity(TEU)"], row["Facilities"], ID);
				cur.execute(query)
				con.commit()
				print("Successfully Modified\n")
			except Exception as er:
				con.rollback()
				print("Failed to modify in the database")
				print(">>>>>>>>>", er)
		elif ch == 4:
			try:
				info = {}
				info["ID"] = int(input("Enter the Ship_ID you want to delete: "))
				query = "DELETE FROM PassengerShip WHERE Ship_ID = '%d'" %(info["ID"]);
				cur.execute(query)
				con.commit()
				print("Successfully Deleted\n")
			except Exception as er:
				con.rollback()
				print("Failed to delete in the database")
				print(">>>>>>>>>", er)
		elif ch == 5:
			return 1
		else:
			print("Please choose the correct option")


def admin(con, cur):
	while(True):
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
		# elif ch == 6:
		# 	agent(con, cur)
		# elif ch == 7:
		# 	route(con, cur)
		# elif ch == 8:
		# 	ticket(con, cur)
		# elif ch == 9:
		# 	department(con, cur)
		# elif ch == 10:
		# 	employee(con, cur)
		# elif ch == 11:
		# 	security(con, cur)
		# elif ch == 12:
		# 	driver(con, cur)
		# elif ch == 13:
		# 	otherStaff(con, cur)
		# elif ch == 14:
		# 	employeeDependent(con, cur)
		# elif ch == 15:
		# 	passPNo(con, cur)
		# elif ch == 16:
		# 	passEmail(con, cur)
		# elif ch == 17:
		# 	empPNo(con, cur)
		# elif ch == 18:
		# 	empEmail(con, cur)
		# elif ch == 19:
		# 	empDepPNo(con, cur)
		# elif ch == 20:
		# 	empDepEmail(con, cur)
		# elif ch == 21:
		# 	stateCountry(con, cur)
		elif ch == 22:
			return 1
		else:
			print("Please choose the correct option")

def user(con, cur):
	while(True):
		print("Do you want to:")
		print("1. Book Ticket")
		print("2. Logout")
		ch = int(input("Enter choice> "))
		if ch == 1:
			return 1
		elif ch == 2:
			return 1
			

def login(con, cur):
	try:
		return 1
	except:
		return 0

def register(con, cur):
	try:
		info = {}
		info["ID"] = int(input("Passenger_ID: "))
		info["Fname"], info["Mname"], info["Lname"] = (input("Name (Fname Minit Lname): ")).split(' ')	
		info["DOB"] = input("DOB (YYYY-MM-DD): ")
		info["Gender"] = input("Gender (Male, Female, Others): ")
		info["Address"] = input("Address : ")
		info["Pin Code"] = int(input("Pin Code : "))
		info["State"] = input("State : ")

		query = "INSERT INTO Passenger(Passenger_ID, First_Name, Middle_Name, Last_Name, DOB, Gender, Address, PinCode, State) VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s')" %(info["ID"], info["Fname"], info["Mname"], info["Lname"], info["DOB"], info["Gender"], info["Address"], info["Pin Code"], info["State"]);
		cur.execute(query)
		con.commit()
		print("Successfully Registered\n")
		return 1

	except Exception as er:
		con.rollback()
		print("Failed to insert into database")
		print(">>>>>>>>>", er)
		return 0


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
						if register(con, cur):
							user(con, cur)
						else:
							tmp = input("Press ENTER to CONTINUE>")
					elif ch == 2:
						if login(con, cur):
							user(con, cur)
						else:
							tmp = input("Press ENTER to CONTINUE>")
					elif ch == 3:
						while(True):
							tmp = input("Enter the password to CONTINUE> ")
							sp.call('clear',shell=True)
							if tmp == 'admin':
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
