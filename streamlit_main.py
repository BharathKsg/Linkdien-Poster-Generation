import streamlit as st
import requests

# FastAPI URL
FASTAPI_URL = "http://localhost:8000/generate_linkedin_post"

# Streamlit UI Components
st.title("LinkedIn Post Generator")

# Get article summary input
article_summary = st.text_area("Enter Article Summary:", height=150)

# Get perspectives input (as comma-separated list)
perspectives_input = st.text_area("Enter Perspectives (comma separated):", height=100)
perspectives = [p.strip() for p in perspectives_input.split(',')] if perspectives_input else []

# Generate button
if st.button("Generate LinkedIn Post"):
    if article_summary and perspectives:
        # Prepare request payload
        payload = {
            "article_summary": article_summary,
            "perspectives": perspectives
        }
        
        # Call FastAPI endpoint
        response = requests.post(FASTAPI_URL, json=payload)
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            linkedin_post = result["linkedin_post"]
            confidence_score = result.get("confidence_score", "N/A")
            
            # Display the result
            st.subheader("Generated LinkedIn Post:")
            st.write(linkedin_post)
            st.subheader("Confidence Score:")
            st.write(confidence_score)
        else:
            st.error("Failed to generate LinkedIn post. Please try again.")
    else:
        st.warning("Please provide both the article summary and perspectives.")

