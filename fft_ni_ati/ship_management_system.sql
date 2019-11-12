drop database if exists SHIP_MANAGEMENT_SYSTEM;
create database SHIP_MANAGEMENT_SYSTEM;
use SHIP_MANAGEMENT_SYSTEM;

drop table if exists State_Country;
create table State_Country(
    State VARCHAR(30) NOT NULL,
    Country VARCHAR(30) NOT NULL,
    PRIMARY KEY (State)
);

drop table if exists Passenger;
create table Passenger(
    Passenger_ID INT UNSIGNED NOT NULL ,
    First_Name VARCHAR(15) NOT NULL,
    Middle_Name VARCHAR(15),
    Last_Name VARCHAR(15) NOT NULL,
    DOB DATE NOT NULL,
    Gender VARCHAR(7) NOT NULL,
    Address VARCHAR(100) NOT NULL,
    PinCode INT UNSIGNED NOT NULL,
    State VARCHAR(30) NOT NULL,
    PRIMARY KEY (Passenger_ID),
    FOREIGN KEY (State) REFERENCES State_Country(State) ON DELETE CASCADE,
    CONSTRAINT aPassenger_ID CHECK(LENGTH(CONVERT(Passenger_ID, CHAR)) = 7),
    CONSTRAINT aPinCode CHECK(LENGTH(CONVERT(PinCode, CHAR)) = 6),
    CONSTRAINT aGender CHECK(Gender = 'Male' OR Gender = 'Female' OR Gender = 'Others')
);

drop table if exists Port;
create table Port(
    Port_ID INT UNSIGNED NOT NULL  ,
    PortName VARCHAR(30) NOT  NULL,
    `PortCapacity(Ships)` INT UNSIGNED NOT NULL,
    PRIMARY KEY (Port_ID),
    CONSTRAINT bPort_ID CHECK(LENGTH(CONVERT(Port_ID, CHAR)) = 5),
    CONSTRAINT `bPortCapacity(Ships)` CHECK(`PortCapacity(Ships)` <= 200)
);

drop table if exists Ship;
create table Ship(
    Ship_ID INT UNSIGNED NOT NULL  ,
    ShipName VARCHAR(30) NOT  NULL,
    ShipType VARCHAR(30) NOT NULL,
    Last_Service_Date DATE NOT NULL,
    SourcePort_ID INT UNSIGNED NOT NULL,
    DestinationPort_ID INT UNSIGNED NOT NULL,
    PRIMARY KEY (Ship_ID),
    FOREIGN KEY (SourcePort_ID) REFERENCES Port(Port_ID) ON DELETE CASCADE,
    FOREIGN KEY (DestinationPort_ID) REFERENCES Port(Port_ID) ON DELETE CASCADE,
    CONSTRAINT cShip_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5),
    CONSTRAINT cSourcePort_ID CHECK(LENGTH(CONVERT(SourcePort_ID, CHAR)) = 5),
    CONSTRAINT cDestinationPort_ID CHECK(LENGTH(CONVERT(DestinationPort_ID, CHAR)) = 5)
);

drop table if exists CargoShip;
create table CargoShip(
    Ship_ID INT UNSIGNED NOT NULL,
    `Capacity(TEU)` FLOAT NOT NULL,
    `Cost(Rupees per TEU)` FLOAT NOT NULL,
    PRIMARY KEY (Ship_ID),
    FOREIGN KEY (Ship_ID) REFERENCES Ship(Ship_ID) ON DELETE CASCADE,
    CONSTRAINT `dCapacity(TEU)` CHECK(`Capacity(TEU)` > 0 AND `Capacity(TEU)` <= 21413),
    CONSTRAINT `dCost(Rupees per TEU)` CHECK(`Cost(Rupees per TEU)` > 0), 
    CONSTRAINT dCargoShip_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5)
);

