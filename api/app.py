"""Main module for the GIS Tools API.

This module initializes the Flask application and registers the blueprints for
various API routes. It serves as the entry point for running the API server.

Attributes:
    app (Flask): The Flask application instance.
"""

from flask import Flask

from api.routes import polygon_routes

app: Flask = Flask(__name__)
app.register_blueprint(polygon_routes.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
