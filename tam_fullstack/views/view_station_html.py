from flask import render_template

route = '/station/<station>'

def view(station):
    return render_template('station.html', station=station)