drop table if exists PassengerShip;
create table PassengerShip(
    Ship_ID INT UNSIGNED NOT NULL,
    `Capacity(Passenger)` INT UNSIGNED NOT NULL,
    Facilities VARCHAR(128),
    PRIMARY KEY (Ship_ID),
    FOREIGN KEY (Ship_ID) REFERENCES Ship(Ship_ID) ON DELETE CASCADE,
    CONSTRAINT `eCapacity(Passenger)` CHECK(`Capacity(Passenger)` <= 500),
    CONSTRAINT eShip_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5)
);

drop table if exists BookingAgent;
create table BookingAgent(
    Agent_ID INT UNSIGNED NOT NULL  ,
    AgentName VARCHAR(45) NOT NULL,
    PRIMARY KEY (Agent_ID),
    CONSTRAINT fAgent_ID CHECK(LENGTH(CONVERT(Agent_ID, CHAR)) = 7)
);

SET sql_mode = '';
drop table if exists Route;
create table Route(
    ArrivalTime TIMESTAMP,
    DepartureTime TIMESTAMP,
    StopNumber INT UNSIGNED NOT NULL,
    Port_ID INT UNSIGNED NOT NULL,
    Ship_ID INT UNSIGNED NOT NULL,
    PRIMARY KEY (DepartureTime, Ship_ID),
    FOREIGN KEY (Ship_Id) REFERENCES Ship(Ship_ID) ON DELETE CASCADE,
    FOREIGN KEY (Port_Id) REFERENCES Port(Port_ID) ON DELETE CASCADE,
    CONSTRAINT gRouteShip_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5),
    CONSTRAINT gPort_ID CHECK(LENGTH(CONVERT(Port_ID, CHAR)) = 5)
);

drop table if exists Ticket;
create table Ticket(
    Ticket_ID INT UNSIGNED NOT NULL,
    Ship_ID INT UNSIGNED NOT NULL,
    SourcePort_ID INT UNSIGNED NOT NULL,
    DestinationPort_ID INT UNSIGNED NOT NULL,
    ArrivalTime TIMESTAMP NOT NULL,
    DepartureTime TIMESTAMP NOT NULL,
    Passenger_ID INT UNSIGNED NOT NULL,
    SeatNo INT UNSIGNED NOT NULL,
    Agent_ID INT UNSIGNED NOT NULL,
    PRIMARY KEY (Ticket_ID),
    FOREIGN KEY (DepartureTime, Ship_Id) REFERENCES Route(DepartureTime, Ship_ID) ON DELETE CASCADE,
    FOREIGN KEY (SourcePort_Id) REFERENCES Port(Port_ID) ON DELETE CASCADE,
    FOREIGN KEY (DestinationPort_Id) REFERENCES Port(Port_ID) ON DELETE CASCADE,
    FOREIGN KEY (Passenger_Id) REFERENCES Passenger(Passenger_ID) ON DELETE CASCADE,
    FOREIGN KEY (Agent_Id) REFERENCES BookingAgent(Agent_ID) ON DELETE CASCADE,
    CONSTRAINT hTicket_ID CHECK(LENGTH(CONVERT(Ticket_ID, CHAR)) = 7),
    CONSTRAINT hTicketShip_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5),
    CONSTRAINT hSourcePort_ID CHECK(LENGTH(CONVERT(SourcePort_ID, CHAR)) = 5),
    CONSTRAINT hDestinationPort_ID CHECK(LENGTH(CONVERT(DestinationPort_ID, CHAR)) = 5),
    CONSTRAINT hPassenger_ID CHECK(LENGTH(CONVERT(Passenger_ID, CHAR)) = 7),
    CONSTRAINT hAgent_ID CHECK(LENGTH(CONVERT(Agent_ID, CHAR)) = 7),
    CONSTRAINT hSeatNo CHECK(SeatNo <= 2000)
);

drop table if exists Department;
create table Department(
    Department_Id INT UNSIGNED NOT NULL  ,
    DepartmentName VARCHAR(30) NOT NULL,
    NumberOfEmployees INT UNSIGNED NOT NULL,
    PRIMARY KEY (Department_ID),
    CONSTRAINT iDepartment_ID CHECK(LENGTH(CONVERT(Department_ID, CHAR)) = 4),
    CONSTRAINT iNumberOfEmployees CHECK(NumberOfEmployees <= 200)
);

