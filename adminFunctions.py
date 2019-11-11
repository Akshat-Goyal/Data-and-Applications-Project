
def passenger(con, cur):
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
				query = 'SELECT * FROM Passenger;'
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
				print("Successfully Added\n")
			except Exception as er:
				con.rollback()
				print("Failed to insert into database")
				print(">>>>>>>>>", er)
		elif ch == 3:
			try:
				info = {}
				ID = int(input("Enter Passenger_ID to modify: "))
				query = "SELECT * FROM Passenger where Passenger_ID = '%d'" %(ID);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Passenger_ID: ")
				if info["ID"] != "":
					row["Passenger_ID"] = int(info["ID"])
				info["name"] = input("Name (Fname Minit Lname): ")
				if info["name"] != "":
					row["First_Name"], row["Middle_Name"], row["Last_Name"] = info["name"].split(' ')	
				info["DOB"] = input("DOB (YYYY-MM-DD): ")
				if info["DOB"] != "":
					row["DOB"] = info["DOB"]
				info["Gender"] = input("Gender (Male, Female, Others): ")
				if info["Gender"] != "":
					row["Gender"] = info["Gender"]
				info["Address"] = input("Address : ")
				if info["Address"] != "":
					row["Address"] = info["Address"]
				info["Pin Code"] = input("Pin Code : ")
				if info["Pin Code"] != "":
					row["PinCode"] = int(info["Pin Code"])
				info["State"] = input("State : ")
				if info["State"] != "":
					row["State"] = info["State"]
				query = "UPDATE Passenger SET Passenger_ID = '%d', First_Name = '%s', Middle_Name = '%s', Last_Name = '%s', DOB = '%s', Gender = '%s', Address = '%s', PinCode = '%d', State = '%s' WHERE Passenger_ID = '%d'" %(row["Passenger_ID"], row["First_Name"], row["Middle_Name"], row["Last_Name"], row["DOB"], row["Gender"], row["Address"], row["PinCode"], row["State"], ID);
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
				info["ID"] = int(input("Enter the Passenger_ID you want to delete: "))
				query = "DELETE FROM Passenger WHERE Passenger_ID = '%d'" %(info["ID"]);
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


def port(con, cur):
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
				query = 'SELECT * FROM Port;'
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
				info["ID"] = int(input("Port_ID: "))
				info["Name"] = input("Port Name : ")	
				info["Capacity"] = int(input("Port Capacity (Ships): "))

				query = "INSERT INTO Port(Port_ID, PortName, PortCapacity(Ships)) VALUES('%d', '%s', '%d')" %(info["ID"], info["Name"], info["Capacity"]);
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
				ID = int(input("Enter Port_ID to modify: "))
				query = "SELECT * FROM Port where Port_ID = '%d'" %(ID);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Port_ID: ")
				if info["ID"] != "":
					row["Port_ID"] = int(info["ID"])
				info["Name"] = input("Port Name : ")
				if info["Name"] != "":
					row["PortName"] = info["Name"]	
				info["Capacity"] = input("Port Capacity (Ships): ")
				if info["Capacity"] != "":
					row["PortCapacity(Ships)"] = int(info["Capacity"])
				query = "UPDATE Port SET Port_ID = '%d', PortName = '%s', PortCapacity(Ships) = '%d' WHERE Port_ID = '%d'" %(row["Port_ID"], row["PortName"], row["PortCapacity(Ships)"], ID);
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
				info["ID"] = int(input("Enter the Port_ID you want to delete: "))
				query = "DELETE FROM Port WHERE Port_ID = '%d'" %(info["ID"]);
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

def ship(con, cur):
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
				query = 'SELECT * FROM Ship;'
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
				info["Name"] = input("Ship Name : ")	
				info["Type"] = input("Ship Type: ")
				info["Service Date"] = input("Service Date (YYYY-MM-DD) : ")
				info["Source"] = int(input("Source : "))
				info["Destination"] = int(input("Destination : "))
				query = "INSERT INTO Ship(Ship_ID, ShipName, ShipType, Last_Service_Date, SourcePort_ID, DestinationPort_ID) VALUES('%d', '%s', '%s', '%s', '%d', '%d')" %(info["ID"], info["Name"], info["Type"], info["Service Date"], info["Source"], info["Destination"]);
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
				query = "SELECT * FROM Ship where Ship_ID = '%d'" %(ID);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Ship_ID: ")
				if info["ID"] != "":
					row["Ship_ID"] = int(info["ID"])
				info["Name"] = input("Ship Name : ")	
				if info["Name"] != "":
					row["ShipName"] = info["Name"]	
				info["Type"] = input("Ship Type: ")
				if info["Type"] != "":
					row["ShipType"] = info["Type"]
				info["Service Date"] = input("Service Date (YYYY-MM-DD) : ")
				if info["Service Date"] != "":
					row["Last_Service_Date"] = info["Service Date"]
				info["Source"] = input("Source : ")
				if info["Source"] != "":
					row["SourcePort_ID"] = int(info["Source"])
				info["Destination"] = input("Destination : ")
				if info["Destination"] != "":
					row["DestinationPort_ID"] = int(info["Destination"])
				query = "UPDATE Ship SET Ship_ID = '%d', ShipName = '%s', ShipType = '%s', Last_Service_Date = '%s', SourcePort_ID = '%d', DestinationPort_ID = '%d' WHERE Ship_ID = '%d'" %(row["Ship_ID"], row["ShipName"], row["ShipType"], row["Last_Service_Date"], row["SourcePort_ID"], row["DestinationPort_ID"], ID);
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
				query = "DELETE FROM Ship WHERE Ship_ID = '%d'" %(info["ID"]);
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


def cargoShip(con, cur):
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
				query = 'SELECT * FROM CargoShip;'
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
				info["Cost"] = float(input("Cost (Rupees per TEU) : "))
				query = "INSERT INTO CargoShip(Ship_ID, Capacity(TEU), Cost(Rupees per TEU)) VALUES('%d', '%f', '%f')" %(info["ID"], info["Capacity"], info["Cost"]);
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
				query = "SELECT * FROM CargoShip where Ship_ID = '%d'" %(ID);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Ship_ID: ")
				if info["ID"] != "":
					row["Ship_ID"] = int(info["ID"])
				info["Capacity"] = input("Capacity (TEU) : ")	
				if info["Capacity"] != "":
					row["Capacity(TEU)"] = float(info["Capacity"])
				info["Cost"] = input("Cost (Rupees per TEU) : ")
				if info["Cost"] != "":
					row["Cost(Rupees per TEU)"] = float(info["Cost"])
				query = "UPDATE CargoShip SET Ship_ID = '%d', Capacity(TEU) = '%f', Cost(Rupees per TEU) = '%f' WHERE Ship_ID = '%d'" %(row["Ship_ID"], row["Capacity(TEU)"], row["Cost(Rupees per TEU)"], ID);
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
				query = "DELETE FROM CargoShip WHERE Ship_ID = '%d'" %(info["ID"]);
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

