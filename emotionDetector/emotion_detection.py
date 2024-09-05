import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    myobj = { 
        "raw_document": { "text": text_to_analyse } 
    }
    
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        # Extract emotion data if available
        try:
            emotion_data = formatted_response['emotionPredictions'][0]['emotion']
            anger_score = emotion_data['anger']
            disgust_score = emotion_data['disgust']
            fear_score = emotion_data['fear']
            joy_score = emotion_data['joy']
            sadness_score = emotion_data['sadness']
            dominant_emotion = max(emotion_data, key=emotion_data.get)
        except (KeyError, IndexError) as e:
            # Handle any case where the data is not structured as expected
            return {"error": f"Failed to extract emotion data: {e}"}
        
    elif response.status_code == 400:
        # Handle a bad request or missing text case
        return {
            'error': 'Bad request, likely due to missing text',
            'status_code': 400
        }
    else:
        # Handle any other unexpected status codes
        return {
            'error': f"Unexpected status code: {response.status_code}",
            'status_code': response.status_code
        }

    # Return extracted emotion data if successful
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
