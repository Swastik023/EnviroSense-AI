from app import db

class AirQuality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    aqi = db.Column(db.Integer, nullable=False)
    pm25 = db.Column(db.Float, nullable=False)
    pm10 = db.Column(db.Float, nullable=False)
    co = db.Column(db.Float, nullable=False)
    no2 = db.Column(db.Float, nullable=False)
    o3 = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<AirQuality {self.city} - AQI: {self.aqi}>"
