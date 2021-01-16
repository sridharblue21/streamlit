import readdata  # read pkl file from here

gender_model = readdata.read_data_gdrive('gender_classify.pkl', type = 'joblib')

def gender_features(word):
    return {'last_letter': word[-1]}

def gender_classify(gender):
        return gender_model.classify(gender_features(gender))
