import streamlit as st

# Define URLs for each language
urls = {
    "English": "https://example.com/english",
    "German": "https://example.com/german",
    "Finnish": "https://example.com/finnish"
}

# Streamlit app
def main():
    st.title("Language Selection")
    
    # Ask user to choose a language
    language = st.selectbox("Choose a language", list(urls.keys()))
    
    # Redirect to the corresponding website based on the selected language
    if st.button("Go to Website"):
        selected_url = urls.get(language)
        if selected_url:
            st.write(f"Redirecting to {selected_url}...")
            # You can use st.markdown to open the website in an iframe
            st.markdown(f'<iframe src="{selected_url}" width="800" height="600"></iframe>', unsafe_allow_html=True)
        else:
            st.error("Invalid language selection")

if __name__ == "__main__":
    main()
