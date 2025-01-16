import streamlit as st
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser


def render_text_summarization(df):
    st.write(" ")
    st.write(" ")
    st.header("Text Summarization")
    st.write(" ")
    st.subheader(
        "Text summarization refers to the technique of shortening long pieces of text. The intention is to create a coherent and fluent summary having only the main points outlined in the document.Automatic text summarization is a common problem in machine learning and natural language processing (NLP).")
    st.write(" ")
    st.write(" ")

    # dfs = df['content']
    for index, row in df.iterrows():
        parser = PlaintextParser.from_string(row['content'], Tokenizer("english"))
        # Using LexRank
        summarizer = LexRankSummarizer()
        # Summarize the document with 4 sentences
        summary = summarizer(parser.document, 3)
        st.write("Summarized Document")
        st.write(" ")
        st.write(row['title'])
        st.write(" ")
        for sentence in summary:
            # st.write("Summarized Document")
            # st.write(row['title'])
            st.write(sentence)