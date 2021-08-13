from pywebio.input import *
from pywebio.output import *
from pywebio.session import set_env
from pywebio import start_server
import pandas as pd
from predictor import predict

def isBothSame(d):
    if d["batting_team"] == d["bowling_team"]:
        return ("bowling_team", "The same team cannot bat and bowl at the same time!")

def main():
    set_env(title = "Score Predictor")
    venues = ["Wankhede Stadium", "MA Chidambaram Stadium", "M Chinnaswamy Stadium", "Eden Gardens", "Arun Jaitley Stadium", "Narendra Modi Stadium"]
    teams = ["Royal Challengers Bangalore", "Mumbai Indians", "Chennai Super Kings", "Delhi Capitals", "Punjab Kings", "Kolkata Knight Riders", "Rajasthan Royals", "Sunrisers Hyderabad"]
    inputDict = input_group("Predict First 6 Overs Score (IPL 2021)", [
        select("Venue", options = venues, name = "venue"),
        select("Innings", options = [1, 2], name = "innings"),
        select("Batting Team", options = teams, name = "batting_team"),
        select("Bowling Team", options = teams, name = "bowling_team")
    ], validate = isBothSame)

    for key in inputDict:
        inputDict[key] = [inputDict[key]]

    result = f"<h1>{predict(pd.DataFrame(inputDict))}</h1> <b>runs</b> will be scored by <b>{inputDict['batting_team'][0]}</b> in the <u>first 6 overs</u>, if they <u>bat {'first' if inputDict['innings'][0] == 1 else 'second'}</u> against <b>{inputDict['bowling_team'][0]}</b> in <b>{inputDict['venue'][0]}</b>."

    put_html(result)

if __name__ == "__main__":
    start_server(main, port = 80, debug = True)

