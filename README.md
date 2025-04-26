# Arxivloader MCP Server and Client

This project provides an MCP (Microservice Communication Protocol) server and client setup for fetching research papers from the [arXiv](https://arxiv.org/). The MCP server processes queries and fetches relevant research papers, while the client communicates with the server using the MCP protocol. This project uses `Streamlit` for a simple UI and integrates tools such as `LangChain`, `Groq`, and `MCP` for communication.

## Features

- **MCP Communication**: Efficient communication between server and client using MCP protocol.
- **Research Paper Retrieval**: Fetches research papers from arXiv based on user queries.
- **Streamlit UI**: A simple web interface to input queries and display research paper results.
- **Tool Integration**: Uses Groq and LangChain for enhanced query handling and processing.

## Requirements

- Python 3.8 or higher
- `streamlit`
- `mcp`
- `langchain`
- `langchain_groq`
- `dotenv`
- `asyncio`

You can install the required dependencies using the following:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone this repository:

```bash
git clone https://github.com/alihassanml/Arxivloader-MCP-Server-and-Client.git
cd Arxivloader-MCP-Server-and-Client
```

2. Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the `.env` file with any required configuration for Groq and MCP settings.

## Usage

1. **Start the MCP Server**:

   Run the server script to start the MCP server:

   ```bash
   python arxivloader.py
   ```

2. **Run the Client with Streamlit**:

   Start the Streamlit client interface to interact with the server:

   ```bash
   streamlit run client.py
   ```

3. **Query Research Papers**:

   Once the client interface is running, you can enter the name of a research paper or a query in the input field. The server will fetch relevant papers and display them.

## Example

Here is an example of how the system works:

1. The user enters a query like "Medical Claim Processing OR Health Insurance Billing" into the Streamlit interface.
2. The MCP server processes the query and fetches relevant research paper data from arXiv.
3. The client displays the fetched paper details, such as title, authors, and publication date.

## Project Structure

```
.
├── arxivloader.py          # MCP server code for handling queries and fetching research papers
├── client.py               # Streamlit client UI to interact with the server
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables for configuration
└── README.md               # Project documentation
```

## Contributing

Feel free to fork this repository and contribute to the project. If you find any bugs or have feature requests, please open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
