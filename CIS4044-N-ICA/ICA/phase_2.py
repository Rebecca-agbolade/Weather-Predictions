from datetime import date
import os           # https://docs.python.org/3/library/os.html
import matplotlib.pyplot as plt # https://matplotlib.org/stable/index.html
import sqlite3
import matplotlib.pyplot

def plot_7_day_precipitation( connection):
    
    connection.row_factory = sqlite3.Row # Use row column names instead of indices

    cursor = connection.cursor()

    query =  """
      SELECT
      date,
      precipitation
       FROM
       daily_weather_entries
       WHERE
       city_id = 4
       AND date BETWEEN '2022-01-01' AND '2022-01-07'
       ORDER BY
        date;   
    """
         
    results = cursor.execute(query)
             # Process the results
    data = {
            "date": [],
            "precipitation": []
        }
    for row in results:       
        data["date"].append(row['date'])
        data["precipitation"].append(row['precipitation'])
    
    print(data['date'], data['precipitation'])

    fig, ax = plt.subplots()

    ax.set_xlabel("precipitation")
    ax.set_ylabel("date")
    ax.set(title = "7 day precipitation(City)", xlabel = "Precipitation", ylabel = "Date")

       # Slightly rotate the x axis labels
    ax.tick_params(axis = 'x', labelrotation = 30)
 # Plot the bars
    ax.bar(x = data["date"], height = data["precipitation"])


    plt.savefig("7_day_precipitation.jpeg")
    plt.show()


def plot_specified_period_specified_cities( connection):
     
    
    connection.row_factory = sqlite3.Row # Use row column names instead of indices

    cursor = connection.cursor()

    query =  """
      SELECT
    cities.id,
    cities.name,
    AVG(daily_weather_entries.precipitation) AS avg_annual_precipitation
FROM
    cities 
JOIN
    daily_weather_entries  ON cities.id = daily_weather_entries.city_id
GROUP BY
    cities.id, cities.name; 
    """
         
    results = cursor.execute(query)
             # Process the results
    data = {
            "name": [],
            "avg_annual_precipitation": []
        }
    for row in results:       
        data["name"].append(row['name'])
        data["avg_annual_precipitation"].append(row['avg_annual_precipitation'])
    
    print(data['name'], data['avg_annual_precipitation'])

    fig, ax = plt.subplots()

    ax.set_xlabel("name")
    ax.set_ylabel("avg_annual_precipitation")
    ax.set(title = "specified period by specified cities", xlabel = "name", ylabel = "avg_annual_precipitation")

       # Slightly rotate the x axis labels
    ax.tick_params(axis = 'x', labelrotation = 30)
 # Plot the bars
    ax.bar(x = data["name"], height = data["avg_annual_precipitation"])


    plt.savefig("specified_period_by_specified_cities.jpeg")
    plt.show()


def Average_yearly_precipitation_by_country ( connection):
     
    
    connection.row_factory = sqlite3.Row # Use row column names instead of indices

    cursor = connection.cursor()

    query =  """
     SELECT
    countries.id AS country_id,
    countries.name AS country_name,
    AVG(daily_weather_entries.precipitation) AS avg_yearly_precipitation
FROM
    countries
JOIN
    cities ON countries.id = cities.country_id
JOIN
    daily_weather_entries ON cities.id = daily_weather_entries.city_id
WHERE
    daily_weather_entries.date BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY
    countries.id, countries.name;
    """
         
    results = cursor.execute(query)
             # Process the results
    data = {
            "country_name": [],
            "avg_yearly_precipitation": []
        }
    for row in results:       
        data["country_name"].append(row['country_name'])
        data["avg_yearly_precipitation"].append(row['avg_yearly_precipitation'])
    
    print(data['country_name'], data['avg_yearly_precipitation'])

    fig, ax = plt.subplots()

    ax.set_xlabel("country_name")
    ax.set_ylabel("avg_yearly_precipitation")
    ax.set(title = "Average Yearly Precipitation by Country", xlabel = "country_name", ylabel = "avg_yearly_precipitation")

       # Slightly rotate the x axis labels
    ax.tick_params(axis = 'x', labelrotation = 30)
 # Plot the bars
    ax.bar(x = data["country_name"], height = data["avg_yearly_precipitation"])
    plt.savefig("Average_yearly_precipitation_by_country.jpeg")
    plt.show()

 

