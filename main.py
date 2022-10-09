import os
import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, url):
    original_link = {"long_url": url}
    headers = {'Authorization': f'Bearer {token}'}
    bitly_url = 'https://api-ssl.bitly.com/v4/shorten'
    new_link = requests.post(bitly_url, json=original_link, headers=headers)
    new_link.raise_for_status()
    return new_link.json()['link']


def count_clicks(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    bitlink = urlparse(url)
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink.netloc}{bitlink.path}/clicks/summary'
    response = requests.get(bitly_url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(bitly_token, url):
    headers = {'Authorization': f'Bearer {bitly_token}'}
    bitlink = urlparse(url)
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink.netloc}{bitlink.path}'
    response = requests.get(bitly_url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Введите ссылку: ')
    args = parser.parse_args()
    url = args.url
 
    try:
        if is_bitlink(bitly_token, url):
            total_clicks = count_clicks(bitly_token, url)
            print(f'Общее количество кликов : {total_clicks}')
        else:
            bitlink = shorten_link(bitly_token, url)
            print(bitlink)
    except requests.HTTPError:
        print("Вы ввели неправильную ссылку")


if __name__ == '__main__':
    main()
