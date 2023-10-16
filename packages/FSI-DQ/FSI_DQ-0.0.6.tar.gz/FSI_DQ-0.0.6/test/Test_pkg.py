from FSI_DQ.__main__ import DataQuality

catalog_name='dev'

schema='data_quality'

input_table='rent_details'

api_key='af16a0a99c2f45dda8c5dee3c1df8b9b'

api_base='https://kinisi-azure-openai.openai.azure.com'

api_version='2023-05-15'

api_type = 'azure'


choice={

    'BusinessContext':1,

    'DQRules':0,

    'AnomalyDetection':0,

    'Standarization':0

}

dq=DataQuality(catalog_name,schema,input_table,choice,api_type,api_key,api_base,api_version)
dq.main()