import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import numpy as np
import scipy as sp
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
import sklearn as sk
# timeseries error = pip install statsmodels --upgrade
# 파이썬, 아나콘다 라이브러리 폴더가 다르므로
# 아나콘다 폴더에 깔아야 함
# 어떻게? conda

import matplotlib as mpl
# mpl.use('Agg')
# matplotlib.use 에러나면 얘 주석처리
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

import seaborn as sns
sns.set()
sns.set_style("whitegrid")
sns.set_color_codes()
