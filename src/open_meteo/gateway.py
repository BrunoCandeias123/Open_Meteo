import requests

class OpenMeteoGateway:
    url_base = "https://api.open-meteo.com/v1/forecast"

    def __init__(self):
        self.session = requests.Session()

    def get_forecast(
        self,
        latitude: float,
        longitude: float,
        hourly: str,
        timezone: str):
        params = {"latitude": latitude
                  , "longitude": longitude
                  , "timezone":timezone
                  , "hourly": hourly}
        resp = self.session.get(self.url_base, params=params)
        resp.raise_for_status()
        return resp.json()