import requests
from bs4 import BeautifulSoup

def matrixify(columns, rows, filler):
	xyz = [[filler]*columns for _ in range(rows)]
	return xyz
def display(matrix):
	for row in matrix:
		print (" ".join(map(str,row)))
def replace_index(matrix, x, y, filler):
	matrix[x][y] = filler
	return matrix
def contains(matrix, string):
	for row in matrix:
		if string in row:
			return True
	return False
def replace(matrix, string, filler):
	for x in range(len(matrix)):
		for y in range(len(matrix[x])):
			if matrix[x][y] == string:
				matrix[x][y] = filler
	return matrix
def webscrape(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			html = response.text
			soup = BeautifulSoup(html, 'html.parser')
			return(soup)
		else:
			return response.status_code
	except:
		return "Error while scraping:"+url

