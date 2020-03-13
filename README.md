# SCRAPING WIKIPEDIA ARTICLES' CONTENT USING THE WIKIPEDIA PYTHON API

Wikipedia has articles now available in around 300 hundred languages. It constitutes one of the best sources of data for projects that require annotated text data. Each article is organized by tags and categories which makes it convenient for various NLP tasks for instance.

Wikipedia is one of the well furnished websites that is not scraping friendly but even more than that provides an API, developers can use to query it and get articles' content.

The structures of wikipedia sub domains (each subdomain corresponding to a different language) often differ from each other. In this repository I have provided two scripts to scrape data from Kabiye (one of the two national languages of Togo republic) subdomain of Wikipedia. The scripts can be used for any other language/subdomain. The articles are organized into a csv file having columns title , content, url and categories.

This script has been used to generate part of one of the the winning datasets at The AI4D African Languages Dataset challenge. The complete dataset is available here.