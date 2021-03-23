from flask import render_template

route = '/stations'
disabled = False

def view():
    return render_template('stations.html')
