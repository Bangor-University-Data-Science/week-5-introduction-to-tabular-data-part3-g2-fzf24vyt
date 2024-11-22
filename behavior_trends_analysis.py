import pandas as pd

def import_data(filename: str) -> pd.DataFrame:
    try:
        df = pd.read_excel("Customer_Behavior.xlsx")
    except ValueError:
        df = pd.read_csv("Customer_Behavior.xlsx")
    return df

def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=['CustomerID'])
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    return df

def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    customer_counts = df.groupby('CustomerID').size().reset_index(name='PurchaseCount')
    loyal_customers_df = customer_counts[customer_counts['PurchaseCount'] >= min_purchases]
    return loyal_customers_df

def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    df['Quarter'] = df['InvoiceDate'].dt.to_period('Q')
    quarterly_revenue_df = df.groupby('Quarter')['Revenue'].sum().reset_index()
    return quarterly_revenue_df

def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    product_demand = df.groupby('StockCode')['Quantity'].sum().nlargest(top_n).reset_index()
    return product_demand

def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
    pattern_df = df.groupby('StockCode').agg(
        avg_quantity=('Quantity', 'mean'),
        avg_unit_price=('UnitPrice', 'mean')
    ).reset_index()
    return pattern_df

def answer_conceptual_questions() -> dict:
    return {
        "Q1": {"A"},
        "Q2": {"B"},
        "Q3": {"C"},
        "Q4": {"A"},
        "Q5": {"A"}
    }
