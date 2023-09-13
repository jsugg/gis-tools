"""Module for handling polygon-related API routes.

This module provides a Flask Blueprint for routes related to polygon calculations.
It uses Pydantic models for request validation and calls functions from the
features.polygon_calculation.polygon module to perform the actual calculations.

Attributes:
    bp (Blueprint): Flask Blueprint for polygon-related routes.
"""

from flask import Blueprint, jsonify, request
from flask.wrappers import Response

from api.models.polygon import Polygon
from features.polygon_calculation import polygon

bp: Blueprint = Blueprint('polygon', __name__, url_prefix='/polygon')

@bp.route('/calculate', methods=['POST'])
def calculate() -> Response:
    """Calculate the area and perimeter of a polygon.

    This route accepts JSON payload containing polygon coordinates and unit.
    It returns a JSON response with the calculated area, perimeter, and unit.

    Returns:
        Response: Flask Response object containing JSON data with calculated area,
                  perimeter, and unit.
    """
    polygon_data: Polygon = Polygon.parse_obj(request.json)
    area: float = polygon.calculate_area(polygon_data.coordinates, polygon_data.unit)
    perimeter: float = polygon.calculate_perimeter(polygon_data.coordinates, polygon_data.unit)
    return jsonify({"area": area, "perimeter": perimeter, "unit": polygon_data.unit})
