import argparse
import pandas as pd
import numpy as np
import logging
import os
import uuid
import json
from datetime import datetime
from multiprocessing import Process, Manager
from shapely.geometry import Polygon
from pyproj import Proj, transform
# from .polygon_service import calculate_area, calculate_perimeter
""" if __name__ == "__main__":
    from polygon_service import calculate_area, calculate_perimeter
else:
    from polygon.polygon_service import calculate_area, calculate_perimeter """
    
# Constants
LOG_DIR = "./log"
RESULTS_DIR = "./results"
TEST_RESULTS_DIR = "./test-results"
DECIMAL_SEPARATOR = ","
UNIT = "km"
UNITS = {"cm": 100000, "m": 1000, "km": 1}

# Create directories if not exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(TEST_RESULTS_DIR, exist_ok=True)

# Logger setup
run_id = str(uuid.uuid4())
log_filename = f"{datetime.now().strftime('%Y-%m-%d')} {run_id}.log"
logging.basicConfig(filename=os.path.join(LOG_DIR, log_filename), level=logging.INFO)

# Argument Parser
parser = argparse.ArgumentParser(description='Calculate area and perimeter of a polygon from CSV file or URL.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--file', '-f', type=str, help='CSV file path.')
group.add_argument('--url', '-u', type=str, help='URL to a CSV file.')
parser.add_argument('--area', '-a', action='store_true', help='Calculate area.')
parser.add_argument('--perimeter', '-p', action='store_true', help='Calculate perimeter.')
parser.add_argument('--decimal-separator', '-d', type=str, default=DECIMAL_SEPARATOR, choices=[',', '.'], help='Decimal separator in CSV file.')
parser.add_argument('--unit', '-U', type=str, default=UNIT, choices=UNITS.keys(), help='Unit of measurement for results.')

# Functions
def read_data(file=None, url=None, decimal_separator=DECIMAL_SEPARATOR):
    try:
        if file:
            data = pd.read_csv(file)
        elif url:
            data = pd.read_csv(url)
        else:
            raise ValueError("Either file or url must be provided.")
        
        if decimal_separator == ',':
            data = data.apply(lambda x: x.str.replace(',', '.').astype('float'), axis=1)
        
        return data
    except Exception as e:
        logging.error(f"Error reading data: {str(e)}")
        raise

def calculate_area(data, unit=UNIT, results=None):
    try:
        #in_proj = Proj('EPSG:4326')
        #out_proj = Proj('EPSG:3857')
        #data['longitude'], data['latitude'] = transform(in_proj, out_proj, data['longitude'].tolist(), data['latitude'].tolist())
        polygon = Polygon(zip(data['longitude'], data['latitude']))
        area = polygon.area / (UNITS[unit] ** 2)
        if results is not None:
            results['area'] = area
        return area
    except Exception as e:
        raise

def calculate_perimeter(data, unit=UNIT, results=None):
    try:
        #in_proj = Proj('EPSG:4326')
        #out_proj = Proj('EPSG:3857')
        #data['longitude'], data['latitude'] = transform(in_proj, out_proj, data['longitude'].tolist(), data['latitude'].tolist())
        polygon = Polygon(zip(data['longitude'], data['latitude']))
        perimeter = polygon.length / UNITS[unit]
        if results is not None:
            results['perimeter'] = perimeter
        return perimeter
    except Exception as e:
        raise

def write_results(run_id, timestamp, file, url, area, perimeter, unit):
    try:
        results = {
            "run_id": run_id,
            "timestamp": timestamp,
            "file": file,
            "url": url,
            "area": area,
            "perimeter": perimeter,
            "unit": unit
        }
        with open(os.path.join(RESULTS_DIR, f"{run_id}.json"), 'w') as f:
            json.dump(results, f)
    except Exception as e:
        logging.error(f"Error writing results: {str(e)}")
        raise

# Main Execution
def main():
    args = parser.parse_args()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        data = read_data(args.file, args.url, args.decimal_separator)
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")
        exit(1)

    manager = Manager()
    results = manager.dict()

    if args.area and args.perimeter:
        process1 = Process(target=calculate_area, args=(data, args.unit, results))
        process2 = Process(target=calculate_perimeter, args=(data, args.unit, results))
        process1.start()
        process2.start()
        process1.join()
        process2.join()
    elif args.area:
        calculate_area(data, args.unit, results)
    elif args.perimeter:
        calculate_perimeter(data, args.unit, results)

    write_results(run_id, timestamp, args.file, args.url, results.get('area'), results.get('perimeter'), args.unit)

if __name__ == "__main__":
    main()
