import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.feature_extraction.text import CountVectorizer


# Get top words
@st.cache_data
def get_top_n_words(corpus, n=None):
    vec = CountVectorizer(stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:n]

def render_unigrams(df):
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

    common_words = get_top_n_words(df['title'], 10)
    # for word, freq in common_words:
    #    (word, freq)
    df2 = pd.DataFrame(common_words, columns=['Words', 'Count'])
    st.table(df2)
    # st.bar_chart(df2["Words"])
    with st.echo(code_location='below'):
        fig = px.scatter(
            x=df2["Words"],
            y=df2["Count"],
            color=df2["Count"],
        )
        fig.update_layout(
            xaxis_title="Words",
            yaxis_title="Count",
        )

        # st.write(fig)
        st.plotly_chart(fig)