def package_import():
    #pip install ucimlrepo
    #pip install xgboost    
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt
    import matplotlib.style as style
    import seaborn as sns
    import scipy.stats as stats
    import pylab
    import warnings
    import seaborn as sns
    import pandas as pd
    warnings.filterwarnings("ignore")

# fetch dataset"
def fetch_dataset():
    package_import()
    from ucimlrepo import fetch_ucirepo
    bank_marketing = fetch_ucirepo(id=222) 
    # data (as pandas dataframes)
    X = bank_marketing.data.features
    y = bank_marketing.data.targets
    return X,y

def clean_data(X,y):
    import pandas as pd
    package_import()
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import MinMaxScaler
    X = X.drop(columns=['contact','poutcome'])  
    job = X['job'].mode()[0]
    edu = X['education'].mode()[0]
    X['job'].fillna(job, inplace=True)
    X['education'].fillna(edu, inplace=True)
    label_encoder = LabelEncoder()
    for col in X.select_dtypes(["object","category"]):
        X[col] = label_encoder.fit_transform(X[col])
    for col in y.select_dtypes(["object","category"]):
         y[col] = label_encoder.fit_transform(y[col])  
    num_cols = X[['age','balance','day_of_week','duration','campaign','pdays','previous']].values.astype(float)
    min_max_scaler = MinMaxScaler()
    num_scaled = min_max_scaler.fit_transform(num_cols)   
    X[['age','balance','day_of_week','duration','campaign','pdays','previous']] = pd.DataFrame(num_scaled)   
    return X,y

#feature selection을 위한 함수 정의
def make_mi_scores(x, y):
    import pandas as pd
    package_import()
    from sklearn.feature_selection import mutual_info_classif
    x = x.copy()
    for colname in x.select_dtypes(["object", "category"]):
        x[colname], _ = x[colname].factorize()
    # All discrete features should now have integer dtypes
    discrete_features = [pd.api.types.is_integer_dtype(t) for t in x.dtypes]
    mi_scores = mutual_info_classif(x, y, discrete_features=discrete_features, random_state=0)
    mi_scores = pd.Series(mi_scores, name="MI Scores", index=x.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores

def plot_mi_scores(scores):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    package_import()
    scores = scores.sort_values(ascending=True)
    width = np.arange(len(scores))
    ticks = list(scores.index)
    plt.barh(width, scores)
    plt.yticks(width, ticks)

#train_test_split
def data_split(X,y):
    package_import()
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    return X_train, X_test, y_train, y_test

#XGBoost 모델 정의 및 훈련
def model_train(X_train, y_train):
    package_import()
    from xgboost import XGBClassifier
    xgb = XGBClassifier(n_estimators=400, learning_rate=0.1, max_depth=3)
    xgb.fit(X_train, y_train)
    return xgb

#모델 성능 평가(정확도, confusion matrix)
def get_clf_eval(xgb, X_test, y_test):
    package_import()
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score
    
    pred = xgb.predict(X_test)
    print(accuracy_score(pred, y_test))
    
    confusion = confusion_matrix(y_test, pred)
    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)
    f1 = f1_score(y_test, pred)
    roc_auc = roc_auc_score(y_test, pred)
    
    print('오차 행렬')
    print(confusion)
    
    print(f'정확도 : {accuracy:.4f}, 정밀도 : {precision:.4f}, 재현율 : {recall:.4f}, F1 : {f1:.4f}, AUC:{roc_auc:4f}')
