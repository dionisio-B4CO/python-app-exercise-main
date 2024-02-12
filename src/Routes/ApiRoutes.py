from flask import Blueprint, jsonify
from src.Services.ApiService import ApiService

api_service = ApiService()

api_bp = Blueprint('api/', __name__)


@api_bp.route('/fetch_todos', methods=['GET'])
def fetch_todos():
    """
    Fetch TODOs from the API.

    ---
    tags:
      - api
    responses:
      200:
        description: Successful response
        schema:
          type: object
          properties:
            message:
              type: string
      500:
        description: Error response
        examples:
          application/json:
            {
              "message": "Error during API request",
              "success": false
            }
        schema:
          type: object
          properties:
            message:
              type: string
            success:
              type: boolean
    """
    try:
        # Execute the API service
        api_service.run()

        # Return a response with 200 OK status
        return jsonify({'message': 'TODOs fetched and saved!'}), 200

    except requests.RequestException as request_error:
        # Handle specific errors related to HTTP requests
        return jsonify({'message': f'Error during API request: \
                        {str(request_error)}', 'success': False}), 500

    except Exception as error:
        # Handle other errors specifically
        return jsonify({'message': f'Unexpected error: {str(error)}',
                        'success': False}), 500
