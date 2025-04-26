# arxivloader.py
from mcp.server.fastmcp import FastMCP
from langchain_community.document_loaders import ArxivLoader

mcp = FastMCP("ArxivLoader")

@mcp.tool()
def query(input):
    loader = ArxivLoader(query=input)
    docs = loader.get_summaries_as_docs()
    
    if docs:  # Check if docs is not empty
        return {'page_content': docs[0].page_content[:300], 'metadata': docs[0].metadata}
    else:
        return {'page_content': 'No documents found', 'metadata': {}}


if __name__ == "__main__":
    import asyncio
    mcp.run("stdio")  # Run the main async function
