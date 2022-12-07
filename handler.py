import os
import pickle
import pandas as pd
from flask import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance
import xgboost as xgb

# Loading Model
model = pickle.load( open('model/model_cross_sell.pkl', 'rb') )

# Initialize API
app = Flask( __name__ )
@app.route( '/predict', methods=['POST'] )

def health_insurance_predict():
    test_json = request.get_json()
    
    if test_json: # there is data
        if isinstance( test_json, dict ): # unique example
            test_raw = pd.DataFrame( test_json, index=[0] )
            
        else: # multiple example
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
            
        # Instantiate HealthInsurance Class
        pipeline = HealthInsurance()
        
        # Data Cleaning
        df1 = pipeline.data_cleaning( test_raw )
        
        # Feature Engeneering
        df2 = pipeline.feature_engineering( df1 )
        
        # Data Preparation
        df3 = pipeline.data_preparation( df2 )
        
        # Model Prediction
        df_response = pipeline.get_prediction( model, test_raw, df3 )
        
        return df_response
    
    else:
        return Response( '{}', status=200, mimetype='application/json' )
        
    
if __name__ == '__main__':
    porti = os.environ.get( 'PORT', 5000 )
    app.run( host='0.0.0.0', port=porti )