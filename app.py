from flask import Flask, jsonify

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return (
        f"Welcome to the Home Page for the SQLAlchemy Homework!!<br/>"
        f"Here are the available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )


@app.route("/api/v1.0/precipitation")
def date_prcp():
 # convert query results to a dictionary using date as the key and prcp as the value
 session = Session(engine)
 results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>='2016-08-23')
 session.close()
 prcp = list(np.ravel(results))
 #return JSON representation of dictionary
 return jsonify(prcp)
@app.route("/api/v1.0/stations")
def stations():
 # return JSON lost of stations from dataset
 session = Session(engine)
 station_name = session.query(Station.idd, Station.station, Stations.name).all()
 session.close()
  #  return jsonify
@app.route("/api/v1.0/tobs")
#def tobs():
 # query the dates and temperature observations of the most active station for the last year
 #return JSON list of TOBS for the previous year

  #  return jsonify
@app.route("/api/v1.0/<start>")
#def justice_league():
 # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
 #When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
 #When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

  #  return 

if __name__ == "__main__":
    app.run(debug=True)
