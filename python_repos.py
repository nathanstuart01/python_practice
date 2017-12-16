import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

#store API response in a variable
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

#PRocess the results
print(response_dict.keys())

#Expolre information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

#Examin the first repository
repo_dict = repo_dicts[0]
print(repo_dict)
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
	print('Name:', repo_dict['name'])
	print('Owner:', repo_dict['owner']['login'])
	description = repo_dict['description']
	print('Description:', str(description).encode('utf-8'))
