from phi.agent import Agent 
from dotenv import load_dotenv 
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools 
from phi.tools.duckduckgo import DuckDuckGo 

load_dotenv()

web_agent=Agent(
    name="web agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["always include sources"],
    # show_tool_calls=True,
    markdown=True

    )

# q="who is president of usa in 2025 ?"
q="what is current price of dollar against egyption pound?"

# web_agent.print_response(q) 


finance_agent=Agent(
    name="finance agent",
    role="get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,company_info=True)],
    instructions=["use tables to show data"],
    # show_tool_calls=True,
    markdown=True

    )
# q="what is current price of dollar against egyption pound?"
q="what is current price of google stock ?"
# finance_agent.print_response(q) 

team_agent=Agent(
    name="team agent",
    team=[finance_agent,web_agent],
    # role="get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    # tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,company_info=True)],
    instructions=["use tables to show data"],
    # show_tool_calls=True,
    markdown=True

    )
q="what is current price of egytpion pound against usa dollar ?"

team_agent.print_response(q,stream=True)