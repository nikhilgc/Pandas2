#Article Views 1

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id']== views['viewer_id']]
    df = df.drop_duplicates(subset=['author_id'],inplace=False)
    df.sort_values(by = ['author_id'], inplace=True) 
    df=df[['author_id']]
    return df.rename(columns = {'author_id':'id'})
    


#Invalid Tweets

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

	df = tweets[tweets['content'].str.len() > 15]
	return df[['tweet_id']]

    