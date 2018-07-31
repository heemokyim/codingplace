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

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelBinarizer, LabelEncoder, OneHotEncoder, Imputer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, Normalizer

sns.set()
sns.set_style("whitegrid")
sns.set_color_codes()
   
# get continuous column
# intact.select_dtypes(include=[np.number]).columns.tolist()

# get string column
# index = X.applymap(lambda x: isinstance(x, str)).all(0)
# index[index].index

#re.findall('.C.(\w+)',formula)
#re.findall('.scale.(\w+)',formula)

# get columns that missing value occured
# tmp =test.isnull().any()
# tmp[tmp].index

def best_close_imputing(intact, missing, verbose=True, is_fit=False, mean=None, std=None):
    # Python 3.6.3
    '''
    1. Impute columns using euclidean similarity + Z-score
    2. Consider only continuous columns when calculating similarity
    
    Params
        data = pd.DataFrame that missing rows + intact rows
    
    Return imputed data
    '''
    
    assert list(intact.columns) == list(missing.columns), 'intact and missing should be same DataFrame'
        
    total_continuous_cols = intact.select_dtypes(include=[np.number]).columns
    
    # Except any non-continuous columns
    tmp = missing.isnull().any()
    imputing_cols = tmp[tmp].index
    imputing_cols = set(total_continuous_cols).intersection(set(imputing_cols))
    imputing_cols = list(imputing_cols)
    
    # Columns to be referred to impute
    refer_continuous_cols = set(total_continuous_cols) - set(imputing_cols)

    # If imputing_cols only contains one element, it should not be in list for proper result
    imputing_cols = imputing_cols.pop() if len(
        imputing_cols) == 1 else imputing_cols
    
    # To calculate similarity, we use z-score
    # Belows are needed components
    if mean is None and std is None:
        data = missing.append(intact)
        mean = data.loc[:, refer_continuous_cols].mean()
        std = data.loc[:, refer_continuous_cols].std()
        del data
#     n = len(refer_continuous_cols)
    
    if is_fit is True:
        return mean, std
    
    for mis in missing.iterrows():
        mis_idx = mis[0]
        mis_val = mis[1][refer_continuous_cols]
        
        # Except Non-continuous columns
        missing_cols = mis[1][mis[1].isnull()].index
        missing_cols = set(total_continuous_cols).intersection(set(missing_cols))
        
        if verbose:
            print(missing_cols)
        
        if len(missing_cols)==0:
            continue
        
        mis_val_z = (mis_val - mean) / std
        
        sim_list = []

        for ict in intact.iterrows():
            ict_idx = ict[0]
            ict_val = ict[1][refer_continuous_cols]

            ict_val_z = (ict_val - mean) / std
            
            # Except NaN when calculating distance
            dist = np.linalg.norm(np.nansum(mis_val_z.values - ict_val_z.values))

            sim_list.append((ict_idx, dist))
        
        best_close_idx = min(sim_list, key=lambda x: x[1])[0]
        
        filler = intact.loc[best_close_idx, missing_cols]
        
        if len(missing_cols)==1:
            filler = float(filler)
        
        missing.loc[mis_idx, missing_cols] = filler

        if verbose is True:
            print('missing index = ',mis_idx, '\tbest_close_idx = ',best_close_idx)
            print('\t','Euclidean distance (intact_idx, distance)')
            print(sim_list,'\n\n')
        
    return missing

# ---------------------------------------------------------------------------
# Refer to category_pipeline for usage

class column_selector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    
    def fit(self, X):
        return self
    
    def transform(self, X, y = None):
        return X[self.attribute_names]
    
class LabelBinarizerPipelineFriendly(LabelBinarizer):
    def fit(self, X, y=None):
        """this would allow us to fit the model based on the X input."""
        super(LabelBinarizerPipelineFriendly, self).fit(X)
    def transform(self, X, y=None):
        return super(LabelBinarizerPipelineFriendly, self).transform(X)

    def fit_transform(self, X, y=None):
        return super(LabelBinarizerPipelineFriendly, self).fit(X).transform(X)

def cat_pipeline(attr):
    return Pipeline([
    ('selector', column_selector(attr)),
    ('label_binarizer', LabelBinarizerPipelineFriendly()),
    ])

def multi_1hot_encoder(attribute_names, n_jobs=1, transformer_weight=None):
    arg_list = [('1hot_{}'.format(attr), cat_pipeline(attr))
                for attr in attribute_names]
    
    return FeatureUnion(arg_list, n_jobs, transformer_weight)
    
    
# ---------------------------------------------------------------------------
# Refer to continuous_pipeline for usage

class best_close_imputer(BaseEstimator, TransformerMixin):
    def __init__(self, verbose = False):
        self.verbose = verbose
        
    def fit(self, X, y = None):
        intact = X.dropna(axis=0,how='any')
        missing = X.drop(intact.index)
        
        mean, std = best_close_imputing(intact, missing, verbose=self.verbose, is_fit=True)
        
        self.intact, self.mean, self.std = intact, mean, std
        return self
        
    def transform(self, X, y = None):
        no_missing = X.dropna(axis=0, how='any')
        missing = X.drop(no_missing.index)
        
        imputed = best_close_imputing(self.intact, missing, verbose=self.verbose, mean=self.mean, std=self.std)
        
        return imputed.append(no_missing).drop_duplicates()


# This below is example
class FeatureEngineer(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):
        # Your field declaration here
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        # Actual feature engineering here
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]

        population_per_household = X[:, population_ix] / X[:, household_ix]

        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]
        
def example_pipeline(attribute_names):
    rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6
    
    return Pipeline([
    ('selector', column_selector(attribute_names)),
    ('imputer', Imputer(strategy='median')),
    ('feature_engineer', FeatureEngineer()),
    ('std_scaler', StandardScaler()),
])