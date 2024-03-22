import streamlit as st

def redirect_url(language):
    if language == 'English':
        return 'https://gaienglish.streamlit.app/'
    elif language == 'German':
        return 'https://gaifinnish.streamlit.app/'
    elif language == 'Finnish':
        return 'https://gaifinnish.streamlit.app/'

def main():
    st.title('Language Redirect App')
    language = st.selectbox('Select Language', ['English', 'German', 'Finnish'])
    if st.button('Go'):
        url = redirect_url(language)
        st.success(f'Redirecting to {url}')
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={url}" />', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
