# Retail Investor Behavior Predictor in US Stock Market


## Raw data
1. Download US market data from https://backtest.pl and run merge_price_files.py in the download folder
or directly use compiled prices and volume data saved in AWS S3:
s3://sagemaker-us-east-1-420440669876/all_prices.csv

2. Download Robinhood user holding data from https://robintrack.net/data-download
or directly use compiled prices and volume data saved in AWS S3:
s3://sagemaker-us-east-1-420440669876/all_holdings.csv

Links to all_prices.csv and all_holdings.csv have been made public. 


## Main program
1. Upload capstone_project_main.ipynb to Amazon Sagemaker and open a Notebook Instance. 
Please use conda_tensorflow_p36 as kernel. 
Currently code is pointing to S3 bucket mentioned above where I stored raw data. If your execution role doesn't have access to it, please download the files following steps above and upload to your local place.  

## Library dependency 
1. pandas - data operations are done in dataframes using pandas in the project
2. sklearn - used for preprocessing (standardization) and modeling (Kmeans, PCA, Logistic Regression)
3. keras - used for preprocessing (one-hot encoding) and modeling (lstm) 
4. numpy
5. seaborn 
6. matplotlib
7. boto3
8. sagemaker
9. math

## References
Please refer to footnotes in the report.
