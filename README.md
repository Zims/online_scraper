# online_scraper
...in progress

Flask web app

In the back-end is a scraper built on Beautiful soup.
It scrapes top 30 entries of the URL given as input.
User goes to yellowpages.com Does a search and copies the url of it.

The flask front-end has 2 input fields. The URL and desired file name.
After the input the scraper is called on the URL and a file with the name+current_time.json is created in the back-end.
