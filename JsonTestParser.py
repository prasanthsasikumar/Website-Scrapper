import json

# Sample JSON data
json_data = '''
{
    "Vehicle Comments": "Comments, *** Puhinui *** Flood Event 23L ***",
    "Vehicle Location": "Item Location, Auckland, North Island",
    "Vehicle Info": "Info, Registration, NUU307, VIN, 7AT08G7HX21303427, No of Keys, 1, Seller Type, Insurer",   
    "Vehicle Details": "Details, Build Year, 2011, Compliance, 11/2021, Make, Honda, Body Type, 4, D, Station Wagon, Model, CRV, Body Colour, Black, Variant, Doors, 4, Seats, 5, Transmission, Automatic, Engine, 2.35L, Drive Type, Front Wheel Drive, Fuel Type, Petrol",
    "Vehicle Damage": "Damage Description, Water Damage, Selling De-Registered"
}
'''
json_data2 = '''
{
    "Vehicle Comments": "Comments, *** Puhinui *** Structural Damage ***",
    "Vehicle Location": "Item Location, Auckland, North Island",
    "Vehicle Info": "Info, Registration, LKK613, VIN, JSAAZC83S00203011, No of Keys, 1, Seller Type, Insurer",   
    "Vehicle Details": "Details, Build Year, 2018, Make, Suzuki, Body Type, 5, D, Hatch, Model, Swift, Body Colour, Silver, Variant, GLC 1.2P/CVT, Doors, 5, Seats, 5, Odometer, 69,654 KM Showing, Transmission, CVT, Engine, 1.24L, Fuel Type, Petrol",
    "Vehicle Damage": "Damage Description, Rear Damage, Right Front Damage, Impact Heavy - Rear, Impact Medium - Front, Impact Light - Right Side, Selling De-Registered"
}
'''

# Parse the JSON data
data = json.loads(json_data)

# Access specific values
comments = data['Vehicle Comments']
location = data['Vehicle Location']
info = data['Vehicle Info']
details = data['Vehicle Details']
#In a coma seperated value string, find the position of the word "Odometer" and return the value after it. Also if odometer is not found, return "N/A"
#odometer = details[details.find("Odometer")+len("Odometer")+1:details.find(",",details.find("Odometer"))] if details.find("Odometer") != -1 else "N/A"


odometer = details[details.find("Odometer")+len("Odometer, "):details.find(" KM Showing")] if details.find("Odometer") != -1 else "N/A"
transmission = details[details.find("Transmission")+len("Transmission, "):details.find(",", details.find("Transmission") + len("Transmission, "))].strip() if details.find("Transmission") != -1 else "N/A"
make = details[details.find("Make") + len("Make, "):details.find(",", details.find("Make") + len("Make, "))].strip() if details.find("Make") != -1 else "N/A"
model = details[details.find("Model") + len("Model, "):details.find(",", details.find("Model") + len("Model, "))].strip() if details.find("Model") != -1 else "N/A"
seats = details[details.find("Seats") + len("Seats, "):details.find(",", details.find("Seats") + len("Seats, "))].strip() if details.find("Seats") != -1 else "N/A"
fuel_type = details[details.find("Fuel Type") + len("Fuel Type, "):].strip() if details.find("Fuel Type") != -1 else "N/A"



#Get the value of Number of Keys from Vehicle Info
keys = info[info.find("No of Keys")+len("No of Keys, "):info.find(",",info.find("No of Keys")+ len("No of Keys, "))].strip() if info.find("No of Keys") != -1 else "N/A"
damage = data['Vehicle Damage']
#remove the value before the first comma
damage = damage[damage.find(",")+1:]

#if comments contains "Selling Registered", then the vehicle is registered
registered = "Yes" if comments.find("Selling Registered") != -1 else "No"

print("Odometer:", odometer)
print("Transmission:", transmission)
print("Make:", make)
print("Model:", model)
print("Seats:", seats)
print("Fuel Type:", fuel_type)
print("Keys:", keys)
print("Damage:", damage)