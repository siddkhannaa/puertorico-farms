import matplotlib.pyplot as plt
import csv
from urllib.request import urlopen

from config import api_key

base_url = f'http://quickstats.nass.usda.gov/api/api_GET/?key={api_key}&'
out = '../out/'

def get_data(params, fn):
    # API GET with parameters
    # output in csv

    url = f'{base_url}{params}'
    result = urlopen(url)
    text = result.read().decode('utf-8')
    file_name = f'{out}{fn}.csv'
    
    fv = open(file_name, 'w', encoding='utf-8')
    fv.write(text)
    fv.close()

def graph_data(fv):
    x = []
    y = []

    with open(fv, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            x.append(row[0])
            y.append(row[1])

    plt.plot(x,y,color='g', marker='o', label='nass data')
    plt.xlabel('x axis data')
    plt.ylabel('y axis data')
    plt.title('nass data')
    plt.grid()
    plt.legend()
    plt.show()