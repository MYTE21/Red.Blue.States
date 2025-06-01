# 🗳️ Red.Blue.States
Scraping a static Wikipedia page [🔗 Red states and blue states](https://en.wikipedia.org/wiki/Red_states_and_blue_states), 
to collect information about presidential elections by states since 1972.

* **Wikipedia Page Link:** [🔗 Red states and blue states](https://en.wikipedia.org/wiki/Red_states_and_blue_states).
* **Scraped Table Link:** [🔗 Table of presidential elections by states since 1972](https://en.wikipedia.org/wiki/Red_states_and_blue_states#:~:text=suburbs%20were%20divided.-,Table%20of%20presidential%20elections%20by%20states%20since%201972,-%5Bedit%5D).

# 🛠 ️Tools and Techniques
1. [🔗 Requests](https://requests.readthedocs.io/en/latest/): Requests is an elegant and simple HTTP library for Python, built for human beings.
2. [🔗 Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/): Beautiful Soup is a Python library used to parse HTML and XML documents, making it easy to extract data from web pages.
3. [🔗 lxml](https://lxml.de/): lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.
4. [🔗 Pandas](https://pandas.pydata.org/): Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
5. [🔗 Regular Expression](https://docs.python.org/3/library/re.html): A regular expression (or *regex*) is a sequence of characters that forms a search pattern used to match, find, or manipulate text based on specific rules.

# 🎄 Environment Setup
1. Install all the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

# 📜 Notebooks

1. [🔗 scraping_static_website.ipynb](notebooks/scraping_static_website.ipynb):
   Scraping a static Wikipedia page [🔗 Red states and blue states](https://en.wikipedia.org/wiki/Red_states_and_blue_states),to collect information about presidential elections by states since 1972.
   This notebook gives a step-by-step demonstration
   to collect the US presidential elections by states and US presidential candidates'
   data and store it in CSV files.</br>
   ***🚀 Skills:** Requests, Beautiful Soup, lxml, Pandas.*
2. [🔗 data_cleaning.ipynb](notebooks/data_cleaning.ipynb): Remove null values,
   as those don't align with the dataset and don't contain any substantial information.
   Furthermore, remove some parts of the strings to make the data more useful and avoid outliers.
   </br>
   ***🚀 Skills:** Regular Expression.*