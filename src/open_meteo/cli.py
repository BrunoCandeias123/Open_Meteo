import click
import logging
from .gateway import OpenMeteoGateway
from .normalizer import normalize_response
from .ingestor import write_csv_pandas

logging.basicConfig(level=logging.INFO)


@click.command()
@click.option("--lat", required=True, type=float, multiple=True)
@click.option("--lon", required=True, type=float, multiple=True)
@click.option("--timezone", default='GMT')
@click.option("--hourly", default= "temperature_2m,apparent_temperature,rain,precipitation_probability,weather_code")
@click.option("--out", default="out.csv")
def run(lat, lon, timezone, hourly, out):
    client = OpenMeteoGateway()
    # if user passed comma separated, pass as CSV param:
    resp = client.get_forecast(latitude=lat, longitude=lon, timezone=timezone, hourly=hourly)
    rows = normalize_response(resp)
    write_csv_pandas(rows, out)
    click.echo(f"Wrote {len(rows)} rows to {out}")

if __name__ == "__main__":
    run()