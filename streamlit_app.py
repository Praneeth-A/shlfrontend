
import streamlit as st
import requests

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")
st.title("SHL Assessment Recommender")

# Input box
query = st.text_area("Enter job description or requirement", height=150)

# Button to trigger recommendation
if st.button("Get Recommendations"):
    if not query.strip():
        st.warning("Please enter a query to proceed.")
    else:
        with st.spinner("Fetching recommendations..."):
            try:
                response = requests.post(
                    "https://shlbackend.onrender.com/recommend",
                    json={"query": query},
                    timeout=360  # reasonable timeout to avoid hanging
                )

                
                data = response.json()
                if data:
                    st.markdown("### ✅ Recommended Assessments")
                    st.table(data)
                else:
                    st.warning("No relevant assessments found.")

            except requests.exceptions.RequestException as e:
                st.error(f"🚨 Network error: {e}")
