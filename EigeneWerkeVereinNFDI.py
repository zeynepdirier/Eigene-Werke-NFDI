# Import necessary libraries
from pyzotero import zotero
import re
import numpy as np 
import csv
import pandas as pd
from openpyxl import Workbook
from openpyxl import load_workbook
import os

# Define Zotero library details
library_id = LIBRARY_ID
library_type = 'group'
api_key = API_KEY

# Initialize Zotero client
zot = zotero.Zotero(library_id, library_type, api_key)

# Define the collection key to retrieve items from
collection_key = COLLECTION_KEY

# Initialize an empty list to store items
items = []

# Pagination variables
start = 0
limit = 9999

# Retrieve items from the specified collection
while True:
    page_items = zot.collection_items(collection_key, start=start, limit=limit)
    
    # Break the loop if no more items are returned
    if not page_items:  
        break
    
    # Extend the items list with the retrieved page of items
    items.extend(page_items)
    start += len(page_items)

# Initialize an empty list to store publication information
publications = [] 

# Iterate through each item to extract relevant publication information
for pub_item in items:

    first_author = pub_item['data']['creators'][0]['lastName'] if 'creators' in pub_item['data'] and pub_item['data']['creators'][0] else ''

    if all(key in pub_item['data'] for key in ['title', 'url', 'date','tags']):
        # Extract relevant data and create a dictionary
        pub_dict = {
            'Author':first_author,
            'Key': pub_item['data']['key'],
            'Title': pub_item['data']['title'],
            'Url': pub_item['data']['url'],
            'Date': pub_item['data']['date'],
            'Language': '',
            'Section': pub_item['data']['tags'][0]['tag'],
            'Notes': []  # Placeholder for notes
        }
        # Append the dictionary to the list of publications
        publications.append(pub_dict)

    # This check is performed only for publications that are not categorized as 'software'   
    if ('language' in pub_item['data']):
        pub_dict['Language'] = pub_item['data']['language']
# Iterate through each item to extract and associate notes with their parent publications
for note_item in items:
    if note_item['data']['itemType'] == 'note':
        # Extract note content
        note_content = note_item['data']['note']
       
        # Remove unnecessary characters from note content
        to_remove = ['data-schema-version="8"', '<', 'p', '\\', '>', '/', 'div']
        for c in to_remove:
            note_content = note_content.replace(c, "").strip()

        # Extract parent item key
        parent_key = note_item['data']['parentItem']
        
        # Associate note with its parent publication
        for p in publications:
            if p['Key'] == parent_key:
                p['Notes'].append(note_content)

# Define fieldnames for CSV writing
fieldnames = ['Author', 'Title', 'Url', 'Date', 'Language', 'Notes', 'Section'] 

# Write publication information to a CSV file
with open('EigeneWerkeVereinNFDI.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', extrasaction='ignore')
    writer.writeheader()
    for pub in publications:
        # Convert notes list to comma-separated string
        pub['Notes'] = ', '.join(pub['Notes'])
        writer.writerow(pub)

# Read the CSV file into a DataFrame
df = pd.read_csv('EigeneWerkeVereinNFDI.csv', delimiter=';')  

# Write the DataFrame to an Excel file
df.to_excel('EigeneWerkeVereinNFDI.xlsx', index=False, engine='openpyxl')


