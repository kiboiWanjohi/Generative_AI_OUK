import streamlit as st
import requests
import json

st.set_page_config(page_title="Codebase Genius", layout="wide")

st.markdown("""
    <style>
    .title { font-size: 3em; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("#  Codebase Genius")
st.markdown("#### AI-powered code documentation generator")
st.markdown("##### By Braimer Omondi")

col1, col2 = st.columns([3, 1])

with col1:
    repo_url = st.text_input(
        "GitHub Repository URL:",
        placeholder="https://github.com/username/repo",
        value="https://github.com/pallets/flask"
    )

with col2:
    analyze_button = st.button(" Analyze")

if analyze_button and repo_url:
    with st.spinner("Analyzing repository..."):
        try:
            response = requests.post(
                f"http://localhost:8001/analyze",
                params={"repo_url": repo_url},
                timeout=60
            )
            
            if response.status_code == 200:
                data = response.json()
                
                st.success("Analysis Complete!")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("###  Code Structure")
                    code_structure = data.get("code_structure", {})
                    st.json(code_structure)
                
                with col2:
                    st.markdown("###  Modules")
                    for module in code_structure.get("modules", []):
                        st.markdown(f"- `{module}`")
                
                st.markdown("---")
                st.markdown("###  Generated Documentation")
                
                markdown_doc = data.get("markdown", "")
                st.markdown(markdown_doc)
                
                st.download_button(
                    label="⬇ Download Markdown",
                    data=markdown_doc,
                    file_name="documentation.md",
                    mime="text/markdown"
                )
            else:
                st.error(f"Error: {response.json().get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f" Error: {str(e)}")
else:
    st.info("Enter a repository URL and click 'Analyze' to generate documentation")
