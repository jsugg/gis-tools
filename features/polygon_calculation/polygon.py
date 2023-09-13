import argparse
import logging
from datetime import datetime
from multiprocessing import Manager, Process
from typing import Dict, Optional

import pandas as pd
from pydantic import BaseModel
from shapely.geometry import Polygon

from config import Config


class PolygonData(BaseModel):
    """Model for Polygon Data."""
    longitude: float
    latitude: float

class Args(BaseModel):
    """Model for command-line arguments."""
    file: Optional[str]
    url: Optional[str]
    area: bool
    perimeter: bool
    decimal_separator: str = Config.DECIMAL_SEPARATOR
    unit: str = Config.UNIT

def read_data(file: Optional[str] = None, url: Optional[str] = None, decimal_separator: str = Config.DECIMAL_SEPARATOR) -> pd.DataFrame:
    """
    Read data from a CSV file or URL.

    Args:
        file (Optional[str]): Path to the CSV file.
        url (Optional[str]): URL to the CSV file.
        decimal_separator (str, optional): Decimal separator in CSV file. Defaults to Config.DECIMAL_SEPARATOR.

    Returns:
        pd.DataFrame: Data read from the file or URL.
    """
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
    except Exception as error:
        logging.error(f"Error reading data: {str(error)}")
        raise

def calculate_area(data: pd.DataFrame, unit: str = Config.UNIT, results: Optional[Dict] = None) -> float:
    """
    Calculate the area of a polygon.

    Args:
        data (pd.DataFrame): Data containing longitude and latitude.
        unit (str, optional): Unit of measurement for results. Defaults to Config.UNIT.
        results (Optional[Dict], optional): Dictionary to store results. Defaults to None.

    Returns:
        float: Calculated area.
    """
    try:
        polygon = Polygon(zip(data['longitude'], data['latitude']))
        area = polygon.area / (Config.UNITS[unit] ** 2)
        if results is not None:
            results['area'] = area
        return area
    except Exception as error:
        logging.error(f"Error calculating area: {str(error)}")
        raise

def calculate_perimeter(data: pd.DataFrame, unit: str = Config.UNIT, results: Optional[Dict] = None) -> float:
    """
    Calculate the perimeter of a polygon.

    Args:
        data (pd.DataFrame): Data containing longitude and latitude.
        unit (str, optional): Unit of measurement for results. Defaults to Config.UNIT.
        results (Optional[Dict], optional): Dictionary to store results. Defaults to None.

    Returns:
        float: Calculated perimeter.
    """
    try:
        polygon = Polygon(zip(data['longitude'], data['latitude']))
        perimeter = polygon.length / Config.UNITS[unit]
        if results is not None:
            results['perimeter'] = perimeter
        return perimeter
    except Exception as error:
        logging.error(f"Error calculating perimeter: {str(error)}")
        raise

import json


def display_and_write_results(results: Dict, unit: str) -> None:
    """
    Display the calculated results in the console and write them to a JSON file.

    Args:
        results (Dict): Dictionary containing the calculated area and/or perimeter.
        unit (str): Unit of measurement for results.
    """
    if 'area' in results:
        print(f"Calculated Area: {results['area']} {unit}²")
    if 'perimeter' in results:
        print(f"Calculated Perimeter: {results['perimeter']} {unit}")

    results_file_path = f"{Config.RESULTS_DIR}/polygon_results_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    with open(results_file_path, 'w') as f:
        json.dump(results, f)

def main():
    """Main function for polygon calculations."""
    parser = argparse.ArgumentParser(description='Calculate area and perimeter of a polygon from CSV file or URL.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--file', '-f', type=str, help='CSV file path.')
    group.add_argument('--url', '-u', type=str, help='URL to a CSV file.')
    parser.add_argument('--area', '-a', action='store_true', help='Calculate area.')
    parser.add_argument('--perimeter', '-p', action='store_true', help='Calculate perimeter.')
    parser.add_argument('--decimal-separator', '-d', type=str, default=Config.DECIMAL_SEPARATOR, choices=[',', '.'], help='Decimal separator in CSV file.')
    parser.add_argument('--unit', '-U', type=str, default=Config.UNIT, choices=Config.UNITS.keys(), help='Unit of measurement for results.')
    
    args = Args(**vars(parser.parse_args()))
    data = read_data(args.file, args.url, args.decimal_separator)
    
    manager = Manager()
    results: Dict = manager.dict()

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

    # Display and write results
    display_and_write_results(results, args.unit)

if __name__ == "__main__":
    main()
