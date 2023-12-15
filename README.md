# csv_to_mysql
Python script that will import a csv file with hedders into a database. 

This script is intended to be used in two parts. First, a command is run that imports a csv file into a newly created database. The field names are taken from the headers in the csv and can be modified by the user before creating the database. The user will identify a field of the csv as a primary key. Second, subsequent csv's can then be imported into the same table. Each subsequent import will ignore primary keys of the csv's that already exist, ensuring no duplicate rows.

To use this repository on most linux machines first create a virtual environment

```bash
./python -m venv ./venv
```