drop table if exists Employee;
create table Employee(
    Employee_ID INT UNSIGNED NOT NULL  ,
    First_Name VARCHAR(15) NOT NULL,
    Middle_Name VARCHAR(15),
    Last_Name VARCHAR(15) NOT NULL,
    DOB DATE NOT NULL,
    Gender VARCHAR(7) NOT NULL,
    Salary INT UNSIGNED NOT NULL,
    Department_ID INT UNSIGNED NOT NULL,
    Address VARCHAR(100) NOT NULL,
    PinCode INT UNSIGNED NOT NULL,
    State VARCHAR(30) NOT NULL,
    PRIMARY KEY (Employee_ID),
    FOREIGN KEY (Department_ID) REFERENCES Department(Department_ID) ON DELETE CASCADE,
    FOREIGN KEY (State) REFERENCES State_Country(State) ON DELETE CASCADE,
    CONSTRAINT jEmployee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7),
    CONSTRAINT jDepartment_ID CHECK(LENGTH(CONVERT(Department_ID, CHAR)) = 4),
    CONSTRAINT jPinCode CHECK(LENGTH(CONVERT(PinCode, CHAR)) = 6),
    CONSTRAINT jGender CHECK(Gender = 'Male' OR Gender = 'Female' OR Gender = 'Others')
);

drop table if exists Security;
create table Security(
    Employee_ID INT UNSIGNED NOT NULL,
    `Experience(Years)` INT UNSIGNED NOT NULL,
    Ship_ID INT UNSIGNED NOT NULL,
    SecurityCompany VARCHAR(64) NOT NULL,
    PRIMARY KEY (Employee_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID) ON DELETE CASCADE,
    FOREIGN KEY (Ship_ID) REFERENCES Ship(Ship_ID) ON DELETE CASCADE,
    CONSTRAINT `kExperience(Years)` CHECK(`Experience(Years)` <= 30),
    CONSTRAINT kEmployee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7),
    CONSTRAINT kSecurityShip_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5)
);

drop table if exists Drivers;
create table Drivers(
    Employee_ID INT UNSIGNED NOT NULL,
    `Experience(Years)` INT UNSIGNED NOT NULL,
    Ship_ID INT UNSIGNED NOT NULL,
    DrivingLicenseID INT UNSIGNED NOT NULL,
    PRIMARY KEY (Employee_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID) ON DELETE CASCADE,
    FOREIGN KEY (Ship_ID) REFERENCES Ship(Ship_ID) ON DELETE CASCADE,
    CONSTRAINT `Experience(Years)` CHECK(`Experience(Years)` <= 30),
    CONSTRAINT lEmployee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7),
    CONSTRAINT lDrivingLicenseID CHECK(LENGTH(CONVERT(DrivingLicenseID, CHAR)) = 7),
    CONSTRAINT lDriverShip_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5)
);

drop table if exists OtherStaff;
create table OtherStaff(
    Employee_ID INT UNSIGNED NOT NULL,
    `Experience(Years)` INT UNSIGNED NOT NULL,
    PRIMARY KEY (Employee_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID) ON DELETE CASCADE,
    CONSTRAINT `mExperience(Years)` CHECK(`Experience(Years)` <= 30),
    CONSTRAINT mEmployee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7)
);

drop table if exists Employee_Dependent;
create table Employee_Dependent(
    Employee_ID INT UNSIGNED NOT NULL,
    First_Name VARCHAR(15) NOT NULL,
    Middle_Name VARCHAR(15),
    Last_Name VARCHAR(15) NOT NULL,
    DOB DATE NOT NULL,
    Gender VARCHAR(7) NOT NULL,
    DependentNo INT UNSIGNED NOT NULL,
    PRIMARY KEY (Employee_ID, DependentNo),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID) ON DELETE CASCADE,
    CONSTRAINT nEmployee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7),
    CONSTRAINT nGender CHECK(Gender = 'Male' OR Gender = 'Female' OR Gender = 'Others')
);

