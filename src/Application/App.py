from flask import Flask
from flasgger import Swagger
import logging
import sys

from src.Services.ApiService import ApiService
from src.Routes.ApiRoutes import api_bp


class App:
    def __init__(self, api_service: ApiService, port=5000):
        """
        Initialize the application.

        This method creates an instance of the API service and a Flask application.
        It also configures the application by registering API routes.
        """
        self._api_service = api_service
        self._app = Flask(__name__)
        self._configure_app()

        # Use the specified port or the default if not provided
        self._port = port

    def _configure_app(self):
        """
        Configure the Flask application.

        This method registers API routes with the Flask application.
        """
        # Blueprints
        self._app.register_blueprint(api_bp, url_prefix='/api')

        # Swagger
        self._app.config['SWAGGER'] = {
            "title": "Demo API",
            'supported_submit_methods': ['get'],
        }
        Swagger(self._app, template={
            "swagger": "2.0",
            "produces": [
                "application/json",
            ],
        })

        # Add a logger for Flask
        log_handler = logging.StreamHandler(sys.stdout)
        log_handler.setLevel(logging.INFO)
        self._app.logger.addHandler(log_handler)

    def api_service(self) -> ApiService:
        """
        Get an instance of the API service.

        Returns:
            ApiService: An instance of the API service.
        """
        return self._api_service

    def run(self):
        """
        Run the Flask application.

        This method starts the Flask development server.
        """
        self._app.run(
            debug=True,
            host='0.0.0.0',
            port=self._port,
            use_reloader=True)
