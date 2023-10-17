{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a9c74743",
   "metadata": {},
   "outputs": [],
   "source": [
    "def package_import():\n",
    "    !pip install ucimlrepo\n",
    "    !pip install xgboost\n",
    "    from ucimlrepo import fetch_ucirepo\n",
    "    import numpy as np\n",
    "    import matplotlib.pyplot as plt\n",
    "    import matplotlib.pyplot as plt\n",
    "    import matplotlib.style as style\n",
    "    import seaborn as sns\n",
    "    import scipy.stats as stats\n",
    "    import pylab\n",
    "    import warnings\n",
    "    import seaborn as sns\n",
    "    import pandas as pd\n",
    "    from sklearn.preprocessing import LabelEncoder\n",
    "    from sklearn.preprocessing import MinMaxScaler\n",
    "    from sklearn.feature_selection import mutual_info_classif\n",
    "    from sklearn.model_selection import train_test_split\n",
    "    from xgboost import XGBClassifier\n",
    "    from sklearn.metrics import accuracy_score\n",
    "    from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score\n",
    "    warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d19bae50",
   "metadata": {},
   "outputs": [],
   "source": [
    "# fetch dataset\n",
    "def fetch_dataset():\n",
    "    bank_marketing = fetch_ucirepo(id=222)\n",
    "\n",
    "    # data (as pandas dataframes)\n",
    "    X = bank_marketing.data.features\n",
    "    y = bank_marketing.data.targets\n",
    "    \n",
    "    return X,y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a7a664a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_data(X,y):\n",
    "    X = X.drop(columns=['contact','poutcome'])\n",
    "    \n",
    "    job = X['job'].mode()[0]\n",
    "    edu = X['education'].mode()[0]\n",
    "    X['job'].fillna(job, inplace=True)\n",
    "    X['education'].fillna(edu, inplace=True)\n",
    "    \n",
    "    label_encoder = LabelEncoder()\n",
    "    for col in X.select_dtypes([\"object\",\"category\"]):\n",
    "        X[col] = label_encoder.fit_transform(X[col])\n",
    "    for col in y.select_dtypes([\"object\",\"category\"]):\n",
    "        y[col] = label_encoder.fit_transform(y[col])\n",
    "        \n",
    "    num_cols = X[['age','balance','day_of_week','duration','campaign','pdays','previous']].values.astype(float)\n",
    "    min_max_scaler = MinMaxScaler()\n",
    "    num_scaled = min_max_scaler.fit_transform(num_cols)\n",
    "\n",
    "    X[['age','balance','day_of_week','duration','campaign','pdays','previous']] = pd.DataFrame(num_scaled)\n",
    "    \n",
    "    return X,y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "3317b596",
   "metadata": {},
   "outputs": [],
   "source": [
    "#feature selection을 위한 함수 정의\n",
    "def make_mi_scores(x, y):\n",
    "    x = x.copy()\n",
    "    for colname in x.select_dtypes([\"object\", \"category\"]):\n",
    "        x[colname], _ = x[colname].factorize()\n",
    "\n",
    "    # All discrete features should now have integer dtypes\n",
    "    discrete_features = [pd.api.types.is_integer_dtype(t) for t in x.dtypes]\n",
    "\n",
    "    mi_scores = mutual_info_classif(x, y, discrete_features=discrete_features, random_state=0)\n",
    "    mi_scores = pd.Series(mi_scores, name=\"MI Scores\", index=X.columns)\n",
    "    mi_scores = mi_scores.sort_values(ascending=False)\n",
    "    return mi_scores\n",
    "\n",
    "def plot_mi_scores(scores):\n",
    "    scores = scores.sort_values(ascending=True)\n",
    "    width = np.arange(len(scores))\n",
    "    ticks = list(scores.index)\n",
    "    plt.barh(width, scores)\n",
    "    plt.yticks(width, ticks)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "81aa2ad5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#train_test_split\n",
    "def data_split(X,y):    \n",
    "    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)\n",
    "    return X_train, X_test, y_train, y_test\n",
    "\n",
    "#XGBoost 모델 정의 및 훈련\n",
    "def model_train(X_train, y_train):\n",
    "    xgb = XGBClassifier(n_estimators=400, learning_rate=0.1, max_depth=3)\n",
    "    xgb.fit(X_train, y_train)   \n",
    "    return xgb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "eda71021",
   "metadata": {},
   "outputs": [],
   "source": [
    "#정확도 평가\n",
    "def accuracy(xgb):\n",
    "    y_pred = xgb.predict(X_test)\n",
    "    pred_proba = xgb.predict_proba(X_test)[:,1]\n",
    "    print(accuracy_score(y_pred, y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3786248c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#confusion matrix 구하기\n",
    "def get_clf_eval(y_test, pred=None, pred_proba=None):\n",
    "    confusion = confusion_matrix(y_test, pred)\n",
    "    accuracy = accuracy_score(y_test, pred)\n",
    "    precision = precision_score(y_test, pred)\n",
    "    recall = recall_score(y_test, pred)\n",
    "    f1 = f1_score(y_test, pred)\n",
    "    roc_auc = roc_auc_score(y_test, pred)\n",
    "    print('오차 행렬')\n",
    "    print(confusion)\n",
    "    print(f'정확도 : {accuracy:.4f}, 정밀도 : {precision:.4f}, 재현율 : {recall:.4f}, F1 : {f1:.4f}, AUC:{roc_auc:4f}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48226b11",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
