import numpy as np
from sklearn import preprocessing
input_data=np.array([[3,-1.5,3,-6.4],[0,3,-1.3,4.1],[1,2.3,-2.9,-4.3]])
data_standerised=preprocessing.scale(input_data)
#print ("mean=",data_standerised.mean(axis=0))
#print ("statndard deviation=",data_standerised.std(axis=0))
data_scaler=preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled=data_scaler.fit_transform(input_data)
#print ("min max scaled data",data_scaled)
data_normalised=preprocessing.normalize(input_data,norm = 'l1')
print ("normalised data",data_normalised)
data_binarised=preprocessing.Binarizer(threshold=1.4).transform(input_data)
print('binarised data\n ',data_binarised)