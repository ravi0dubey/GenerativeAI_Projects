import numpy as np
from PIL import Image
from pinecone import Pinecone
import boto3
from io import BytesIO
from tensorflow import keras
from keras.models import Model
from keras import Sequential
from keras.layers import Dense,Flatten
from keras.applications.vgg16 import VGG16,preprocess_input
import numpy as np
from glob import glob
import os
from dotenv import load_dotenv






class VGG16ImageNet:
    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
        print(dotenv_path)
        pinecone_connection = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.s3 = boto3.client('s3', aws_access_key_id= aws_access_key_id, aws_secret_access_key= aws_secret_access_key)
        self.model = VGG16(weights='imagenet', include_top=True)
        # self.feature_extractor = Model(inputs=self.model.input, outputs=self.model.get_layer('flatten').output)
        self.feature_extractor = Model(inputs=self.model.input, outputs=self.model.get_layer('fc1').output)
        self.pinecone_index = pinecone_connection.Index("image-vectors")
        

    def preprocess_image(self, img):
        img = img.resize((224, 224))  
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        return preprocess_input(img_array)

    def generate_vector(self, img):
        preprocessed_img = self.preprocess_image(img)
        feature_vector = self.feature_extractor.predict(preprocessed_img)
        return feature_vector
        
    def index_vector(self, img_path, vector):
        key = img_path
        vec =  vector.tolist()
        vectors_to_upsert = [{"id": key, "values": vec[0]} ]
        self.pinecone_index.upsert(vectors=vectors_to_upsert, namespace="ns1")

    def search_top_match(self, query_vector):
        query_vector =  query_vector.tolist()
        results = self.pinecone_index.query(namespace="ns1",vector=query_vector, top_k=1,include_values=True)
        return results

if __name__ == "__main__":
    image_vectorizer = VGG16ImageNet()
    bucket_name = "images-scraped"
    response = image_vectorizer.s3.list_objects_v2(Bucket=bucket_name)
    image_paths = [obj['Key'] for obj in response['Contents']]

    for img_path in image_paths:
        img_object = image_vectorizer.s3.get_object(Bucket=bucket_name, Key=img_path)
        img_data = img_object['Body'].read()
        img = Image.open(BytesIO(img_data))
        vector = image_vectorizer.generate_vector(img)
        image_vectorizer.index_vector(img_path, vector)


    test_img_path = "D:\\Study\\Data Science\\Vector_DB\\Astha_pic1.jpg" 
    test_img = Image.open(test_img_path)
    test_vector = image_vectorizer.generate_vector(test_img)
    print("Dimension of the generated vector:", test_vector.shape)
    top_match = image_vectorizer.search_top_match(test_vector)
    ids = [match['id'] for match in top_match['matches']]
    print("Top match:", ids)