def Grouped_bar_chart(connection, year):
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    query = f"""
      SELECT
            cities.id AS city_id,
            cities.name AS locality_name,
            daily_weather_entries.min_temp AS min_temperature,
            daily_weather_entries.max_temp AS max_temperature,
            daily_weather_entries.mean_temp AS mean_temperature,
            daily_weather_entries.precipitation AS precipitation
        FROM
            cities
            JOIN countries ON cities.country_id = countries.id
            JOIN daily_weather_entries ON cities.id = daily_weather_entries.city_id
        WHERE            
            date = '2020-03-05' 
    """

    results = cursor.execute(query)

    data = {
        "min_temperature": [],
        "max_temperature": [],
        "mean_temperature": [],
        "precipitation": [],
         "city_id": [],
         "locality_name": [],
    }

    for row in results:
        data["min_temperature"].append(row['min_temperature'])
        data["max_temperature"].append(row['max_temperature'])
        data["mean_temperature"].append(row['mean_temperature'])
        data["precipitation"].append(row['precipitation'])
        data["city_id"].append(row['city_id'])
        data["locality_name"].append(row['locality_name'])


    fig, ax = plt.subplots()

    # Plot the bars for min temperature
    ax.bar(data["locality_name"], data["min_temperature"], label='Min Temperature')

    # Plot the bars for max temperature
    ax.bar(data["locality_name"], data["max_temperature"], label='Max Temperature', bottom=data["min_temperature"])

    # Plot the bars for mean temperature
    ax.bar(data["locality_name"], data["mean_temperature"], label='Mean Temperature',
           bottom=[sum(x) for x in zip(data["min_temperature"], data["max_temperature"])])

    # Plot the bars for precipitation
    ax.bar(data["locality_name"], data["precipitation"], label='Precipitation',
           bottom=[sum(x) for x in zip(data["min_temperature"], data["max_temperature"], data["mean_temperature"])])

    ax.set_xlabel("City")
    ax.set_ylabel("Temperature and Precipitation")
    ax.set_title(f"Grouped Bar Chart for All Cities in Date {year}")

    # Slightly rotate the x-axis labels
    ax.tick_params(axis='x', labelrotation=30)

    # Inserting legend
    ax.legend()
    plt.savefig("Grouped_bar_chart.jpeg")
    plt.show()


def scatter_plot(connection):
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    query = f"""        
        SELECT daily_weather_entries.date,
        countries.id AS country_id,
        countries.name AS country_name,
        AVG(daily_weather_entries.mean_temp) AS avg_yearly_temperature,
        AVG(daily_weather_entries.precipitation) AS avg_yearly_precipitation
        FROM countries JOIN cities ON countries.id = cities.country_id JOIN
        daily_weather_entries ON cities.id = daily_weather_entries.city_id
        WHERE daily_weather_entries.date BETWEEN '2020-01-01' AND '2020-01-31'
        GROUP BY daily_weather_entries.date, countries.name;
    """

    results = cursor.execute(query)

    data = {
            "date": [],
            "avg_yearly_temperature": [],
            "avg_yearly_precipitation": [],
        }

    for row in results:
            data["date"].append(row['date'])
            data["avg_yearly_temperature"].append(row['avg_yearly_temperature'])
            data["avg_yearly_precipitation"].append(row['avg_yearly_precipitation'])

    fig, ax = plt.subplots()

        # Use scatter plot for individual data points
    ax.scatter(data["date"], data["avg_yearly_temperature"], label='avg_yearly_temperature', marker='o')
    ax.scatter(data["date"], data["avg_yearly_precipitation"], label='avg_yearly_precipitation', marker='*')

    ax.set_xlabel("date")
    ax.set_ylabel("Temperature (°C) / Precipitation")
    ax.set_title("Average Yearly Temperature and Precipitation")
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Scatter_Plot.jpeg")
    plt.show()

def multi_line_chart(connection):
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    query = f"""
    SELECT
        date,
        daily_weather_entries.min_temp AS min_temperature,
        daily_weather_entries.max_temp AS max_temperature
    FROM
        cities
        JOIN countries ON cities.country_id = countries.id
        JOIN daily_weather_entries ON cities.id = daily_weather_entries.city_id
    WHERE
        cities.id = 1 AND
        strftime('%Y-%m', date) = '2020-05'
    """
    results =cursor.execute(query)
    data = {
    "date": [],
    "min_temperature": [],
    "max_temperature": [],
    }
    for row in results:
            data["date"].append(row['date'])
            data["min_temperature"].append(row['min_temperature'])
            data["max_temperature"].append(row['max_temperature'])
    fig, ax = plt.subplots()
    # Plot multiline chart for min and max temperatures
    ax.plot(data["date"], data["min_temperature"], label='Min Temperature')
    ax.plot(data["date"], data["max_temperature"], label='Max Temperature' )
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title(f"Daily Min and Max Temperature for City ")
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Multi_Line_Chart.jpeg")



if __name__ == "__main__":
    # Create a SQLite3 connection and call the various functions
    # above, printing the results to the terminal.
   with sqlite3.connect("CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
            connection.row_factory = sqlite3.Row # Use row column names instead of indices
            plot_7_day_precipitation( connection)
            print()
            plot_specified_period_specified_cities( connection)
            print()
            Average_yearly_precipitation_by_country ( connection)
            print()
            Grouped_bar_chart(connection,2021)
            print()
            scatter_plot(connection)
            print()
            multi_line_chart(connection)
            print()

           
           


