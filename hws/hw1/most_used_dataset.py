import sys
from bs4 import BeautifulSoup
import requests


# feel free to define other functions



def list_of_pairs(n):
    """ Get first n datasets

    Output: list of (dataset title, url)
    """
    ### Your coode here
    data = "https://catalog.data.gov/dataset?q=&sort=views_recent+desc"
    response = requests.get(data)
    
    soup = BeautifulSoup(response.text, "lxml")
    title = soup.find_all('h3', {"class":"dataset-heading"})

    links = [title[i].find('a') for i in range(len(title))]

    dataset_links = [link['href'] for link in links]
    for i in range(len(dataset_links)):
        dataset_links[i] = 'https://catalog.data.gov' + dataset_links[i]
    
    dataset_titles = [link.text for link in links]

    output = list(zip(dataset_titles, dataset_links))
    
    if n<=20:
        return output[:n]
    
    elif n<=40:
        data = "https://catalog.data.gov/dataset?q=&sort=views_recent+desc&page=2"
        response = requests.get(data)
        
        soup = BeautifulSoup(response.text, "lxml")
        title = soup.find_all('h3', {"class":"dataset-heading"})

        links = [title[i].find('a') for i in range(len(title))]

        dataset_links = [link['href'] for link in links]
        for i in range(len(dataset_links)):
            dataset_links[i] = 'https://catalog.data.gov' + dataset_links[i]
        
        dataset_titles = [link.text for link in links]

        output_two = list(zip(dataset_titles, dataset_links))
    
        output = output + output_two
        return output[:n]
    elif n<=50:
        data = "https://catalog.data.gov/dataset?q=&sort=views_recent+desc&page=2"
        response = requests.get(data)
        
        soup = BeautifulSoup(response.text, "lxml")
        title = soup.find_all('h3', {"class":"dataset-heading"})

        links = [title[i].find('a') for i in range(len(title))]

        dataset_links = [link['href'] for link in links]
        for i in range(len(dataset_links)):
            dataset_links[i] = 'https://catalog.data.gov' + dataset_links[i]
        
        dataset_titles = [link.text for link in links]

        output_two = list(zip(dataset_titles, dataset_links))
    
        output = output + output_two
        data = "https://catalog.data.gov/dataset?q=&sort=views_recent+desc&page=3"
        response = requests.get(data)
        
        soup = BeautifulSoup(response.text, "lxml")
        title = soup.find_all('h3', {"class":"dataset-heading"})

        links = [title[i].find('a') for i in range(len(title))]

        dataset_links = [link['href'] for link in links]
        for i in range(len(dataset_links)):
            dataset_links[i] = 'https://catalog.data.gov' + dataset_links[i]
        
        dataset_titles = [link.text for link in links]

        output_three = list(zip(dataset_titles, dataset_links))
    
        output = output + output_three
        return output[:n]
   











if __name__ == "__main__":
    n = int(sys.argv[1])
    pairs = list_of_pairs(n)
    for title, url in pairs:
        print(title, url)


