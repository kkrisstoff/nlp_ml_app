import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.feature_extraction.text import CountVectorizer

@st.cache_data
def get_top_n_bigram(corpus, n=None):
    vec = CountVectorizer(ngram_range=(2, 2), stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:n]


def render_bigrams(df):
    st.markdown("""

                                                             """, unsafe_allow_html=True)
    st.write(' ')
    st.markdown('N Grams', unsafe_allow_html=True)
    st.write(' ')
    st.markdown(
        'N-grams of texts are extensively used in text mining and natural language processing tasks. They are basically a set of co-occuring words within a given window and when computing the n-grams you typically move one word forward (although you can move X words forward in more advanced scenarios). When N=1, this is referred to as unigrams and this is essentially the individual words in a sentence. When N=2, this is called bigrams and when N=3 this is called trigrams. When N>3 this is usually referred to as four grams or five grams and so on.',
        unsafe_allow_html=True)
    st.write(' ')
    st.write(' ')
    common_words = get_top_n_bigram(df['title'], 10)
    df4 = pd.DataFrame(common_words, columns=['Bigrams', 'Count'])
    st.table(df4)
    fig = px.bar(df4, x='Bigrams', y='Count', color='Count', height=500)
    st.plotly_chart(fig)