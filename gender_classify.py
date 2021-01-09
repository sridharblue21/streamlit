import joblib  # Save to file to pkl file

gender_model = joblib.load('gender_classify.pkl')

def gender_features(word):
    return {'last_letter': word[-1]}

def gender_classify(gender):
        return gender_model.classify(gender_features(gender))
