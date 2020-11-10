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
#def justice_league():
 #   """Return the justice league data as json"""

  #  return jsonify(justice_league_members)




if __name__ == "__main__":
    app.run(debug=True)
