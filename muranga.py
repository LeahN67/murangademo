"""
GreenScope Analytics - Murang'a County Carbon Empowerment Initiative
Tabbed Dashboard Layout - FIXED
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page Configuration
st.set_page_config(
    page_title="GreenScope | Murang'a Carbon Empowerment",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS STYLES - Simplified and reliable
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #f8fafc; }
    
    /* Hero Section */
    .hero-container {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: white;
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 1rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 20px;
        background-color: #f8fafc;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        font-weight: 600;
        color: #64748b;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #059669 !important;
        color: white !important;
        border-color: #059669 !important;
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<div class="hero-container">
    <h1 style="color: white; font-size: 2.5rem; font-weight: 800; margin: 0;">🌱 Murang'a County Carbon Empowerment Initiative</h1>
    <p style="color: rgba(255,255,255,0.9); font-size: 1.25rem; margin-top: 0.75rem;">Turning Climate-Smart Farming into Sustainable Income for 57,975 Farmers</p>
</div>
""", unsafe_allow_html=True)

# TABS
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Overview", "2️⃣ The Problem", "3️⃣ GreenScope Solution", "4️⃣ Farmer Impact", "5️⃣ County Impact"])

# TAB 1: OVERVIEW
with tab1:
    st.subheader("Quick Facts")
    
    # Metrics using columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("👨‍🌾 Registered Farmers", "57,975")
    with col2:
        st.metric("💰 Revenue/Hectare", "$50-200")
    with col3:
        st.metric("🌽 Maize Price", "KES 3,500")
    with col4:
        st.metric("☕ Main Crops", "Coffee, Tea")
    
    st.markdown("---")
    
    # Summary Cards
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown("#### ❌ The Challenge")
            st.markdown("""
            Murang'a farmers practice climate-smart agriculture but lose 
            **$50-200/hectare/year** in unclaimed carbon revenue due to 
            measurement complexity, high verification costs, and lack of market access.
            """)
    
    with col2:
        with st.container():
            st.markdown("#### ✅ The Solution")
            st.markdown("""
            GreenScope Platform automates carbon measurement using satellite data, 
            AI calculation, and bundles small farms into market-viable projects. 
            Revenue split: **70% farmer | 20% coop | 10% platform**.
            """)
    
    st.markdown("---")
    st.subheader("Projected Impact at Scale")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("👨‍🌾")
        st.markdown("### 30,000")
        st.caption("Farmers by Year 3")
    
    with col2:
        st.markdown("💵")
        st.markdown("### $3.75M")
        st.caption("Annual Carbon Revenue")
    
    with col3:
        st.markdown("📈")
        st.markdown("### +35-62%")
        st.caption("Income Increase per Farm")
    
    st.markdown("---")
    st.subheader("Growth Trajectory")
    
    # Growth Chart
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    years = ['Year 1', 'Year 2', 'Year 3']
    farmers = [5000, 15000, 30000]
    revenue = [0.625, 1.875, 3.75]
    
    fig.add_trace(
        go.Bar(
            x=years, y=revenue, name="Carbon Revenue ($M)",
            marker_color='#059669', text=[f"${r:.2f}M" for r in revenue],
            textposition='outside', textfont=dict(size=14, weight='bold'),
            opacity=0.8
        ),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Scatter(
            x=years, y=farmers, name="Farmers Enrolled",
            mode='lines+markers+text', line=dict(color='#f59e0b', width=4),
            marker=dict(size=12), text=[f"{f:,}" for f in farmers],
            textposition="top center", textfont=dict(size=12, color='#f59e0b', weight='bold')
        ),
        secondary_y=True,
    )
    
    fig.update_layout(
        title=dict(text="3-Year Scaling Roadmap", font=dict(size=16, weight='bold'), x=0.5),
        plot_bgcolor='white', paper_bgcolor='white',
        font=dict(family="Inter, sans-serif"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=400, margin=dict(t=80, b=50)
    )
    
    fig.update_yaxes(title_text="Revenue ($ Million)", secondary_y=False, gridcolor='#f1f5f9', range=[0, 4.5])
    fig.update_yaxes(title_text="Number of Farmers", secondary_y=True, range=[0, 35000])
    fig.update_xaxes(gridcolor='#f1f5f9')
    
    st.plotly_chart(fig, use_container_width=True)

# TAB 2: THE PROBLEM
with tab2:
    st.header("❌ The Problem: Farmers Are Missing Out")
    
    st.markdown("""
    **Murang'a farmers practice climate-smart agriculture but cannot access carbon markets due to systemic barriers.**
    """)
    
    st.subheader("Current Climate-Smart Practices:")
    st.markdown("""
    - **Agroforestry:** Shade trees on coffee farms
    - **Regenerative Agriculture:** Composting, cover crops, reduced tillage
    - **Livestock Management:** Methane reduction protocols
    - **Land Restoration:** Revegetating degraded areas
    """)
    
    st.subheader("Barriers to Carbon Market Access:")
    
    problem_data = {
        'Challenge': ['Measurement Complexity', 'Verification Costs', 'Scale Requirements', 'Data Fragmentation'],
        'Description': [
            'Soil carbon quantification requires specialized expertise and expensive equipment',
            'Third-party auditing costs $10,000-$50,000 per project—prohibitive for smallholders',
            'Buyers require 1,000+ ton volumes; individual farms are too small',
            'KIAMIS records lack carbon tracking and buyer connectivity'
        ]
    }
    st.dataframe(pd.DataFrame(problem_data), use_container_width=True, hide_index=True)
    
    st.error("**Impact:** Farmers lose $50-200/hectare/year. A 3-hectare farm forfeits $150-600 yearly in potential carbon income.")

# TAB 3: GREENSCOPE SOLUTION
with tab3:
    st.header("✅ The Solution: GreenScope Platform")
    
    st.markdown("""
    **An integrated digital infrastructure automating carbon measurement, verification, and market access.**
    """)
    
    st.subheader("Implementation Process:")
    
    # Process steps in 3 columns
    cols = st.columns(3)
    steps = [
        ("1️⃣", "Farmer Onboarding", "Enrollment via cooperatives"),
        ("2️⃣", "Activity Logging", "Mobile-based practice recording"),
        ("3️⃣", "Satellite Verification", "Remote sensing confirmation"),
        ("4️⃣", "Carbon Calculation", "AI quantification"),
        ("5️⃣", "Project Aggregation", "Bundling small farms"),
        ("6️⃣", "Revenue Distribution", "70% farmer | 20% coop | 10% platform")
    ]
    
    for i, (emoji, title, desc) in enumerate(steps):
        with cols[i % 3]:
            with st.container():
                st.markdown(f"**{emoji} {title}**")
                st.caption(desc)
    
    st.markdown("---")
    st.subheader("Data Integration Sources:")
    
    # Data sources in 3 columns
    col1, col2, col3 = st.columns(3)
    sources = [
        ("🛰️", "Satellite Imagery", "Tree cover, vegetation indices"),
        ("🌧️", "Climate Data", "Rainfall, temperature, soil moisture"),
        ("🧪", "Soil Analytics", "Type, organic matter, carbon content"),
        ("📱", "Field Records", "Planting dates, tree counts"),
        ("🏛️", "KIAMIS Database", "57,975 farmer profiles")
    ]
    
    for i, (emoji, label, desc) in enumerate(sources):
        with [col1, col2, col3][i % 3]:
            with st.container():
                st.markdown(f"**{emoji} {label}**")
                st.caption(desc)
    
    st.markdown("---")
    st.success("**Result:** Automated MRV (Measurement, Reporting, Verification) reduces costs by 80% and enables smallholder participation in carbon markets.")

# TAB 4: FARMER IMPACT
with tab4:
    st.header("👨‍🌾 Farmer Impact: Income Projections")
    
    st.markdown("**Three representative farm profiles demonstrating carbon revenue potential.**")
    
    st.markdown("---")
    
    # Case 1: Coffee
    st.subheader("☕ Case 1: Coffee Agroforestry System (2 hectares)")
    case1_data = {
        'Revenue Stream': ['Coffee Sales', 'Shade Tree Carbon Credits', 'Sustainability Premium', 'TOTAL'],
        'Annual Amount': ['KES 180,000', '+ KES 45,000', '+ KES 18,000', 'KES 243,000'],
        'Details': ['Baseline crop income', 'New carbon revenue', 'Certification bonus', '+35% increase']
    }
    st.dataframe(pd.DataFrame(case1_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Case 2: Maize
    st.subheader("🌽 Case 2: Regenerative Maize Operation (5 hectares)")
    case2_data = {
        'Revenue Stream': ['Maize Sales (50 bags)', 'Market Timing Optimization', 'Soil Carbon Credits', 'Input Cost Reduction', 'TOTAL'],
        'Annual Amount': ['KES 175,000', '+ KES 21,000', '+ KES 62,500', '+ KES 25,000', 'KES 283,500'],
        'Details': ['Baseline KES 3,500/bag', 'Price alert +12%', 'Regenerative practices', 'Compost replaces synthetics', '+62% increase']
    }
    st.dataframe(pd.DataFrame(case2_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Case 3: Dairy
    st.subheader("🐄 Case 3: Improved Dairy System (10 cows)")
    case3_data = {
        'Revenue Stream': ['Milk Sales', 'Methane Reduction Credits', 'Feed Efficiency Gains', 'TOTAL'],
        'Annual Amount': ['KES 360,000', '+ KES 52,000', '+ KES 30,000', 'KES 442,000'],
        'Details': ['Baseline dairy income', 'Feed optimization protocol', 'Improved conversion ratio', '+23% increase']
    }
    st.dataframe(pd.DataFrame(case3_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.info("**Key Insight:** Carbon revenue provides 23-62% income increases while improving long-term farm sustainability and climate resilience.")

# TAB 5: COUNTY IMPACT
with tab5:
    st.header("🏛️ County-Wide Economic Impact")
    
    st.markdown("**Scaling carbon markets across Murang'a County.**")
    
    st.markdown("---")
    
    st.subheader("Phase 1 Projection: 10,000 Farmers (17% of registered)")
    
    county_data = {
        'Metric': ['Participating Farmers', 'Average Farm Size', 'Total Land Area', 'Annual Carbon Sequestration', 'Market Carbon Price', 'GROSS CARBON REVENUE', 'Farmer Share (70%)', 'Cooperative Share (20%)', 'Platform Operations (10%)'],
        'Value': ['10,000', '2.5 hectares', '25,000 hectares', '50,000 tCO₂e', '$25 / tCO₂e', '$1.25M/year', '$875,000', '$250,000', '$125,000'],
        'Context': ['Initial cohort', 'County average', 'Aggregated coverage', '2 tCO₂e/hectare', 'Current voluntary market', 'KES 162.5 million', 'KES 113.7M direct income', 'KES 32.5M reinvestment', 'KES 16.2M maintenance']
    }
    st.dataframe(pd.DataFrame(county_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    st.subheader("Strategic County Benefits:")
    st.markdown("""
    - **Household Income:** Average KES 11,370 additional income per farmer annually
    - **Cooperative Infrastructure:** KES 32.5M for storage, transport, training
    - **Climate Leadership:** First Kenyan county with operational carbon aggregation
    - **Investment Magnet:** Proven pipeline attracts climate finance
    - **Replication Blueprint:** Model for 46 other counties
    """)
    
    st.subheader("3-Year Scaling Roadmap:")
    
    scaling_data = {
        'Phase': ['Year 1: Pilot', 'Year 2: Expansion', 'Year 3: Scale'],
        'Farmers': ['5,000', '15,000', '30,000 (52%)'],
        'Annual Carbon Revenue': ['$625,000 (KES 81M)', '$1.875M (KES 244M)', '$3.75M (KES 487M)']
    }
    st.dataframe(pd.DataFrame(scaling_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.warning("**Economic Impact:** At full scale, the program generates KES 487 million annually in new county income, positioning Murang'a as Kenya's climate finance leader.")

# DEFINITIONS (Outside tabs, collapsible)
st.markdown("---")
with st.expander("📚 Key Terminology & Definitions"):
    definitions = [
        ("Carbon Credit", "A tradeable certificate representing 1 metric ton of CO₂ equivalent removed or avoided. Market pricing: $20-50 per credit."),
        ("Carbon Sequestration", "Capturing atmospheric CO₂ and storing it in biological reservoirs (trees, soil). Agricultural focus on land management."),
        ("Agroforestry", "Integration of trees into farming systems. Shade-grown coffee provides carbon storage and biodiversity benefits."),
        ("Regenerative Agriculture", "Soil health focus: minimal tillage, cover crops, biodiversity. Healthy soils sequester more carbon."),
        ("KIAMIS", "Kenya Integrated Agriculture Management Information System. National database of registered farmers."),
        ("MRV", "Measurement, Reporting, Verification. Standardized protocol for quantifying carbon reductions. GreenScope automates this."),
    ]
    
    for term, desc in definitions:
        with st.container():
            st.markdown(f"**{term}**")
            st.caption(desc)

# FOOTER
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%); border-radius: 16px; margin-top: 2rem; border: 1px solid #e2e8f0;">
    <div style="font-size: 1.5rem; font-weight: 700; color: #047857; margin-bottom: 0.5rem;">🌱 GreenScope Analytics</div>
    <div style="color: #64748b; margin-bottom: 1rem;">Transforming climate action into measurable farmer prosperity</div>
    <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
        <span style="background: white; padding: 0.5rem 1rem; border-radius: 9999px; font-size: 0.875rem; color: #059669; font-weight: 500; border: 1px solid #e2e8f0;">Simple</span>
        <span style="background: white; padding: 0.5rem 1rem; border-radius: 9999px; font-size: 0.875rem; color: #059669; font-weight: 500; border: 1px solid #e2e8f0;">Transparent</span>
        <span style="background: white; padding: 0.5rem 1rem; border-radius: 9999px; font-size: 0.875rem; color: #059669; font-weight: 500; border: 1px solid #e2e8f0;">Scalable</span>
        <span style="background: white; padding: 0.5rem 1rem; border-radius: 9999px; font-size: 0.875rem; color: #059669; font-weight: 500; border: 1px solid #e2e8f0;">Impactful</span>
    </div>
</div>
""", unsafe_allow_html=True)