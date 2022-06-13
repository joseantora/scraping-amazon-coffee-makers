# scraping-amazon-coffee-makers

This is a project that seeks to obtain information on coffee makers and the opinions of people about them.

## Installation

It is recommended to use a virtual environment before installing the libraries used in the project. To install the libraries, use the following command:

```bash
pip install -r requirements.txt
```

## Usage

First, be sure to navigate into the project folder in order to execute the commands "..\scraping-amazon-coffee-makers". To make the spider perform the crawl, use the following command:

```bash
scrapy crawl coffee_makers -o coffee_makers.csv -t csv
```