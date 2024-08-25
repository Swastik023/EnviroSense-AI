from app import db

class Energy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    solar = db.Column(db.Float, nullable=False)
    wind = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Energy {self.lat},{self.lon} - Solar: {self.solar} kWh>"
