
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

				query = "INSERT INTO Port(Port_ID, PortName, `PortCapacity(Ships)`) VALUES('%d', '%s', '%d')" %(info["ID"], info["Name"], info["Capacity"]);
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
				query = "UPDATE Port SET Port_ID = '%d', PortName = '%s', `PortCapacity(Ships)` = '%d' WHERE Port_ID = '%d'" %(row["Port_ID"], row["PortName"], row["PortCapacity(Ships)"], ID);
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
				query = "INSERT INTO CargoShip(Ship_ID, `Capacity(TEU)`, `Cost(Rupees per TEU)`) VALUES('%d', '%f', '%f')" %(info["ID"], info["Capacity"], info["Cost"]);
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
				query = "UPDATE CargoShip SET Ship_ID = '%d', `Capacity(TEU)` = '%f', `Cost(Rupees per TEU)` = '%f' WHERE Ship_ID = '%d'" %(row["Ship_ID"], row["Capacity(TEU)"], row["Cost(Rupees per TEU)"], ID);
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
				query = "INSERT INTO PassengerShip(Ship_ID, `Capacity(TEU)`, Facilities) VALUES('%d', '%f', '%s')" %(info["ID"], info["Capacity"], info["Facilities"]);
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
				query = "UPDATE PassengerShip SET Ship_ID = '%d', `Capacity(TEU)` = '%f', Facilities = '%s' WHERE Ship_ID = '%d'" %(row["Ship_ID"], row["Capacity(TEU)"], row["Facilities"], ID);
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


def agent(con, cur):
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
				query = 'SELECT * FROM BookingAgent;'
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
				info["ID"] = int(input("Agent_ID: "))
				info["Name"] = input("Agent Name : ")
				query = "INSERT INTO BookingAgent(Agent_ID, AgentName) VALUES('%d', '%s')" %(info["ID"], info["Name"]);
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
				ID = int(input("Enter Agent_ID to modify: "))
				query = "SELECT * FROM BookingAgent where Agent_ID = '%d'" %(ID);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Agent_ID: ")
				if info["ID"] != "":
					row["Agent_ID"] = int(info["ID"])
				info["Name"] = input("Agent Name : ")	
				if info["Name"] != "":
					row["AgentName"] = info["Name"]
				query = "UPDATE BookingAgent SET Agent_ID = '%d', AgentName = '%s' WHERE Agent_ID = '%d'" %(row["Agent_ID"], row["AgentName"], ID);
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
				info["ID"] = int(input("Enter the Agent_ID you want to delete: "))
				query = "DELETE FROM BookingAgent WHERE Agent_ID = '%d'" %(info["ID"]);
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


def route(con, cur):
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
				query = 'SELECT * FROM Route;'
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
				info["PID"] = int(input("Port_ID: "))
				info["SNo"] = int(input("Stop Number : "))
				info["ATime"] = input("Arrival Time (YYYY-MM-DD HH-MM-SS) : ")	
				info["DTime"] = input("Departure Time (YYYY-MM-DD HH-MM-SS) : ")	
				query = "INSERT INTO Route(Ship_ID, Port_ID, StopNumber, ArrivalTime, DepartureTime) VALUES('%d', '%d', '%d', '%s', '%s')" %(info["ID"], info["PID"], info["SNo"], info["ATime"], info["DTime"]);
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
				Time = input("Enter Departure Time (YYYY-MM-DD HH-MM-SS) to modify: ")	
				query = "SELECT * FROM Route where Ship_ID = '%d' AND DepartureTime = '%s'" %(ID, Time);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Ship_ID: ")
				if info["ID"] != "":
					row["Ship_ID"] = int(info["ID"])
				info["PID"] = input("Port_ID: ")
				if info["PID"] != "":
					row["Port_ID"] = int(info["PID"])
				info["SNo"] = input("Stop Number: ")
				if info["SNo"] != "":
					row["StopNumber"] = int(info["SNo"])
				info["ATime"] = input("Arrival Time (YYYY-MM-DD HH-MM-SS) : ")	
				if info["ATime"] != "":
					row["ArrivalTime"] = info["ATime"]
				info["DTime"] = input("Departure Time (YYYY-MM-DD HH-MM-SS) : ")	
				if info["DTime"] != "":
					row["DepartureTime"] = info["DTime"]
				query = "UPDATE Route SET Ship_ID = '%d', Port_ID = '%d', StopNumber = '%d', ArrivalTime = '%s', DepartureTime = '%s' WHERE Ship_ID = '%d' AND DepartureTime = '%s'" %(row["Ship_ID"], row["Port_ID"], row["Stop Number"], row["ArrivalTime"], row["DepartureTime"], ID, Time);
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
				info["Time"] = input("Enter the Departure Time (YYYY-MM-DD HH-MM-SS) you want to delete: ")
				query = "DELETE FROM Route WHERE Ship_ID = '%d' AND DepartureTime = '%s'" %(info["ID"], info["Time"]);
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


