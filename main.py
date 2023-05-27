from calendar import c
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from ScrapeVehiclePage import scrape_vehicle_page
from CSVSaver import CarDataWriter
from PageLengthFinder import count_number_of_pages
import json
import datetime

# Get today's date
today = datetime.date.today()
# Create the filename with today's date
filename = f"car_data_{today}.csv"
# Create an instance of CarDataWriter with the filename
writer = CarDataWriter(filename)
writer.initialize()

url = "https://manheim.co.nz/damaged-vehicles/search?PageNumber=1&RecordsPerPage={}&searchType=Z&page={}"

numberOfEntries = 120  # Specify the value of N here
current_page = 1 # Specify the value of page here

# Format the URL with the values of N and page
formatted_url = url.format(numberOfEntries, current_page)

number_of_pages = count_number_of_pages(formatted_url)

while current_page <= number_of_pages:
    
    # Send a GET request to the formatted_url
    response = requests.get(formatted_url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the section with class "vehicle-list"
    vehicle_list_section = soup.find("section", class_="vehicle-list")

    # Find all the <li> elements with class "vehicle-item"
    list_items = vehicle_list_section.find_all("li", class_="vehicle-item")

    def return_JSON_values(json_data, parameter):
        data = json.loads(json_data)
        details = data['Vehicle Details']
        info = data['Vehicle Info']
        damage = data['Vehicle Damage']
        comments = data['Vehicle Comments']

        if parameter == "Odometer":
            odometer = details[details.find("Odometer")+len("Odometer, "):details.find(" KM Showing")] if details.find("Odometer") != -1 else "N/A"
            return odometer
        
        elif parameter == "Transmission":
            transmission = details[details.find("Transmission")+len("Transmission, "):details.find(" Engine")] if details.find("Transmission") != -1 else "N/A"
            return transmission
        
        elif parameter == "Make":
            make = details[details.find("Make") + len("Make, "):details.find(",", details.find("Make") + len("Make, "))].strip() if details.find("Make") != -1 else "N/A"
            return make
        
        elif parameter == "Model":
            model = details[details.find("Model") + len("Model, "):details.find(",", details.find("Model") + len("Model, "))].strip() if details.find("Model") != -1 else "N/A"
            return model
        
        elif parameter == "Seats":
            seats = details[details.find("Seats") + len("Seats, "):details.find(",", details.find("Seats") + len("Seats, "))].strip() if details.find("Seats") != -1 else "N/A"
            return seats
        elif parameter == "Fuel Type":
            fuel_type = details[details.find("Fuel Type") + len("Fuel Type, "):].strip() if details.find("Fuel Type") != -1 else "N/A"
            return fuel_type
        
        elif parameter == "No of Keys":
            keys = info[info.find("No of Keys")+len("No of Keys, "):info.find(",",info.find("No of Keys")+ len("No of Keys, "))].strip() if info.find("No of Keys") != -1 else "N/A"
            return keys
        
        elif parameter == "Damage Description":
            damage = damage[damage.find(",")+1:]
            return damage   
        
        elif parameter == "Registration Status":
            registered = "Yes" if comments.find("Selling Registered") != -1 else "No"
            return registered
        
        else:
            return "N/A"

    try:
        current_entry = 1
        # Iterate over each <li> element
        for item in list_items:
            # Find the value of class "vehicle"
            vehicle = item.find(class_="vehicle").get_text(strip=True)

            # Find the header with class "card-header"
            header = item.find(class_="card-header")
            
            # Find the <a> tag within the header
            a_tag = header.find("a")
            href = urljoin(url, a_tag["href"]) if a_tag and "href" in a_tag.attrs else "N/A"
            
            # Find the span with the corresponding ID
            span_id = item.find("span", id=lambda value: value and value.startswith("stprice-"))
            price = span_id.get_text(strip=True) if span_id else "N/A"

            # Call the scrape_vehicle_page() function from ScrapeVehiclePage.py
            json_data = scrape_vehicle_page(href)
            
            # Display the results
            # print("Vehicle:", vehicle)
            # print("Href:", href)
            # print("Price:", price)
            # print("JSON Data:")
            # print(json_data)
            # print("-------------------------")
            car_data = {
                'Manufacturer': return_JSON_values(json_data, "Make"),
                'Model': return_JSON_values(json_data, "Model"),
                'Registration Status': return_JSON_values(json_data, "Registration Status"),
                'Price': price,
                'Mileage': return_JSON_values(json_data, "Odometer"),
                'Keys': return_JSON_values(json_data, "No of Keys"),
                'Damage description': return_JSON_values(json_data, "Damage Description"),
                'Transmission': return_JSON_values(json_data, "Transmission"),
                'Seats': return_JSON_values(json_data, "Seats"),
                'Fuel Type': return_JSON_values(json_data, "Fuel Type"),
                'Link': href,
            }
            # Get the values and convert them to strings, replacing commas with colons
            values = [str(value).replace(',', ':') for key, value in car_data.items() if key != 'Damage description']
            # Join the values with commas
            csv_line = ', '.join(values)
            print(csv_line)

            writer.save_entry(car_data, ((current_page-1)*numberOfEntries)+current_entry)
            current_entry += 1

    except Exception as exception:
        print("An error occurred. Program crashed." + exception)
        writer.wrap_up()          

    #end of while loop
    current_page += 1
    formatted_url = url.format(numberOfEntries, current_page)
    print("Page {} of {} completed".format(current_page, number_of_pages))


# Wrap up the CSV file writing process
writer.wrap_up()
print("Program completed successfully.")


