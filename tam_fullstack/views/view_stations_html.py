from flask import render_template

route = '/stations'

def view():
    return render_template('stations.html')
