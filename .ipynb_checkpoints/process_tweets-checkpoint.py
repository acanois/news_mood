from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def add_to_df(analyzer, user, tweet, dataframe, write_row):
    sent_score = analyzer.polarity_scores(tweet['text'])
    dataframe.loc[write_row, 'Source'] = user
    dataframe.loc[write_row, 'Text'] = tweet['text']
    dataframe.loc[write_row, 'Date'] = tweet['created_at'] 
    dataframe.loc[write_row, 'Sent.Compound'] = sent_score['compound']
    dataframe.loc[write_row, 'Sent.Positive'] = sent_score['pos']
    dataframe.loc[write_row, 'Sent.Neutral'] = sent_score['neu']
    dataframe.loc[write_row, 'Sent.Negative'] = sent_score['neg']

def retrieve_tweets(api, user, file_name, dataframe, write_row):
    analyzer = SentimentIntensityAnalyzer()
    for curr_page in range(5):

        tweets = api.user_timeline(user, page=curr_page)
        
        for tweet in tweets:
            add_to_df(analyzer, user, tweet, dataframe, write_row)
            write_row += 1