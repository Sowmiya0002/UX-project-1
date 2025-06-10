import streamlit as st
import google.generativeai as genai
from streamlit_extras.add_vertical_space import add_vertical_space

# --- Gemini API Setup ---
genai.configure(api_key="AIzaSyCYZdy-q6TuvRFJP4XN8LSqWQsr4Yehwpg")
model = genai.GenerativeModel("gemini-2.0-flash")

# --- Page Config ---
st.set_page_config(page_title="UX Competitive Audit", layout="wide")

# --- Custom Banner ---
st.markdown("""
    <div style="background-color:#0E1117;padding:30px;border-radius:10px;margin-bottom:20px">
        <h1 style="color:#FFFFFF;text-align:center;"> UX Competitive Feature Comparator (AI-powered)</h1>
        <p style="color:#AAAAAA;text-align:center;font-size:18px;">
            Compare product features and discover actionable UX insights with AI.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- Intro Section ---
st.markdown("""
###  What Does This Tool Do?

This tool helps UX designers and product teams perform a quick competitive feature comparison.  
Just enter your product details and a competitor's URL — the AI will simulate an audit and provide key insights!

---
""")

# --- Input Form ---
with st.form("audit_form"):
    st.markdown("#### 🔷 Your Product Description / Feature List")
    your_product = st.text_area("Describe your product or list its main features:", height=180)

    st.markdown("#### 🔴 Competitor Website URL")
    competitor_url = st.text_input("Paste the competitor’s website URL:")

    add_vertical_space(1)
    submit = st.form_submit_button("🚀 Generate UX Report")

# --- Gemini Analysis ---
if submit:
    if not your_product or not competitor_url:
        st.warning("⚠️ Please provide both your product information and the competitor’s URL.")
    else:
        with st.spinner("🔍 Analyzing UX insights, please wait..."):
            prompt = f"""
You are a senior UX designer conducting a competitive audit.

Your client's product:
{your_product}

The competitor’s website to review is: {competitor_url}

Simulate the competitor’s feature set based on typical product sites and analyze the following:
- UX Strengths of competitor
- UX Weaknesses (including accessibility, usability, clarity)
- Design opportunities for your client
- Recommended improvements for your client to gain an edge

Format the output as a UX Designer's Insight Report with sections:
1. Feature Summary
2. UX Strengths
3. UX Weaknesses
4. Opportunities for Differentiation
5. Actionable Recommendations
"""

            response = model.generate_content(prompt)
            result = response.text

        st.markdown("## 📄 UX Designer’s Competitive Insight Report")
        st.markdown("---")
        st.markdown(result)

# --- Footer ---
st.markdown("""
---
<div style='text-align:center; color:gray; font-size:13px;'>
    Made by Sowmiya | SNS Ihub
</div>
""", unsafe_allow_html=True)
