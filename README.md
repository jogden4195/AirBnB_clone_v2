# HBNB

Version 1: This is the console/ command line interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON file.

Version 2: We (Jenn and Bryan) forked this existing codebase to improve on it.
This version will now handle conversion from a JSON file storage system to a database focused storage.
We will implement new and update existing functions so the code is compatible with SQL and also swap between storage formats without losing any data.
Unit tests are also used and TDD is practiced.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

### Authors
Miranda Evans, Kevin Yook, Jennifer Ogden, Bryan Leung



#### Extra Trivia Info
**What is Unit testing and how to implement it in a large project?**  
Testing the functions of the project and core libraries.
This is important for finding bugs and TDD.
Retrofitting testing on an existing project is difficult.
Ideally write tests during or before the coding, after is bad practice.
Tests must be required by all or else no one will use them.
StackOverflow answer: "Start by working testing into your bug fix process- every fixed bug gets a test. This will start to work testing into your existing code over time. New code must always have tests, of course."  

**What is \*args and how to use it?**  
Arguments without a keyword or specified parameter like psudoFunction("Lies") or fake(3).
Read below for difference of args and kwargs.  

**What is \*\*kwargs and how to use it?**  
Keyword arguments so psudoFunction(name="BOB") and fake(id=3) are examples.
The difference from above is args will activate code in an argv[1] to argv[n] type of layout.
Kwargs will assign the correct values to a hash map or a dict.  

**How to handle named arguments in a function?**  
With kwargs as said above.  

**How to create a MySQL database?**  
CREATE DATABASE databaseName;
https://www.wikihow.com/Create-a-Database-in-MySQL  

**How to create a MySQL user and grant it privileges?**  
GRANT ALL PRIVILEGES ON \*.\* TO 'username'@'localhost' IDENTIFIED BY 'password';
https://www.a2hosting.com/kb/developer-corner/mysql/managing-mysql-databases-and-users-from-the-command-line  

**What ORM means?**  
Object Relational Mapping. Used for databases.  

**How to map a Python Class to a MySQL table?**  
Using an ORM, with SQLAlchemy. https://www.sqlalchemy.org/  

**How to handle 2 different storage engines with the same codebase?**  
wut?  

**How to use environment variables?**  
look up how to linux  
