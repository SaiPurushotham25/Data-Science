🤖 CREW AI – Multi-Agent Collaboration Framework

This project showcases a multi-agent system built using the CrewAI framework, designed to automate blog content creation. It features two specialized agents:
DEV Community

Senior Blog Researcher Agent: Utilizes the YoutubeChannelSearchTool to gather relevant information from YouTube based on a given topic.

Senior Blog Writer Agent: Generates comprehensive blog content using insights provided by the researcher agent.

The system leverages Google's Gemini-1.5-flash model for natural language processing tasks.

📁 Project Structure

CREW AI/
├── agents.py       # Defines the agents and orchestrates the workflow

├── crew.py         # Sets up the CrewAI environment

├── tasks.py        # Specifies tasks assigned to each agent

├── tools.py        # Implements tools like YoutubeChannelSearchTool

├── requirements.txt# Lists project dependencies

└── README.md       # Project documentation

🧰 Tech Stack
CrewAI: Framework for building collaborative AI agents.

CrewAI Tools: Provides tools like YoutubeChannelSearchTool.

LangChain Google GenAI: Integrates Google's Gemini models.

Python Dotenv: Manages environment variables.

🔧 Installation & Setup

1.Clone the Repository:

git clone https://github.com/SaiPurushotham25/Data-Science.git

cd Data-Science/Agentic\ AI/CREW\ AI

2.Create a Virtual Environment:

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install Dependencies:

pip install -r requirements.txt

4.Set Up Environment Variables:

Create a .env file in the project root directory and add your Google API key:

GOOGLE_API_KEY=your_google_api_key_here

🚀 Usage
1.Run the Agents:
python agents.py

2.Provide a Topic:

When prompted, enter a topic for the blog. The researcher agent will fetch relevant information from YouTube, and the writer agent will generate the blog content based on the gathered insights.

📝 Example

Input:
Enter the blog topic: Artificial Intelligence in Healthcare

Output:
[Researcher Agent]: Fetched top 5 YouTube videos related to 'Artificial Intelligence in Healthcare'.
[Writer Agent]: Generated a comprehensive blog post based on the research.

📌 Notes
Ensure your Google API key has access to the Gemini models.

The YoutubeChannelSearchTool requires proper configuration to fetch data effectively.

Customize the agents' roles and tasks in agents.py and tasks.py as needed.

🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

📄 License
This project is licensed under the MIT License.

📬 Contact
For any questions or feedback, please reach out to Sai Purushotham.

