#!/usr/bin/python3


import requests

# *******  Program Requirements ****** #
# run sudo apt-get update
# sudo apt-get install python3-pip
# sudo apt-get install python3-requests or pip3 install requests

# Note: create a lists of wordpress sites in txt format e.g "urls.txt"
# Save the lists on the same directory as the python script, or in any folder -- make sure
# to ge the path of the  urls
# **************************************************** #


def check_wordpress_site(url):
	try:
		response = requests.get(url, timeout=10)
		if response.status_code == 200:
			if 'wp-content' in response.text or 'wp-includes' in response.text:
				return f"{url} is a wordpress site and is running."
			else:
				f"{url} is running but does not appear to be a WordPress site."
		else:
			return f"Failed to access {url}. Status code: {response.status_code}"
	except requests.exceptions.RequestException as e:
		return f"An error occured with {url} : {e}"

def check_wordpress_sites_from_list(file_path):
	with open(file_path, 'r') as file:
		urls = file.readlines()

	results = []
	for url in urls:
		url = url.strip()
		if url:
			result = check_wordpress_site(url)
			results.append(result)

if __name__ == "__main__":

	file_path = input("Enter the path to the file containing the list of URLS: ")
	results = check_wordpress_sites_from_list(file_path)
	for result in results:
		print(result)
