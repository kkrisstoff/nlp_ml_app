import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def render_word_cloud(df):
    X_train1 = df['title']

    st.markdown("""

                                                                                """, unsafe_allow_html=True)
    st.write(' ')
    st.markdown('WordCloud', unsafe_allow_html=True)
    st.write(' ')
    st.markdown(
        'Word clouds or tag clouds are graphical representations of word frequency that give greater prominence to words that appear more frequently in a source text. The larger the word in the visual the more common the word was in the document(s).',
        unsafe_allow_html=True)
    st.write(' ')
    st.write(' ')
    long_string = ','.join(list(X_train1.values))
    # Create a WordCloud object
    wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
    # Generate a word cloud
    wordcloud.generate(long_string)
    # Visualize the word cloud
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud)
    st.image(wordcloud.to_array(), width=700)
    st.write("Word Cloud")
    # Generate word cloud
    long_string = ','.join(list(X_train1.values))
    wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color='salmon',
                          colormap='Pastel1',
                          collocations=False, stopwords=STOPWORDS).generate(long_string)
    # Visualize the word cloud
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud)
    st.image(wordcloud.to_array(), width=700)
    st.write("Word Cloud")
    wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color='black', colormap='Set2',
                          collocations=False, stopwords=STOPWORDS).generate(long_string)
    # Visualize the word cloud
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud)
    st.image(wordcloud.to_array(), width=700)
    # wordcloud.to_image()
