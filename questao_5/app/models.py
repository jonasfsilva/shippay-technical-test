from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user_claims = db.Table(
    "user_claims",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("claim_id", db.Integer, db.ForeignKey("claims.id")),
)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    users = db.relationship("User", back_populates="role")


class Claim(db.Model):
    __tablename__ = "claims"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, default=True)
    users = db.relationship("User", secondary=user_claims, back_populates="claims")


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    senha = db.Column(db.String, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    role = db.relationship("Role", back_populates="users")
    claims = db.relationship("Claim", secondary=user_claims, back_populates="users")
