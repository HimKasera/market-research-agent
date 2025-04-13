from langchain.tools.base import BaseTool
from dotenv import load_dotenv
from typing import Type
import os
import requests

load_dotenv()

class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = "Search the web using Serper API for industry/company data."

    def _run(self, query: str) -> str:
        api_key = os.getenv("SERPER_API_KEY")
        if not api_key:
            return "❌ SERPER_API_KEY not found in environment."

        url = "https://google.serper.dev/search"
        headers = {"X-API-KEY": api_key}
        data = {"q": query}

        try:
            res = requests.post(url, headers=headers, json=data)
            res.raise_for_status()
            results = res.json()
            if "organic" in results:
                return "\n".join([f"- {r['title']}: {r['link']}" for r in results["organic"][:5]])
            return str(results)
        except Exception as e:
            return f"❌ Request failed: {e}"

    def _arun(self, query: str):
        raise NotImplementedError("Async method not implemented.")
