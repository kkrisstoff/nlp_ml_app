import streamlit as st


def render_snapshot(df):
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.subheader('Display the dataframe')
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.dataframe(df)
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.markdown("""

                                                                                   """, unsafe_allow_html=True)
    st.markdown('The no of articles :', unsafe_allow_html=True)
    st.write(df.shape[0])
    st.write(" ")
    st.write("The Url Link ")
    for index, row in df.iterrows():
        st.write(row['link'])
