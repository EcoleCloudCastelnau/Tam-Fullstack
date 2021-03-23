from tam_fullstack.tools import download_csv, parse_csv
from flask import jsonify

route = '/api/station/<station>'

def view(station):
  csv = download_csv()
  data = []

  for row in parse_csv(csv):
    if row['stop_name'] == station:
      data.append({'route_short_name': row['route_short_name'],
                    'trip_headsign': row['trip_headsign'],
                    'delay_min': round(int(row['delay_sec']) / 60),
                    'is_theorical': row['is_theorical']
                  })
  return jsonify(data)
