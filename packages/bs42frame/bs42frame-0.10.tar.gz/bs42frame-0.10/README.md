# bs4 to pd.DataFrame 

## Tested against Windows / Python 3.11 / Anaconda

## pip install bs42frame

```python
Parse HTML content and extract information using BeautifulSoup.

This function takes HTML content as input, parses it using BeautifulSoup, and extracts
information about the HTML structure, tag attributes, tag text, and the BeautifulSoup
object for each element found in the HTML.

Args:
	html (str, bytes, or file path): The HTML content to be parsed. It can be provided as
		a string, bytes, or a file path. If a file path is provided, the function will
		attempt to read the file.

Returns:
	pandas.DataFrame: A DataFrame containing the extracted information from the HTML.
		The DataFrame columns include 'aa_tag' (HTML tag name), 'aa_attrs' (list of tag
		attributes), 'aa_text' (text content of the tag), 'aa_soup' (BeautifulSoup object
		for the tag), 'aa_old_index' (original index of the tag), 'aa_key' (attribute
		key), and 'aa_value' (attribute value).

Example:
	from bs42frame import parse_html
	df = parse_html(
		html=r"C:\Users\hansc\Downloads\Your Repositories.mhtml"
	)
	#      aa_tag            aa_text                                          aa_soup  aa_old_index                     aa_key             aa_value
	# 1000   span  Import repository  [\r\n                Import repository\r\n\r\n]           274       ActionListItem-label                class
	# 1001     li                                                                  []           275               presentation                 role
	# 1002     li                                                                  []           275                       true          aria-hidden
	# 1003     li                                                                  []           275                       true  data-view-component
	# 1004     li                                                                  []           275  ActionList-sectionDivider                class
```