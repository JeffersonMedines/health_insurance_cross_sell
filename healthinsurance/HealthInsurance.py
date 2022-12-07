import pickle
import pandas as pd
import numpy as np

class HealthInsurance():
    def __init__( self ):
        self.home_path = ''
        self.annual_premium_scaler = pickle.load( open( self.home_path + 'src/features/annual_premium_scaler.pkl', 'rb' ) )
        self.age_scaler = pickle.load( open( self.home_path + 'src/features/age_scaler.pkl', 'rb' ) )
        self.vintage_scaler = pickle.load( open( self.home_path + 'src/features/vintage_scaler.pkl', 'rb' ) )
        self.target_encoding_region_code_scaler = pickle.load( open( self.home_path + 'src/features/target_encoding_region_code_scaler.pkl', 'rb' ) )
        self.target_encode_gender_scaler = pickle.load( open( self.home_path + 'src/features/target_encode_gender_scaler.pkl', 'rb' ) )
        self.fe_policy_sales_channel_scaler = pickle.load( open( self.home_path + 'src/features/fe_policy_sales_channel_scaler.pkl', 'rb' ) )
        
    def data_cleaning( self, df1 ):
        ## 1.6 Change Types

        df1['region_code'] = df1['region_code'].astype( int )

        # Check Change
        df1['region_code'].dtypes

        ## 1.7 Drop Columns

        if 'id.1'  in df1.columns:
            df1 = df1.drop( columns='id.1' )
        else:
            pass

        if 'id.2'  in df1.columns:
            df1 = df1.drop( columns='id.2' )
        else:
            pass

        return df1

    def feature_engineering( self, df2 ):
        # vehicle_damage
        # df2['vehicle_damage'] = df2['vehicle_damage'].apply( lambda x: 1 if x == 'Yes' else 0 )

        # # vehicle_age
        # df2['vehicle_age'] = df2['vehicle_age'].apply( lambda x: 'below_1_year' if x == '< 1 Year' else 
        #                                                          'between_1_2_year' if x == '1-2 Year' else 
        #                                                          'over_2_years' )
    
        return df2

    def data_preparation( self, df5 ):
        # Annual Premium
        df5['annual_premium'] = self.annual_premium_scaler.transform( df5[['annual_premium']].values )

        ## 5.2 Rescaling 

        # Age
        df5['age'] = self.age_scaler.transform( df5[['age']].values )

        # Vintage
        df5['vintage'] = self.vintage_scaler.transform( df5[['vintage']].values )

        ## 5.3 Encoder

        # region_code - target encoding / frequency encoding / weighted target encoding
        df5.loc[:, 'region_code'] = df5['region_code'].map( self.target_encoding_region_code_scaler )

        # Gender - One Hot encoding / Target encoding
        df5.loc[:, 'gender'] = df5['gender'].map( self.target_encode_gender_scaler )

        # vehicle_age - one hot encoding / frequency encoding / order encoding
        # df5 = pd.get_dummies( df5, prefix='vehicle_age', columns=['vehicle_age'] )

        # policy_sales_channel - Target encoding / frequency encoding
        df5.loc[:, 'policy_sales_channel'] = df5['policy_sales_channel'].map( self.fe_policy_sales_channel_scaler )

        # 6.0 STEP 06 - FEATURE SELECTION
        cols_selected = [ 'vintage', 'annual_premium', 'age', 'region_code', 'vehicle_damage', 'policy_sales_channel', 'previously_insured' ]
    
        return df5[ cols_selected ]

    def get_prediction( self, model, original_data, test_data ):
        # Model Prediction
        pred = model.predict_proba( test_data )
        
        # Join Predicton into Original Data
        original_data['prediction'] = pred[:, 1].tolist()
        
        return original_data.to_json( orient='records', date_format='iso' )