import streamlit as st
import pandas as pd
from lead_scoring import score_leads
from email_enrichment import mock_enrich_emails

@st.cache_data
def load_data():
    df = pd.read_csv('leads_sample.csv')
    return df

def deduplicate_leads(df):
    if 'Website' in df.columns:
        # Extract domain from website URLs
        df['Domain'] = df['Website'].str.extract(r'https?://(?:www\.)?([^/]+)')
        deduped_df = df.drop_duplicates(subset=['Domain'])
        df.drop(columns=['Domain'], inplace=True)  # Clean up
    else:
        deduped_df = df.drop_duplicates(subset=['Company'], keep='first')

    return deduped_df

def main():
    st.set_page_config(page_title="Smart Lead Scoring Tool", layout="wide")
    st.title("Smart Lead Scoring & Enrichment Tool")

    df = load_data()

    # Sidebar Filters
    st.sidebar.header("Filter Leads")

    # Industry filter
    industries = df['Industry'].dropna().unique().tolist()
    selected_industries = st.sidebar.multiselect("Industry", industries, default=industries)

    # City filter 
    if 'City' in df.columns:
        cities = df['City'].dropna().unique().tolist()
        selected_cities = st.sidebar.multiselect("City", cities, default=cities)
    else:
        selected_cities = []

    # Revenue range filter
    min_revenue = float(df['Revenue'].min())
    max_revenue = float(df['Revenue'].max())
    revenue_range = st.sidebar.slider("Revenue Range (in millions)", min_revenue, max_revenue, (min_revenue, max_revenue))

    remove_duplicates = st.sidebar.checkbox("Remove duplicate leads", value=True)

    # Filter data 
    if selected_industries:
        filtered_df = df[df['Industry'].isin(selected_industries)]
    else:
        filtered_df = df.copy()

    if selected_cities:
        filtered_df = filtered_df[filtered_df['City'].isin(selected_cities)]

    filtered_df = filtered_df[
        (filtered_df['Revenue'] >= revenue_range[0]) &
        (filtered_df['Revenue'] <= revenue_range[1])
    ]


    if remove_duplicates:
        filtered_df = deduplicate_leads(filtered_df)

    # Score the filtered leads
    scored_df = score_leads(filtered_df)

    
    enriched_df = mock_enrich_emails(scored_df)

   
    min_score = st.sidebar.slider("Minimum Lead Score", 0, 100, 50)
    scored_filtered = enriched_df[enriched_df['LeadScore'] >= min_score]

    # summary
    st.info(
        f"Showing leads in **{', '.join(selected_industries)}**"
        f"{' from ' + ', '.join(selected_cities) if selected_cities else ''} "
        f"with revenue between **${revenue_range[0]:,.0f}M** and **${revenue_range[1]:,.0f}M** "
        f"and lead score >= **{min_score}**."
    )

    
    tabs = st.tabs(["📊 Lead Dashboard", "🔍 Lead Details", "📤 Export Leads"])

    with tabs[0]:
        st.subheader(f"Leads with score ≥ {min_score} (Total: {len(scored_filtered)})")
        # dataframe with lead score 
        st.dataframe(
            scored_filtered[['Company', 'Industry', 'Revenue', 'GrowthPct', 'Employees', 'YearFounded', 'LeadScore', 'Email']]
            .style.bar(subset=["LeadScore"], color="#00ff99")
            .format({"LeadScore": "{:.2f}", "Revenue": "${:,.0f}"})
        )

        if st.checkbox("Show raw data"):
            st.write(enriched_df)

    with tabs[1]:
        selected_company = st.selectbox("Select a Company to view details", options=scored_filtered['Company'].tolist())
        if selected_company:
            lead = scored_filtered[scored_filtered['Company'] == selected_company].iloc[0]

            st.markdown("### Lead Details")
            st.write(f"**Company:** {lead['Company']}")
            st.write(f"**Industry:** {lead['Industry']}")
            st.write(f"**Revenue:** ${lead['Revenue']:,}")
            st.write(f"**Growth %:** {lead['GrowthPct']}%")
            st.write(f"**Employees:** {lead['Employees']}")
            st.write(f"**Year Founded:** {lead['YearFounded']}")
            st.write(f"**Lead Score:** {lead['LeadScore']:.2f}")
            st.write(f"**Email:** {lead['Email']}")
            if 'Website' in lead and pd.notna(lead['Website']):
                st.markdown(f"[🌐 Website]({lead['Website']})")

    with tabs[2]:
        st.markdown("### Export Filtered Leads")
        st.download_button(
            label="📥 Download Filtered Leads as CSV",
            data=scored_filtered.to_csv(index=False),
            file_name="filtered_leads.csv",
            mime="text/csv",
        )

    # Footer
    st.markdown("---")
    st.caption("🔍 Built by Atchuth Vutukuri for Caprae Capital's AI Pre-Screening Challenge — Empowering smarter lead decisions with AI ✨")

if __name__ == "__main__":
    main()
