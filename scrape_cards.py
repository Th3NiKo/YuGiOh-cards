'''
Script for scraping both images of cards and infos
Save images in folder by convention ID.jpg
Save cards info as csv
'''

import os
import requests
import pandas as pd
from tqdm import tqdm

def scrape_cards():
    #Prepare requests and get total number of cards
    parameters = {'num': 100, 'offset': 0, 'view': 'List', 'misc': 'yes'}
    site_name = "https://db.ygoprodeck.com/api_internal/v7/cardinfo.php"
    req = requests.get(site_name, params=parameters)
    req.raise_for_status()
    total_cards = req.json()['meta']['total_rows']

    #Create pandas dataframe
    columns_names = ['Name', 'Desc', 'Type', 'Race', 'Archetype', 'Attribute', 'Atk', 'Def', 'Level']
    columns_names_lower = [x.lower() for x in columns_names]
    cards_database = pd.DataFrame(columns=columns_names)

    #Create folder for images
    if not os.path.exists('images'):
        os.makedirs('images')

    #Go through all pages
    for offset in tqdm(range(0, total_cards, 100)):
        parameters['offset'] = offset
        req = requests.get(site_name, params=parameters)
        req.raise_for_status()

        #Go through all cards in actual page
        actual_cards_json = req.json()['data']
        for actual_card in actual_cards_json:
            actual_card_id = actual_card['id']
            new_row = []

            #Gather columns, append None if not exists
            for single_column in columns_names_lower:
                if single_column in actual_card:
                    new_row.append(actual_card[single_column])
                else:
                    new_row.append(None)
            cards_database = cards_database.append(pd.DataFrame([new_row], columns=columns_names, index=[actual_card_id]))

            #Save image
            img_url = actual_card['card_images'][0]['image_url']
            img_req = requests.get(img_url, stream = True)
            img_req.raise_for_status()

            with open("images/" + str(actual_card_id) + ".jpg", 'wb') as f:
                f.write(img_req.content)
                
    cards_database.index.name = "Id"
    cards_database.to_csv("cards_database.csv")
        

def main():
    scrape_cards()

if __name__ == "__main__":
    main()

