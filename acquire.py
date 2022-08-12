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
    
    # setup
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/stores'
    
    # For each page -- until next page is None
    url = domain + endpoint
    response = requests.get(url)
    data = response.json()
    stores = pd.DataFrame(data['payload']['stores'])
   
    return stores

def get_sales():
    # setup
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/sales'
    sales = []

    # For each page -- until next page is None
    url = domain + endpoint
    response = requests.get(url)
    data = response.json()
    while True:

            url = domain + endpoint

            response = requests.get(url)
            data = response.json()
            print(f'\r {data["payload"]["page"]} of {data["payload"]["max_page"]}: {url}', end='')
            sales.extend(data['payload']['sales'])
            endpoint = data['payload']['next_page']
            if endpoint is None:
                break
    sales = pd.DataFrame(sales)
    return sales


def sales_data_to_csv():
        def get_sales():
        # setup
            domain = 'https://python.zgulde.net'
            endpoint = '/api/v1/sales'
            sales = []

            # For each page -- until next page is None
            url = domain + endpoint
            response = requests.get(url)
            data = response.json()
            while True:

                    url = domain + endpoint

                    response = requests.get(url)
                    data = response.json()
                    print(f'\r {data["payload"]["page"]} of {data["payload"]["max_page"]}: {url}', end='')
                    sales.extend(data['payload']['sales'])
                    endpoint = data['payload']['next_page']
                    if endpoint is None:
                        break
            sales = pd.DataFrame(sales)
            return sales
        sales = get_sales()
        return sales.to_csv('sales.csv' , index=False)

def stores_data_to_csv():
    def get_store_data():
        
        # setup
        domain = 'https://python.zgulde.net'
        endpoint = '/api/v1/stores'
        
        # For each page -- until next page is None
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        stores = pd.DataFrame(data['payload']['stores'])
    
        return stores
    stores = get_store_data()
    return stores.to_csv('stores.csv' , index=False)

def items_data_to_csv():
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
    items = get_items()
    return  items.to_csv('items.csv' , index=False)

# function that merges tables together

def get_overall_sales_data():

    sales = get_sales()
    stores = get_store_data()
    items = get_items()

    #Left merge items onto sales
    overall_sales = sales.merge(items, how='left',left_on='item', right_on='item_id')
    #Left merge stores onto  dataframe
    overall_sales = overall_sales.merge(stores, how='left', left_on='store', right_on='store_id')
    #Drop unnecessary columns from my dataframe
    overall_sales.drop(columns=[ 'item',  'store_id'], inplace=True)
    # code to rearrange coluns
    overall_sales = overall_sales[['sale_date', 'sale_id', 'sale_amount',  'item_id','item_name', 'item_price', 'item_upc12', 'item_upc14', 'store', 'store_address', 'store_city', 'store_state', 'store_zipcode']]
    return overall_sales 
# Retrive data
def get_power():
    power_df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    return power_df


    