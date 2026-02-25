from extensions import db
from datetime import datetime


class Payment(db.Model):
    """
    Rent payment made by a tenant.
    recorded by landlord.
    """

    __tablename__ = "payments"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    month_for = db.Column(db.String(20), nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey("tenants.id"), nullable=False)
    recorded_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "payment_date": self.payment_date.isoformat(),
            "month_for": self.month_for,
            "tenant_id": self.tenant_id,
            "recorded_by": self.recorded_by
        }