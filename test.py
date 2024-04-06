import turtle
from urllib import request
import csv


def get_quake_data(year: int) -> list[dict]:
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "csv",
        "starttime": f"{year}-01-01",
        "endtime": f"{year}-01-02",
        "minlatitude": 21.9267,
        "maxlatitude": 24.9571,
        "minlongitude": 119.8579,
        "maxlongitude": 123.0428,
        "minmagnitude": 4.5, 
    }
    response = request.urlopen(
        url + "?" + "&".join([f"{k}={v}" for k, v in params.items()]))
    reader = csv.reader(response.read().decode().splitlines())
    header = next(reader)
    quake_data = [dict(zip(header, row)) for row in reader]
    return quake_data


def main():
    r = get_quake_data(2021)
    print(r)


if __name__ == "__main__":
    main()
