import pandas as pd

def mock_enrich_emails(df):
    def generate_email(company, domain):
        base = company.lower().replace(" ", "")
        return f"info@{domain}" if domain else f"{base}@example.com"

    if 'Website' in df.columns:
        df['Domain'] = df['Website'].str.extract(r'https?://(?:www\.)?([^/]+)', expand=False)
    else:
        df['Domain'] = None

    df['Email'] = df.apply(lambda row: generate_email(row['Company'], row['Domain']), axis=1)
    df.drop(columns=['Domain'], inplace=True)

    return df
