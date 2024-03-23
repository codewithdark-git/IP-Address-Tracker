import streamlit as st
import pandas as pd
import requests
import pydeck as pdk

def get_geo_data(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            st.error(f"Failed to fetch location data: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error fetching location data: {e}")
        return None


# Streamlit app
def main():
    # Create an expander to contain the description in the second column
    with st.expander("Description"):
        st.markdown("""
                    
                    The IP Address Tracker is a user-friendly web application designed to help users track the geographical location of any IP address. Whether you're curious about the origin of a specific IP address or need to identify the location of a particular device, this app provides a simple and intuitive solution.

                    With just a few clicks, users can input an IP address into the app, and it will quickly retrieve detailed location information, including the country, region, city, latitude, longitude, and postal code associated with that IP address. The app utilizes the reliable [ipinfo.io](https://ipinfo.io/) API to fetch accurate and up-to-date location data.

                    One of the key features of this app is its interactive map visualization, powered by Google Maps. Users can see the exact location of the IP address pinpointed on the map, making it easy to visualize its geographical context. Custom marker designs are used to enhance the visualization and provide an aesthetically pleasing experience.

                    Whether you're a network administrator, cybersecurity enthusiast, or simply curious about the locations behind various IP addresses, the IP Address Tracker app is an invaluable tool that streamlines the process of IP address geolocation.  start Me on [Github](https://github.com/codewithdark-git)
                """)

    st.title("IP Address Tracker")

    ip_address = st.text_input("Enter IP Address:")
    if st.button("Get Location"):
        geo_data = get_geo_data(ip_address)
        if geo_data:

            st.write(f"Country: {geo_data.get('country')}")
            st.write(f"Region: {geo_data.get('region')}")
            st.write(f"City: {geo_data.get('city')}")
            st.write(f"Postal Code: {geo_data.get('postal')}")

            # Create a DataFrame with latitude and longitude columns
            df = pd.DataFrame({'latitude': [float(geo_data.get('loc').split(',')[0])],
                               'longitude': [float(geo_data.get('loc').split(',')[1])]})

            # Show the location on a Google Map with custom marker designs
            st.pydeck_chart(pdk.Deck(
                map_style='mapbox://styles/mapbox/streets-v11',
                initial_view_state=pdk.ViewState(
                    latitude=float(geo_data.get('loc').split(',')[0]),
                    longitude=float(geo_data.get('loc').split(',')[1]),
                    zoom=10,
                    pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        'ScatterplotLayer',
                        data=df,
                        get_position='[longitude, latitude]',
                        get_radius=200,
                        get_fill_color=[255, 0, 0],  # Dot color (red)
                        get_icon='https://img.icons8.com/color/48/000000/marker--v1.png',  # Custom icon
                        pickable=True,
                    ),
                ],
            ))
        else:
            st.error("Location not found for the provided IP.")


if __name__ == "__main__":
    main()
