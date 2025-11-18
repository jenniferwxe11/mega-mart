# Mega Mart Analytics Project

## Overview
MegaMart is a simulated omnichannel retailer in Singapore, offering a wide range of products including electronics, fashion, groceries, and home goods. The company operates through 50 physical stores and an e-commerce platform. Frequent marketing campaigns (email, SMS, push notifications) are run with A/B testing to optimize conversion and retention.

This project demostrates an end-to-end analytics solution covering data engineering, modeling, machine learning, dashboards, and operational documentation.

## Business Goals
- Understand customer segments for targeted marketing
- Increase Average Order Value (AOV)
- Optimize campaign ROI
- Reduce customer churn via predictive models
- Track revenue trends and operational KPIs across channels

## Business Questions
- Which customer segments are most valuable?
- What is our churn rate and which customers are at risk?
- How effective are different marketing campaigns and channels?
- What products drive the most profit across channels?

## Tech Stack
- **Python:** Pandas, NumPy, Faker, Matplotlib, Seaborn, scikit-learn
- **SQL:** BiqQuery
- **ELT & Data Modeling:** DBT
- **Workflow Orchestration:** Airflow (cloud deployment)
- **Visualization & BI:** Looker Studio
- **DevOps & CI/CD:** Github Actions, Cloud Build
- **Version Control:** Github

## Deliverables

### Data Engineering
- Simulated raw data reflecting real-world distributions with minor noise
- Cleaned and transformed tables ready for analysis
- Fact and dimension tables stored in BigQuery with consistent schema
- ELT pipelines automated and validated with Airflow + DBT


### Analytics & Machine Learning
- Customer segmentation using RFM and clustering
- Churn prediction model for retention strategies
- Campaign uplift analysis with A/B testing framework
- Customer Lifetime Value (LTV) forecasting

### Visualization & Reporting
- KPI dashboards in Looker Studio for executive and operational views
- Conversion funnels, revenue trends, campaign ROI, and product-level insights

### Project Management & DevOps
- Github repository with structured code, DBT Models, and Jupyter Notebooks
- CI/CD pipelines ensuring reproducible analytics
- Agile workflow tracking in Jira
- Project Documentation in Confluence

## Key KPIs
- Revenue trends (by region, channel, season, product category)
- Average Order Value (AOV)
- Customer Lifetime Value (LTV)
- Customer Acqusition Cost (CAC)
- Churn and retention metrics
- Campaign ROI and lift
- Funnel conversion rates
- A/B test effectivenes

## Actionable Insights

## How to Run
Step 1: Clone this repo
```
git clone https://github.com/jenniferwxe/mega-mart.git
cd mega-mart
```
Step 2: Create a virtual environment
```
python -m venv venv
```
Step 3: Activate virtual environment
```
source venv\Scripts\active # Windows
source venv/bin/activate   # macOS/Linux
```
Step 3: Install dependencies
```
pip install -r requirements.txt
```
Step 4: Generate raw data
``` ```
Full Singapore Geospatial GEOJSON is required:
1. Download from https://data.gov.sg/datasets/d_4765db0e87b9c86336792efe8a1f7a66/view
2. Save under data_generation/raw_data
3. Rename it singapore_areas.geojson


## Author
Jennifer Wang
https://www.linkedin.com/in/jenniferwangxueer/
