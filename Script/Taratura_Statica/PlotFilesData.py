import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from math import *

import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import summary_table
from statsmodels.sandbox.regression.predstd import wls_prediction_std


def fit_regression_model(df):
    y = df['value']
    x = df[['mass']]
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    print(model.summary())
    return model


def print_residual_plot(model):
    fig = plt.figure(figsize=(8, 6))
    fig = sm.graphics.plot_regress_exog(model, 'mass', fig=fig)
    plt.show()
    return


def create_data_frame(lst, lst2):
    df = pd.DataFrame(list(zip(lst, lst2)), columns=['mass', 'value'])
    print()
    return df


def prepare_arrays(masses_X, masses_value_y, std_dev='0'):

    '''Fa il grafico e calcola tutti i dati della regressione Lineare
    :param masses_X : valore di tensione
    :param masses_value_y : valore in grammi
    '''

    df = create_data_frame(masses_X, masses_value_y)
    model = fit_regression_model(df)

    masses_X = [[masses_X[i]] for i in range(len(masses_X))]
    masses_X = np.array(masses_X)
    masses_value_y = np.array(masses_value_y)

    # masses_value_Y_ = [[masses_value_y[i]] for i in range(len(masses_value_y))]
    # masses_value_Y_ = np.array(masses_value_Y_)

    '''
    # Split the data into training/testing sets
    masses_X_train = masses_X[:-20]
    masses_X_test = masses_X[-20:]

    # Split the targets into training/testing sets
    means_y_train = means_y[:-20]
    means_y_test = means_y[-20:]
    '''

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(masses_X, masses_value_y)

    # Make predictions using the testing set
    means_y_pred = regr.predict(masses_X)

    reg_coeff = regr.coef_
    mean_squared_er = round(mean_squared_error(masses_value_y, means_y_pred), 20)
    dev_std = sqrt(mean_squared_er)
    det_coeff = round(r2_score(masses_value_y, means_y_pred), 20)

    # The coefficients
    print("Coefficients: \n", reg_coeff)
    # The mean squared error
    print(f"Mean squared error: {mean_squared_er}")
    print(f"stddev: {dev_std}")
    # The coefficient of determination: 1 is perfect prediction
    print(f"Coefficient of determination: {det_coeff}")

    st, data, ss2 = summary_table(model, alpha=0.05)
    prstd, iv_l, iv_u = wls_prediction_std(model)

    fittedvalues = data[:, 2]
    predict_mean_se = data[:, 3]
    predict_mean_ci_low, predict_mean_ci_upp = data[:, 4:6].T
    predict_ci_low, predict_ci_upp = data[:, 6:8].T

    # Check we got the right things

    print(np.max(np.abs(model.fittedvalues - fittedvalues)))
    print(np.max(np.abs(iv_l - predict_ci_low)))
    print(np.max(np.abs(iv_u - predict_ci_upp)))

    # Plot outputs
    plt.scatter(masses_X, masses_value_y, color="black")
    plt.plot(masses_X, means_y_pred, color="blue", linewidth=3)

    plt.plot(masses_X, predict_ci_low, 'r--', lw=2)
    plt.plot(masses_X, predict_ci_upp, 'r--', lw=2)
    plt.plot(masses_X, predict_mean_ci_low, 'r--', lw=2)
    plt.plot(masses_X, predict_mean_ci_upp, 'r--', lw=2)

    # plt.xticks()
    # plt.yticks()
    plt.rcParams.update({'font.size': 14})
    plt.xlabel('Segnale [V/V]')
    plt.ylabel('Massa [g]')

    plt.show()

    print_residual_plot(model)
