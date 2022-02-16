from bs4 import BeautifulSoup
import requests

def get_links(table_tag):
    links = []

    for row_data in table_tag.select("tr"):
        link_tag = row_data.find('a', href=True)

        if(link_tag == None):
            continue

        links.append('https://www.mapa.gob.es/app/consultafertilizante/' + link_tag.get('href'))  

    return links  


def get_products(url):
    page = requests.get(url)
    page.encoding='utf-8'
    pagetext = page.text
    tree = BeautifulSoup(pagetext, features="lxml")

    table_tag = tree.select("table")[1]
    links = get_links(table_tag)
    tab_data = [[item.text for item in row_data.select("th,td")]
                for row_data in table_tag.select("tr")]

    data = tab_data[2::]

    for i in range(0,len(data)):
        data[i].append(links[i])

    return data


def get_composition(components, equivalencies, url):
    page = requests.get(url)
    page.encoding='utf-8'
    pagetext = page.text

    tree = BeautifulSoup(pagetext, features="lxml")
    if(len(tree.select("table"))>2):
        table_tag = tree.select("table")[3]
        tab_data = [[item.text for item in row_data.select("th,td")]
                        for row_data in table_tag.select("tr")]

        composition = ''
        for e in tab_data:
            if(e[0] in components and e[1] != '-'):
                if e[0] in equivalencies.keys():
                    composition += e[1] +'% ' + equivalencies[e[0]] + '; '
                else: 
                    composition += e[1] +'% ' + e[0] + '; '

        return composition[0:-2]
    else:
        return None