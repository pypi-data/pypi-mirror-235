'''
Date         : 2022-10-25 17:21:52
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-10-12 10:32:46
LastEditors  : BDFD
Description  : 
FilePath     : \execdata\standardization.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''


import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit


def encode(df):
    lable = LabelEncoder()
    for column in df:
        if df[column].dtypes == 'object':
            df[column] = lable.fit_transform(df[column])
    return df


def split(df, test_size=0.2, random_state=66):
    df_train, df_test = train_test_split(
        df, test_size=test_size, random_state=random_state)
    return df_train, df_test


def sep(df_train, df_test, target_variable):
    X_train = df_train.drop(target_variable, axis=1)
    y_train = df_train[target_variable]
    X_test = df_test.drop(target_variable, axis=1)
    y_test = df_test[target_variable]
    return X_train, y_train, X_test, y_test


def train_split(df, target_variable, test_size=0.2, random_state=66):
    df_train, df_test = train_test_split(
        df, test_size=test_size, random_state=random_state)
    X_train, y_train, X_test, y_test = sep(df_train, df_test, target_variable)
    return X_train, y_train, X_test, y_test


def strat_split(df, column):
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=66)
    for train_index, test_index in split.split(df, df[column]):
        df_train = df.loc[train_index]
        df_test = df.loc[test_index]
    return df_train, df_test
