# scraping-amazon-coffee-makers

This is a project that seeks to obtain information on coffee makers and the top reviews of people about them. 
Our team members are:
- Sebastián Galindo 15452
- Jose Antonio Ramirez 15441
- Diego Castañeda 15151

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

## Output

This program generates a .csv file named "coffee_makers.csv" containing the following structure:

- Name
- URL
- Rating
- Review

## Team contributions

Our team contributions are divided as follow:

- Diego Castañeda: System desing and scrapy usage investigator for scraping Amazon websites.
- Jose Antonio Ramirez: Creator of base project structure and initital scrape over amazon coffee makers.
- Sebastián Galindo: Creator of scrapy recursion over amazon coffee makers pages and output with top reviews.