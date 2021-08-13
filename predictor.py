### Custom definitions and classes if any ###
import pandas as pd
import pickle

# The function which predicts from the given data row (in the form of a single-row dataframe)
def predict(input_df):
    # Declare a dictionary to map team names to their respective regions
    teams = {"Mumbai Indians": "Mumbai",
             "Kolkata Knight Riders": "Kolkata",
             "Chennai Super Kings": "Chennai",
             "Kings XI Punjab": "Punjab",
             "Punjab Kings": "Punjab",
             "Rising Pune Supergiant": "Pune",
             "Rising Pune Supergiants": "Pune",
             "Pune Warriors": "Pune",
             "Delhi Daredevils": "Delhi",
             "Delhi Capitals": "Delhi",
             "Gujarat Lions": "Gujarat",
             "Deccan Chargers": "Hyderabad",
             "Sunrisers Hyderabad": "Hyderabad",
             "Royal Challengers Bangalore": "Bangalore",
             "Rajasthan Royals": "Rajasthan",
             "Kochi Tuskers Kerala": "Kerala"}
    
    # Basic preprocess input data
    input_df["venue"] = [input_df["venue"][0].split(',')[0].replace('.', ' ').strip()]
    input_df["batting_team"] = [teams[input_df["batting_team"][0]]]
    input_df["bowling_team"] = [teams[input_df["bowling_team"][0]]]
    
    # Load the encoders and the model
    with open("venues.pkl", "rb") as venuesEncoderFile:
        venuesEncoder = pickle.load(venuesEncoderFile)
    with open("teams.pkl", "rb") as teamsEncoderFile:
        teamsEncoder = pickle.load(teamsEncoderFile)
    with open("model.pkl", "rb") as modelFile:
        model = pickle.load(modelFile)
        
    # Advance preprocess input data and return the prediction
    input_df["venue"] = venuesEncoder.transform(input_df["venue"])
    input_df["batting_team"] = teamsEncoder.transform(input_df["batting_team"])
    input_df["bowling_team"] = teamsEncoder.transform(input_df["bowling_team"])
    X = input_df.values
    prediction = round(model.predict(X)[0])
    return prediction

def predictRuns(input_test):
    prediction = 0
    
    ### Your Code Here ###
    cols = ["venue", "innings", "batting_team", "bowling_team"]
    input_df = pd.read_csv(input_test)[cols]
    
    # Return the prediction
    prediction = predict(input_df)
    return prediction

# print(predict_runs("test_file.csv"))
