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
    Passenger_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
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
    CONSTRAINT Passenger_ID CHECK(LENGTH(CONVERT(Passenger_ID, CHAR)) = 7),
    CONSTRAINT PinCode CHECK(LENGTH(CONVERT(PinCode, CHAR)) = 6),
    CONSTRAINT Gender CHECK(Gender = 'Male' OR Gender = 'Female' OR Gender = 'Others')
);

drop table if exists Port;
create table Port(
    Port_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    PortName VARCHAR(30) NOT  NULL,
    `PortCapacity(Ships)` INT UNSIGNED NOT NULL,
    PRIMARY KEY (Port_ID),
    CONSTRAINT Port_ID CHECK(LENGTH(CONVERT(Port_ID, CHAR)) = 5),
    CONSTRAINT `PortCapacity(Ships)` CHECK(`PortCapacity(Ships)` <= 200)
);

drop table if exists Ship;
create table Ship(
    Ship_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ShipName VARCHAR(30) NOT  NULL,
    ShipType VARCHAR(30) NOT NULL,
    Last_Service_Date DATE NOT NULL,
    SourcePort_ID INT UNSIGNED NOT NULL,
    DestinationPort_ID INT UNSIGNED NOT NULL,
    PRIMARY KEY (Ship_ID),
    FOREIGN KEY (SourcePort_ID) REFERENCES Port(Port_ID) ON DELETE CASCADE,
    FOREIGN KEY (DestinationPort_ID) REFERENCES Port(Port_ID) ON DELETE CASCADE,
    CONSTRAINT Ship_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5),
    CONSTRAINT SourcePort_ID CHECK(LENGTH(CONVERT(SourcePort_ID, CHAR)) = 5),
    CONSTRAINT DestinationPort_ID CHECK(LENGTH(CONVERT(DestinationPort_ID, CHAR)) = 5)
);

drop table if exists CargoShip;
create table CargoShip(
    Ship_ID INT UNSIGNED NOT NULL,
    `Capacity(TEU)` FLOAT NOT NULL,
    `Cost(Rupees per TEU)` FLOAT NOT NULL,
    PRIMARY KEY (Ship_ID),
    FOREIGN KEY (Ship_ID) REFERENCES Ship(Ship_ID) ON DELETE CASCADE,
    CONSTRAINT `Capacity(TEU)` CHECK(`Capacity(TEU)` > 0 AND `Capacity(TEU)` <= 21413),
    CONSTRAINT `Cost(Rupees per TEU)` CHECK(`Cost(Rupees per TEU)` > 0), 
    CONSTRAINT Ship_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5)
);

drop table if exists PassengerShip;
create table PassengerShip(
    Ship_ID INT UNSIGNED NOT NULL,
    `Capacity(TEU)` FLOAT NOT NULL,
    Facilities VARCHAR(128),
    PRIMARY KEY (Ship_ID),
    FOREIGN KEY (Ship_ID) REFERENCES Ship(Ship_ID) ON DELETE CASCADE,
    CONSTRAINT `Capacity(TEU)` CHECK(`Capacity(TEU)` > 0 AND `Capacity(TEU)` <= 21413),
    CONSTRAINT Ship_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5)
);

drop table if exists BookingAgent;
create table BookingAgent(
    Agent_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    AgentName VARCHAR(45) NOT NULL,
    PRIMARY KEY (Agent_ID),
    CONSTRAINT Agent_ID CHECK(LENGTH(CONVERT(Agent_ID, CHAR)) = 7)
);

SET sql_mode = '';
drop table if exists Route;
create table Route(
    ArrivalTime TIMESTAMP NOT NULL,
    DepartureTime TIMESTAMP NOT NULL,
    StopNumber INT UNSIGNED NOT NULL,
    Port_ID INT UNSIGNED NOT NULL,
    Ship_ID INT UNSIGNED NOT NULL,
    PRIMARY KEY (DepartureTime, Ship_ID),
    FOREIGN KEY (Ship_Id) REFERENCES Ship(Ship_ID) ON DELETE CASCADE,
    FOREIGN KEY (Port_Id) REFERENCES Port(Port_ID) ON DELETE CASCADE,
    CONSTRAINT Ship_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5),
    CONSTRAINT Port_ID CHECK(LENGTH(CONVERT(Port_ID, CHAR)) = 5)
);

drop table if exists Ticket;
create table Ticket(
    Ticket_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    Ship_ID INT UNSIGNED NOT NULL,
    Port_ID INT UNSIGNED NOT NULL,
    DepartureTime TIMESTAMP NOT NULL,
    Passenger_ID INT UNSIGNED NOT NULL,
    SeatNo INT UNSIGNED NOT NULL,
    Agent_ID INT UNSIGNED NOT NULL,
    PRIMARY KEY (Ticket_ID),
    FOREIGN KEY (DepartureTime, Ship_Id) REFERENCES Route(DepartureTime, Ship_ID) ON DELETE CASCADE,
    FOREIGN KEY (Port_Id) REFERENCES Port(Port_ID) ON DELETE CASCADE,
    FOREIGN KEY (Passenger_Id) REFERENCES Passenger(Passenger_ID) ON DELETE CASCADE,
    FOREIGN KEY (Agent_Id) REFERENCES BookingAgent(Agent_ID) ON DELETE CASCADE,
    CONSTRAINT Ticket_ID CHECK(LENGTH(CONVERT(Ticket_ID, CHAR)) = 7),
    CONSTRAINT Ship_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5),
    CONSTRAINT Port_ID CHECK(LENGTH(CONVERT(Port_ID, CHAR)) = 5),
    CONSTRAINT Passenger_ID CHECK(LENGTH(CONVERT(Passenger_ID, CHAR)) = 7),
    CONSTRAINT Agent_ID CHECK(LENGTH(CONVERT(Agent_ID, CHAR)) = 7),
    CONSTRAINT SeatNo CHECK(SeatNo <= 2000)
);

