import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt


@st.cache_data
def sentiment_textblob(text):
    x = TextBlob(text).sentiment.polarity

    if x < 0:
        return 'neg'
    elif x == 0:
        return 'neu'
    else:
        return 'pos'


def plot_sentiment_barchart(text):
    sentiment = text.map(lambda x: sentiment_textblob(x))

    plt.bar(sentiment.value_counts().index,
            sentiment.value_counts(), color=['cyan', 'red', 'green', 'black'], edgecolor='yellow')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()



def render_textBlob_analysis(df):
    st.markdown("""

                                    """, unsafe_allow_html=True)
    t_word = "The sentiment property returns a namedtuple of the form Sentiment(polarity, subjectivity). The polarity score is a float within the range [-1.0, 1.0]. The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective."
    st.write(' ')
    st.markdown('TextBlob Sentiment Analyzer', unsafe_allow_html=True)
    st.write(' ')
    st.markdown(
        'The sentiment property returns a namedtuple of the form Sentiment(polarity, subjectivity). The polarity score is a float within the range [-1.0, 1.0]. The subjectivity is a float within the range [0.0, 1.0]',
        unsafe_allow_html=True)
    st.write(' ')
    st.write(' ')
    plot_sentiment_barchart(df['title'])
