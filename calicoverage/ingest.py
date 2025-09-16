import os
import pandas as pd

import minsearch

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data')
DATA_FILE = os.path.join(DATA_PATH, 'cms_faq.csv')

def load_index(data_path=DATA_FILE):
    df = pd.read_csv(data_path)
    
    documents = df.to_dict(orient='records')

    index = minsearch.Index(
        text_fields=['category',
                     'question',
                     'answer'],
        keyword_fields=['id'])

    index.fit(documents)

    return index