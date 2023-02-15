import pandas as pd 
import numpy as np
from top2vec import Top2Vec
import streamlit as st

model = Top2Vec.load('models/book_recomm_model.vec')

with pd.read_csv('dataset/amazon_reviews_books.csv', 
                chunksize=10000, 
                #sep='\\t' , 
                engine = 'python',
                usecols=['product_title','product_parent','review_headline','review_body','review_date','star_rating'],
                nrows= 100000) as reader:
    
    df = pd.DataFrame()
    for chunk in reader:
        df = pd.concat([df, chunk])

def submit():
    if query != "":
        documents, document_scores, document_ids = model.query_documents(query, num_docs=5)
        results = df.loc[document_ids,['product_title','star_rating','review_body']]
        
        st.dataframe(results)
        

    if keywords != "":
        documents, document_scores, document_ids = model.search_documents_by_keywords(
            keywords=[keywords], num_docs=5)

        results = df.loc[document_ids,['product_title','star_rating','review_body']]
        
        st.dataframe(results)

st.write("What kind of book are you looking for?")

query = st.text_area(label="Describe an ideal book or book title")

st.write('Or search by keywords' )

keywords = st.text_input(label="Separate keywords using a comma")

#st.button("Clear",on_click=clear)

st.button("Submit", on_click=submit())

 

        

