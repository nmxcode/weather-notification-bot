import os


class WeatherBot:

    def __init__(self, weather_client, api_sender, webhook_url):

        self.weather_client = weather_client
        self.api_sender = api_sender
        self.webhook_url = webhook_url

    def run(self):

        city_name = input("Enter city name: ")

        places = self.weather_client.search_city(city_name)

        for index, place in enumerate(places):
            print(
                index,
                place["name"],
                place.get("country")
            )

        city_index = int(input("Select city number: "))

        if not 0 <= city_index < len(places):
            raise ValueError("Invalid selection!")

        selected_city = places[city_index]

        weather_data = self.weather_client.get_weather(
            selected_city
        )

        print(weather_data)

        echo_response, echo_result, verified = (
            self.api_sender.send_to_postman(weather_data)
        )

        print("Postman Status:", echo_response.status_code)
        print("Data Verified:", verified)

        webhook_response = self.api_sender.send_to_webhook(
            self.webhook_url,
            weather_data
        )

        print("Webhook Status:", webhook_response.status_code)
        print("Weather notification sent successfully!")