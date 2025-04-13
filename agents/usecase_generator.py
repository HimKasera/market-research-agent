from crewai import Agent

usecase_agent = Agent(
    role="AI Use Case Strategist",
    goal="Generate AI/GenAI use cases aligned with the company’s domain and trends",
    backstory="Specialist in converting market insights into real-world AI solutions.",
    verbose=True
)
