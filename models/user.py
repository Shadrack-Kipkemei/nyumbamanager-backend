from extenstions import db, bcrypt
from datetime import datetime


class User(db.Model):
    """
    User model.
    A user can either be:
    - landlord
    - tenant
    """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False) # landlord or tenant
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    # ----------------
    # Relationships
    # ----------------

    # One landlord to many properties
    properties = db.relationship("Property", backref="landlord", lazy=True)

    # One tenant to one profile
    tenant_profile = db.relationship("TenantProfile", backref="user", uselist=False, cascade="all, delete")

    # One landlord to many recorded payments
    payments_recorded = db.relationship("Payment", backref="landlord_recorder", lazy=True)


    # ----------------
    # Password methods
    # ----------------
    def set_password(self, password):
        """Hash and store password securely"""
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        """Verify password"""
        return bcrypt.check_password_hash(self.password_hash, password)

    
    # ----------------
    # Serialization
    # ----------------
    deft to_dict(self):
        """Convert object to dictionary (safe fields only)"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "created_at": self.created_at.isoformat()
        }
