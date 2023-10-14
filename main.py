import os
import numpy as nd
def main_menu():
    """Displays the menu and reads for key inputs to allow for navigation"""
    response = ""
    while response.upper != "Q":
        os.system("cls")
        print("Welcome to the AQUA (Air Quality Analytics) platform. Please type one of the following and press enter to continue\n \n (R) Reporting \n (I) Intelligence \n (M) Monitoring \n (A) About \n (Q) Quit")
        response = input()
        if response.upper() == "R":        
            reporting_menu()
        elif  response.upper() == "I":
            intelligence_menu()
        elif  response.upper() == "M":
            monitoring_menu()
        elif  response.upper() == "A":
            about()
        elif  response.upper() == "Q":
            quit()



def reporting_menu():
    report = []
    import reporting
    choice = ""
    while ["Q", "1", "2", "3"].count(choice.upper()) == 0:
        os.system("cls")
        print("""Pollution Reporting Module:
        Which Monitoring Station would you like to see the reports for? 
        Please type one of the following and press enter to continue, or enter 'Q' to return to the main menu
    
        (1) Marylebone
        (2) North Kensington
        (3) Harlington""")
        choice = input()
        print("Loading Station Data...")
        if choice == "1":
            station_file = open("data/Pollution-London Marylebone Road.csv", "r")
            station_name = "Marylebone Road"
        elif choice == "2":
            station_file = open("data/Pollution-London N Kensington.csv", "r")
            station_name = "North Kensington"
        elif choice == "3":
            station_file = open("data/Pollution-London Harlington.csv", "r")
            station_name = "Harlington"
    if choice.upper() != "Q":
        station_data = nd.array(station_file.readline().replace("\n", "").split(","))
        for x in range(8760):
            station_data = nd.vstack((station_data, station_file.readline().replace("\n", "").split(",")))
        choice = ""
    while ["Q", "1", "2", "3"].count(choice.upper()) == 0:
        os.system("cls")
        print("You have selected " + station_name + " Monitoring Station.")
        print("""Which pollutant would you like to see the reports for? 
        Please type one of the following and press enter to continue, or enter 'Q' to return to the main menu
    
        (1) Nitric Oxide
        (2) PM10 inhalable particulate matter
        (3) PM2.5 inhalable particulate matter""")
        choice = input()
        if choice == "1":
            pollutant_name = "Nitric Oxide"
            pollutant_code = "no"
        elif choice == "2":
            pollutant_name = "PM10 inhalable particulate matter"
            pollutant_code = "pm10"
        elif choice == "3":
            pollutant_name = "PM2.5 inhalable particulate matter"
            pollutant_code = "pm25"
    if choice.upper() != "Q":
        choice = ""
    while ["Q", "1", "2"].count(choice.upper()) == 0:
        os.system("cls")
        print("You have selected " + station_name + " Monitoring Station, and are checking " + pollutant_name + " levels.")
        print("""WARNING: There are """ + str(reporting.count_missing_data(station_data, station_name, pollutant_code)) + """ missing data points in this set. 
    If unreplaced, these data points will not be counted in average or median calculation.
    How would you like to handle this?
    Please type one of the following and press enter to continue, or enter 'Q' to return to the main menu
    
    (1) Leave these points unreplaced
    (2) Replace them with a custom value""")
        replaced = False
        choice = input()
        if choice == "2":
            while not replaced:
                try:
                    os.system("cls")
                    new_value = float(input("Please enter the numerical value you'd like to replace the empty data points with:\t"))
                    station_data = reporting.fill_missing_data(station_data, new_value, station_name, pollutant_code)
                    replaced = True
                except:
                    print("Please enter a numerical value. Press enter to try again or enter Q to exit to main menu")
                    choice = str(input())
                    if choice.upper() == "Q":
                        break
    if choice.upper() != "Q":
        choice = ""
    while ["Q", "1", "2", "3", "4", "5"].count(choice.upper()) == 0:
        os.system("cls")
        print("You have selected " + station_name + " Monitoring Station, and are checking " + pollutant_name + " levels.")
        if replaced:
            print("You have replaced empty data points with " + str(new_value))
        print("""How would you like to analyse this data? 
        Please type one of the following and press enter to continue, or enter 'Q' to return to the main menu
    
        (1) Daily Averages
        (2) Daily Medians
        (3) Hourly Averages
        (4) Monthly Averages
        (5) Peak Hour for a Given Day""")
        choice = input()
        if choice == "1":           
            print("DAILY AVERAGES:")
            report = reporting.daily_average(station_data, station_name, pollutant_code)
            print("Date\t\t " + pollutant_name + " levels")
        elif choice == "2": 
            print("DAILY MEDIANS:")
            report = reporting.daily_median(station_data, station_name, pollutant_code)
            print("Date\t\t " + pollutant_name + " levels")
        elif choice == "3": 
            print("HOURLY AVERAGES:")
            report = reporting.hourly_average(station_data, station_name, pollutant_code)
            print("Hour\t\t " + pollutant_name + " levels")
        elif choice == "4": 
            print("MONTHLY MEDIAN")
            report = reporting.monthly_average(station_data, station_name, pollutant_code)
            print("Month\t " + pollutant_name + " levels")
        elif choice == "5":
            valid_day = False
            day_list = []
            for i in range (1, 8761, 24):
                day_list.append(station_data[i, 0])
            while choice.upper() != "Q" and not valid_day:
                os.system("cls")
                choice = input("Which day would you like to analyse (Please enter in the format YYYY-MM-DD)\n Dates can be between 2021-01-01 to 2021-12-31 inclusive.\n Alternatively enter Q to return to the main menu.\n")
                if day_list.count(choice) > 0:
                    valid_day = True
            if choice.upper() != "Q":      
                print("PEAK HOUR FOR "+choice+":")
                print(reporting.peak_hour_date(station_data, choice, station_name, pollutant_code))





        if choice.upper() != "Q":
            for i in report:
                print(i + ":\t" + str(report[i]))
            choice = input("Press enter to return to Report Viewer, or enter Q to return to main menu:\t")
        





   

