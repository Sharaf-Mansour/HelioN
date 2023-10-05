import pandas as pd
import statsmodels.api as sm
import subprocess
from statsmodels.tsa.stattools import adfuller

# Run the nvidia-smi command and capture the output
output = subprocess.check_output(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader,nounits'])
gpu_utilization = [int(x) for x in output.decode().split('\n')[:-1]]
# Print the GPU utilization
print(gpu_utilization)

# Load the CSV file into a DataFrame
file_data=pd.read_csv('C:\\Users\\shara\\Downloads\\merged_without_ffill.csv',index_col='time', parse_dates=True)
file_data.head()
#file_required=file_data[['proton_vx_gse','proton_speed,K']]
#file_required=file_required['K'].dropna()
#print(file_required.head())
#data=file_data['proton_speed']
#print(file_data.head())

#data=data.sort_index()
#simple_data=data[0:2457]
#data_smooth = file_required.rolling(window=2).mean().dropna()
#stationary_result=adfuller(data_smooth)
#print('ADF Statistic:',stationary_result[0])
#print('p-value:', stationary_result[1])
# Display the DataFrame in the VS Code output pane
#print(file_data)
#nan_values=file_data['proton_speed'].isna()
#model = sm.tsa.SARIMAX(data_smooth, order=(2,1,1), seasonal_order=(1,0,1,7))
#model = sm.tsa.ARIMA(data_smooth, order=(2, 1, 1))
#results = model.fit()

#data=file_data['proton_speed']

#results= model.fit()
#aic=results.aic
#print('AIC: ',aic)