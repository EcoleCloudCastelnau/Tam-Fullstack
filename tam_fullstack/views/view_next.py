from tam_fullstack.tools import download_csv, parse_csv
from flask import jsonify, request

route = '/api/next'

def view():
  csv = download_csv()
  data = {}

  route_short_name = request.args.get('route_short_name')
  station = request.args.get('station')
  direction = request.args.get('direction')

  print(route_short_name, station, direction)

  for line in parse_csv(csv):
    if line['stop_name'] == station:
        if line['trip_headsign'] == direction:
          if line['route_short_name'] == route_short_name:
            data['route_short_name'] = line['route_short_name']
            data['trip_headsign'] = line['trip_headsign']
            data['delay_sec'] = line['delay_sec']
            data['is_theorical'] = line['is_theorical']
  return data
