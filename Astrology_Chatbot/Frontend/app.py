import streamlit as st
from datetime import date
import sys
import os

# Add Backend folder to sys.path so we can import from 'app' inside Backend
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Backend'))
sys.path.insert(0, backend_path)
from app.core.astro import fetch_astrology_data  # Your backend function

# The detailed fallback message for "Unknown" signs:
unknown_chart_message = """
A mystery!

While we don't have the exact details of your birth chart, I can still offer some general insights based on common astrological patterns that may apply to anyone with an Unknown Sun, Moon, and Ascendant (also known as the Rising Sign or Asc).

**The Missing Pieces**

In astrology, the missing Sun, Moon, and Ascendant can be seen as a metaphor for inner uncertainty, self-discovery, or even an opportunity for introspection. The Universe may be nudging you to explore your own inner world, values, and direction in life.

**A Bumpy but Thrilling Journey**

With an Unknown chart, you might be navigating an unconventional, unpredictable path. This can be both exciting and intimidating. You've likely experienced sudden twists and turns in your life, which have helped shape your resilience and adaptability. Keep in mind that your resourcefulness and ability to roll with the punches can be assets in times of uncertainty.


"""

st.title("Astrology Chatbot")

dob = st.date_input("Date of Birth", min_value=date(1950, 1, 1), max_value=date.today())
tob = st.text_input("Time of Birth (e.g., 10:30)")
pob = st.text_input("Place of Birth")
question = st.text_input("Your Question")

if st.button("ASK"):
    if dob and tob and pob and question:
        dob_str = dob.strftime("%Y-%m-%d")
        response = fetch_astrology_data(dob_str, tob, pob)

        sun = response.get("Sun", "Unknown")
        moon = response.get("Moon", "Unknown")
        asc = response.get("Ascendant", "Unknown")

        st.write("Sun Sign:", sun)
        st.write("Moon Sign:", moon)
        st.write("Ascendant:", asc)

        # If all are Unknown, show the detailed fallback message
        if sun == "Unknown" and moon == "Unknown" and asc == "Unknown":
            st.markdown(unknown_chart_message)
    else:
        st.warning("Please fill all fields before asking.")
