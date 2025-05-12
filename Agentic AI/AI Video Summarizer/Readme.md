🎬 AI Video Summarizer Agent
An interactive AI-powered application that analyzes video content and provides detailed summaries or answers to user queries. Built using Streamlit, Phidata's Agentic AI framework, and Google's Gemini 2.0 Flash experimental model, this tool offers a seamless experience for extracting insights from videos.

🚀 Features
Video Summarization: Upload a video file and receive a comprehensive summary of its content.

Query-Based Insights: Pose specific questions about the video, and the AI agent will provide detailed answers.

Web Search Integration: Enhances responses by fetching supplementary information from the web using DuckDuckGo.

Interactive Interface: User-friendly Streamlit interface for easy interaction.


🧰 Tech Stack
Frontend: Streamlit for building the web interface.

AI Framework: Phidata for creating the Agentic AI agent.

Language Model: Google Gemini 2.0 Flash experimental model.

Web Search Tool: DuckDuckGo for fetching additional context.

Environment Management: python-dotenv for handling environment variables.


📦 Installation
Clone the Repository:
bash
Copy
Edit
git clone https://github.com/SaiPurushotham25/Data-Science.git 

cd Data-Science/Agentic\ AI/AI\ Video\ Summarizer

Create a Virtual Environment:

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Set Up Environment Variables:

Create a .env file in the project root directory and add your Google API key:

GOOGLE_API_KEY=your_google_api_key_here

🧪 Usage

Run the Application:
streamlit run app.py

Interact with the Application:

Open the provided local URL in your browser.

Upload a video file (.mp4, .mov, or .avi).

Enter your query or request a summary in the text area.

Click on the "Analyze Video" button to receive insights.




📝 Example
After uploading a video and entering a query like:

"Summarize the key points discussed in this lecture."

The AI agent will process the video and provide a detailed summary, incorporating additional context from web searches if necessary.


📁 Project Structure

AI Video Summarizer/

├── app.py

├── requirements.txt

├── .env

└── README.md

🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.


📄 License
This project is licensed under the MIT License.

📬 Contact
For any questions or feedback, please reach out to Sai Purushotham.

Note: Ensure you have the necessary API keys and permissions to use Google's Gemini model and DuckDuckGo's search functionalities.
