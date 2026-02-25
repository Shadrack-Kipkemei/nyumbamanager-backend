from extensions import db


class Property(db.Model):
    """
    Represents a rental property owned by a landlord.
    Example: 'Sunset Apartments'
    """

    __tablename__ = "properties"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    landlord_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


    # One property to many units
    units = db.relationship("Unit", backref="property", lazy=True, cascade="all, delete")
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "landlord_id": self.landlord_id
        }