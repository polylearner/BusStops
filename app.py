from flask import Flask, render_template
from session_bus_stops import getBusStop, getLatLongFromPostcode

app = Flask(__name__)


@app.route('/')
def index():
    route1 = '490008660N'
    route2 = '490008660S'
    r = getBusStop(route1)
    r2 = getBusStop(route2)

    return render_template('index.html', busStop1 = r, busStop2 = r2)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 