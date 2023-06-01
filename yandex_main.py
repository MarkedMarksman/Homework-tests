import requests

def add_directory_to_yandex_disk(directory, ya_token, yandex_api_url):
    headers = {
        'accept': 'application/json',
        'authorization': f'OAuth {ya_token}'
    }
    r = requests.put(yandex_api_url + "v1/disk/resources",
                    params={'path': directory},
                    headers=headers)


    return r.status_code
