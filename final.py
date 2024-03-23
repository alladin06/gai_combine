import streamlit as st
import requests

def redirect_url(language):
    if language == 'English':
        return 'https://gaienglish.streamlit.app/'
    elif language == 'German':
        return 'https://gaigerman.streamlit.app/'
    elif language == 'Finnish':
        return 'https://gaifinnish.streamlit.app/'

def main():
    st.title('Language Redirect App')
    language = st.selectbox('Select Language', ['English', 'German', 'Finnish'])
    if st.button('Go'):
        url = redirect_url(language)
        response = requests.get(url)
        if response.status_code == 200:
            st.success(f"Redirecting to {language} site...")
            st.write(f"Redirect URL: {response.url}")
        else:
            st.error("Failed to redirect")

if __name__ == "__main__":
    main()
