"""Module for defining Pydantic models related to polygons.

This module contains Pydantic models that define the structure of a polygon
and its coordinates. These models are used for data validation and serialization
in the API.
"""

from typing import List

from pydantic import BaseModel, Field


class Coordinate(BaseModel):
    """Defines a geographic coordinate.

    Attributes:
        longitude (float): The longitude of the coordinate.
        latitude (float): The latitude of the coordinate.
    """
    longitude: float = Field(..., description="Longitude of the coordinate")
    latitude: float = Field(..., description="Latitude of the coordinate")

class Polygon(BaseModel):
    """Defines a polygon using a list of coordinates.

    Attributes:
        coordinates (List[Coordinate]): A list of Coordinate objects forming the polygon.
        unit (str): The unit for area and perimeter calculation. Defaults to 'km'.
    """
    coordinates: List[Coordinate] = Field(..., description="List of coordinates forming the polygon")
    unit: str = Field("km", description="Unit for area and perimeter calculation")
