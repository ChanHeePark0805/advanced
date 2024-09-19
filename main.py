import numpy as np
import pandas as pd

Solar = pd.read_csv('C:/Users/cksgm/Downloads/Data1/Data1/Solar_4.csv')
Solar["DeliveryDT"]=pd.to_datetime(Solar["DeliveryDT"])
print('c')