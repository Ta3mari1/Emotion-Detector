import requests
import json

def emotion_detector(text_to_analyze):
  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
   
    response = requests.post(url, json=input_json, headers=headers)
    
    
    if response.status_code != 200:
        return {"error": f"Failed to fetch emotions: {response.status_code}"}
    
 
    response_data = json.loads(response.text)
    
  
    emotions = response_data['emotionPredictions'][0]['emotion']
    
    
    dominant_emotion = max(emotions, key=emotions.get)
    
   
    result = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }
    
    return result