import pandas as pd

def score_leads(df):
    df['RevenueScore'] = df['Revenue'] / df['Revenue'].max()
    df['GrowthScore'] = df['GrowthPct'] / 100
    df['EmployeesScore'] = df['Employees'].apply(lambda x: 1 if 50 <= x <= 150 else 0.5)
    df['AgeScore'] = df['YearFounded'].apply(lambda y: 1 if y >= 2015 else 0.7)
    df['KeywordScore'] = df['Keywords'].apply(lambda k: 0.1 if 'SaaS' in k else 0)

    df['LeadScore'] = (
        df['RevenueScore'] * 0.4 +
        df['GrowthScore'] * 0.3 +
        df['EmployeesScore'] * 0.1 +
        df['AgeScore'] * 0.1 +
        df['KeywordScore'] * 0.1
    )

    df['LeadScore'] = df['LeadScore'] * 100

    return df.sort_values(by='LeadScore', ascending=False)
