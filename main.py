from crewai import Task, Crew
from agents.research_agent import research_agent
from agents.usecase_generator import usecase_agent
from agents.resource_collector import resource_agent

company_name = "Ford Motors"

task1 = Task(
    description=f"Research and summarize the industry Ford operates in, its key products, and AI transformation trends.",
    expected_output="Bullet-point summary of Ford's industry, products, and operational focus.",
    agent=research_agent
)

task2 = Task(
    description="Generate at least 5 practical GenAI/LLM/ML use cases for the company, referencing trends and improvements in customer service, operations, or supply chain.",
    expected_output="Markdown table of use cases with goal, tech stack, benefit.",
    agent=usecase_agent
)

task3 = Task(
    description="Search Kaggle, HuggingFace, and GitHub for datasets, repos or tools that align with the above use cases.",
    expected_output="List of 5–10 datasets or repos with clickable links.",
    agent=resource_agent
)

crew = Crew(
    tasks=[task1, task2, task3],
    agents=[research_agent, usecase_agent, resource_agent],
    verbose=True
)

result = crew.run()
with open("outputs/use_case_proposal.md", "w") as f:
    f.write(result)
