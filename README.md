# Book-Recommendation-Using-NLP

DOCUMENTATION OF CONCEPTS AND WORKFLOW
In natural language understanding (NLU) tasks, there is a hierarchy of lenses through which we can extract meaning — from words to sentences to paragraphs to documents. At the document level, one of the most useful ways to understand text is by analyzing its topics (also refer NER). The process of learning, recognizing, and extracting these topics across a collection of documents is called topic modeling.
Overview
All topic models are based on the same basic assumption:
● each document consists of a mixture of topics, and
● each topic consists of a collection of words.
In other words, topic models are built around the idea that the semantics of our document are actually being governed by some hidden, or “latent,” variables that we are not observing. As a result, the goal of topic modeling is to uncover these latent variables — topics — that shape the meaning of our document and corpus.
Topic Modeling Difference and Related Algorithms
Topic Modeling is performed on unsupervised information and has a clear distinction from text classification and clustering tasks. Unlike text classification or clustering, which aims to make information retrieval easy, and make clusters of documents, Topic Modeling is not aiming to find similarities in documents. In Topic Modeling, usually, there is a plurality of topics, and text is distributed.
Topic Modeling makes clusters of three types of words – co-occurring words; distribution of words, and histogram of words topic-wise. There are several Topic Modeling models such as bag-of-words, unigram model, generative model.
The best and frequently used   to define and work out with Topic Modeling that digs out topic probabilities from statistical
data available. While using the Topic Modeling methodology, there are some challenges. One of the first challenges faced is that Topic Modeling doesn’t provide a fixed number of topics, hence, approaches such as the LDA or LSA
Topic Modeling methods and techniques are used for extensive text mining tasks. This approach is known for handling long format content and lesser effective for working out with short text. It is essentially used in machine learning for finding thematic relations in a large collection of documents with textual data.
 is LDA or Latent Dirichlet Allocation
algorithm
 conditioning to handle issues like overfitting, non-linearity, and discovery of too
require
  many generic words which are not useful.
 
 Applications of Topic Modeling
● text mining
● text classification
● text summarization,
● information retrieval,
● and recommendation engines.
LDA
The algorithm was first introduced in 2003 and treats topics as probability distributions for the occurrence of different words.
Top2Vec
With the introduction of transformer models and embedding algorithms such as Doc2Vec,
. In fact, an algorithm called Top2Vec makes it possible to build topic models using embedding vectors and clustering.
How does Top2Vec work?
Top2Vec is an algorithm that detects topics present in the text and generates jointly embedded topic, document, and word vectors. At a high level, the algorithm performs the following steps to discover topics in a list of documents.
1. Generate embedding vectors for documents and words.
2. Perform dimensionality reduction on the vectors using an
algorithm such as UMAP.
3. Cluster the vectors using a clustering algorithm such as
HDBSCAN.
4. Assign topics to each cluster.
While Top2Vec is much more complex than the standard LDA approach to topic modeling, it may be able to give us better results since the embedding vectors for words and documents can effectively capture the meaning of words and phrases.
Summary
Top2Vec is a recently developed topic modeling algorithm that may replace LDA in the near future. Unlike LDA, Top2Vec generates jointly embedded word and document vectors and clusters these vectors in order to find topics within text data.
we can create much more sophisticated topic models that capture semantic
 similarities in words
   
 DEPLOYMENT ON GOOGLE APP ENGINE
App Engine applications automatically scale based on incoming traffic. Load balancing, microservices, authorization, SQL and NoSQL databases, traffic splitting, logging, search, versioning, roll out and roll backs, and security scanning are all supported natively and are highly customizable.
App Engine's Flexible Environment supports a host of programming languages, including Java, Python, PHP, NodeJS, Ruby, and Go. App Engine's Standard Environment is an additional option for certain languages including Python. The two environments give users maximum flexibility in how their application behaves since each environment has certain strengths.
Activate Cloud Shell
Cloud Shell is a virtual machine that is loaded with development tools. It offers a persistent 5GB home directory and runs on the Google Cloud. Cloud Shell provides command-line access to your Google Cloud resources
Authenticate API requests
The Datastore, Storage, and Vision APIs are automatically enabled for you in this lab. In order to make requests to the APIs, you will need service account credentials.
Creating an App Engine app

 1. Next, create an App Engine instance by using:
