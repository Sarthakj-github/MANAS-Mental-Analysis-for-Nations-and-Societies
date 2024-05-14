import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso, ElasticNet, LinearRegression, BayesianRidge
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor


def read_data():
    df1 = pd.read_csv('mental-and-substance-use-as-share-of-disease.csv')
    df2 = pd.read_csv('prevalence-by-mental-and-substance-use-disorder.csv')
    return df1, df2


def fill_missing_values(df1, df2):
    numeric_columns = df1.select_dtypes(include=[np.number]).columns
    df1[numeric_columns] = df1[numeric_columns].fillna(df1[numeric_columns].mean())
    numeric_columns = df2.select_dtypes(include=[np.number]).columns
    df2[numeric_columns] = df2[numeric_columns].fillna(df2[numeric_columns].mean())
    df1.dropna(inplace=True)
    df2.dropna(inplace=True)
    return df1, df2


def convert_data_types(df1, df2):
    df1['DALYs (Disability-Adjusted Life Years) - Mental disorders - Sex: Both - Age: All Ages (Percent)'] = df1[
        'DALYs (Disability-Adjusted Life Years) - Mental disorders - Sex: Both - Age: All Ages (Percent)'].astype(
        float)
    df2['Schizophrenia disorders (share of population) - Sex: Both - Age: Age-standardized'] = df2[
        'Schizophrenia disorders (share of population) - Sex: Both - Age: Age-standardized'].astype(float)
    df2['Bipolar disorders (share of population) - Sex: Both - Age: Age-standardized'] = df2[
        'Bipolar disorders (share of population) - Sex: Both - Age: Age-standardized'].astype(float)
    df2['Eating disorders (share of population) - Sex: Both - Age: Age-standardized'] = df2[
        'Eating disorders (share of population) - Sex: Both - Age: Age-standardized'].astype(float)
    df2['Anxiety disorders (share of population) - Sex: Both - Age: Age-standardized'] = df2[
        'Anxiety disorders (share of population) - Sex: Both - Age: Age-standardized'].astype(float)
    df2['Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)'] = df2[
        'Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)'].astype(float)
    df2['Depressive disorders (share of population) - Sex: Both - Age: Age-standardized'] = df2[
        'Depressive disorders (share of population) - Sex: Both - Age: Age-standardized'].astype(float)
    df2['Prevalence - Alcohol use disorders - Sex: Both - Age: Age-standardized (Percent)'] = df2[
        'Prevalence - Alcohol use disorders - Sex: Both - Age: Age-standardized (Percent)'].astype(float)
    return df1, df2


def merge_data(df1, df2):
    merged_df = pd.merge(df1, df2, on=['Entity', 'Code', 'Year'])
    return merged_df


def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


def process_input_data(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    data.popitem()
    data = {key: float(value) for key, value in data.items()}
    new_data = pd.DataFrame({
        'Schizophrenia disorders (share of population) - Sex: Both - Age: Age-standardized': [data['schizophrenia']],
        'Bipolar disorders (share of population) - Sex: Both - Age: Age-standardized': [data['bipolar']],
        'Eating disorders (share of population) - Sex: Both - Age: Age-standardized': [data['eating']],
        'Anxiety disorders (share of population) - Sex: Both - Age: Age-standardized': [data['anxiety']],
        'Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)': [data['drugUse']],
        'Depressive disorders (share of population) - Sex: Both - Age: Age-standardized': [data['depressive']],
        'Prevalence - Alcohol use disorders - Sex: Both - Age: Age-standardized (Percent)': [data['alcoholUse']]
    })
    return new_data


def fit_models(X_train, y_train, new_data):
    models = [
        Ridge(), Lasso(), ElasticNet(), LinearRegression(), BayesianRidge(),
        SVR(), DecisionTreeRegressor(), RandomForestRegressor(), XGBRegressor(),
        KNeighborsRegressor(), MLPRegressor(max_iter=500), GradientBoostingRegressor()
    ]

    output_dict = {}
    for model in models:
        model.fit(X_train, y_train)
        predicted_output = model.predict(new_data)
        output_value = float(predicted_output[0])
        output_dict[type(model).__name__] = output_value

    with open('data.json', 'w') as json_file:
        json.dump(output_dict, json_file)


def master_function(file_path):
    df1, df2 = read_data()
    df1, df2 = fill_missing_values(df1, df2)
    df1, df2 = convert_data_types(df1, df2)
    merged_df = merge_data(df1, df2)
    X = merged_df[['Schizophrenia disorders (share of population) - Sex: Both - Age: Age-standardized',
                   'Bipolar disorders (share of population) - Sex: Both - Age: Age-standardized',
                   'Eating disorders (share of population) - Sex: Both - Age: Age-standardized',
                   'Anxiety disorders (share of population) - Sex: Both - Age: Age-standardized',
                   'Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)',
                   'Depressive disorders (share of population) - Sex: Both - Age: Age-standardized',
                   'Prevalence - Alcohol use disorders - Sex: Both - Age: Age-standardized (Percent)']]
    y = merged_df['DALYs (Disability-Adjusted Life Years) - Mental disorders - Sex: Both - Age: All Ages (Percent)']
    X_train, X_test, y_train, y_test = split_data(X, y)
    new_data = process_input_data(file_path)
    fit_models(X_train, y_train, new_data)

# master_function("fetchedData/input.json")