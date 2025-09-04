# Open Meteo CLI

A command-line tool to fetch weather forecasts for multiple locations using the [Open-Meteo](https://open-meteo.com/) API.

## Features

- Query weather data for one or more locations (latitude/longitude pairs)
- Select hourly weather variables (temperature, rain, etc.)
- Output results to a CSV file
- Simple CLI interface

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/BrunoCandeias123/Open_Meteo
   cd Open_Meteo
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the CLI from the project root:

```
python -m src.open_meteo.cli --lat <LAT1> --lon <LON1> [--lat <LAT2> --lon <LON2> ...] [--timezone <TZ>] [--hourly <VARS>] [--out <FILE>]
```

**Example:**

```
python -m src.open_meteo.cli --lat 52.52 --lon 13.41 --lat 48.85 --lon 2.35 --hourly temperature_2m,rain --out forecast.csv
```

This fetches weather data for Berlin and Paris and writes it to `forecast.csv`.

## Options

- `--lat` (float, required, multiple): Latitude(s) of location(s)
- `--lon` (float, required, multiple): Longitude(s) of location(s)
- `--timezone` (string, default: GMT): Timezone for the forecast
- `--hourly` (string, default: temperature_2m,apparent_temperature,rain,precipitation_probability,weather_code): Comma-separated list of hourly variables
- `--out` (string, default: out.csv): Output CSV file

## Project Structure

```
Open_Meteo/
├── src/
│   └── open_meteo/
│       ├── cli.py
│       ├── gateway.py
│       ├── normalizer.py
│       └── ingestor.py
├── requirements.txt
└── README.md
```


## Author

Bruno Candeias