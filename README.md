# robo-advisor

Issues requests to the [AlphaVantage Stock Market API](https://www.alphavantage.co/) in order to provide automated stock or cryptocurrency trading recommendations.

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Fork this repository under your own control, then clone or download the resulting repository onto your computer. Then navigate there from the command line:

After cloning the repo, navigate there from the command-line:

cd ~/Desktop/robo-advisor


#Environment Setup
Create and activate a new Anaconda virtual environment:

conda create -n stocks-env python=3.7 # (first time only)

conda activate stocks-env

From within the virtual environment, install the required packages specified in the "requirements.txt":

pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)

#Alphavantage

Your program will need an API Key to issue requests to the AlphaVantage API. 

go to "GET YOUR FREE API KEY TODAY"

https://www.alphavantage.co/


#Security Requirements

The program's source code should absolutely not include the secret API Key value. To not include the API key:

Create a file called ".env" and place the environment variable in the ".env" file

Set an environment variable called ALPHAVANTAGE_API_KEY:

ALPHAVANTAGE_API_KEY="abc123"

The local ".gitignore" file prevents the ".env" file and its contents from being tracked


## Usage

from the command-line:

python app/robo_advisor.py