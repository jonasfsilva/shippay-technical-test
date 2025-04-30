from flask import Flask
from config import Config
from models import db, Role
from routes import routes

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        if not Role.query.filter_by(description="default").first():
            default_role = Role(description="default")
            db.session.add(default_role)
            db.session.commit()

    app.run(debug=True)