drop table if exists Passenger_PhoneNumber;
create table Passenger_PhoneNumber(
    Passenger_ID INT UNSIGNED NOT NULL,
    PhoneNumber VARCHAR(20) NOT NULL,
    PRIMARY KEY (PhoneNumber),
    FOREIGN KEY (Passenger_ID) REFERENCES Passenger(Passenger_ID) ON DELETE CASCADE,
    CONSTRAINT oPhoneNumber CHECK(LENGTH(PhoneNumber) = 10 AND PhoneNumber NOT LIKE '%[^0-9]%'),
    CONSTRAINT oPassenger_ID CHECK(LENGTH(CONVERT(Passenger_ID, CHAR)) = 7)
);

drop table if exists Passenger_EmailID;
create table Passenger_EmailID(
    Passenger_ID INT UNSIGNED NOT NULL,
    EmailID VARCHAR(320) NOT NULL,
    PRIMARY KEY (EmailID),
    FOREIGN KEY (Passenger_ID) REFERENCES Passenger(Passenger_ID) ON DELETE CASCADE,
    CONSTRAINT pEmailID CHECK(EmailID LIKE '%@%.%'),
    CONSTRAINT pPassenger_ID CHECK(LENGTH(CONVERT(Passenger_ID, CHAR)) = 7)
);

drop table if exists Employee_PhoneNumber;
create table Employee_PhoneNumber(
    Employee_ID INT UNSIGNED NOT NULL,
    PhoneNumber VARCHAR(20) NOT NULL,
    PRIMARY KEY (PhoneNumber),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID) ON DELETE CASCADE,
    CONSTRAINT qPhoneNumber CHECK(LENGTH(PhoneNumber) = 10 AND PhoneNumber NOT LIKE '%[^0-9]%'),
    CONSTRAINT qEmployee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7)
);

drop table if exists Employee_EmailID;
create table Employee_EmailID(
    Employee_ID INT UNSIGNED NOT NULL,
    EmailID VARCHAR(320) NOT NULL,
    PRIMARY KEY (EmailID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID) ON DELETE CASCADE,
    CONSTRAINT rEmailID CHECK(EmailID LIKE '%@%.%'),
    CONSTRAINT rEmployee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7)
);

drop table if exists EmployeeDependent_PNo;
create table EmployeeDependent_PNo(
    Employee_ID INT UNSIGNED NOT NULL,
    DependentNo INT UNSIGNED NOT NULL,
    PhoneNumber VARCHAR(20) NOT NULL,
    PRIMARY KEY (PhoneNumber),
    FOREIGN KEY (Employee_ID, DependentNo) REFERENCES Employee_Dependent(Employee_ID, DependentNo) ON DELETE CASCADE,
    CONSTRAINT sPhoneNumber CHECK(LENGTH(PhoneNumber) = 10 AND PhoneNumber NOT LIKE '%[^0-9]%'),
    CONSTRAINT sEmployee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7)
);

drop table if exists EmployeeDependent_EmailID;
create table EmployeeDependent_EmailID(
    Employee_ID INT UNSIGNED NOT NULL,
    DependentNo INT UNSIGNED NOT NULL,
    EmailID VARCHAR(320) NOT NULL,
    PRIMARY KEY (EmailID),
    FOREIGN KEY (Employee_ID, DependentNo) REFERENCES Employee_Dependent(Employee_ID, DependentNo) ON DELETE CASCADE,
    CONSTRAINT tEmailID CHECK(EmailID LIKE '%@%.%'),
    CONSTRAINT tEmployee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7)
);

