import streamlit as st
import requests

API_URL = "http://localhost:8000/verify"

st.set_page_config(page_title="Udyam Verifier", page_icon="🏢")

st.title("Udyam Verifier")

st.markdown("Enter the Udyam Registration Number and Company Name to verify.")

udyam_no = st.text_input("Udyam Registration Number (e.g. UDYAM-XX-00-0000000)")
company_name = st.text_input("Company Name")

if st.button("Verify", type="primary"):
    if not udyam_no or not company_name:
        st.error("Please provide both Udyam Number and Company Name.")
    else:
        with st.spinner("Verifying... This may take up to a minute due to CAPTCHA solving."):
            try:
                response = requests.post(
                    API_URL, 
                    json={"udyam_no": udyam_no, "company_name": company_name},
                    timeout=90
                )
                response.raise_for_status()
                result = response.json()
                
                if result.get("status") == "valid":
                    st.success(" Registration Valid")
                    st.json(result)
                elif result.get("status") == "not verified":
                    st.warning(f" Not Verified: {result.get('reason')}")
                    st.json(result)
                elif "error" in result:
                    st.error(f" Error: {result.get('error')}")
                else:
                    st.info("Result:")
                    st.json(result)
            except requests.exceptions.RequestException as e:
                st.error(f"Failed to connect to the API. Make sure the FastAPI backend is running at {API_URL}\n\nDetails: {e}")
