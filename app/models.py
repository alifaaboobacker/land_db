from . import db

class LandRecord(db.Model):
    __tablename__ = 'land_records'
    id = db.Column(db.Integer, primary_key=True)
    parcel_id = db.Column(db.String(50))
    plot_number = db.Column(db.String(50))
    owner_name = db.Column(db.String(100))
    area = db.Column(db.String(100))
    location = db.Column(db.String(255))
    registration_date = db.Column(db.Date)
