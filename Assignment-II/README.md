# get_Journal - Journal Classification using Jac and Gemini API

## Overview

This project demonstrates classifying a research title into a journal subject area using a combination of:

- Jac language walker (`get_Journal.jac`) that interacts with the Gemini Large Language Model (LLM) via the ByLLM interface.
- Python runner script (`get-journal.py`) that loads environment variables, gets user input, and invokes Jac functions.

The Jac code encapsulates the AI logic, while Python handles environment setup, user interaction, and integration.

## Files

### get_Journal.jac

- Defines the `get_Journal` function which uses the Gemini LLM to classify a given research title.
- Uses the `byllm` Model interface to access Gemini.
- Returns the journal classification as an enum type.

### get-journal.py


- Captures user input for the research title.
- Calls the Jac `get_Journal` function with the user input.
- Prints out the classification result.

## Setup

1. Install dependencies:

pip install jaclang python-dotenv

text

2. Obtain an API key for Google's Gemini generative language from the Elsevier/Google Developer Portal.

3. Create a `.env` file named `api-key.env` with:

4. Compile the Jac source (`get_Journal.jac`) with `jaclang` to generate the Python module accessible by the runner script.

## Usage

Run the Python runner:

python3 get-journal.py


You will be prompted to enter a research title. The script will output the best journal classification based on the Gemini LLM inference in Jac.


