import streamlit as st
import google.generativeai as genai

# --- Gemini API Setup ---
genai.configure(api_key="AIzaSyCYZdy-q6TuvRFJP4XN8LSqWQsr4Yehwpg")
model = genai.GenerativeModel("gemini-2.0-flash")

# --- Streamlit UI ---
st.set_page_config(page_title="UX Competitive Audit", layout="wide")
st.title("UX Competitive Feature Comparator (AI-powered)")

st.markdown("""
Provide a brief description of your product and the competitor’s website URL.  
This AI tool simulates a competitive UX audit and generates designer-friendly insights.
""")

with st.form("audit_form"):
    your_product = st.text_area("🟦 Your Product Description / Feature List", height=200)
    competitor_url = st.text_input("🟥 Competitor Website URL")

    submit = st.form_submit_button("Compare features")

# --- Gemini Analysis ---
if submit:
    if not your_product or not competitor_url:
        st.warning("Please provide both your product info and the competitor's URL.")
    else:
        with st.spinner("Generating UX insights..."):
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
            result = response.text  # ✅ Corrected here

        st.markdown("## 📄 UX Designer’s Competitive Insight Report")
        st.markdown(result)
