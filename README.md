# Ice-Cafe

## Overview

This application manages an ice cream parlor's seasonal flavor offerings, ingredient inventory, customer flavor suggestions, and allergy concerns. Users can maintain a cart of their favorite products, search and filter offerings, and add allergens if they don’t already exist.

## How to Run

### Prerequisites
- Python 3.10+
- SQLite

### Create the database
First, make sure to create the database and tables by running the following command:
```sh
python app/models.py
```

### Run the application
1. To run the Streamlit application locally:
   Run the following in terminal.
   ```sh
   streamlit run run.py
   ```

2. You can also run the application using Docker.

   Build the Docker image:
   ```sh
   docker build -t ice-cream-parlor .
   ```
   Run the Docker container:
   ```sh
   docker run -it -p 8501:8501 ice-cream-parlor
   ```



