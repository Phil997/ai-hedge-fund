# My API - Finanzdaten API

**Base URL:** `http://<host>:<port>` (via `MY_API_URL` env var)

---

## Endpunkte

### 1. Preise (Historical Prices)

```
GET /prices/?ticker=AAPL&interval=day&interval_multiplier=1&start_date=2024-01-01&end_date=2024-12-31
```

| Parameter | Typ | erforderlich | Beschreibung |
|----------|-----|------------|-------------|
| ticker | string | ✓ | Aktien-Symbol (z.B. AAPL) |
| interval | string | ✓ | "day" |
| interval_multiplier | int | ✓ | 1 |
| start_date | string | ✓ | ISO Datum (YYYY-MM-DD) |
| end_date | string | ✓ | ISO Datum (YYYY-MM-DD) |

**Response:**
```json
{
  "ticker": "AAPL",
  "prices": [
    {
      "open": 185.50,
      "close": 187.25,
      "high": 188.00,
      "low": 184.50,
      "volume": 45000000,
      "time": "2024-01-02T00:00:00Z"
    }
  ]
}
```

---

### 2. Finanzkennzahlen (Financial Metrics)

```
GET /financial-metrics/?ticker=AAPL&report_period_lte=2024-12-31&limit=10&period=ttm
```

| Parameter | Typ | requerido | Beschreibung |
|----------|-----|----------|-------------|
| ticker | string | ✓ | Aktien-Symbol |
| report_period_lte | string | ✓ | Höchstes Datum (YYYY-MM-DD) |
| limit | int | ✓ | Anzahl Ergebnisse |
| period | string | ✓ | "ttm" oder "annual" |

**Response:**
```json
{
  "financial_metrics": [
    {
      "ticker": "AAPL",
      "report_period": "2024-12-31",
      "period": "ttm",
      "currency": "USD",
      "market_cap": 3000000000000,
      "enterprise_value": 2900000000000,
      "price_to_earnings_ratio": 28.5,
      "price_to_book_ratio": 45.2,
      "price_to_sales_ratio": 7.8,
      "enterprise_value_to_ebitda_ratio": 22.1,
      "enterprise_value_to_revenue_ratio": 6.5,
      "free_cash_flow_yield": 0.025,
      "peg_ratio": 1.8,
      "gross_margin": 0.46,
      "operating_margin": 0.29,
      "net_margin": 0.24,
      "return_on_equity": 1.45,
      "return_on_assets": 0.32,
      "return_on_invested_capital": 0.38,
      "asset_turnover": 1.2,
      "inventory_turnover": 25.0,
      "receivables_turnover": 15.5,
      "days_sales_outstanding": 23,
      "operating_cycle": 250,
      "working_capital_turnover": 4.5,
      "current_ratio": 1.5,
      "quick_ratio": 1.2,
      "cash_ratio": 0.8,
      "operating_cash_flow_ratio": 1.4,
      "debt_to_equity": 1.8,
      "debt_to_assets": 0.45,
      "interest_coverage": 15.0,
      "revenue_growth": 0.08,
      "earnings_growth": 0.12,
      "book_value_growth": 0.06,
      "earnings_per_share_growth": 0.10,
      "free_cash_flow_growth": 0.09,
      "operating_income_growth": 0.11,
      "ebitda_growth": 0.10,
      "payout_ratio": 0.25,
      "earnings_per_share": 6.5,
      "book_value_per_share": 4.2,
      "free_cash_flow_per_share": 5.8
    }
  ]
}
```

---

### 3. Bilanzdaten (Line Items)

```
POST /financials/search/line-items
```

**Body:**
```json
{
  "tickers": ["AAPL"],
  "line_items": ["revenue", "net_income", "total_assets", "total_equity"],
  "end_date": "2024-12-31",
  "period": "ttm",
  "limit": 10
}
```

| Parameter | Typ | erforderlich | Beschreibung |
|----------|-----|------------|-------------|
| tickers | array[string] | ✓ | Liste von Tickers |
| line_items | array[string] | ��� | Gewünschte Felder |
| end_date | string | ✓ | Datum (YYYY-MM-DD) |
| period | string | ✓ | "ttm" oder "annual" |
| limit | int | ✓ | Anzahl |

