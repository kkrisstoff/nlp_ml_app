import streamlit as st
import warnings
from sklearn.feature_extraction.text import CountVectorizer


# Helper function
def print_topics(model, count_vectorizer, n_top_words):
    words = count_vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(model.components_):
        w_stl = (" ".join([words[i]
                           for i in topic.argsort()[:-n_top_words - 1:-1]]))
        st.write(w_stl)


def render_topic_modeling(df):
    st.write(" ")
    st.write(" ")
    st.header("Topic Modeling")
    st.write(" ")
    # st.write(" ")
    st.subheader(
        "Topic modeling is a method for unsupervised classification of documents, similar to clustering on numeric data, which finds some natural groups of items (topics) even when we’re not sure what we’re looking for.Topic modeling provides methods for automatically organizing, understanding, searching, and summarizing large electronic archives.")
    st.write(" ")
    st.write(" ")

    warnings.simplefilter("ignore", DeprecationWarning)
    # Load the LDA model from sk-learn
    from sklearn.decomposition import LatentDirichletAllocation as LDA

    # Tweak the two parameters below
    number_topics = 10
    number_words = 6
    X_train1 = df['content']
    # Initialise the count vectorizer with the English stop words
    count_vectorizer = CountVectorizer(stop_words='english')
    # Fit and transform the processed titles
    count_data = count_vectorizer.fit_transform(X_train1)
    # Create and fit the LDA model
    lda = LDA(n_components=number_topics, n_jobs=-1)
    lda.fit(count_data)
    # Print the topics found by the LDA model
    st.write("Topics:")
    print_topics(lda, count_vectorizer, number_words)