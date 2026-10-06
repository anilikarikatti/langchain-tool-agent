from langchain.tools import tool


@tool
def search_web(query: str) -> str:
    """
    Search the web for current information.

    Args:
        query: Search query.
    """

    # Temporary mock result
    return (
        f"Search results for '{query}': "
        "AI agent systems use language models to reason about "
        "tasks and invoke tools dynamically."
    )




    # i want to go to bengaluru , tommorrow , how isa weather there ? 

    # latest news about anantnag kannada actor , about dada saheb palke ? 