**Verfügbare line_items:**
- revenue
- net_income
- total_assets
- total_liabilities
- total_equity
- operating_income
- cost_of_revenue
- gross_profit
- research_and_development
- selling_general_and_administrative
- operating_expenses
- interest_expense
- income_tax_expense
- cash_and_equivalents
- accounts_receivable
- inventory
- current_assets
- current_liabilities
- long_term_debt
- retained_earnings

**Response:**
```json
{
  "search_results": [
    {
      "ticker": "AAPL",
      "report_period": "2024-12-31",
      "period": "ttm",
      "currency": "USD",
      "revenue": 385000000000,
      "net_income": 97000000000
    }
  ]
}
```

---

### 4. Insider-Trades

```
GET /insider-trades/?ticker=AAPL&filing_date_lte=2024-12-31&limit=1000
```

| Parameter | Typ | erforderlich | Beschreibung |
|----------|-----|------------|-------------|
| ticker | string | ✓ | Aktien-Symbol |
| filing_date_lte | string | ✓ | Höchstes Datum |
| filing_date_gte | string | - | Niedrigstes Datum |
| limit | int | ✓ | Anzahl |

**Response:**
```json
{
  "insider_trades": [
    {
      "ticker": "AAPL",
      "issuer": "AAPL",
      "name": "John Doe",
      "title": "CEO",
      "is_board_director": true,
      "transaction_date": "2024-12-15",
      "transaction_shares": 10000,
      "transaction_price_per_share": 195.50,
      "transaction_value": 1955000,
      "shares_owned_before_transaction": 500000,
      "shares_owned_after_transaction": 510000,
      "security_title": "Common Stock",
      "filing_date": "2024-12-16"
    }
  ]
}
```

---

### 5. Nachrichten (Company News)

```
GET /news/?ticker=AAPL&end_date=2024-12-31&limit=1000
```

| Parameter | Typ | erforderlich | Beschreibung |
|----------|-----|------------|-------------|
| ticker | string | ✓ | Aktien-Symbol |
| end_date | string | ✓ | Höchstes Datum |
| start_date | string | - | Niedrigstes Datum |
| limit | int | ✓ | Anzahl |

**Response:**
```json
{
  "news": [
    {
      "ticker": "AAPL",
      "title": "Apple Reports Record Earnings",
      "author": "Jane Smith",
      "source": "Reuters",
      "date": "2024-12-15T10:00:00Z",
      "url": "https://example.com/article",
      "sentiment": "positive"
    }
  ]
}
```

---

### 6. Company Facts

```
GET /company/facts/?ticker=AAPL
```

| Parameter | Typ | erforderlich | Beschreibung |
|----------|-----|------------|-------------|
| ticker | string | ✓ | Aktien-Symbol |

**Response:**
```json
{
  "company_facts": {
    "ticker": "AAPL",
    "name": "Apple Inc.",
    "cik": "0000320193",
    "industry": "Technology",
    "sector": "Consumer Electronics",
    "category": "Computer Hardware",
    "exchange": "NASDAQ",
    "is_active": true,
    "listing_date": "1980-12-12",
    "location": "Cupertino, CA",
    "market_cap": 3000000000000,
    "number_of_employees": 164000,
    "sec_filings_url": "https://sec.gov/...",
    "sic_code": "3571",
    "sic_industry": "Electronic Computers",
    "sic_sector": "Manufacturing",
    "website_url": "https://apple.com",
    "weighted_average_shares": 15500000000
  }
}
```

---

## Fehlerbehandlung

| Status Code | Bedeutung |
|-------------|-----------|
| 200 | Erfolgreich |
| 400 | Bad Request (fehlende Parameter) |
| 404 | Ticker nicht gefunden |
| 429 | Rate Limit überschritten |
| 500 | Server Fehler |

**Rate Limit:** Bei 429: Linearer Backoff (60s, 90s, 120s...)

---

## Hinweise

- Alle Datumsangaben in ISO 8601 Format (YYYY-MM-DD)
- Market Cap und andere große Werte als Floats (nicht als Strings)
- Bei fehlenden Daten: `null` (nicht weggelassen)