 #!/usr/bin/python
# Basic packages to get the scirpt up and running
import webbrowser, wikipedia, sys

def main(argv):
	# Ask the user for a page to query
	page_search = wikipedia.page(input('Page Search: '))
	# Open a web browser to the page
	webbrowser.open_new(page_search.url)

if __name__ == '__main__':
   main(sys.argv[1:])