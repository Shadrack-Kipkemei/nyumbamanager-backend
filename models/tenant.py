from extensions import db


class Tenant(db.Model):
    """
    Extra information about a tenant.
    Linked to User and Unit.
    """

    __tablename__ = "tenants"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), nullable=False)
    id_number = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    unit_id = db.Clumn(db.Integer, db.ForeignKey("units.id"), nullable=False)

    # One tenant to many payments
    payments = db.relationship("Payment", backref="tenant", lazy=True, cascade="all, delete")
    def to_dict(self):
        return {
            "id": self.id,
            "phone": self.phone,
            "id_number": self.id_number,
            "user_id": self.user_id,
            "unit_id": self.unit_id
        }