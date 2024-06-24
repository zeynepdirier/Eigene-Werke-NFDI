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
library_id = LIBRARY_ID   # Unique identifier for the Zotero library
library_type = 'group'   # Type of the Zotero library (can be 'user' or 'group')
api_key = API_KEY # API key for accessing Zotero API

# Initialize Zotero client
zot = zotero.Zotero(library_id, library_type, api_key)  # Creates an instance of Zotero library to interact with the Zotero API

# Initialize an empty list to store items
items = []

# Pagination variables
start = 0  # Starting index for pagination
limit = 9999  # Maximum number of items to retrieve per request

# Retrieve items from the specified collection
while True:
    page_items = zot.items(start=start, limit=limit)  # Fetch items from Zotero
    
    if not page_items:  # Break the loop if no more items are returned
        break
    
    items.extend(page_items)  # Extend the items list with the retrieved page of items
    start += len(page_items)  # Update the starting index for the next page

# Initialize an empty list to store publication information
publications = [] 

# Iterate through each item to extract relevant publication information
for pub_item in items:
    author_names = []  # Initialize an empty list to store author names
    # Check if 'creators' key exists in item data
    if 'creators' in pub_item['data']:
        for creator in pub_item['data']['creators']:
            # Check if 'firstName' and 'lastName' keys exist in creator
            if all(key in creator for key in ['firstName', 'lastName']):
                name = creator['firstName'] + ' ' + creator['lastName']  # Concatenate first and last names
                author_names.append(name)  # Append the full name to the author_names list

    # Check if all required keys exist in item data
    if all(key in pub_item['data'] for key in ['title', 'date', 'tags','itemType']):
        # Create a dictionary with publication details
        pub_dict = {
            'Authors': ', '.join(author_names),  # Convert author names list to a comma-separated string
            'Title': pub_item['data']['title'],
            'Date': pub_item['data']['date'],
            'ID': '',
            'Konsortium': '',
            'Publication Type': pub_item['data']['itemType'],
            'Quelle': '',
            'Duplikat / Preprint': ''
        }
        publications.append(pub_dict)  # Add the publication dictionary to the publications list

        # Iterate through tags to extract additional information
        for t in pub_item['data']['tags']:
            if t['tag'].startswith('Konsortium'):
                pub_dict['Konsortium'] = t['tag']  

            if t['tag'].startswith('Quelle'):
                pub_dict['Quelle'] = t['tag']
        
            if t['tag'] == 'Duplikat / Preprint':
                pub_dict['Duplikat / Preprint'] = 'ja'  # Set 'Duplikat / Preprint' flag
    # Check if the publication has a 'DOI' property
    # This check is performed only for publications that are not categorized as 'software'
    if 'DOI' in pub_item['data']:
        # If the publication has a 'DOI' property, set the 'ID' key to the 'DOI' value
        pub_dict['ID'] = pub_item['data']['DOI']
    else:
        # If the publication does not have a 'DOI' property, set the 'ID' key to the 'extra' value
        pub_dict['ID'] = pub_item['data']['extra']


# Define field names for CSV output
fieldnames = ['Authors', 'Title', 'ID', 'Date', 'Konsortium', 'Publication Type', 'Quelle', 'Duplikat / Preprint'] 

# Write publication information to a CSV file
with open('EigeneWerkeKonsortienNFDI.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', extrasaction='ignore')
    writer.writeheader()  # Write column headers to the CSV file
    for pub in publications:
        writer.writerow(pub)  # Write each publication to the CSV file

# Read the CSV file into a DataFrame
df = pd.read_csv('EigeneWerkeKonsortienNFDI.csv', delimiter=';')  

# Write the DataFrame to an Excel file
df.to_excel('EigeneWerkeKonsortienNFDI.xlsx', index=False, engine='openpyxl')  # Export DataFrame to Excel without row indices
