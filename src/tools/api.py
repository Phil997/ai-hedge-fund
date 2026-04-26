import os

from src.tools import financial_datasets, my_api


def get_prices(ticker: str, start_date: str, end_date: str, api_key: str = None):
    if os.environ.get("FINANCIAL_DATASETS_API_KEY"):
        return financial_datasets.get_prices(ticker, start_date, end_date, api_key)
    elif os.environ.get("MY_API_URL"):
        return my_api.get_prices(ticker, start_date, end_date)
    else:
        raise Exception("No data source configured. Set MY_API_URL or FINANCIAL_DATASETS_API_KEY")


def get_financial_metrics(
    ticker: str,
    end_date: str,
    period: str = "ttm",
    limit: int = 10,
    api_key: str = None,
):
    if os.environ.get("FINANCIAL_DATASETS_API_KEY"):
        return financial_datasets.get_financial_metrics(ticker, end_date, period, limit, api_key)
    elif os.environ.get("MY_API_URL"):
        return my_api.get_financial_metrics(ticker, end_date, period, limit)
    else:
        raise Exception("No data source configured. Set MY_API_URL or FINANCIAL_DATASETS_API_KEY")


def search_line_items(
    ticker: str,
    line_items: list[str],
    end_date: str,
    period: str = "ttm",
    limit: int = 10,
    api_key: str = None,
):
    if os.environ.get("FINANCIAL_DATASETS_API_KEY"):
        return financial_datasets.search_line_items(ticker, line_items, end_date, period, limit, api_key)
    elif os.environ.get("MY_API_URL"):
        return my_api.search_line_items(ticker, line_items, end_date, period, limit)
    else:
        raise Exception("No data source configured. Set MY_API_URL or FINANCIAL_DATASETS_API_KEY")


def get_insider_trades(
    ticker: str,
    end_date: str,
    start_date: str | None = None,
    limit: int = 1000,
    api_key: str = None,
):
    if os.environ.get("FINANCIAL_DATASETS_API_KEY"):
        return financial_datasets.get_insider_trades(ticker, end_date, start_date, limit, api_key)
    elif os.environ.get("MY_API_URL"):
        return my_api.get_insider_trades(ticker, end_date, start_date, limit)
    else:
        raise Exception("No data source configured. Set MY_API_URL or FINANCIAL_DATASETS_API_KEY")


def get_company_news(
    ticker: str,
    end_date: str,
    start_date: str | None = None,
    limit: int = 1000,
    api_key: str = None,
):
    if os.environ.get("FINANCIAL_DATASETS_API_KEY"):
        return financial_datasets.get_company_news(ticker, end_date, start_date, limit, api_key)
    elif os.environ.get("MY_API_URL"):
        return my_api.get_company_news(ticker, end_date, start_date, limit)
    else:
        raise Exception("No data source configured. Set MY_API_URL or FINANCIAL_DATASETS_API_KEY")


def get_market_cap(
    ticker: str,
    end_date: str,
    api_key: str = None,
):
    if os.environ.get("FINANCIAL_DATASETS_API_KEY"):
        return financial_datasets.get_market_cap(ticker, end_date, api_key)
    elif os.environ.get("MY_API_URL"):
        return my_api.get_market_cap(ticker, end_date)
    else:
        raise Exception("No data source configured. Set MY_API_URL or FINANCIAL_DATASETS_API_KEY")


def prices_to_df(prices):
    if os.environ.get("FINANCIAL_DATASETS_API_KEY"):
        return financial_datasets.prices_to_df(prices)
    elif os.environ.get("MY_API_URL"):
        return my_api.prices_to_df(prices)
    else:
        raise Exception("No data source configured. Set MY_API_URL or FINANCIAL_DATASETS_API_KEY")


def get_price_data(ticker: str, start_date: str, end_date: str, api_key: str = None):
    if os.environ.get("FINANCIAL_DATASETS_API_KEY"):
        return financial_datasets.get_price_data(ticker, start_date, end_date, api_key)
    elif os.environ.get("MY_API_URL"):
        return my_api.get_price_data(ticker, start_date, end_date)
    else:
        raise Exception("No data source configured. Set MY_API_URL or FINANCIAL_DATASETS_API_KEY")
