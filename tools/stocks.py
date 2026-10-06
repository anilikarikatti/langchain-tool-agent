from langchain.tools import tool


@tool
def get_stock_price(symbol: str) -> str:
    """
    Get the current stock price for a company.

    Args:
        symbol: Stock ticker symbol such as AAPL, MSFT, or TSLA.
    """

    # Temporary mock data for learning
    stocks = {
        "AAPL": 250.12,
        "MSFT": 510.45,
        "TSLA": 421.30,
        "GOOGL": 285.50,
        "NVDA": 185.20,
    }

    symbol = symbol.upper()

    if symbol not in stocks:
        return f"Stock price unavailable for {symbol}"

    return f"{symbol} current price is ${stocks[symbol]}"