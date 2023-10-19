# Import the dependencies.
from flask import Flask, jsonify, render_template
import datetime as dt
import numpy as np
# Database Setup
#################################################
# Import SQLAlchemy and other necessary libraries
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Create an engine to connect to your SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the database tables into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session (link) from Python to the DB
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Query the precipitation data for the last 12 months
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= '2016-08-23').all()

    # Convert the results to a dictionary
    precipitation_data = {}
    for date, prcp in results:
        precipitation_data[date] = prcp

    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    # Query the list of stations
    results = session.query(Station.station).all()

    # Convert the results to a list
    station_list = [result[0] for result in results]

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    
    station_counts = session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.station).desc()).all()

    most_active_station_id = station_counts[0][0]

    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    most_recent_date = most_recent_date[0]  # Extract the date from the result

# Convert the most_recent_date to a datetime object
    most_recent_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d') 
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    tobs_data = session.query(Measurement.tobs).\
    filter(Measurement.station == most_active_station_id).\
    filter(Measurement.date >= one_year_ago).all()
    # Return the JSON list of temperature observations
    
    return jsonify(list(np.ravel(tobs_data)))

# Dynamic Routes for Temperature Statistics
@app.route("/api/v1.0/<start>")
def temp_stats_start(start):
# Calculate temperature statistics for dates greater than or equal to the start date
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')  

    tobs_data = session.query(Measurement.tobs).\
    filter(Measurement.date >= start_date).all()
    # Return the JSON list of temperature observations
    tobs_data_list = list(np.ravel(tobs_data))
    max_temp = max(tobs_data_list)
    min_temp = min(tobs_data_list)
    average_temp = round(np.mean(tobs_data_list),2)
    return jsonify([max_temp, min_temp, average_temp])

@app.route("/api/v1.0/<start>/<end>")
def temp_stats_start_end(start, end):
    # Calculate temperature statistics for the specified date range
    # Complete this route based on the provided start and end dates
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    end_date =  dt.datetime.strptime(end, '%Y-%m-%d')

    tobs_data = session.query(Measurement.tobs).\
    filter(Measurement.date >= start_date, Measurement.date <= end_date).all()
    # Return the JSON list of temperature observations
    tobs_data_list = list(np.ravel(tobs_data))
    max_temp = max(tobs_data_list)
    min_temp = min(tobs_data_list)
    average_temp = round(np.mean(tobs_data_list),2)
    return jsonify([max_temp, min_temp, average_temp])

# Define a route for rendering the HTML template
@app.route("/webpage")
def webpage():
    # Render the "webpage.html" template
    return render_template("webpage.html")

if __name__ == "__main__":
    app.run(debug=True)
