import os
import phonenumbers
from dotenv import load_dotenv
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Load the environment variables from the .env file
load_dotenv()

# Fetch the API key and phone number from the environment variables
API_KEY = os.getenv('API_KEY')
PHONE = os.getenv('PHONE')

# Set the OpenCage Geocode API key
key = API_KEY

# Parse the phone number into the international format
pepnumber = phonenumbers.parse(PHONE)

# Use the geocoder from the 'phonenumbers' library to get the location of the number (city/country)
location = geocoder.description_for_number(pepnumber, "pt")
print(location)

# Parse the number again to get the carrier
service_pro = phonenumbers.parse(PHONE)
# Use 'carrier' to get the carrier for the number
print(carrier.name_for_number(service_pro, "pt"))

# Initialize the OpenCageGeocode client with the API key
geocoder = OpenCageGeocode(key)

# Convert the location to a string and geocode it to get coordinates (latitude and longitude)
query = str(location)
results = geocoder.geocode(query) # Send the location as a query to the OpenCage API.
# print(results) # Print the full API result (disabled).

# Extract the latitude and longitude from the results
lat = results[0]["geometry"]["lat"] # Get the latitude of the first result.
lng = results[0]["geometry"]["lng"] # Get the longitude of the first result.

# Displays latitude and longitude in the console
print(lat, lng)

# Creates a map centered on the obtained coordinates
myMap = folium.Map(location=[lat, lng], zoom_start=9) # Creates a map with the initial zoom defined.
# Adds a marker to the map with the coordinates and location
folium.Marker([lat, lng], popup=location).add_to(myMap)

# Saves the generated map as an HTML file
myMap.save("mylocation.html")