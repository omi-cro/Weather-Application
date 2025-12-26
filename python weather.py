import requests

API_KEY = "9062dcdff6aae21954570edbf49bea3b"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        print("\nWeather Details")
        print("----------------")
        print(f"City        : {city}")
        print(f"Temperature : {temperature}°C")
        print(f"Condition   : {condition.capitalize()}")
    else:
        print("\n City not found. Please try again.")

def main():
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
