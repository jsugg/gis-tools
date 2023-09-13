import argparse
import uuid
from config import Config
from utils.logger import setup_logger
from utils.file_handler import create_directories
from features.polygon_calculation.polygon import main as polygon_main

def main():
    # Generate run_id
    run_id = str(uuid.uuid4())
    
    # Setup CLI
    parser = argparse.ArgumentParser(description='GIS Tools: A utility for engineers working with GIS calculations.',
                                     formatter_class=argparse.RawTextHelpFormatter)
    
    subparsers = parser.add_subparsers(dest='feature', help='Feature to execute')
    
    # Polygon Calculation CLI
    polygon_parser = subparsers.add_parser('polygon', help='Polygon calculations')
    polygon_parser.add_argument('--file', '-f', type=str, help='CSV file path for polygon data.')
    polygon_parser.add_argument('--url', '-u', type=str, help='URL to a CSV file for polygon data.')
    polygon_parser.add_argument('--area', '-a', action='store_true', help='Calculate area of polygon.')
    polygon_parser.add_argument('--perimeter', '-p', action='store_true', help='Calculate perimeter of polygon.')
    polygon_parser.add_argument('--decimal-separator', '-d', type=str, default=Config.DECIMAL_SEPARATOR, choices=[',', '.'], help='Decimal separator in CSV file.')
    polygon_parser.add_argument('--unit', '-U', type=str, default=Config.UNIT, choices=Config.UNITS.keys(), help='Unit of measurement for results.')
    
    # Future features can be added here
    
    args = parser.parse_args()
    
    # Setup
    create_directories()
    setup_logger(run_id)
    
    # Feature execution
    if args.feature == 'polygon':
        polygon_main(args)
    else:
        print("Invalid feature selected. Use --help for more information.")

if __name__ == "__main__":
    main()
