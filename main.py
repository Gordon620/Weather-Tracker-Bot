import requests

# Define your API key here
API_KEY = "your_openweathermap_api_key"  # Replace with your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """
    Fetch weather data for a given city.
    :param city_name: Name of the city to fetch weather for.
    :return: Formatted weather data or an error message.
    """
    try:
        # Construct the API request URL
        params = {"q": city_name, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            # Extract weather details
            city = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            weather_description = data["weather"][0]["description"]

            # Format the weather information
            weather_info = (f"Weather in {city}, {country}:\n"
                            f"Temperature: {temp}°C\n"
                            f"Feels like: {feels_like}°C\n"
                            f"Humidity: {humidity}%\n"
                            f"Wind speed: {wind_speed} m/s\n"
                            f"Description: {weather_description.capitalize()}")

            return weather_info
        else:
            # Handle errors such as invalid city names
            return f"Error: {data.get('message', 'Unable to fetch weather data.')}"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """
    Main function to interact with the user and display weather data.
    """
    print("Welcome to the Weather Tracker Bot!")
    print("Type 'exit' to quit.\n")
    while True:
        city_name = input("Enter a city name: ")
        if city_name.lower() == 'exit':
            print("Goodbye!")
            break
        weather_info = get_weather(city_name)
        print(weather_info)
        print("-" * 40)

if __name__ == "__main__":
    main()