def ticket(con, cur):
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
				query = 'SELECT * FROM Ticket;'
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
				info["ID"] = int(input("Ticket_ID: "))
				info["SID"] = int(input("Ship_ID: "))
				info["PID"] = int(input("Port_ID: "))
				info["PsID"] = int(input("Passenger_ID: "))
				info["AID"] = int(input("Agent_ID: "))
				info["seat"] = int(input("Seat Number : "))
				info["time"] = input("Departure Time (YYYY-M-DD HH-MM-SS) : ")
				query = "INSERT INTO Ticket(Ticket_ID, Ship_ID, Port_ID, Passenger_ID, Agent_ID, SeatNo, DepartureTime) VALUES('%d', '%d', '%d', '%d', '%d', '%d', '%s')" %(info["ID"], info["SID"], info["PID"], info["PsID"], info["AID"], info["seat"], info["time"]);
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
				ID = int(input("Enter Ticket_ID to modify: "))
				query = "SELECT * FROM Ticket where Ticket_ID = '%d'" %(ID);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Ticket_ID: ")
				if info["ID"] != "":
					row["Ticket_ID"] = int(info["ID"])
				info["SID"] = input("Ship_ID: ")
				if info["SID"] != "":
					row["Ship_ID"] = int(info["SID"])
				info["PID"] = input("Port_ID: ")
				if info["PID"] != "":
					row["Port_ID"] = int(info["PID"])
				info["PsID"] = input("Passenger_ID: ")
				if info["PsID"] != "":
					row["Passenger_ID"] = int(info["PsID"])
				info["AID"] = input("Agent_ID: ")
				if info["AID"] != "":
					row["Agent_ID"] = int(info["AID"])
				info["seat"] = input("Seat Number : ")
				if info["seat"] != "":
					row["SeatNo"] = int(info["seat"])
				info["time"] = input("Departure Time (YYYY-M-DD HH-MM-SS) : ")
				if info["time"] != "":
					row["DepartureTime"] = int(info["time"])
				query = "UPDATE Ticket SET Ticket_ID = '%d', Ship_ID = '%d', Port_ID = '%d', Passenger_ID = '%d', Agent_ID = '%d', SeatNo = '%d', DepartureTime = '%s' WHERE Ticket_ID = '%d'" %(row["Ticket_ID"], row["Ship_ID"], row["Port_ID"], row["Passenger_ID"], row["Agent_ID"], row["SeatNo"], row["DepartureTime"], ID);
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
				info["ID"] = int(input("Enter the Ticket_ID you want to delete: "))
				query = "DELETE FROM Ticket WHERE Ticket_ID = '%d'" %(info["ID"]);
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


def department(con, cur):
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
				query = 'SELECT * FROM Department;'
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
				info["ID"] = int(input("Department_ID: "))
				info["Name"] = input("Department Name: ")
				info["ENo"] = int(input("Number Of Employees: "))
				query = "INSERT INTO Department(Department_ID, DepartmentName, NumberOfEmployees) VALUES('%d', '%s', '%d')" %(info["ID"], info["Name"], info["ENo"]);
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
				ID = int(input("Enter Department_ID to modify: "))
				query = "SELECT * FROM Department where Department_ID = '%d'" %(ID);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Department_ID: ")
				if info["ID"] != "":
					row["Department_ID"] = int(info["ID"])
				info["Name"] = input("Department Name: ")
				if info["Name"] != "":
					row["DepartmentName"] = info["Name"]
				info["ENo"] = input("Number Of Employees: ")
				if info["ENo"] != "":
					row["NumberOfEmployees"] = int(info["ENo"])
				query = "UPDATE Department SET Department_ID = '%d', DepartmentName = '%s', NumberOfEmployees = '%d' WHERE Department_ID = '%d'" %(row["Department_ID"], row["DepartmentName"], row["NumberOfEmployees"], ID);
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
				info["ID"] = int(input("Enter the Department_ID you want to delete: "))
				query = "DELETE FROM Department WHERE Department_ID = '%d'" %(info["ID"]);
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


