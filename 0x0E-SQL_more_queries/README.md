SQL - More queries 

The project describes and demonstarate the following:
		
   	How to create a new MySQL user
    	How to manage privileges for a user to a database or table
    	What’s a PRIMARY KEY
    	What’s a FOREIGN KEY
    	How to use NOT NULL and UNIQUE constraints
    	How to retrieve datas from multiple tables in one request
    	What are subqueries
    	What are JOIN and UNION

TASKS:
	0. My Privileges
	Script that lists all privileges of the MySQL users user_0d_1 
	and user_0d_2 on your server (in localhost).

	1. Root user 
	Script that creates the MySQL server user user_0d_1.
	with the following conditions:

    	user_0d_1 should have all privileges on your MySQL server
    	The user_0d_1 password should be set to user_0d_1_pwd
    	If the user user_0d_1 already exists, your script should not fail

	2. Read user 
	Script that creates the database hbtn_0d_2 and the user user_0d_2.
	with the following conditions:

    	user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
    	The user_0d_2 password should be set to user_0d_2_pwd
    	If the database hbtn_0d_2 already exists, your script should not fail
    	If the user user_0d_2 already exists, your script should not fail

