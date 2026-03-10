# ROOT Sustainability audit

ROOT is a Data analysis platform generally used in high energy physics but it's capabalities can also be used to analyse genomic sequence data.
RAMtools are a set of root macros that facilitates the use of ROOT for genomic data.

In the sustainabilty audit of root. I tried simulating a very small genomic analysis workflow with very small data , If you have a high end laptop or workstation grade computing device you can use data of larger sizes for better accuraccy and analysis.

## How to setup environment

Requirements :

Hardware :
This analysis can only be reproduced in Ubuntu 22 , 24 , 25 and MacOS systems for now.

Requirements for using RAMtools

- git
- ROOT 6.26+
- C++17 compatible compiler
- CMake 3.16+

Requirements for this audit

- Python 3.10+
- pip
- Codecarbon (installed in the active venv)

STEPS:

1. Install git if you do not already have it

2. Clone this repository and move into it:

    Open a terminal and run :

    ```bash
    git clone https://github.com/neo-0007/root-sustainability-audit.git
    cd root-sustainabilty-audit
    ```

3. I have created a bash script for easy installation of all the requriements necessary :

    I was able to test this script in Ubuntu 24.04 and Ubuntu 22.04 but it should work for Ubuntu 25.04
    For MacOS this script downloaded root 6.38 which fails building RAMtools. If you are using MacOS you should install root 6.36  from [here](https://root.cern/releases/release-63600/) following [these instructions](https://root.cern/install/). For MacOS the setup script will install other deps

    Make the setup script executable and run it :

    ```bash
        chmod +x setup.sh
        ./setup.sh
    ```

    This step will take some time depending on your system and internet connection

4. Create a python venv and activate it :

    ```bash
        python -m venv .venv
        source .venv/bin/activate
    ```

5. Install all python dependencies

    ```bash
        pip install -r requirements.txt
    ```

## How to run the analysis

1. Run the analyzer

    ```bash
        python analyzer.py
    ```

2. You will be prompted to enter a download link
    - Open the dataset_links.txt in the repository and copy a link for a data you want the analyzer to run on.
    - Preferably run the analyzer on all the files one by one
    - The energy usage data will be printed in the terminal after each run
    - Note them down for analysis

3. If you want to do a detailed analysis of the data you obtained from the audit follow the steps from [this doc](https://docs.google.com/document/d/1t0w1LUO2Bi1DVWr4mBfoWkihPA2nINWpOd1UYPgIi9c/edit?usp=sharing)
