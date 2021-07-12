# LAW SCRAPER

Backend includes a web crawler that scrapes federal government websites for most recent laws and regularly sends mailing list emails containing information about the laws that were recently passed. Frontend includes a stylish website where new readers learn about the purpose behind the web scraping application and sign up to receive emails. 

## This application currently supports:
- U.S. federal laws
- Canadian federal laws (in progress)

## Setting up application on own machine:

1. Make sure Python (>= 3.8) and JavaScript are properly installed.
2. Clone this repository.
3. Open up terminal at ``` LawScraper/ ``` and install all package.json dependencies with ``` npm install ```.
4. Stay in the same folder and install Python requirements with ``` pip install -r requirements.txt ```.

## Running Backend:
1. Go to ``` LawScraper/ ```
2. Run ``` python backend/main.py ```

## Running Frontend:
1. Go to ``` LawScraper/ ```
2. Run ``` npm start ```
3. Go to your preferred web browser and go to ``` localhost:3000/views/index.html ```
