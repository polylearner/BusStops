from flask import Flask, render_template
from session_bus_stops import getBusStops, getLatLongFromPostcode

app = Flask(__name__)


@app.route('/')
def index():
    r = getBusStops()

    return render_template('index.html', busStops = r)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 