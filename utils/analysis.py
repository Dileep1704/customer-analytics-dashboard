import pandas as pd

def root_cause_analysis(df):
    insights = []

    # Define last 30 days
    latest_date = df['order_date'].max()
    cutoff = latest_date - pd.Timedelta(days=30)

    recent = df[df['order_date'] >= cutoff]
    previous = df[df['order_date'] < cutoff]

    # Edge case
    if previous.empty or recent.empty:
        return ["Not enough data for analysis"]

    recent_rev = recent['sales'].sum()
    prev_rev = previous['sales'].sum()

    # Check revenue trend
    if recent_rev < prev_rev:
        insights.append("Revenue dropped in the last 30 days")

        # Category-level analysis
        cat_recent = recent.groupby('category')['sales'].sum()
        cat_prev = previous.groupby('category')['sales'].sum()

        diff = (cat_recent - cat_prev).fillna(0)

        worst_category = diff.idxmin()
        insights.append(f"Major decline in category: {worst_category}")

        # Region-level analysis
        region_recent = recent.groupby('region')['sales'].sum()
        region_prev = previous.groupby('region')['sales'].sum()

        region_diff = (region_recent - region_prev).fillna(0)

        worst_region = region_diff.idxmin()
        insights.append(f"Region impacted most: {worst_region}")

    else:
        insights.append("Revenue is stable or growing")

    return insights