def employee(con, cur):
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
				query = 'SELECT * FROM Employee;'
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
				info["ID"] = int(input("Employee_ID: "))
				info["Fname"], info["Mname"], info["Lname"] = (input("Name (Fname Minit Lname): ")).split(' ')	
				info["DOB"] = input("DOB (YYYY-MM-DD): ")
				info["Salary"] = int(input("Salary : "))
				info["DID"] = int(input("Department_ID : "))
				info["Gender"] = input("Gender (Male, Female, Others): ")
				info["Address"] = input("Address : ")
				info["Pin Code"] = int(input("Pin Code : "))
				info["State"] = input("State : ")
				query = "INSERT INTO Employee(Employee_ID, First_Name, Middle_Name, Last_Name, DOB, Gender, Address, PinCode, State, Salary, Department_ID) VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%d', '%d')" %(info["ID"], info["Fname"], info["Mname"], info["Lname"], info["DOB"], info["Gender"], info["Address"], info["Pin Code"], info["State"], info["Salary"], info["DID"]);
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
				ID = int(input("Enter Employee_ID to modify: "))
				query = "SELECT * FROM Employee where Employee_ID = '%d'" %(ID);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Employee_ID: ")
				if info["ID"] != "":
					row["Employee_ID"] = int(info["ID"])
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
				info["Salary"] = input("Salary: ")
				if info["Salary"] != "":
					row["Salary"] = int(info["Salary"])
				info["DID"] = input("Department_ID: ")
				if info["DID"] != "":
					row["Department_ID"] = int(info["DID"])
				query = "UPDATE Employee SET Employee_ID = '%d', First_Name = '%s', Middle_Name = '%s', Last_Name = '%s', DOB = '%s', Gender = '%s', Address = '%s', PinCode = '%d', State = '%s', Salary = '%d', Department_ID = '%d' WHERE Employee_ID = '%d'" %(row["Employee_ID"], row["First_Name"], row["Middle_Name"], row["Last_Name"], row["DOB"], row["Gender"], row["Address"], row["PinCode"], row["State"], row["Salary"], row["Department_ID"], ID);
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
				info["ID"] = int(input("Enter the Employee_ID you want to delete: "))
				query = "DELETE FROM Employee WHERE Employee_ID = '%d'" %(info["ID"]);
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


def security(con, cur):
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
				query = 'SELECT * FROM Security;'
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
				info["ID"] = int(input("Employee_ID : "))
				info["Exp"] = int(input("Experience (Years) : "))
				info["SID"] = int(input("Ship_ID : "))
				info["SC"] = input("Security Company : ")
				query = "INSERT INTO Security(Employee_ID, `Experience(Years)`, Ship_ID, SecurityCompany) VALUES('%d', '%d', '%d', '%s')" %(info["ID"], info["Exp"], info["SID"], info["SC"]);
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
				ID = int(input("Enter Employee_ID to modify: "))
				query = "SELECT * FROM Security where Employee_ID = '%d'" %(ID);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Employee_ID: ")
				if info["ID"] != "":
					row["Employee_ID"] = int(info["ID"])
				info["Exp"] = input("Experience (Years): ")
				if info["Exp"] != "":
					row["Experience(Years)"] = int(info["Exp"])
				info["SID"] = input("Ship_ID: ")
				if info["SID"] != "":
					row["Ship_ID"] = int(info["SID"])
				info["SC"] = input("Security Company: ")
				if info["SC"] != "":
					row["SecurityCompany"] = info["SC"]
				query = "UPDATE Security SET Employee_ID = '%d', `Experience(Years)` = '%d', Ship_ID = '%d', SecurityCompany = '%s' WHERE Employee_ID = '%d'" %(row["Employee_ID"], row["Experience(Years)"], row["Ship_ID"], row["SecurityCompany"], ID);
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
				info["ID"] = int(input("Enter the Employee_ID you want to delete: "))
				query = "DELETE FROM Security WHERE Employee_ID = '%d'" %(info["ID"]);
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