gcloud app create
Creating a storage bucket
1. First, set the environment variable CLOUD_STORAGE_BUCKET
Sample code layout
The sample has the following layout:
templates/
  homepage.html
/* HTML template that uses Jinja2 */
/* App Engine application configuration file */
/* Python Flask web application */
app.yaml
main.py
requirements.txt /* List of dependencies for the project */ Copied!
content_copy
main.py
This Python file is a Flask web application. The application allows users to submit photos (preferably of faces), which are stored in Cloud Storage and analyzed using the face detection feature of the Cloud Vision API. Key information about each photo

 is stored in Datastore, Google Cloud's NoSQL database, where it is accessed each time a user visits the website.
This application uses the Google Cloud client libraries for Storage, Datastore, and Vision. These client libraries make it easy to access Cloud APIs from your favorite programming languages.
Let's take a look at some key snippets of the code.
The imports section at the top is where we import the various packages we need for our code. This is how we import our Google Cloud client libraries for Datastore, Storage, and Vision:
from google.cloud import datastore
from google.cloud import storage
from google.cloud import vision
Code that directs what happens when a user visits the root URL of the website
Here is the code for what happens when a user visits the root URL of the website. A Datastore client object is created, which is used to access the Datastore client library. A query on Datastore is run for entities of kind Faces. Finally, the HTML template is rendered, passing in the image_entities we extract from Datastore as a variable.
@app.route('/')
def homepage():

 # Create a Cloud Datastore client.
    datastore_client = datastore.Client()
    # Use the Cloud Datastore client to fetch information from
Datastore about
# each photo.
    query = datastore_client.query(kind='Faces')
    image_entities = list(query.fetch())
    # Return a Jinja2 HTML template and pass in image_entities as a
parameter.
    return render_template('homepage.html',
image_entities=image_entities)
Datastore is Google Cloud's NoSQL database solution. Data is stored in objects called entities. Each entity is assigned a unique identifying key, which can be created using a kind and a key name string. A kind is an organizational bucket for what type of entity it is. For example, we might want to set up kinds for Photos, People, and Animals.
Each entity can have multiple developer-defined properties, which can have values of a number of types, including integers, floats, strings, dates, or binary data:
   # Create a Cloud Datastore client.
    datastore_client = datastore.Client()

     # Fetch the current date / time.
    current_datetime = datetime.now()
    # The kind for the new entity.
    kind = 'Faces'
    # The name/ID for the new entity.
    name = blob.name
    # Create the Cloud Datastore key for the new entity.
    key = datastore_client.key(kind, name)
    # Construct the new entity using the key. Set dictionary values for
entity
    # keys blob_name, storage_public_url, timestamp, and joy.
    entity = datastore.Entity(key)
    entity['blob_name'] = blob.name
    entity['image_public_url'] = blob.public_url
    entity['timestamp'] = current_datetime
    entity['joy'] = face_joy
    # Save the new entity to Datastore.
    datastore_client.put(entity)

 Deploying the App to App Engine Flexible
App Engine Flexible uses a file called app.yaml to describe an application's deployment configuration. If this file is not present, App Engine will try to guess the deployment configuration. However, it is a good idea to provide this file.
 runtime: python
 env: flex
 entrypoint: gunicorn -b :$PORT main:app
 runtime_config:
 python_version: 3
 env_variables:
 CLOUD_STORAGE_BUCKET:
 manual_scaling:
 instances: 1
This is the basic configuration needed to deploy a Python 3 App Engine Flex application
6. Deploy your app on App Engine by using gcloud: gcloud app deploy

Flask App Deployment on Colab
1. Sign up for a ngrok account with GitHub
2. Find your auth token
3. Replace it in the appropriate place in the Colab Notebook
4. Make sure the model and dataset are in your Google Drive and the links
pointing to them are correct (personalized to your Drive)
Streamlit Cloud Deployment
1. Sign up to Streamlit Cloud using GitHub
2. Push the Topic Modeling code to GitHub on the master branch
3. Go to your cloud dashboard and paste the repository url or choose using the
interface
4. Just press deploy
5. Non-standard packages like Top2Vec need to be listed on a requirements.txt file so
Streamlit will install them
