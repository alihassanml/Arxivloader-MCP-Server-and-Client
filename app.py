import streamlit as st
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import asyncio
from langchain_groq import ChatGroq

load_dotenv()

# Initialize the Groq model
model = ChatGroq(model="llama3-70b-8192")

# Set up the server parameters
server_params = StdioServerParameters(
    command="python",
    args=["arxivloader.py"],
)

async def get_agent_response(query: str):
    """Fetch agent's response for a given query."""
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": query})
            return agent_response

# Streamlit layout
st.title("FastMCP ")

user_query = st.chat_input("Enter Research Paper Name")

if user_query:
    with st.spinner('Processing your request...'):
        response = asyncio.run(get_agent_response(user_query))
        st.markdown(f"### Agent's Response:")
        st.write(response)
