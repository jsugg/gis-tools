# GIS Tools

![System Diagram](https://showme.redstarplugin.com/s/SOoSOu2p)

This repository contains a small project that aims to create tools to facilitate the work of people working with multiple GIS tools. The first milestone is to streamline the process of creating flood and flow studies using automated pipelines and developing tools tailored to the task combined with AI. It has a modular system design, so there'll be more modules to be implemented, and it's served as an API.

## System Overview

The diagram above provides a high-level overview of how the system works. When a user makes an HTTP API request, it is processed by the API, which then sends a request to the `polygon.py` script. This script reads data from a CSV file or URL, calculates the area and perimeter of the polygon defined by the data, and writes the results to a JSON file. The API then returns these results to the user.

## Features

- **Automated Pipelines**: Streamline the process of creating flood and flow studies.
- **AI Integration**: Utilize AI to enhance the accuracy and efficiency of the tools.
- **Modular Design**: The system is designed to be modular, allowing for the easy addition of more modules in the future.
- **Multi-threading**: The system uses multi-threading to improve the speed of calculations, especially for large areas and complex perimeters.

## Getting Started

To get started with this project, clone the repository and install the dependencies listed in the `Pipfile`.

## Usage

The main functionality of the system is contained in the `polygon.py` script. This script can be run from the command line and accepts several arguments:

- `--file` or `-f`: The path to a CSV file containing the polygon data.
- `--url` or `-u`: A URL to a CSV file containing the polygon data.
- `--area` or `-a`: Calculate the area of the polygon.
- `--perimeter` or `-p`: Calculate the perimeter of the polygon.
- `--decimal-separator` or `-d`: The decimal separator used in the CSV file.
- `--unit` or `-U`: The unit of measurement for the results.

## Contributing

We welcome contributions to this project. If you have a feature you'd like to add, please open an issue to discuss it before making a pull request.

## License

This project is licensed under the terms of the MIT license. See the `LICENSE` file for details.

If you're interested in contributing to the development of this plugin, you can check out the open issues on the [project's GitHub page](https://github.com/bra1nDump/show-me-chatgpt-plugin/issues).
