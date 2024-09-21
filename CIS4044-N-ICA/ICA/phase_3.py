# Author: <REBECCA AGBOLADE>
# Student ID: <D3077427>
import sqlite3
import phase_1
import phase_2
import sqlite3

def main():
    with sqlite3.connect("CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
        connection.row_factory = sqlite3.Row
        while True:
           
            print("1: Select all countries",)
            print("2: Select all cities",)
            print("3: Average annual temperature ",)
            print("4: average_seven_day_precipitation",)
            print ("5: average_mean_temp_by_city",)
            print( "6: average_annual_precipitation_by_country",)
            print( "7: plot_specified_period_specified_cities",)
            print( "8: Average yearly precipitation by country",)
            print("9: Grouped bar chart by year",)
            print( "10: Multi line chart",)
            print( "11: Scatter plot chart",)
            print("12: Drop Table From Database",)
            print( "13: Delete Database",)
            print("14: Quit Application")
            
            # Print the menu
            # for menu_item in Menu_Selections:
            #     print(menu_item)
            # Get user choice
            choice = int(input("Enter your choice (1-14): "))          
            if choice == 1:
                phase_1.select_all_countries(connection)
            elif choice == 2:
                phase_1.select_all_cities(connection)
            elif choice == 3:                
                phase_1.average_annual_temperature(connection, "1", "2020")
            elif choice == 4:
                phase_1.average_seven_day_precipitation(connection, "3", "2020-07-14")  
            elif choice == 5: 
                phase_1. average_mean_temp_by_city(connection, "2020-07-14", "2021-07-14","4")
            elif choice == 6:
                phase_1.average_annual_precipitation_by_country(connection,"2021","2")
            elif choice == 7:
                 phase_2.plot_specified_period_specified_cities(connection)
            elif choice ==8:
                phase_2.Average_yearly_precipitation_by_country ( connection)
            elif choice ==9:
                phase_2. Grouped_bar_chart(connection,2020)
            elif choice ==10:
                phase_2.Multi_line_chart(connection) 
            elif choice == 11:
                year = input("Please enter a date? ")
                phase_2.scatter_plot(connection)
            elif choice == 12:
                table_name = input("Enter the table name to drop (Cities, countries, daily_weather_enteries): ")
                drop_query = f"DROP TABLE IF EXISTS {table_name};"
                cursor = connection.cursor()
                cursor.execute(drop_query)
                print(f"Table '{table_name}' dropped successfully.")
            elif choice == 13:
                 with sqlite3.connect("../db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
                    cursor = connection.cursor()
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                    tables = cursor.fetchall()
                    # Drop each table
                    for table in tables:
                        drop_query = f"DROP TABLE IF EXISTS {table[0]};"
                        cursor.execute(drop_query)
                        print(f"Table '{table[0]}' dropped successfully.")                              
            elif choice == 14:
                print("Quitting the application.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 14.")


if __name__ == "__main__":
    main()

 

