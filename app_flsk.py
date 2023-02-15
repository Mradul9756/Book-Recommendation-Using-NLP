from flask import Flask, request, render_template
#from flask_ngrok import run_with_ngrok
import pandas as pd
from top2vec import Top2Vec
#import threading
#import getpass
#import os
#from pyngrok import ngrok, conf


#os.environ["FLASK_ENV"] = "development"

#print("Enter your authtoken, which can be copied from https://dashboard.ngrok.com/auth")
#conf.get_default().auth_token = getpass.getpass()

app = Flask(__name__)
#run_with_ngrok(app)

#port = 5001

#Open a ngrok tunnel to the HTTP server
#public_url = ngrok.connect(port).public_url
#print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

# Update any base URLs to use the public ngrok URL
#app.config["BASE_URL"] = public_url

# Start the Flask server in a new thread
#threading.Thread(target=app.run, kwargs={"use_reloader": False}).start()

model = Top2Vec.load('models/book_recomm_model.vec')

#with open('/content/drive/MyDrive/Colab Notebooks/templates/index.html') as index:
#  index_html = index.read()

#with open('/content/drive/MyDrive/Colab Notebooks/templates/results.html') as results:
#  results_html = results.read()

def load_df():
    with pd.read_csv('dataset/amazon_reviews_books.csv', 
                 chunksize=10000, 
                 nrows = 100000,
                 sep=',' , 
                 usecols=['product_title','review_body','star_rating'],
                 ) as reader:
    
        df_small = pd.DataFrame()
        for chunk in reader:
          df_small = pd.concat([df_small, chunk])
     
    return df_small

df_small = load_df()

@app.route('/', methods=["GET"])
def index():
  return render_template('index.html')

@app.route("/results/", methods=['GET'])
def results():
    query = request.args.get('query')
     
    if query:
       documents, document_scores, document_ids = model.query_documents(query, num_docs=5)
       results = df_small.loc[document_ids,['product_title','star_rating','review_body']]
       results.sort_values(by=['star_rating'], ascending=False)
       results = results.to_html()

    return render_template('results.html', results=results)


if __name__ == "__main__":
    app.run()