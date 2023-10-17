#!/usr/bin/env python3
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import joblib
import numpy as np
from pkg_resources import resource_filename
import fire, warnings
from dataclasses import dataclass

@dataclass
class Regbot:
  macdsignal: float
  macd_histogram: float
  grad_histogram: float
  pct_change: float
  grad_vol_sma: float
  ratio4: float
  rsi_05: float
  rsi_15: float
  close_grad: float
  close_grad_neg: float

  reg_model_path: str = resource_filename(__name__, 'minute_model.pkl')
  scaler_path: str = resource_filename(__name__, 'minutescaler.gz')

  def loadmodel(self):
    try:
      return joblib.load(open(f'{self.reg_model_path}', 'rb'))
    except Exception as e:
      return {
        'Error': e
      }


  def prepareInput(self):
    try:
      test_data = np.array([[self.macdsignal,
                            self.macd_histogram,self.grad_histogram,self.pct_change,self.grad_vol_sma,self.ratio4,self.rsi_05,self.rsi_15,
                            self.close_grad,self.close_grad_neg]]
                            )
      scaler = joblib.load(f'{self.scaler_path}')
      return scaler.transform(test_data)
    except Exception as e:
      return {
        'Error': e
      }


  def buySignalGenerator(self,thr):
    try:
      return (self.loadmodel().predict_proba(self.prepareInput())[:,1] > thr).astype(int)[0]
    except Exception as e:
      return {
        'Error': e
      }




def signal(macdsignal,macd_histogram,
          grad_histogram,pct_change,grad_vol_sma,ratio4,rsi_05,rsi_15,close_grad,
          close_grad_neg
          ):
  args = [macdsignal,macd_histogram, \
          grad_histogram,pct_change,grad_vol_sma,ratio4,rsi_05,rsi_15, \
          close_grad,close_grad_neg
          ]

  try:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        return Regbot(*args).buySignalGenerator(0.5)
  except Exception as e:
    return {
      'Error': e
    }


if __name__ == '__main__':
  fire.Fire(signal)
