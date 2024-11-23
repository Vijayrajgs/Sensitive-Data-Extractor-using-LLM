from flask import Flask
from app.models.database import init_db
from app.config import Config
from app.routes import home, upload_file, view_scan, history, delete_entry  # Import routes setup function

def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from Config class

    # Initialize MongoDB
    init_db(app)

     # Register the routes directly here
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/Upload', 'upload_file', upload_file, methods=['GET', 'POST'])
    app.add_url_rule('/view_scan/<filename>', 'view_scan', view_scan, methods=['GET'])
    app.add_url_rule('/History', 'history', history, methods=['GET'])
    app.add_url_rule('/Delete_entry/<scan_id>', 'delete_entry', delete_entry, methods=['POST'])

    return app
