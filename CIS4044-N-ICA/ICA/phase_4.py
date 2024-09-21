import sqlite3
import requests

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": 35.6895,
	"longitude":139.6917,
	"start_date": "2020-01-01",
	"end_date": "2022-12-31",
	"hourly": "temperature_2m",
	"daily": ["temperature_2m_max", "temperature_2m_min", "temperature_2m_mean", "precipitation_hours"]
}

data = requests.get(url, params)
data = data.json()	
date = data['daily']['time']
max_temp = data['daily']['temperature_2m_max']
min_temp = data['daily']['temperature_2m_min']
mean_temp = data['daily']['temperature_2m_mean']
precipitation = data['daily']['precipitation_hours']

def insert_daily_weather_entry(conn, date, min_temp, max_temp, mean_temp, precipitation):
	cursor = conn.cursor()
	for date, min_temp, max_temp, mean_temp, precipitation in zip(date, min_temp, max_temp, mean_temp, precipitation):
		query = """ INSERT INTO daily_weather_entries (date, min_temp, max_temp, mean_temp, precipitation, city_id) 
			VALUES (?, ?, ?, ?, ?, ?)
		"""
	
		data = (date, min_temp, max_temp, mean_temp, precipitation, 6)

		cursor.execute(query, data)

		conn.commit()

def insert_country(conn):
	cursor = conn.cursor()
	name = input("enter a country name: ")
	timezone = input("Enter the timezone: ")
	query = f"""
			INSERT INTO countries (name, timezone) VALUES (?, ?)
	"""
	data = (name, timezone)
	cursor.execute(query, data)

	conn.commit()
        
def insert_city(conn):
	cursor = conn.cursor()
	name = input("enter a country name: ")
	countryID = input("Enter country ID: ")	
	query = f"""
			INSERT INTO cities (name, longitude, latitude, country_id) VALUES (?, ?, ?, ?)
	"""
	data = (name, params["longitude"], params["latitude"], countryID)
	cursor.execute(query, data)

	conn.commit()



with sqlite3.connect("CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as conn:
	conn.row_factory = sqlite3.Row 

	#print("1 - Insert into daily_weather_entries table")
	print("1 - Insert countries table")
	#print("1 - Insert into cities table")
	select = input("Select a function to perform: ")
	if select == "1":
		insert_daily_weather_entry(conn, date, min_temp, max_temp, mean_temp, precipitation)
	elif select == "2":
		insert_country(conn)
	elif select == "3":
		insert_city(conn)
