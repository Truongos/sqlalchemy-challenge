# sqlalchemy-challenge

Requirements
Jupyter Notebook Database Connection (10 points)
To receive all points, you must
Use the SQLAlchemy create_engine() function to connect to your SQLite database (1 point)

Use the SQLAlchemy automap_base() function to reflect your tables into classes (3 points)

Save references to the classes named station and measurement (4 points)

Link Python to the database by creating a SQLAlchemy session (1 point)

Close your session at the end of your notebook (1 point)

Precipitation Analysis (16 points)
To receive all points, you must
Create a query that finds the most recent date in the dataset (8/23/2017) (2 points)

Create a query that collects only the date and precipitation for the last year of data without passing the date as a variable (4 points)

Save the query results to a Pandas DataFrame to create date and precipitation columns (2 points)

Sort the DataFrame by date (2 points)

Plot the results by using the DataFrame plot method with date as the x and precipitation as the y variables (4 points)

Use Pandas to print the summary statistics for the precipitation data (2 points)

Station Analysis (16 points)
To receive all points, you must
Design a query that correctly finds the number of stations in the dataset (9) (2 points)

Design a query that correctly lists the stations and observation counts in descending order and finds the most active station (USC00519281) (2 points)

Design a query that correctly finds the min, max, and average temperatures for the most active station (USC00519281) (3 points)

Design a query to get the previous 12 months of temperature observation (TOBS) data that filters by the station that has the greatest number of observations (3 points)

Save the query results to a Pandas DataFrame (2 points)

Correctly plot a histogram with bins=12 for the last year of data using tobs as the column to count. (4 points)

API SQLite Connection & Landing Page (10 points)
To receive all points, your Flask application must
Correctly generate the engine to the correct sqlite file (2 points)

Use automap_base() and reflect the database schema (2 points)

Correctly save references to the tables in the sqlite file (measurement and station) (2 points)

Correctly create and binds the session between the python app and database (2 points)

Display the available routes on the landing page (2 points)

API Static Routes (15 points)
To receive all points, your Flask application must include
A precipitation route that:

Returns json with the date as the key and the value as the precipitation (3 points)

Only returns the jsonified precipitation data for the last year in the database (3 points)

A stations route that:

Returns jsonified data of all of the stations in the database (3 points)
A tobs route that:

Returns jsonified data for the most active station (USC00519281) (3 points)

Only returns the jsonified data for the last year of data (3 points)

API Dynamic Route (15 points)
To receive all points, your Flask application must include
A start route that:

Accepts the start date as a parameter from the URL (2 points)

Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset (4 points)

A start/end route that:

Accepts the start and end dates as parameters from the URL (3 points)

Returns the min, max, and average temperatures calculated from the given start date to the given end date (6 points)

Coding Conventions and Formatting (8 points)
To receive all points, your code must
Place imports at the top of the file, just after any module comments and docstrings, and before module globals and constants. (2 points)

Name functions and variables with lowercase characters, with words separated by underscores. (2 points)

Follow DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code. (2 points)

Use concise logic and creative engineering where possible. (2 points)

Deployment and Submission (6 points)
To receive all points, you must
Submit a link to a GitHub repository that’s cloned to your local machine and contains your files. (2 points)

Use the command line to add your files to the repository. (2 points)

Include appropriate commit messages in your files. (2 points)

Comments (4 points)
To receive all points, your code must
Be well commented with concise, relevant notes that other developers can understand. (4 points)