def driver(con, cur):
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
				query = 'SELECT * FROM Drivers;'
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
				info["ID"] = int(input("Employee_ID : "))
				info["Exp"] = int(input("Experience (Years) : "))
				info["SID"] = int(input("Ship_ID : "))
				info["LID"] = int(input("Driving License ID : "))
				query = "INSERT INTO Drivers(Employee_ID, `Experience(Years)`, Ship_ID, DrivingLicenseID) VALUES('%d', '%d', '%d', '%d')" %(info["ID"], info["Exp"], info["SID"], info["LID"]);
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
				ID = int(input("Enter Employee_ID to modify: "))
				query = "SELECT * FROM Drivers where Employee_ID = '%d'" %(ID);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Employee_ID: ")
				if info["ID"] != "":
					row["Employee_ID"] = int(info["ID"])
				info["Exp"] = input("Experience (Years): ")
				if info["Exp"] != "":
					row["Experience(Years)"] = int(info["Exp"])
				info["SID"] = input("Ship_ID: ")
				if info["SID"] != "":
					row["Ship_ID"] = int(info["SID"])
				info["LID"] = input("Driving License ID: ")
				if info["LID"] != "":
					row["DrivingLicenseID"] = int(info["LID"])
				query = "UPDATE Drivers SET Employee_ID = '%d', `Experience(Years)` = '%d', Ship_ID = '%d', DrivingLicenseID = '%d' WHERE Employee_ID = '%d'" %(row["Employee_ID"], row["Experience(Years)"], row["Ship_ID"], row["DrivingLicenseID"], ID);
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
				info["ID"] = int(input("Enter the Employee_ID you want to delete: "))
				query = "DELETE FROM Drivers WHERE Employee_ID = '%d'" %(info["ID"]);
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


def otherStaff(con, cur):
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
				query = 'SELECT * FROM OtherStaff;'
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
				info["ID"] = int(input("Employee_ID : "))
				info["Exp"] = int(input("Experience (Years) : "))
				query = "INSERT INTO OtherStaff(Employee_ID, `Experience(Years)`) VALUES('%d', '%d')" %(info["ID"], info["Exp"]);
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
				ID = int(input("Enter Employee_ID to modify: "))
				query = "SELECT * FROM Drivers where Employee_ID = '%d'" %(ID);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Employee_ID: ")
				if info["ID"] != "":
					row["Employee_ID"] = int(info["ID"])
				info["Exp"] = input("Experience (Years): ")
				if info["Exp"] != "":
					row["Experience(Years)"] = int(info["Exp"])
				query = "UPDATE OtherStaff SET Employee_ID = '%d', `Experience(Years)` = '%d' WHERE Employee_ID = '%d'" %(row["Employee_ID"], row["Experience(Years)"], ID);
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
				info["ID"] = int(input("Enter the Employee_ID you want to delete: "))
				query = "DELETE FROM OtherStaff WHERE Employee_ID = '%d'" %(info["ID"]);
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


def employeeDependent(con, cur):
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
				query = 'SELECT * FROM Employee_Dependent;'
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
				info["ID"] = int(input("Employee_ID: "))
				info["Fname"], info["Mname"], info["Lname"] = (input("Name (Fname Minit Lname): ")).split(' ')	
				info["DOB"] = input("DOB (YYYY-MM-DD): ")
				info["Gender"] = input("Gender (Male, Female, Others): ")
				info["DNo"] = int(input("Dependent No. : "))

				query = "INSERT INTO Employee_Dependent(Employee_ID, First_Name, Middle_Name, Last_Name, DOB, Gender, DependentNo) VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%d')" %(info["ID"], info["Fname"], info["Mname"], info["Lname"], info["DOB"], info["Gender"], info["DNo"]);
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
				ID = int(input("Enter Employee_ID to modify: "))
				query = "SELECT * FROM Employee_Dependent where Employee_ID = '%d'" %(ID);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Employee_ID: ")
				if info["ID"] != "":
					row["Employee_ID"] = int(info["ID"])
				info["name"] = input("Name (Fname Minit Lname): ")
				if info["name"] != "":
					row["First_Name"], row["Middle_Name"], row["Last_Name"] = info["name"].split(' ')	
				info["DOB"] = input("DOB (YYYY-MM-DD): ")
				if info["DOB"] != "":
					row["DOB"] = info["DOB"]
				info["Gender"] = input("Gender (Male, Female, Others): ")
				if info["Gender"] != "":
					row["Gender"] = info["Gender"]
				info["DNo"] = input("Dependent No: ")
				if info["DNo"] != "":
					row["DependentNo"] = int(info["DNo"])
				query = "UPDATE Employee_Dependent SET Employee_ID = '%d', First_Name = '%s', Middle_Name = '%s', Last_Name = '%s', DOB = '%s', Gender = '%s', DependentNo = '%d' WHERE Employee_ID = '%d'" %(row["Employee_ID"], row["First_Name"], row["Middle_Name"], row["Last_Name"], row["DOB"], row["Gender"], row["DependentNo"], ID);
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
				info["ID"] = int(input("Enter the Employee_ID you want to delete: "))
				query = "DELETE FROM Employee_Dependent WHERE Employee_ID = '%d'" %(info["ID"]);
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


