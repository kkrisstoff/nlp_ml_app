import streamlit as st
from collections import Counter
import seaborn as sns
import spacy as spacy


# Entity recognition
def plot_most_common_named_entity_barchart(text, entity="PERSON"):
    nlp = spacy.load("en_core_web_sm")

    def _get_ner(text, ent):
        doc = nlp(text)
        return [X.text for X in doc.ents if X.label_ == ent]

    entity_filtered = text.apply(lambda x: _get_ner(x, entity))
    entity_filtered = [i for x in entity_filtered for i in x]

    counter = Counter(entity_filtered)
    x, y = map(list, zip(*counter.most_common(10)))
    sns.barplot(x=y, y=x).set_title(entity)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()


def render_entity_extraction(df):
    st.write(" ")
    st.write(" ")
    st.header("Entity Extraction")
    st.write(" ")
    # st.write(" ")
    st.subheader(
        "Named entity recognition is an information extraction method in which entities that are present in the text are classified into predefined entity types like “Person”,” Place”,” Organization”, etc.By using NER we can get great insights about the types of entities present in the given text dataset.")
    st.write(" ")
    st.write(" ")
    plot_most_common_named_entity_barchart(df['title'], entity="PERSON")