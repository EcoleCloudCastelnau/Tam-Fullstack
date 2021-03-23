from flask import render_template

route = '/next'

def view():
    return render_template('next_departure.html')