def passPNo(con, cur):
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
				query = 'SELECT * FROM Passenger_PhoneNumber;'
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
				info["Pno"] = input("Phone Number: ")	
				query = "INSERT INTO Passenger_PhoneNumber(Passenger_ID, PhoneNumber) VALUES('%d', '%s')" %(info["ID"], info["Pno"]);
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
				Pno = input("Enter Phone Number to modify: ")
				query = "SELECT * FROM Passenger_PhoneNumber where PhoneNumber = '%s'" %(Pno);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Passenger_ID: ")
				if info["ID"] != "":
					row["Passenger_ID"] = int(info["ID"])
				info["Pno"] = input("Phone Number: ")
				if info["Pno"] != "":
					row["PhoneNumber"] = info["Pno"]	
				query = "UPDATE Passenger_PhoneNumber SET PhoneNumber = '%s', Passenger_ID = '%d' WHERE PhoneNumber = '%s'" %(row["PhoneNumber"], row["Passenger_ID"], Pno);
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
				info["Pno"] = input("Enter the Phone Number you want to delete: ")
				query = "DELETE FROM Passenger_PhoneNumber WHERE PhoneNumber = '%d'" %(info["Pno"]);
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


def empPNo(con, cur):
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
				query = 'SELECT * FROM Employee_PhoneNumber;'
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
				info["ID"] = int(input("Employee_ID: "))
				info["Pno"] = input("Phone Number: ")	
				query = "INSERT INTO Employee_PhoneNumber(Employee_ID, PhoneNumber) VALUES('%d', '%s')" %(info["ID"], info["Pno"]);
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
				Pno = input("Enter Phone Number to modify: ")
				query = "SELECT * FROM Employee_PhoneNumber where PhoneNumber = '%s'" %(Pno);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Employee_ID: ")
				if info["ID"] != "":
					row["Employee_ID"] = int(info["ID"])
				info["Pno"] = input("Phone Number: ")
				if info["Pno"] != "":
					row["PhoneNumber"] = info["Pno"]	
				query = "UPDATE Employee_PhoneNumber SET PhoneNumber = '%s', Employee_ID = '%d' WHERE PhoneNumber = '%s'" %(row["PhoneNumber"], row["Employee_ID"], Pno);
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
				info["Pno"] = input("Enter the Phone Number you want to delete: ")
				query = "DELETE FROM Employee_PhoneNumber WHERE PhoneNumber = '%d'" %(info["Pno"]);
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


def empDepPNo(con, cur):
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
				query = 'SELECT * FROM EmployeeDependent_PNo;'
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
				info["ID"] = int(input("Employee Dependent Phone No.: "))
				info["Dno"] = int(input("Dependent No.: "))
				info["Pno"] = input("Phone Number: ")	
				query = "INSERT INTO EmployeeDependent_PNo(Employee_ID, PhoneNumber, DependentNo) VALUES('%d', '%s', '%d')" %(info["ID"], info["Pno"], info["Dno"]);
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
				Pno = input("Enter Phone Number to modify: ")
				query = "SELECT * FROM EmployeeDependent_PNo where PhoneNumber = '%s'" %(Pno);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Employee_ID: ")
				if info["ID"] != "":
					row["Employee_ID"] = int(info["ID"])
				info["Dno"] = input("Dependent No.: ")
				if info["Dno"] != "":
					row["DependentNo"] = int(info["Dno"])
				info["Pno"] = input("Phone Number: ")
				if info["Pno"] != "":
					row["PhoneNumber"] = info["Pno"]	
				query = "UPDATE EmployeeDependent_PNo SET PhoneNumber = '%s', Employee_ID = '%d', DependentNo = '%d' WHERE PhoneNumber = '%s'" %(row["PhoneNumber"], row["Employee_ID"], row["DependentNo"], Pno);
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
				info["Pno"] = input("Enter the Phone Number you want to delete: ")
				query = "DELETE FROM EmployeeDependent_PNo WHERE PhoneNumber = '%d'" %(info["Pno"]);
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


