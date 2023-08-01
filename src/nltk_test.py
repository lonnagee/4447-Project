# %%
import pandas as pd
import numpy as np
import emoji
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# %%
reviews_df = pd.read_csv('../data/yelp_academic_dataset_review.csv')

# %%
reviews_df.head()