INSERT INTO State_Country VALUES('Maharashtra', 'India');
INSERT INTO State_Country VALUES('California', 'USA');
INSERT INTO Passenger VALUES(1000000, 'Swastik', '', 'Murawat', '2000-02-21', 'Male', 'Mumbai', '134589', 'Maharashtra');
INSERT INTO Passenger VALUES(1100000, 'Fanish', '', 'Jain', '2000-02-21', 'Male', 'Mumbai', '134589', 'Maharashtra');
INSERT INTO Passenger_PhoneNumber VALUES(1000000, '9234567890');
INSERT INTO Passenger_PhoneNumber VALUES(1100000, '9234567892');
INSERT INTO Passenger_EmailID VALUES(1000000, 'swas@gmail.com');
INSERT INTO Passenger_EmailID VALUES(1100000, 'fan@gmail.com');
INSERT INTO Port VALUES(10000, 'Gandhi Port', 10);
INSERT INTO Port VALUES(11000, 'Nehru Port', 10);
INSERT INTO Port VALUES(12000, 'Indra Port', 10);
INSERT INTO Ship VALUES(10000, 'Rock', 'A-Type', '1900-02-21', 10000, 11000);
INSERT INTO Ship VALUES(11000, 'Stone', 'B-Type', '1901-02-21', 10000, 12000);
INSERT INTO Ship VALUES(12000, 'Stone', 'B-Type', '1901-02-21', 10000, 11000);
INSERT INTO PassengerShip VALUES(10000, 200, 'Good');
INSERT INTO CargoShip VALUES(11000, 100, 200);
INSERT INTO CargoShip VALUES(12000, 50, 100);
INSERT INTO BookingAgent VALUES(1000000, 'Paytn');
INSERT INTO BookingAgent VALUES(1100000, 'PayPl');
INSERT INTO Route VALUES(NULL, '2000-02-21 01-00-00', 1, 10000, 10000);
INSERT INTO Route VALUES('2000-02-21 01-30-00', '2000-02-21 01-35-00', 2, 12000, 10000);
INSERT INTO Route VALUES('2000-02-21 02-00-00', '2000-02-21 02-30-00', 3, 11000, 10000);
INSERT INTO Ticket VALUES(1000000, 10000, 10000, 11000, '2000-02-21 02-00-00', '2000-02-21 01-00-00', 1000000, 1, 1000000);
INSERT INTO Ticket VALUES(1100000, 10000, 10000, 12000, '2000-02-21 01-30-00', '2000-02-21 01-00-00', 1000000, 1, 1100000);
INSERT INTO Department VALUES(1000, 'Driver', 1);
INSERT INTO Department VALUES(1100, 'Security', 1);
INSERT INTO Employee VALUES(1000000, 'Swam', '', 'Kam', '2000-02-21', 'Male', 10000, 1000, 'Mumbai', '134589', 'Maharashtra');
INSERT INTO Employee VALUES(1100000, 'Kan', '', 'Hoe', '2000-02-21', 'Male', 11000, 1100, 'Mumbai', '134589', 'Maharashtra');
INSERT INTO Drivers VALUES(1000000, 5, 10000, 1634231);
INSERT INTO Security VALUES(1100000, 5, 10000, 'A-Company');
INSERT INTO Employee_Dependent VALUES(1000000, 'Lan', 'J', 'Kam', '2000-02-21', 'Male', 1);
INSERT INTO Employee_Dependent VALUES(1100000, 'OM', 'Prakash', 'Yadav', '2000-02-21', 'Male', 1);
INSERT INTO Employee_PhoneNumber VALUES(1000000, '9214567890');
INSERT INTO Employee_PhoneNumber VALUES(1100000, '9254567892');
INSERT INTO Employee_EmailID VALUES(1000000, 'swam@gmail.com');
INSERT INTO Employee_EmailID VALUES(1100000, 'kan@gmail.com');
INSERT INTO EmployeeDependent_PNo VALUES(1000000, 1, '9234537890');
INSERT INTO EmployeeDependent_PNo VALUES(1100000, 1, '9234517892');
INSERT INTO EmployeeDependent_EmailID VALUES(1000000, 1, 'lan@gmail.com');
INSERT INTO EmployeeDependent_EmailID VALUES(1100000, 1, 'om@gmail.com');