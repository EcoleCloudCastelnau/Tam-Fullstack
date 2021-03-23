from tam_fullstack.tools import download_csv, parse_csv
from flask import jsonify

route = '/api/stations'

def view():
  csv = download_csv()
  stations = set()

  for row in parse_csv(csv):
    stations.add(row['stop_name'])

  stations = list(stations)
  stations.sort()
  return jsonify(stations)