drop table if exists Department;
create table Department(
    Department_Id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    DepartmentName VARCHAR(30) NOT NULL,
    NumberOfEmployees INT UNSIGNED NOT NULL,
    PRIMARY KEY (Department_ID),
    CONSTRAINT Department_ID CHECK(LENGTH(CONVERT(Department_ID, CHAR)) = 4),
    CONSTRAINT NumberOfEmployees CHECK(NumberOfEmployees <= 200)
);

drop table if exists Employee;
create table Employee(
    Employee_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
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
    CONSTRAINT Employee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7),
    CONSTRAINT Department_ID CHECK(LENGTH(CONVERT(Department_ID, CHAR)) = 4),
    CONSTRAINT PinCode CHECK(LENGTH(CONVERT(PinCode, CHAR)) = 6),
    CONSTRAINT Gender CHECK(Gender = 'Male' OR Gender = 'Female' OR Gender = 'Others')
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
    CONSTRAINT `Experience(Years)` CHECK(`Experience(Years)` <= 30),
    CONSTRAINT Employee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7),
    CONSTRAINT Ship_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5)
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
    CONSTRAINT Employee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7),
    CONSTRAINT DrivingLicenseID CHECK(LENGTH(CONVERT(DrivingLicenseID, CHAR)) = 7),
    CONSTRAINT Ship_ID CHECK(LENGTH(CONVERT(Ship_ID, CHAR)) = 5)
);

drop table if exists OtherStaff;
create table OtherStaff(
    Employee_ID INT UNSIGNED NOT NULL,
    `Experience(Years)` INT UNSIGNED NOT NULL,
    PRIMARY KEY (Employee_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID) ON DELETE CASCADE,
    CONSTRAINT `Experience(Years)` CHECK(`Experience(Years)` <= 30),
    CONSTRAINT Employee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7)
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
    CONSTRAINT Employee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7),
    CONSTRAINT Gender CHECK(Gender = 'Male' OR Gender = 'Female' OR Gender = 'Others')
);

drop table if exists Passenger_PhoneNumber;
create table Passenger_PhoneNumber(
    Passenger_ID INT UNSIGNED NOT NULL,
    PhoneNumber VARCHAR(20) NOT NULL,
    PRIMARY KEY (PhoneNumber),
    FOREIGN KEY (Passenger_ID) REFERENCES Passenger(Passenger_ID) ON DELETE CASCADE,
    CONSTRAINT PhoneNumber CHECK(PhoneNumber NOT LIKE '%[^0-9]%'),
    CONSTRAINT Passenger_ID CHECK(LENGTH(CONVERT(Passenger_ID, CHAR)) = 7)
);

drop table if exists Passenger_EmailID;
create table Passenger_EmailID(
    Passenger_ID INT UNSIGNED NOT NULL,
    EmailID VARCHAR(320) NOT NULL,
    PRIMARY KEY (EmailID),
    FOREIGN KEY (Passenger_ID) REFERENCES Passenger(Passenger_ID) ON DELETE CASCADE,
    CONSTRAINT Passenger_ID CHECK(LENGTH(CONVERT(Passenger_ID, CHAR)) = 7)
);

drop table if exists Employee_PhoneNumber;
create table Employee_PhoneNumber(
    Employee_ID INT UNSIGNED NOT NULL,
    PhoneNumber VARCHAR(20) NOT NULL,
    PRIMARY KEY (PhoneNumber),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID) ON DELETE CASCADE,
    CONSTRAINT PhoneNumber CHECK(PhoneNumber NOT LIKE '%[^0-9]%'),
    CONSTRAINT Employee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7)
);

drop table if exists Employee_EmailID;
create table Employee_EmailID(
    Employee_ID INT UNSIGNED NOT NULL,
    EmailID VARCHAR(320) NOT NULL,
    PRIMARY KEY (EmailID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID) ON DELETE CASCADE,
    CONSTRAINT Employee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7)
);

drop table if exists EmployeeDependent_PNo;
create table EmployeeDependent_PNo(
    Employee_ID INT UNSIGNED NOT NULL,
    DependentNo INT UNSIGNED NOT NULL,
    PhoneNumber VARCHAR(20) NOT NULL,
    PRIMARY KEY (PhoneNumber),
    FOREIGN KEY (Employee_ID, DependentNo) REFERENCES Employee_Dependent(Employee_ID, DependentNo) ON DELETE CASCADE,
    CONSTRAINT PhoneNumber CHECK(PhoneNumber NOT LIKE '%[^0-9]%'),
    CONSTRAINT Employee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7)
);

drop table if exists EmployeeDependent_EmailID;
create table EmployeeDependent_EmailID(
    Employee_ID INT UNSIGNED NOT NULL,
    DependentNo INT UNSIGNED NOT NULL,
    EmailID VARCHAR(320) NOT NULL,
    PRIMARY KEY (EmailID),
    FOREIGN KEY (Employee_ID, DependentNo) REFERENCES Employee_Dependent(Employee_ID, DependentNo) ON DELETE CASCADE,
    CONSTRAINT Employee_ID CHECK(LENGTH(CONVERT(Employee_ID, CHAR)) = 7)
);
