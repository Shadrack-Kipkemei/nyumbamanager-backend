from extensions import db


class Unit(db.Model):
    """
    Individual rental unit inside a property.
    Example: Unit A1
    """

    __tablename__ = "units"
    id = db.Column(db.Integer, primary_key=True)
    unit_number = db.Column(db.String(50), nullable=False)
    rent_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default="vacant")
    property_id = db.Column(db.Integer, db.ForeignKey("properties.id"), nullable=False)


    # One unit to one tenant
    tenant = db.relationship("Tenant", backref="unit", uselist=False, cascade="all, delete")
    def to_dict(self):
        return {
            "id": self.id,
            "unit_number": self.unit_number,
            "rent_amount": self.rent_amount,
            "status": self.status,
            "property_id": self.property_id
        }