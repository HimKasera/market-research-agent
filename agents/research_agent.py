from crewai import Agent
from tools.web_search_tool import WebSearchTool

research_agent = Agent(
    role="Industry Research Expert",
    goal="Understand the company's industry, segment, products, and priorities",
    backstory="Expert analyst skilled in market trends and AI transformation.",
    tools=[WebSearchTool()],  # ✅ Now it's an instance of a valid BaseTool
    verbose=True
)
