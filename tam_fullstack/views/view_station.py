from tam_fullstack.tools import download_csv, parse_csv
from flask import jsonify

route = '/api/station/<station>'

def view(station):
  csv = download_csv()
  data = []

  for line in parse_csv(csv):
    if line['stop_name'] == station:
      data.append({'route_short_name': line['route_short_name'],
                    'trip_headsign': line['trip_headsign'],
                    'delay_sec': round(int(line['delay_sec']) / 60),
                    'is_theorical': line['is_theorical']
                  })
  return jsonify(data)
