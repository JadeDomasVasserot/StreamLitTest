import streamlit as st

st.title("Application Streamlit avec API intégrée")

st.header("Documentation API")
st.markdown(
    '<iframe src="http://localhost:8000/docs" width="100%" height="800"></iframe>',
    unsafe_allow_html=True,
)
# st.markdown(
#     '<iframe src="URL NGROK" width="100%" height="800"></iframe>',
#     unsafe_allow_html=True,
# )
