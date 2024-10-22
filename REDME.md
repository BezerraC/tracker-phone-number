# Tracker Phone Number

The **Tracker Phone Number** project is a simple Python application that allows you to track the approximate location of a phone number, display the number's carrier, and generate an interactive map with the location using the OpenCage API.

## Features

- Analyzes a phone number to obtain:
- Location (country or city).
- Associated phone carrier.
- Geocodes the location into geographic coordinates (latitude and longitude) using the OpenCage API.
- Generates an interactive HTML map with a marker at the tracked location.

## Technologies Used

- **Python**: Main language of the project.
- **Phonenumbers**: Library for analyzing and processing phone numbers.
- **OpenCage API**: Geocoding service for converting addresses into geographic coordinates.
- **Folium**: Library for creating interactive maps.
- **dotenv**: Library to load environment variables from a `.env` file.

## Requirements

- Python 3.x
- [OpenCage Geocoder](https://opencagedata.com/) account to get the API key.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/BezerraC/tracker-phone-number.git
cd tracker-phone-number
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root of the project and add the following variables:

```plaintext
API_KEY=YOUR_OPENCAGE_API_KEY
PHONE=YOUR_PHONE_NUMBER
```

Replace `YOUR_OPENCAGE_API_KEY` with your OpenCage API key and `YOUR_PHONE_NUMBER` with the phone number you want to track (in international format).

4. Run the script:

```bash
python main.py
```

## How It Works

1. The script loads the phone number and API key from the `.env` file.
2. The phone number is parsed to extract the location (city or country) and the carrier.
3. The location is converted to geographic coordinates using the OpenCage API.
4. An interactive map is generated with the found location, and saved as `mylocation.html`.

## Usage Example

When running the script with a valid phone number, the terminal will display something like this:

```bash
São Paulo
Vivo
-23.550520 -46.633308