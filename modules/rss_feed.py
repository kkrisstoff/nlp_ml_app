import pandas as pd
import feedparser

# url_link = "https://rss.nytimes.com/services/xml/rss/nyt/US.xml"
# rss_feed = RSSFeed(url_link)
#
# st.write(rss_feed.ndf)
# df_n = rss_feed.ndf['title']  # Extracting the 'title' column as the corpus for bigram extraction

class RSSFeed():
    ndf = ''
    feedurl = ""

    def __init__(self, paramrssurl):
        self.feedurl = paramrssurl
        self.ndf = self.parse()

    def parse(self):
        global ndf
        ndf = pd.DataFrame(columns=['title', 'link', 'description', 'published', 'content'])
        thefeed = feedparser.parse(self.feedurl)
        for thefeedentry in thefeed.entries:
            title = thefeedentry.get("title", "")
            link = thefeedentry.get("link", "")
            descr = thefeedentry.get("description", "")
            published = thefeedentry.get("published", "")
            content = ""
            if thefeedentry.get("content"):
                content = thefeedentry.get("content")[0].get("value", "")
            # Create a new DataFrame for the current row
            new_row_df = pd.DataFrame(
                [{
                    'title': title,
                    'link': link,
                    'description': descr,
                    'published': published,
                    'content': content
                }]
            )
            # Use concat to add the new row to ndf
            ndf = pd.concat([ndf, new_row_df], ignore_index=True)
        return ndf
