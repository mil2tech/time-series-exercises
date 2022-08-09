import pandas as pd

import requests

def get_items():

    import pandas as pd

    import requests

    # setup
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/items'
    items = []
    while True:

        url = domain + endpoint

        response = requests.get(url)
        data = response.json()
        print(f'\r {data["payload"]["page"]} of {data["payload"]["max_page"]}: {url}', end='')
        items.extend(data['payload']['items'])
        endpoint = data['payload']['next_page']
        if endpoint is None:
            break
    items = pd.DataFrame(items)
    return items

def get_store_data():
    import pandas as pd
    import requests
    # setup
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/stores'
    # For each page -- until next page is None
    url = domain + endpoint
    response = requests.get(url)
    data = response.json()
    stores = pd.DataFrame(data['payload']['stores'])
    stores = pd.DataFrame(stores)
    return stores