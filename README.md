# Eigene-Werke-NFDI
## Zotero4NFDI: Cooperation between NFDI4Ing and Text+ 
### Scripts for reading individual or all publications from a Zotero library

Contact persons NFDI4Ing: Zeynep Dirier (https://orcid.org/0009-0000-4816-3771) 
& Évariste Demandt (https://orcid.org/0000-0002-5705-0071)

Contact persons Text+: Annica Skupch (https://orcid.org/0009-0005-9075-255X) & Thorsten Trippel (https://orcid.org/0000-0002-7211-7393)

Library NFDI4Ing: https://www.zotero.org/groups/5133250/bibliothek_nfdi4ing/library 

Library Text+: https://www.zotero.org/groups/4533881/textplus/library

Library NFDI: https://www.zotero.org/groups/5266641/nfdi-bibliografie/library 

NFDI4Ing and Text+ are two consortia of the National Research Data Infrastructure (NFDI), each systematically recording the metadata of their publications in their own Zotero bibliographies. Additionally, efforts are underway to compile the publications of all 26 consortia in an - as yet incomplete - "NFDI library". For internal and external reporting, NFDI4Ing and Text+ have written Python scripts to automatically read and process the metadata of their publications. The scripts, together with the data from NFDI4Ing read out on a key date, are available https://zenodo.org/records/12680673 (DOI: 10.5281/zenodo.12680673) and from Text+ at https://zenodo.org/records/12605448 (DOI: 10.5281/zenodo.12605448). All scripts are published under the CC BY 4.0 license, and reuse is expressly encouraged!

Background to the NFDI4Ing library: On September 29, 2023, the NFDI4Ing consortium submitted an interim report for the first funding period. The NFDI4Ing library was created in advance for the purpose of automated literature management for the interim report. The first Python script from NFDI4Ing reads a subfolder of the library for demonstration purposes and also exports tags and notes. The second Python script reads all publications of the - so far incomplete - "Library NFDI" and exports tags.

Background to the Text+ library: In June 2024, the National Research Data Infrastructure conducted a comprehensive structural evaluation. As part of this evaluation, all consortia were asked to submit a list of all publications published since their foundation. The script focuses exclusively on the publications and exports tags, without reading notes or attachments.


This repository contains code and resources for the Eigene Werke NFDI project. The following instructions will help you get started with running the code in this repository.

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Running the Code](#running-the-code)
4. [Usage](#usage)
5. [Acknowledgements](#acknowledgements)


## Requirements

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.8 or later.
- You have a Unix-based system (Linux or macOS) or Windows.
- You have installed `pip` (Python package installer).

## Installation

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```sh
   git clone https://github.com/zeynepdirier/Eigene-Werke-NFDI.git
   cd Eigene-Werke-NFDI
   ```
2. **Create a Virtual Environment**

  It is recommended to create a virtual environment to manage dependencies. Run the following commands:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Running the code

1. **Configuration** 

   Ensure that any necessary configuration files or environment variables are set up as required by the project. This information can typically be found in the documentation or comments within the code.

2. **Run the Main Script**

   To start the main script, use the following command:
   ```sh
   python <filename>.py
   ```
   Replace <filename>.py with the name of the script you intend to run.

## **Usage**
   Provide a brief overview of how to use the code or any specific commands or options that need to be passed.
   For example:

   ```sh
   python <filename>.py --input data/input_file.csv --output results/output_file.csv
   ```
   Explain any significant parameters or configuration options here.

## **Acknowledgements**
   The authors would like to thank the Federal Government and the Heads of Government of the Länder, as well as the Joint Science Conference (GWK), for their funding and support within the framework of the NFDI4Ing consortium. Funded by the German Research Foundation (DFG) – 442146713.


