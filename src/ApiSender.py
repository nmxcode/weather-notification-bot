from urllib.parse import urlparse


class ApiSender:

    def __init__(self, api_key, timeout=30):

        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def send_post(self, url, data):

        response = self.session.post(
            url,
            json=data,
            headers=self.headers,
            timeout=self.timeout
        )

        response.raise_for_status()

        return response

    def send_to_postman(self, data):

        url = "https://postman-echo.com/post"

        response = self.send_post(url, data)

        result = response.json()

        verified = result.get("json") == data

        return response, result, verified

    def send_to_webhook(self, webhook_url, data):

        parsed_url = urlparse(webhook_url)

        if (
            parsed_url.scheme != "https"
            or parsed_url.hostname != "webhook.site"
            or not parsed_url.path.strip("/")
        ):
            raise ValueError("Invalid Webhook URL!")

        response = self.send_post(
            webhook_url,
            data
        )

        return response