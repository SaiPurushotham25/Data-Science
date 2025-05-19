import requests

def fetch_astrology_data(dob: str, tob: str, pob: str):
    api_url = "https://freeastrologyapi.com/api/birth-chart"
    headers = {
        "Authorization": "KaPcL8h43X8CPVsZyMsaT4lySDIHa9Mp6gyPpLCI"
    }
    params = {
        "date_of_birth": dob,
        "time_of_birth": tob,
        "place_of_birth": pob
    }
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        # Extract necessary information from the response
        return {
            "Sun": data["sun_sign"],
            "Moon": data["moon_sign"],
            "Ascendant": data["ascendant"]
        }
    else:
        # Handle errors appropriately
        return {
            "Sun": "Unknown",
            "Moon": "Unknown",
            "Ascendant": "Unknown"
        }
