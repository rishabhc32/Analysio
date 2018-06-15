import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier


def plot_feature_importance_diabetes(model):
    diabetes_features = [x for i,x in enumerate(diabetes.columns) if i!=8]
    plt.figure(figsize=(8,6))
    n_features = 8
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), diabetes_features)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.ylim(-1, n_features)

def feature_dependence_tree(X_train, y_train):
    tree = DecisionTreeClassifier(max_depth=3, random_state=0)
    tree.fit(X_train, y_train)

    plot_feature_importance_diabetes(tree)
    plt.show()

def feature_dependence_gradient_boost(X_train, y_test):
    gb = GradientBoostingClassifier(random_state=0, max_depth=1)
    gb.fit(X_train, y_train)

    plot_feature_importance_diabetes(gb)
    plt.show()

def show_hist(data):
    data.groupby('Outcome').hist(figsize=(9, 9))

if __name__ == '__main__':

    diabetes = pd.read_csv('diabetes.csv')
    show_hist(diabetes)

    X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)

    feature_dependence_tree(X_train, y_train)
    feature_dependence_gradient_boost(X_train, y_train)
    