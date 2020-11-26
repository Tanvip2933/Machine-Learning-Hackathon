import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("real_fraud.csv")

X = data[['having_IPhaving_IP_Address', 'URLURL_Length',
          'Shortining_Service', 'having_At_Symbol', 'double_slash_redirecting',
          'Prefix_Suffix', 'Favicon']]
y = data['Result']
X = np.array(X)
y = np.array(y)

le = LabelEncoder()

y = le.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=500)

sv = SVC(kernel='linear').fit(X, y)
pickle.dump(sv, open('probability_checker.pkl', 'wb'))
