import joblib
import pandas as pd
static_path="./static/Models/"
def createFeatures(DataFrameObj, textCol):
  vectorizer =joblib.load(static_path+"vectorizer.pkl")
  features = vectorizer.transform(DataFrameObj[textCol])

  return features.toarray()
def decode(output):
  encoder=joblib.load(static_path+"encoder.pkl")
  decode_output=encoder.inverse_transform(output)
  return decode_output
def predict_model(text):
  DATA=pd.DataFrame({"Text":[text]})
  feature=createFeatures(DATA,"Text")
  model=joblib.load(static_path+"NB_Model.pkl")
  output_predict=model.predict(feature)
  decode_output=decode(output_predict)
  return decode_output[0]
  