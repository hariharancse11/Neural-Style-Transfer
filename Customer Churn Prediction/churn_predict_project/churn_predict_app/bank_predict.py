import pickle

def bankChurnPrediction(CreditScore,	Geography,	Gender,	Age,	Tenure,	Balance,	NumOfProducts,	HasCrCard,	IsActiveMember,	EstimatedSalary):
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    CLASS_NAMES = ['Will Stay', 'Will Exit']
    if Geography=='France':
        France = 1
        Germany = 0
    elif Geography=='Germany':
        France = 0
        Germany = 1
    else:
        France = 0
        Germany = 0

    if Gender=='Female':
        Female = 1
    else:
        Female = 0
    pred = loaded_model.predict([[CreditScore,	Age,	Tenure,	Balance,	NumOfProducts,	HasCrCard,	IsActiveMember,	EstimatedSalary,France,	Germany, Female]])
    return(CLASS_NAMES[pred[0]])