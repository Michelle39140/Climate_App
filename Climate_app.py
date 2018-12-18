from flask import Flask,jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

# connect to database ############################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine,reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = scoped_session(sessionmaker(bind=engine))
# -- when use session=Session(bind=engine), it return an error due to SQLAlchemy doesn't allow to share a session across threads (wsgi); use scoped_session to create a unique session sloved the problem
###################################################################

# Flask setup
app=Flask(__name__)

# Flask routes

dt_now = dt.date(year=2017,month=8,day=23)
dt_yearago = dt_now.replace(year = dt_now.year-1)
# 0. Home page
@app.route("/")
def home():
    return (
        "<h1>Welcome to Hawaii!</h1>"\
        +"<h3>Available Routes:</h3>"\
        +"<ul><li><a href='/api/v1.0/precipitaion'>/api/v1.0/precipitaion</a></li>"\
        +"<li><a href='/api/v1.0/tobs'>/api/v1.0/tobs</a></li>"\
        +"<li><a href='/api/v1.0/stations'>/api/v1.0/stations</a></li>"\
        +"<li>/api/v1.0/start-date" 
        +"(e.g. <a href='/api/v1.0/2017-01-01'>/api/v1.0/2017-01-01</a>)</li>"\
        +"<li>/api/v1.0/start-date/end-date"
        +"(e.g. <a href='/api/v1.0/2017-01-01/2017-06-01'>/api/v1.0/2017-01-01/2017-06-01</a>)</li></ul>")


# 1. Return a JSON list of Precipitation for the previous year
@app.route("/api/v1.0/precipitaion")
def prcp():
    q_result = session.query(Measurement.date,func.avg(Measurement.prcp)).\
    filter(Measurement.date>=dt_yearago).\
    group_by(Measurement.date).\
    order_by(Measurement.date.desc()).all()

    dic = {}
    for q in q_result:
        dic[q[0]]=q[1]

    return jsonify(dic)

# 2. Return a JSON list of Temperature Observations (tobs) for the previous year
@app.route("/api/v1.0/tobs")
def tobs():
    q_result = session.query(Measurement.date,func.avg(Measurement.tobs)).\
    filter(Measurement.date>=dt_yearago).\
    group_by(Measurement.date).\
    order_by(Measurement.date.desc()).all()
    
    dic = {}
    for q in q_result:
        dic[q[0]]=q[1]
    return jsonify(dic)

# 3. Return a JSON list of stations from the dataset
@app.route("/api/v1.0/stations")
def station():
    q_result = session.query(Station.station,Station.name).all()
    
    lst = []
    for q in q_result:
        dic={}
        dic["station"]=q[0]
        dic["name"]=q[1]
        lst.append(dic)
    return jsonify(lst)

# 4. Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date
@app.route("/api/v1.0/<start>")
def start_date(start):
    q_result = session.query(Measurement.date,func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
    filter(Measurement.date>=start).\
    group_by(Measurement.date).\
    order_by(Measurement.date.desc()).all()
    
    lst = []
    for q in q_result:
        dic={}
        dic["date"]=q[0]
        dic["TMIN"]=q[1]
        dic["TAVG"]=q[2]
        dic["TMAX"]=q[3]
        lst.append(dic)
    return jsonify(lst)

# 5. Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range.
@app.route("/api/v1.0/<start>/<end>")
def date_range(start,end):
    q_result = session.query(Measurement.date,func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
    filter(Measurement.date>=start).\
    filter(Measurement.date<=end).\
    group_by(Measurement.date).\
    order_by(Measurement.date.desc()).all()
    
    lst = []
    for q in q_result:
        dic={}
        dic["date"]=q[0]
        dic["TMIN"]=q[1]
        dic["TAVG"]=q[2]
        dic["TMAX"]=q[3]
        lst.append(dic)
    return jsonify(lst)

# start server
if __name__ == "__main__":
    app.run