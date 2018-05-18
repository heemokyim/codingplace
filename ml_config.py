import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import numpy as np
import scipy as sp
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
import sklearn as sk
import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.font_manager as fm
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
sns.set()
sns.set_style("whitegrid")
sns.set_color_codes()

def best_close_imputing(missing, intact, not_imputing_cols=None):
    '''
    Impute axis of missing value from best close data point.
    
    params
        1. missing = pd.DataFrame that missing occured
        2. intact = pd.DataFrame that no missing occured
        
    Returns best-close-imputed pd.DataFrame
    '''
    
    cols = list(missing.columns)

    for each in not_imputing_cols:
        cols.remove(each)

    for mis in missing.iterrows():
        mis_idx = mis[0]
        mis_val = mis[1][cols]

        z_score = []

        for ict in intact.iterrows():
            ict_idx = ict[0]
            ict_val = ict[1][cols]

            dist = np.linalg.norm(np.nansum(mis_val.values - ict_val.values))

            z_score.append((ict_idx, dist))

        best_close_idx = min(z_score, key=lambda x: x[1])[0]
        best_close_row = intact.iloc[best_close_idx][cols]

        missing_idx = mis[1][mis[1].isnull()].index
        mis_val[missing_idx] = best_close_row[missing_idx]

        missing.loc[mis_idx, missing_idx] = best_close_row[missing_idx]

    return missing