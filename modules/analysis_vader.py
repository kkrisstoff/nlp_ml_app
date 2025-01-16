import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Download vader_lexicon resource
import nltk
nltk.download('vader_lexicon')

@st.cache_data
def sentiment_vader(text):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(text)
    ss.pop('compound')
    return max(ss, key=ss.get)


def plot_sentiment_barchart(text):
    sentiment = text.map(sentiment_vader)  # No need to pass sid anymore

    # Plotting
    plt.bar(sentiment.value_counts().index,
            sentiment.value_counts(), color=['cyan', 'red', 'green', 'black'], edgecolor='yellow')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()


def render_vader_analysis(df):
    st.markdown("""

                                    """, unsafe_allow_html=True)
    st.write(' ')
    st.markdown('Vader Sentiment Analyzer', unsafe_allow_html=True)
    st.write(' ')
    st.markdown(
        'VADER ( Valence Aware Dictionary for Sentiment Reasoning) is a model used for text sentiment analysis that is sensitive to both polarity (positive/negative) and intensity (strength) of emotion. ... VADER sentimental analysis relies on a dictionary that maps lexical features to emotion intensities known as sentiment scores.',
        unsafe_allow_html=True)
    st.write(' ')
    st.write(' ')
    plot_sentiment_barchart(df['title'])