def monitoring_menu():
    """Your documentation goes here"""
    # Your code goes here



def intelligence_menu():
    import intelligence
    choice = ""
    """Your documentation goes here"""
    while choice.upper() != "Q":
        os.system("cls")
        try:
            f = open("./data/map-red-pixels.jpg")
            f.close
        except:
            print("Red pixels (Roads with pavement on both sides) have not been mapped. This is required for all other functions in this module.\nPress enter to map red pixels or enter Q to return to main menu")
            choice = input()
            if choice.upper() != "Q":
                print("Mapping Red Pixels...")
                intelligence.find_red_pixels("./data/map.png")
                input("Process complete")
        os.system("cls")
        print("Red pixels (Roads with pavement on both sides): Mapped")
        if choice.upper() != "Q":
            try:
                f = open("./data/map-cyan-pixels.jpg")
                f.close
                print("Cyan pixels (Roads where there is no information regarding pavement availability):\tMapped")
            except:
                print("Cyan pixels (Roads where there is no information regarding pavement availability):\tNot Mapped")
            print("Mobility Intelligence Module:\nHow would you like to analyse the pavement data?\nPlease type one of the following and press enter to continue, or enter 'Q' to return to the main menu")
            print("""
        (1) Remap Red Pixels
        (2) Map Cyan Pixels
        (3) Detect connected Red Pixel components
        (4) Detect and sort connected Red Pixel components and map the largest 2""")
            choice = input()
            if choice == "1":           
                print("Mapping Red Pixels...")
                intelligence.find_red_pixels("./data/map.png")
                input("Process complete")
            elif choice == "2": 
                print("Mapping Cyan Pixels...")
                intelligence.find_cyan_pixels("./data/map.png")
                input("Process complete")
            elif choice == "3": 
                print("Detecting connected components...")
                intelligence.detect_connected_components("./data/map-red-pixels.jpg")
                input("Process complete")
            elif choice == "4": 
                print("Detecting and sorting connected components...")
                intelligence.detect_connected_components_sorted(intelligence.detect_connected_components("./data/map-red-pixels.jpg"))
                input("Process complete")


def about():
    """Displays course and candidate numbers"""
    os.system("cls")
    print("ECM1400")
    print("255357")
    input("\nPress enter to return to the main menu")

def quit():
    """Exits the program"""
    exit()




if __name__ == '__main__':

    main_menu()