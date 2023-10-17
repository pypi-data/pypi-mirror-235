import pandas as pd
from regbot import signal

df = pd.read_csv('../reinforce/regbot_v65_training.csv')

y_pred = []
def getSignal(macdsignal,macd_histogram,grad_histogram,pct_change,grad_vol_sma,ratio4,rsi_05,rsi_15,close_grad,close_grad_neg):
    
    args = [macdsignal,macd_histogram,grad_histogram,pct_change,grad_vol_sma,ratio4,rsi_05,rsi_15,close_grad,close_grad_neg]
    try:
        return signal(*args)
    except Exception as e:
        print(e)

#print(df.head())
#print(df.columns)
df = df.sample(frac=1).reset_index(drop=True)
#print(df.head())
df = df[df['targets'] == 1].head(20)
#print(df.head())

df['result'] = df.apply(lambda row: getSignal(row['macdsignal'],row['macd-histogram'],
                                              row['grad-histogram'],row['pct-change'],row['grad-vol-sma'],row['ratio4'],row['rsi-05'],
                                              row['rsi-15'],row['close-gradient'],row['close-gradient-neg']), axis=1)

print(df.head())

print(len(df[df['result'] == df['targets']]), len(df))
