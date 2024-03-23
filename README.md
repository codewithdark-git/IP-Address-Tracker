# IP Address Tracker

## Overview
This is a simple Streamlit web application that allows users to track the geographical location of an IP address. It retrieves location data using the [ipinfo.io](https://ipinfo.io/) API and visualizes the location on a map.

## Features
- Users can input an IP address and retrieve its geographical location information.
- The app displays the IP address, country, region, city, latitude, longitude, and postal code of the provided IP address.
- It visualizes the location on a Google Map using custom marker designs.

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/codewithdark-git/ip-address-tracker.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
4. Access the app in your web browser at `http://localhost:8501`.

## Dependencies
- Streamlit
- Requests
- Pandas
- Pydeck

## Credits
- This app was created by [Your Name].

## License
This project is licensed under the [MIT License](LICENSE).
