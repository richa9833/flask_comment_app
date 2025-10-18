from flask import Flask
from flask_cors import CORS
from extensions import db  # ✅ import db from extensions

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Import and register routes
from routes.comments import comments_bp
app.register_blueprint(comments_bp)

# Import models (after db is set up)
from models import Comment

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return {"message": "Flask Comment API is running successfully 🚀"}

if __name__ == "__main__":
    app.run(debug=True)
    print(app.url_map)
