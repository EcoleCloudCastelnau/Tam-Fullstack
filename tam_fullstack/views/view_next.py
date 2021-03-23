from tam_fullstack.tools import download_csv, parse_csv
from flask import jsonify, request

route = '/api/next'

def view():
  csv = download_csv()
  data = {}

  route_short_name = request.args.get('route_short_name')
  stop_name = request.args.get('stop_name')
  trip_headsign = request.args.get('trip_headsign')

  print(route_short_name, stop_name, trip_headsign)

  for row in parse_csv(csv):
    if row['stop_name'] == stop_name:
        if row['trip_headsign'] == trip_headsign:
          if row['route_short_name'] == route_short_name:
            data['delay_min'] = round(int(row['delay_sec']) / 60)
  return data
