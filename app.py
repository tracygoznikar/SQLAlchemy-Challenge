import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine,reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return (
        f"Welcome to the Home Page for the SQLAlchemy Homework!!<br/>"
        f"<h3>Available Routes:</h3>"
        f"<ul><li>/api/v1.0/precipitation</li>"
        f"<li>/api/v1.0/stations</li>"
        f"<li>/api/v1.0/tobs</li>"
        f"<li>/api/v1.0/start_date</li>"
        f"<li>/api/v1.0/start_date/end_date</li></ul>"
    )






@app.route("/api/v1.0/precipitation")
def date_prcp():
 # convert query results to a dictionary using date as the key and prcp as the value
 session = Session(engine)
 prcp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>='2016-08-23')
 session.close()
 prcp = list(np.ravel(prcp))
 #return JSON representation of dictionary
 return jsonify(prcp)
@app.route("/api/v1.0/stations")
def stations():
 # return JSON lost of stations from dataset
 session = Session(engine)
 station_name = session.query(Station.idd, Station.station, Stations.name).all()
 session.close()
 station_name = list(np.ravel(station_name))
  #  return jsonify
 return jsonify(station_name)
#@app.route("/api/v1.0/tobs")
#def tobs():
 # query the dates and temperature observations of the most active station for the last year
 #return JSON list of TOBS for the previous year

  #  return jsonify
#@app.route("/api/v1.0/<start>")
#def justice_league():
 # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
 #When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
 #When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

if __name__ == "__main__":
    app.run(debug=True)