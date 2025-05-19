 Astrology Chatbot
An AI-powered astrology chatbot that provides personalized astrological insights based on your birth details. Built with Python, Streamlit, and integrates with the FreeAstrologyAPI to deliver real-time astrological readings.

✨ Features
Personalized Readings: Enter your date, time, and place of birth to receive customized astrological insights.

Interactive Chat Interface: Engage with the chatbot through a user-friendly Streamlit interface.

Real-time API Integration: Fetches astrological data dynamically using the FreeAstrologyAPI.

Modular Architecture: Clean separation between frontend and backend for maintainability.


🗂️ Project Structure

Astrology_Chatbot/

├── Backend/

│   ├── app/

│   │   ├── api/

│   │   │   └── endpoints.py

│   │   ├── core/

│   │   │   └── astro.py

│   │   ├── Database/

│   │   │   └── storage.py

│   │   └── models/

│   │       └── user.py
│   └── main.py

├── Frontend/

│   └── app.py

└── requirements.txt

🛠️ Installation

1. Clone the Repository
git clone https://github.com/SaiPurushotham25/Data-Science.git
cd Data-Science/Astrology_Chatbot

2.Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install Dependencies
Install Dependencies

4. Set Up Environment Variables
ASTROLOGY_API_KEY=your_api_key_here
OPENROUTER_API_KEY=your_api_key_here

Usage
1.Start the Backend Server

Navigate to the Backend/ directory and run:
uvicorn main:app --reload

2.Launch the Frontend Interface

Open a new terminal, navigate to the Frontend/ directory, and run:
streamlit run app.py

This will open the Streamlit app in your default web browser.

3.Interact with the Chatbot

Enter your Date of Birth (DOB), Time of Birth (TOB), and Place of Birth (POB).

Type your question in the input field.

Click the ASK button to receive your personalized astrological reading.

Example:
Input:
DOB: 2002-04-25
TOB: 21:10
POB: Visakhapatnam, India
Question: Tell me about my life

 Dependencies
Python 3.10

Streamlit

FastAPI

Requests

Uvicorn

License
This project is licensed under the MIT License.

Acknowledgments
FreeAstrologyAPI for providing the astrological data.

Streamlit for the interactive frontend framework.

FastAPI for the backend API development.
