from django.shortcuts import render
import urllib.request
import json
from urllib.parse import quote

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city', '').strip()

        if city == '':
            data = {"error": "City name cannot be empty."}
            return render(request, "main/index.html", data)

        # URL encode the city name to handle special characters
        city_encoded = quote(city)

        # Construct the URL with the encoded city name
        api_key = "a632cb03f884be030297204a54d1a949"  # Replace with your API key if needed
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_encoded}&appid={api_key}'

        try:
            # Get JSON data from API
            with urllib.request.urlopen(url) as response:
                source = response.read()

            # Parse JSON data
            list_of_data = json.loads(source)

            # Handle API errors
            if list_of_data.get("cod") != "200":
                data = {"error": list_of_data.get("message", "Failed to fetch weather data.")}
            else:
                # Extract data safely
                data = {
                    "country_code": str(list_of_data.get('city', {}).get('country', 'N/A')),
                    "city_name": str(list_of_data.get('city', {}).get('name', 'N/A')),
                    "coordinate": "{} {}".format(
                        str(list_of_data.get('city', {}).get('coord', {}).get('lon', 'N/A')),
                        str(list_of_data.get('city', {}).get('coord', {}).get('lat', 'N/A'))
                    ),
                    "temp": "{} K".format(str(list_of_data.get('list', [{}])[0].get('main', {}).get('temp', 'N/A'))),
                    "pressure": str(list_of_data.get('list', [{}])[0].get('main', {}).get('pressure', 'N/A')),
                    "humidity": str(list_of_data.get('list', [{}])[0].get('main', {}).get('humidity', 'N/A')),
                }
        except Exception as e:
            data = {"error": f"Error fetching data: {str(e)}"}

        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
