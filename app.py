from flask import Flask, jsonify

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/"):
def index():
    return (
        f"Welcome to the Home Page for the SQLAlchemy Homework!!<br/>"
        f"Here are the available routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )



#@app.route("/api/v1.0/pre")
#def justice_league():
 #   """Return the justice league data as json"""

  #  return jsonify(justice_league_members)




if __name__ == "__main__":
    app.run(debug=True)
