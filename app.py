import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
import cufflinks

from modules.rss_feed import RSSFeed
from modules.intro import render_intro
from modules.snapshot import render_snapshot
from modules.word_cloud import render_word_cloud
from modules.unigrams import render_unigrams
from modules.bigrams import render_bigrams
from modules.trigrams import render_trigrams
from modules.topic_modeling import render_topic_modeling
from modules.text_summarization import render_text_summarization
from modules.parts_of_speech import render_parts_of_speech
from modules.text_stat import render_text_stat
from modules.entity_extraction import render_entity_extraction
from modules.analysis_textBlob import render_textBlob_analysis
from modules.analysis_vader import render_vader_analysis

nltk.download('punkt')
cufflinks.go_offline()
cufflinks.set_config_file(world_readable=True, theme='pearl')


@st.cache_data
def full_text(my_url):
    article = requests.get(my_url)
    articles = BeautifulSoup(article.content, 'html.parser')
    articles_body = articles.find_all('body')
    p_blocks = articles_body[0].find_all('p')
    p_blocks_df = pd.DataFrame(columns=['element_name', 'parent_hierarchy', 'element_text', 'element_text_Count'])

    for p_block in p_blocks:
        parents_list = [parent.name + 'id: ' + parent.get('id', '') for parent in p_block.parents if parent is not None]
        parents_list.reverse()
        parent_hierarchy = ' -> '.join(parents_list)
        new_row = pd.DataFrame([{
            "element_name": p_block.name,
            "parent_hierarchy": parent_hierarchy,
            "element_text": p_block.text,
            "element_text_Count": len(p_block.text)
        }])
        p_blocks_df = pd.concat([p_blocks_df, new_row], ignore_index=True)

    if len(p_blocks_df) > 0:
        p_blocks_df_groupby = p_blocks_df.groupby('parent_hierarchy')['element_text_Count'].sum().reset_index()
        max_hierarchy = p_blocks_df_groupby.loc[p_blocks_df_groupby['element_text_Count'].idxmax(), 'parent_hierarchy']
        merged_text = '\n'.join(p_blocks_df.loc[p_blocks_df['parent_hierarchy'] == max_hierarchy, 'element_text'])
    else:
        merged_text = ''

    return merged_text


@st.cache_data
def preprocess(review_text):
    review_text = review_text.str.replace("(<br/>)", "")
    review_text = review_text.str.replace('(<a).*(>).*(</a>)', '')
    review_text = review_text.str.replace('(&amp)', '')
    review_text = review_text.str.replace('(&gt)', '')
    review_text = review_text.str.replace('(&lt)', '')
    review_text = review_text.str.replace('(\xa0)', ' ')
    return review_text


# st.set_page_config(layout="wide")
st.title('News Articles Analysis -NLP App')
st.header("""
This app displays the news articles appeared in the top News Publications!
""")

st.sidebar.header('Please select the news org from the dropdown list')
lnews = ["NY Times", "LA Times", "CNN", "Washington Post", "USA Today"]
s_news = st.sidebar.selectbox('News', lnews)
st.sidebar.header('Please select the Function')

lnlp = ["Intro", "Snapshot", "Unigrams", "Bigrams", "Trigrams", "WordCloud", "Text Stat", "Topic Modeling",
        "Entity Extraction", "Sentiment Analysis TextBlob", "Sentiment Analysis-Vader", "Text Summarization",
        "Parts of Speech"]

s_nlp = st.sidebar.selectbox('Functions', lnlp)


def load_data(news, nlp):
    if news == "NY Times":
        # st.write(news)
        # st.write(nlp)
        if nlp == "Intro":
            render_intro()

        url_link = "https://rss.nytimes.com/services/xml/rss/nyt/US.xml"
        rss_feed = RSSFeed(url_link)
        df = rss_feed.ndf
        # st.header('Display the dataframe')
        # st.dataframe(df)
        pd.set_option('display.max_rows', df.shape[0] + 1)
        df.reset_index(inplace=True, drop=True)
        for ind in df.index:
            url = df['link'][ind]
            text = full_text(url)
            df['content', ind] = text

        # Build the corpus.
        corpus = []
        for ind in df.index:
            # corpus = df['content'][ind]
            corpus.append(df['title'][ind])

        df = df.dropna()
        df_n = df
        df_n['title'] = preprocess(df['title'])

        if nlp == "Snapshot":
            render_snapshot(df)

        if nlp == "WordCloud":
            render_word_cloud(df)

        if nlp == "Unigrams":
            render_unigrams(df_n)

        if nlp == "Bigrams":
            render_bigrams(df_n)

        if nlp == 'Trigrams':
            render_trigrams(df_n)

        if nlp == "Sentiment Analysis TextBlob":
            render_textBlob_analysis(df)

        if nlp == "Sentiment Analysis-Vader":
            render_vader_analysis(df)

        if nlp == "Entity Extraction":
            render_entity_extraction(df)

        if nlp == "Topic Modeling":
            render_topic_modeling(df)

        if nlp == "Text Summarization":
            render_text_summarization(df)

        if nlp == "Parts of Speech":
            render_parts_of_speech(df)

        if nlp == "Text Stat":
            render_text_stat(df)


load_data(s_news, s_nlp)
