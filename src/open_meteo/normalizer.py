def normalize_response(responses_json):
    all_rows = []

    #Be able to treat single or multiple locations as lists to loop over)
    if isinstance(responses_json, dict):
        responses_json = [responses_json]

    for block in responses_json:

        resp_latitude = block.get("latitude", {})
        resp_longitude = block.get("longitude", {})
        resp_timezone = block.get("timezone", {})
        resp_hourly_units_time = block.get("hourly_units", {}).get("time", {})  
        resp_hourly = block.get("hourly", {})
        resp_times = resp_hourly.get("time", [])
        variable_keys = [k for k in resp_hourly.keys() if k != "time"] # make iteration on columns in hourly, besides time.
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
        all_rows.extend(rows)
    return all_rows
