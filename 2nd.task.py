import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        print(f"Weather in {city}: {description}, {temp_celsius:.2f} °C")
    else:
        print("Error fetching data. Check city name or API key.")

if __name__ == "__main__":
    api_key = "27e40629b50efd73266061b55ed28763"
    city = input("Enter municipality name: ")
    get_weather(city, api_key)