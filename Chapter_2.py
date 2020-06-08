# -----------------------------------------------------------------------------------------
# Create a script to manage the task list.
# It should provide a text user interface with options to list, add, edit and delete tasks.
# The task should be identified by a hash value calculated from its contents.
# -----------------------------------------------------------------------------------------

import sqlite3
import pandas as pd


# function checks if table already exist and
# create new one if don't
def init_table():
    # get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='TASK_LIST' ''')

    # checkout if table already exist
    if c.fetchone()[0] == 1:
        print('Table exists.')

    # creation of table if it doesn't exist yet
    else:
        c.execute('''CREATE TABLE TASK_LIST(
            ID              INTEGER                ,
            NAME            CHAR(50)               ,
            DEAD_LINE_DATE  DATE                   ,
            DESCRIPTION     CHAR(50)               
            );''')


# function print out all commands available in this program
def command_list():
    print("""
            You are in TASK LIST 1.0 application by Szymon Grzebyta
------------------------- COMMAND LIST ----------------------------

To list all tasks                            -  list_all

To list all tasks in given period            - list

To find specific task by name                -  show

To add new task                              -  add

To edit task                                 -  edit

To remove task                               -  remove

To quit                                      -  quit

-------------------------------------------------------------------
""")


# converts user's input into operations on database
def operate(user_input):

    if user_input == 'list_all':
        print(pd.read_sql_query("""
        SELECT *
        FROM TASK_LIST
        """, conn))


    elif user_input == "list":
        # asking user to specify time
        constrain = input("when ? [today / tomorrow / exact date in format YYYY-MM-DD] ")

        if constrain == "today":
            print(pd.read_sql_query("""
            SELECT *
            FROM TASK_LIST
            WHERE DEAD_LINE_DATE LIKE DATE('NOW', 'localtime')
            """, conn))

        elif constrain == "tomorrow":
            print(pd.read_sql_query("""
            SELECT *
            FROM TASK_LIST
            WHERE DEAD_LINE_DATE LIKE DATE('NoW', 'localtime', '+1 day')
            """, conn))

        # exact date
        elif len(constrain) == 10:
            # SQLite needs ' at the begining and end
            constrain = "\'"+constrain+ "\'"
            print(pd.read_sql_query("""
            SELECT *
            FROM TASK_LIST
            WHERE DEAD_LINE_DATE LIKE  """+constrain
            , conn))

        else:
            print("wrong date")


    elif user_input == "show":

        # putting user input into variables
        id = hash(input("name "))

        # find all records in data base which have name1 in it's name
        print(pd.read_sql_query("""
        SELECT * FROM TASK_LIST
        WHERE ID LIKE """ + str(id) , conn))


    elif user_input == "add":

        # putting user input into variables
        name = input("name ")
        dead_line = input("dead line date in format YYYY-MM-DD HH:MM ")
        description = input("description ")

        # put information into database
        # the task is identified by a hash value calculated from its name
        c.execute("""
        INSERT INTO TASK_LIST(ID, NAME, DEAD_LINE_DATE, DESCRIPTION)
        VALUES(?, ?, ?, ?)
        """, [hash(name), name, dead_line, description])


    elif user_input == "edit":

        id = input("hash_id ")
        column_name = input("column NAME / DEAD_LINE_DATE / DESCRIPTION ")
        new_value = input("new value ")

        c.execute("""
        UPDATE TASK_LIST
        SET  ? = ?
        WHERE ID = ? 
        """, [column_name, new_value, id])

    # option to remove record form datebase
    elif user_input == "remove":

        # asking user for id of record to remove
        id = input("hash_id  ")

        c.execute("""
        DELETE FROM TASK_LIST
        WHERE ID = ? 
        """, [id, ])


    else:
        print("invalid input")

    # commit changes on database
    conn.commit()



if __name__ == '__main__':

    # initialization of connection with date base
    conn = sqlite3.connect('mysqlite.db')
    c = conn.cursor()

    # initialization of table in date base
    init_table()

    # printing out all necessary commands
    command_list()

    # looping while user don't type quit to end program
    while True:
        # asking user input
        user_input = input("type comand ")

        # break point
        if user_input == "quit":
            break

        else:
            # function that converts user's input into operations on database
            operate(user_input)
        print("\n")