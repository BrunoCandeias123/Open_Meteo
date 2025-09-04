# import requests
# url = "https://api.open-meteo.com/v1/forecast"
# params = {
# 	"latitude": [52.52, 41.5503, 38.7167, 43.7064, 35.6895],
# 	"longitude": [13.41, -8.42, -9.1333, -79.3986, 139.6917],
# 	"hourly": "temperature_2m,apparent_temperature,rain,precipitation_probability,weather_code",
# 	"timezone": "GMT",
# }
# responses = requests.get(url, params=params)


# responses_json = responses.json()

def normalize_response(responses_json):
    all_rows = []

    #Be able to treat single or multiple locations as lists to loop over)
    if isinstance(responses_json, dict):
        responses_json = [responses_json]

    for block in responses_json:

        #print(block)
        
        resp_latitude = block.get("latitude", {})
        #print("resp_latitude: ",resp_latitude)

        resp_longitude = block.get("longitude", {})
        #print("resp_longitude: ",resp_longitude)

        resp_timezone = block.get("timezone", {})
        #print("resp_timezone: ",resp_timezone)

        resp_hourly_units_time = block.get("hourly_units", {}).get("time", {})  
        #print("resp_hourly_units_time: ", resp_hourly_units_time)

        resp_hourly = block.get("hourly", {})
        #print("resp_hourly: ", resp_hourly)

        resp_times = resp_hourly.get("time", [])
        #print("resp_times: ", resp_times)

        variable_keys = [k for k in resp_hourly.keys() if k != "time"]
        variable_values = [resp_hourly[k] for k in variable_keys]

        rows = [
            {"time": t,
            "latitude" : resp_latitude,
            "longitude" : resp_longitude,
            "hourly_units_time" : resp_hourly_units_time,
            "timezone" : resp_timezone,
            **dict(zip(variable_keys, vals))}
            for t, vals in zip(resp_times, zip(*variable_values))
        ]
        #print(rows)
        all_rows.extend(rows)
    return all_rows
