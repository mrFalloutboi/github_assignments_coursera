import json

# Mocked emotion detector (no API call).
def emotion_detector(text, api_key=None, service_url=None):
    # Instead of calling Watson, return a fake response
    emotions = {
        "sadness": 0.1,
        "joy": 0.8,
        "fear": 0.05,
        "disgust": 0.02,
        "anger": 0.03
    }
    return {
        "text": text,
        "emotions": emotions
    }

if __name__ == "__main__":
    sample_text = "I am so happy today because I passed my exam!"
    result = emotion_detector(sample_text)
    print(json.dumps(result, indent=2))
