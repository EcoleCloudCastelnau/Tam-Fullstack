from tam_fullstack.tools import download_csv, parse_csv
from flask import jsonify

route = '/api/stations'

def view():
  csv = download_csv()
  stations = set()

  for line in parse_csv(csv):
    stations.add(line['stop_name'])

  stations = list(stations)
  stations.sort()
  return jsonify(stations)
