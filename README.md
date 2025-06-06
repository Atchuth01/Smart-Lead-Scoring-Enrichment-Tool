
# Smart Lead Scoring & Enrichment Tool 🚀

## Overview

This is a Streamlit-based interactive web app designed to help businesses score, filter, and enrich sales leads effectively using simple but practical AI-driven business logic. It integrates customizable lead scoring based on company financials, growth, employees, and keywords, along with mock email enrichment to simulate contact discovery.

---

--> You can find the linkof my web app here:
https://lead-scoring-enrichment-tool.streamlit.app/


## Features

- Upload and load lead data from CSV (`leads_sample.csv` included as sample)  
- Dynamic filters for Industry, City, Revenue Range, and Lead Score  
- Duplicate lead removal based on company domain or name  
- Custom lead scoring based on:  
  - Revenue  
  - Growth percentage  
  - Number of employees  
  - Company age  
  - Keyword presence (e.g., SaaS)  
- Mock email enrichment generating professional-like email addresses  
- Interactive tabs for:  
  - Lead Dashboard with sortable score bars  
  - Detailed view of individual lead info  
  - Export filtered leads to CSV file download  
- Responsive UI with sidebar filtering and clean layout

---

## Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Atchuth01/Smart-Lead-Scoring-Enrichment-Tool.git
   cd Smart-Lead-Scoring-Enrichment-Tool
  

2. **Create & activate virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/macOS
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```


4. **Run the app**

   ```bash
   streamlit run app.py
   ```

5. Open your browser at `http://localhost:8501` to view the app.

---

## Usage Screenshots

--> Check teh 'screenshots' folder

---

## Sample Run Instructions

* Use the sidebar to filter leads by Industry, City, Revenue range, and minimum Lead Score.
* Optionally remove duplicate leads based on domain/company name.
* View scored leads in the dashboard tab with intuitive score bars.
* Click the “Lead Details” tab to select a company and see detailed information including mock email.
* Export filtered leads as CSV from the “Export Leads” tab.

---

## About This Tool

### Why Lead Scoring?

Lead scoring prioritizes sales leads to focus efforts on prospects with the highest potential, improving sales efficiency and conversion rates.

### Business Logic Used

* Revenue normalized against max revenue to assess financial size.
* Growth percentage to capture momentum.
* Employee count to focus on small-to-mid sized companies (50-150 employees favored).
* Company age to prefer newer, potentially more innovative companies (founded ≥ 2015).
* Keyword presence (like "SaaS") to boost relevance in software-as-a-service domain.

### Why Mock Enrichment?

Real email enrichment APIs can be costly and require access permissions. Mock enrichment simulates email generation for demo and development purposes, showcasing integration without external dependencies.

### Real-World Use Case Alignment

This tool can assist sales and marketing teams in lead qualification, data cleansing, and contact discovery, helping businesses improve pipeline quality with minimal manual effort.

---

## License

MIT License

---

## Contact

Created by Atchuth Vutukuri for Caprae Capital's AI Pre-Screening Challenge.
Feel free to reach out for questions or collaborations.

---

