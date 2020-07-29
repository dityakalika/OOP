import requests
from bs4 import BeautifulSoup

url = 'https://www.detik.com/'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print('success! Response =', response.status_code)
        print('Content', response.text)
        soup = BeautifulSoup(response.text, features="html.parser")
        print('\nHasil pemanggilan', url)
        print('Title dari url',soup.title)
        # karena kita mau judul yang lebih bersih dari lambang2 aneh ketik dengan '.string'
        print('Title dari url', soup.title.string)
    else:
        print('Woops, ada kesalahan requests', response.status_code)
except Exception as e:
    print('There is an error', e)
print('Program ended')