import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_Json= { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, headers = header, json = Input_Json)
    emotions = response.json()["emotionPredictions"][0]["emotion"]
    
    err_code = response.status_code
    if err_code == 500:
        input("Invalid entry, Please enter statement: ")
    elif err_code == 400:
        return {
                "anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None, 
                "dominant_emotion": None
                }
    
    dominant_emotion = max(emotions, key = emotions.get)
    emotions.update({"dominant_emotion" : dominant_emotion})
    return emotions