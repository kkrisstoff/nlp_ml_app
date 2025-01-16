import streamlit as st
import inspect
import textstat


def render_text_stat(df):
    st.markdown("""

        """, unsafe_allow_html=True)

    textstat.set_lang("en")
    text = df['content', 2]
    funcs = ["textstat." + inspect.getmembers(textstat, predicate=inspect.ismethod)[i][0] for i in range(1, 28)]
    st.write(" ")
    st.markdown(
        'Textstat is an easy to use library to calculate statistics from text. It helps determine readability, complexity, and grade level.',
        unsafe_allow_html=True)
    st.write(" ")
    for elem in funcs:
        method = eval(elem)
        textstat.set_lang("en")
        w_1 = (elem.split(".")[1])
        st.write(w_1)
        st.write(method(text))
        st.write(" ")