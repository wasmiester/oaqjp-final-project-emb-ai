"""Server file for flask main"""
from flask import Flask
from final_project import emotion_detection

app= Flask(__name__)

@app.route("/emotionDetector")

def emotion_detector():
    """print flask response"""
    statement = input("enter statement: ")
    emotions = emotion_detection.emotion_detector(statement)
    result =(f"<b>For the given statement, the system response is "
    f"'anger': {emotions['anger']}, "
    f"'disgust': {emotions['disgust']}, "
    f"'fear': {emotions['fear']}, "
    f"'joy': {emotions['joy']} and "
    f"'sadness': {emotions['sadness']}. "
    f"The dominant emotion is {emotions['dominant_emotion']}.</b>")
    return result
