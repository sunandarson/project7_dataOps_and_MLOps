#!python3

def colPreparation():
    labelEncoder = ['Gender','Driving_License','Previously_Insured','Vehicle_Damage']
    oneHotEncoder = ['Vehicle_Age','Region_Code','Policy_Sales_Channel']
    StandarScaler = ['Age','Annual_Premium','Vintage']
    
    return labelEncoder, oneHotEncoder, StandarScaler