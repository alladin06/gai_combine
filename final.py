import streamlit as st
import webbrowser
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
        if language=='English':
            webbrowser.open_new_tab("https://gaienglish.streamlit.app/")
        elif language=='German':
           webbrowser.open_new_tab("https://gaigerman.streamlit.app/") 
        else:
            webbrowser.open_new_tab("https://gaifinnish.streamlit.app/")

if __name__ == "__main__":
    main()

