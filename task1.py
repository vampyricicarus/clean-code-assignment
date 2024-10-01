class Weather:
    def __init__(self, city):
        self.city = city
        self.data = self.fetch_weather_data(city)

    @staticmethod
    def fetch_weather_data(city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(city, {})

    @staticmethod
    def parse_weather_data(data):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

def get_detailed_forecast(city):
    # Function to provide a detailed weather forecast for a city
    data = Weather.fetch_weather_data(city)
    return Weather.parse_weather_data(data)

def display_weather(city):
    # Function to display the basic weather forecast for a city
    data = Weather.fetch_weather_data(city)
    if not data:
        print(f"Weather data not available for {city}")
    else:
        weather_report = Weather.parse_weather_data(data)
        print(weather_report)

def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = get_detailed_forecast(city)
        else:
            display_weather(city)

if __name__ == "__main__":
    main()