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
            data['delay'] = round(int(line['delay_sec']) / 60) 
  return data
