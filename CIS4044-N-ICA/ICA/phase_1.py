# Author: <REBECCA AGBOLADE>
# Student ID: <D3077427>

import sqlite3
from unicodedata import name
from datetime import datetime, timedelta

# Phase 1 - Starter
# 
# Note: Display all real/float numbers to 2 decimal places.

'''
Satisfactory
'''

def select_all_countries(connection):
    # Queries the database and selects all the countries 
    # stored in the countries table of the database.
    # The returned results are then printed to the 
    # console. 
    try: 
        
            
        # Define the query
        query = "SELECT * from [countries]"

        # Get a cursor object from the database connection
        # that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        results = cursor.execute(query).fetchall()
        

        # Iterate over the results and display the results.
        for row in results:
            print(f"Country Id: {row['id']} -- Country Name: {row['name']} -- Country Timezone: {row['timezone']}")

    except sqlite3.OperationalError as ex:
        print(ex)

def select_all_cities(connection):
    # Queries the database and selects all the countries 
    # stored in the countries table of the database.
    # The returned results are then printed to the 
    # console. 
    try: 
        
            
        # Define the query
        query = "SELECT * from [cities]"

        # Get a cursor object from the database connection
        # that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        results = cursor.execute(query).fetchall()
        

        # Iterate over the results and display the results.
        for row in results:
            print(f"cities Id: {row['id']} -- cities Name: {row['name']} -- cities Longitude: {row['Longitude']} -- cities Latitude:{row['Latitude']} -- country_id:{row['country_id']}")

    except sqlite3.OperationalError as ex:
        print(ex)
    # TODO: Implement this function
    pass

'''
Good
'''
def average_annual_temperature(connection, city_id, year):
    # Queries the database and selects all the countries 
    # stored in the countries table of the database.
    # The returned results are then printed to the 
    # console. 
    try: 
        #connection.row_factory = sqlite3    
        # Define the query
        query = f"""
        SELECT city_id, AVG(mean_temp) AS avg_temp
                 FROM daily_weather_entries
                  WHERE date LIKE '{year}%'
                        AND city_id = {city_id}
                        """

        # Get a cursor object from the database connection
        # that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        results = cursor.execute(query)
        
        # Iterate over the results and display the results.
        for row in results:
            print(f"Average Annual temperature for city with ID {row['city_id']} is {row['avg_temp']}")
         
            
    except sqlite3.OperationalError as ex:
        print(ex)
    
    # TODO: Implement this function
    pass


def average_seven_day_precipitation(connection, city_id, start_date):
    # TODO: Implement this function
    pass

    try: 
   

        
        query = f"""
        SELECT
        AVG(precipitation) AS average_precipitation		
        FROM
        daily_weather_entries
        WHERE
        city_id = {city_id} and date BETWEEN ? and ?;
        """
        end_date = (datetime.strptime(start_date,"%Y-%m-%d")+ timedelta(days=6)).strftime("%Y-%m-%d")

        print(f"Query Parameter = Average SevenDay Precipitation starting from {start_date} to {end_date} ")
        
        
        # Define the query
        # Get a cursor object from the database connection
        # that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        results = cursor.execute(query, (start_date,end_date)).fetchall()
        

        # Iterate over the results and display the results.
        for row in results:
            print(f"Average Seven day precipitation from {start_date} TO {end_date} is {row['average_precipitation']}")

    except sqlite3.OperationalError as ex:
        print(ex)

'''
Very good
'''
def average_mean_temp_by_city( connection, date_from, date_to,city_id):
    # TODO: Implement this function      
    pass

    try: 
        
        query = f"""
        SELECT

        AVG(mean_temp) AS average_temp	
        FROM
        daily_weather_entries
        WHERE
         city_id ={city_id} AND Date BETWEEN '{date_from}' AND '{date_to}'
        """
        
        
        # Define the query
        # Get a cursor object from the database connection
        # that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        results = cursor.execute(query).fetchall()
        

        # Iterate over the results and display the results.
        for row in results:
            print(f"Average temp by city from {date_from} to {date_to} is {row['average_temp']}")

    except sqlite3.OperationalError as ex:
        print(ex)

def average_annual_precipitation_by_country(connection,year,countries_id):
    # TODO: Implement this function
    pass
    try: 
        
        query = f"""
     SELECT
     countries.name,
     AVG(precipitation) AS average_annual_precipitation
     FROM
     daily_weather_entries
     JOIN
     cities ON daily_weather_entries.city_id = cities.id
     JOIN
    countries ON cities.country_id = countries.id
     WHERE 
     countries.id = {countries_id} and date between '{year}-01-01' and '{year}-12-31'
    GROUP BY
    countries.name;
        """
        
        
        # Define the query
        # Get a cursor object from the database connection
        # that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        results = cursor.execute(query).fetchall()
        

        # Iterate over the results and display the results.
        for row in results:
            print(f"average_annual_precipitation_by_country for {row['name']} {row['average_annual_precipitation']}")

    except sqlite3.OperationalError as ex:
        print(ex) 

'''
Excellent

You have gone beyond the basic requirements for this aspect.

'''

if __name__ == "__main__":
    # Create a SQLite3 connection and call the various functions
    # above, printing the results to the terminal.
   with sqlite3.connect("CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
            connection.row_factory = sqlite3.Row # Use row column names instead of indices
            #select_all_countries(connection)
            print()
           # select_all_cities(connection)
            print()
            average_annual_temperature(connection, "2", "2020")
            print()
            #average_seven_day_precipitation(connection, "3", "2020-07-14")
            print()
            #average_mean_temp_by_city(connection, "2020-07-14", "2021-07-14","4")
            print()
           # average_annual_precipitation_by_country(connection,"2021","2")
            print()
           
          

            
            
            