# GIS Tools

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.8-blue)

## Overview

GIS Tools is a work in progress for a comprehensive library designed to aid engineers and scientists working with Geographic Information Systems (GIS). The library offers a range of functionalities, from polygon calculations to future GIS-related features, all served through a RESTful API.

## Features

- **Polygon Calculations**: Compute area, perimeter, and other properties of polygons.
- **Extensible Architecture**: Easily add more GIS-related functionalities.
- **RESTful API**: Access all functionalities through a well-documented API.
- **High Test Coverage**: Unit, integration, and performance tests with 100% coverage.

## Installation

Clone the repository and navigate to the project root directory. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Running the API Server
From the project root directory, run:
```
make start-api
```

The API will be accessible at http://127.0.0.1:5000/.

Running Tests
To run all tests and generate a coverage report, execute:
```
make test
```

## API Documentation

### Polygon Calculations
Endpoint: /polygon/calculate
Method: POST
Payload:

```
{
  "coordinates": [
    {"longitude": 0, "latitude": 0},
    {"longitude": 1, "latitude": 0},
    {"longitude": 1, "latitude": 1},
    {"longitude": 0, "latitude": 1}
  ],
  "unit": "km"
}
```
Response:
```
{
  "area": 1.0,
  "perimeter": 4.0,
  "unit": "km"
}
```

## Contributing
Contributions are welcome! 

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
