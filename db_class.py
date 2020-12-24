from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from cryptography import utils, x509
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://y:123@localhost:5432/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["IMAGE_UPLOADS"] = 'uploads'


db = SQLAlchemy(app)
migrate = Migrate(app, db)


def time_stamp():
    now = datetime.now()
    print("now =", now)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string






class Band(db.Model):
  __tablename__ = 'band'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  title = db.Column(db.String(), nullable=False)
  main_image = db.Column(db.String(), nullable=False, default='/static/deafult_band.jpg')
  image1 = db.Column(db.String(), default='/static/deafult_band2.jpg')
  image2 = db.Column(db.String(), default='/static/deafult_band3.jpg')
  band_member_name1 = db.Column(db.String(), nullable=False,  )
  band_member_image1 = db.Column(db.String(), nullable=False,  default='/static/profile.png')
  band_member_name2 = db.Column(db.String())
  band_member_image2 = db.Column(db.String())
  band_member_name3 = db.Column(db.String())
  band_member_image3 = db.Column(db.String())
  email = db.Column(db.String(), nullable=False)
  mobile = db.Column(db.String(), nullable=False)
  full_desc = db.Column(db.String(), nullable=False)
  def __repr__(self):
    return "{} ".format(self.name)


class Event(db.Model):
  __tablename__ = 'event'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  title = db.Column(db.String(), nullable=False)
  date = db.Column(db.String(), nullable=False)
  image = db.Column(db.String(), nullable=False)
  address = db.Column(db.String(), nullable=False)
  price = db.Column(db.String(), nullable=False)
  full_desc = db.Column(db.String(), nullable=False)
  like = db.Column(db.Integer, default=0)
  #completed = db.Column(db.Boolean, nullable = False, default=False)
  band_id = db.Column(db.Integer, db.ForeignKey('band.id'))
  band = db.relationship(Band)



class Comment(db.Model):
  __tablename__ = 'comment'
  id = db.Column(db.Integer, primary_key=True)
  sender_name = db.Column(db.String(), nullable=False, default='user')
  content = db.Column(db.Boolean(), nullable=False, default='')
  date = db.Column(db.Boolean(), nullable=False, default=time_stamp())
  event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
  event = db.relationship(Event)
  def __repr__(self):
    return "<Comment ID: {}, name: {}>".format(self.id, self.date)



  def __repr__(self):
    return "<Event ID: {}, name: {}, Band Id:{}>".format(self.id, self.name, self.band_id)
db.create_all()
