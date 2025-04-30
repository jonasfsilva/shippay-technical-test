from flask import Blueprint, request, jsonify
from models import db, User, Role, Claim
import secrets
import string

routes = Blueprint("routes", __name__)


def generate_password(length=12):
    return "".join(
        secrets.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


@routes.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha") or generate_password()
    role_id = data.get("role_id")
    claim_ids = data.get("claim_ids", [])

    if any([nome, email, role_id]):
        return jsonify({"error": "nome, email e role_id são obrigatórios"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "email ja cadastrado"}), 400

    role = Role.query.get(role_id)
    if not role:
        return jsonify({"error": "role_id invalido"}), 400

    claims = Claim.query.filter(Claim.id.in_(claim_ids)).all() if claim_ids else []

    user = User(nome=nome, email=email, senha=senha, role=role, claims=claims)
    db.session.add(user)
    db.session.commit()

    return (
        jsonify(
            {
                "id": user.id,
                "nome": user.nome,
                "email": user.email,
                "role": role.description,
                "claims": [c.description for c in claims],
            }
        ),
        201,
    )