def empDepEmail(con, cur):
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
				query = 'SELECT * FROM EmployeeDependent_EmailID;'
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
				info["ID"] = int(input("Employee Dependent Email ID: "))
				info["Dno"] = int(input("Dependent No.: "))
				info["mail"] = input("Email ID: ")	
				query = "INSERT INTO EmployeeDependent_EmailID(Employee_ID, EmailID, DependentNo) VALUES('%d', '%s', '%d')" %(info["ID"], info["mail"], info["Dno"]);
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
				mail = input("Enter Email ID to modify: ")
				query = "SELECT * FROM EmployeeDependent_EmailID where EmailID = '%s'" %(mail);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Employee_ID: ")
				if info["ID"] != "":
					row["Employee_ID"] = int(info["ID"])
				info["Dno"] = input("Dependent No.: ")
				if info["Dno"] != "":
					row["DependentNo"] = int(info["Dno"])
				info["mail"] = input("Email ID: ")
				if info["mail"] != "":
					row["EmailID"] = info["mail"]	
				query = "UPDATE EmployeeDependent_EmailID SET EmailID = '%s', Employee_ID = '%d', DependentNo = '%d' WHERE EmailID = '%s'" %(row["EmailID"], row["Employee_ID"], row["DependentNo"], mail);
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
				info["mail"] = input("Enter the Email ID you want to delete: ")
				query = "DELETE FROM EmployeeDependent_EmailID WHERE EmailID = '%s'" %(info["mail"]);
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


def empEmail(con, cur):
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
				query = 'SELECT * FROM Employee_EmailID;'
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
				info["ID"] = int(input("Employee Email ID: "))
				info["mail"] = input("Email ID: ")	
				query = "INSERT INTO Employee_EmailID(Employee_ID, EmailID) VALUES('%d', '%s')" %(info["ID"], info["mail"]);
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
				mail = input("Enter Email ID to modify: ")
				query = "SELECT * FROM Employee_EmailID where EmailID = '%s'" %(mail);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Employee_ID: ")
				if info["ID"] != "":
					row["Employee_ID"] = int(info["ID"])
				info["mail"] = input("Email ID: ")
				if info["mail"] != "":
					row["EmailID"] = info["mail"]	
				query = "UPDATE Employee_EmailID SET EmailID = '%s', Employee_ID = '%d' WHERE EmailID = '%s'" %(row["EmailID"], row["Employee_ID"], mail);
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
				info["mail"] = input("Enter the Email ID you want to delete: ")
				query = "DELETE FROM Employee_EmailID WHERE EmailID = '%s'" %(info["mail"]);
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


def passEmail(con, cur):
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
				query = 'SELECT * FROM Passenger_EmailID;'
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
				info["ID"] = int(input("Passenger Email ID: "))
				info["mail"] = input("Email ID: ")	
				query = "INSERT INTO Passenger_EmailID(Passenger_ID, EmailID) VALUES('%d', '%s')" %(info["ID"], info["mail"]);
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
				mail = input("Enter Email ID to modify: ")
				query = "SELECT * FROM Passenger_EmailID where EmailID = '%s'" %(mail);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["ID"] = input("Passenger_ID: ")
				if info["ID"] != "":
					row["Passenger_ID"] = int(info["ID"])
				info["mail"] = input("Email ID: ")
				if info["mail"] != "":
					row["EmailID"] = info["mail"]	
				query = "UPDATE Passenger_EmailID SET EmailID = '%s', Passenger_ID = '%d' WHERE EmailID = '%s'" %(row["EmailID"], row["Passenger_ID"], mail);
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
				info["mail"] = input("Enter the Email ID you want to delete: ")
				query = "DELETE FROM Employee_EmailID WHERE EmailID = '%s'" %(info["mail"]);
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


def stateCountry(con, cur):
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
				query = 'SELECT * FROM State_Country;'
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
				info["state"] = input("State: ")
				info["country"] = input("Country: ")	
				query = "INSERT INTO State_Country(State, Country) VALUES('%s', '%s')" %(info["state"], info["country"]);
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
				state = input("Enter State to modify: ")
				query = "SELECT * FROM State_Country where State = '%s'" %(state);
				cur.execute(query)
				row = cur.fetchone()
				print("Enter the entries you want to modify otherwise press 'ENTER'")
				info["state"] = input("State: ")
				if info["state"] != "":
					row["State"] = info["state"]
				info["country"] = input("Country: ")
				if info["country"] != "":
					row["Country"] = info["country"]	
				query = "UPDATE State_Country SET State = '%s', Country = '%s' WHERE State = '%s'" %(row["State"], row["Country"], state);
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
				info["state"] = input("Enter the State you want to delete: ")
				query = "DELETE FROM State_Country WHERE State = '%s'" %(info["state"]);
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
