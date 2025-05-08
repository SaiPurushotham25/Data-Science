from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

import os
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))



#creatr a senior blog content reseacher
blog_researcher=Agent(
    role='Blog Researcher from youtube videos',
    goal='get the relevant video transcript for the topic {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning and GEN AI and providing suggestion"
        
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
    
)

# creating a senior blog writer agent with YT Tool
blog_writer=Agent(
    role="Blog writer",
    goal="Narrate compelling tech stories about the video {topic} from the YT video",
    verbose=True,
    memory=True,
    backstory=(
        "with a flair for simplying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)