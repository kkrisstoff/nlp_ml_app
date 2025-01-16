import streamlit as st
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
import seaborn as sns


# Parts of Speech Tagging
def plot_parts_of_speach_barchart(text):
    # Ensure the necessary NLTK models and corpora are downloaded
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt')

    def _get_pos(text):
        # Tokenize the text and get part-of-speech tags
        pos = nltk.pos_tag(word_tokenize(text))
        # Check if pos is not empty before accessing
        if pos:
            pos = list(map(list, zip(*pos)))[1]
            return pos
        return []

    # Apply the function to each text entry, ensuring text is not empty
    tags = text.apply(lambda x: _get_pos(x) if x.strip() != '' else [])
    # Flatten the list of lists into a single list of tags
    tags = [x for sublist in tags for x in sublist]

    # Check if tags is not empty
    if tags:
        counter = Counter(tags)
        x, y = list(map(list, zip(*counter.most_common(7))))
        sns.barplot(x=y, y=x)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    else:
        st.write("No part-of-speech tags to display.")


def render_parts_of_speech(df):
    st.markdown("""

                        """, unsafe_allow_html=True)
    st.write(" ")
    st.markdown('Noun (NN)- Joseph, London, table, cat, teacher, pen, city', unsafe_allow_html=True)
    st.markdown('Verb (VB)- read, speak, run, eat, play, live, walk, have, like, are, is',
                unsafe_allow_html=True)
    st.markdown('Adjective(JJ)- beautiful, happy, sad, young, fun, three', unsafe_allow_html=True)
    st.markdown('Adverb(RB)- slowly, quietly, very, always, never, too, well, tomorrow', unsafe_allow_html=True)
    st.markdown('Preposition (IN)- at, on, in, from, with, near, between, about, under', unsafe_allow_html=True)
    st.markdown('Conjunction (CC)- and, or, but, because, so, yet, unless, since, if', unsafe_allow_html=True)
    st.markdown('Pronoun(PRP)- I, you, we, they, he, she, it, me, us, them, him, her,this',
                unsafe_allow_html=True)
    st.markdown('Interjection (INT)- Ouch! Wow! Great! Help! Oh! Hey! Hi!', unsafe_allow_html=True)
    plot_parts_of_speach_barchart(df['content'])
