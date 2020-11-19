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
    results = session.query(Measurement.date,Measurement.prcp).order_by(Measurement.date).all()
    session.close()
    return jsonify(dict(results))
 #return JSON representation of dictionary
@app.route("/api/v1.0/stations")
def stations():
 # return JSON lost of stations from dataset
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()
    result =list(np.ravel(results))
  #  return jsonify
    return jsonify(result)
@app.route("/api/v1.0/tobs")
def tobs():
 # query the dates and temperature observations of the most active station for the last year
 #return JSON list of TOBS for the previous year
    session = Session(engine)
    tob_ls_t = session.query(Measurement.tobs).\
    filter(Measurement.date>='2016-08-23').\
    filter(Measurement.station =='USC00519281').all()
    session.close()
    result =list(np.ravel(tob_ls_t))
    return jsonify(result)
  #  return jsonify

@app.route("/api/v1.0/<start>")
def start():
    session = Session(engine)
    tob_ls_t = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
    filter(Measurement.date>=start).all()
    session.close()
    result =list(np.ravel(tob_ls_t))
    result_dict = {'TMIN':result[0],'TAVG':round(result[1],1),'TMAX ':result[2]}
    return jsonify(result_dict)
 # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
@app.route("/api/v1.0/<start>/<end>")
def s_e(start,end):
    session = Session(engine)
    tob_ls_t = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
    filter(Measurement.date>=start).filter(Measurement.date<=end).all()
    session.close()
    result =list(np.ravel(tob_ls_t))
    result_dict = {'TMIN':result[0],'TAVG':round(result[1],1),'TMAX ':result[2]}
    return jsonify(result_dict)
 #When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
 #When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

if __name__ == "__main__":
    app.run(debug=True)