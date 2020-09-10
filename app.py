from flask import Flask, render_template
from session_bus_stops import getBusStop1, getBusStop2, getLatLongFromPostcode

app = Flask(__name__)


@app.route('/')
def index():
    r = getBusStop1()
    r2 = getBusStop2()

    return render_template('index.html', busStop1 = r, busStop2 = r2)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 