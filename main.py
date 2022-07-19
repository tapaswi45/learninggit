import pandas as pd
import os

file = r"D:\Data Wranging 7 ML\Data+and+Code\Data and Code\section 2\bostonTxt.txt"
df=pd.read_csv(file,sep='\t')

print(df.head(30))

