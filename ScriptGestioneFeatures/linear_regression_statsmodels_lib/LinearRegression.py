import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


def create_data_frame():
    df = pd.DataFrame({'hours': [1, 2, 4, 5, 5, 6, 6, 7, 8, 10, 11, 11, 12, 12, 14],
                       'score': [64, 66, 76, 73, 74, 81, 83, 82, 80, 88, 84, 82, 91, 93, 89]})
    return df


def print_scatter_plot(df):
    plt.scatter(df.hours, df.score)
    plt.title('Hours studied vs. Exam Score')
    plt.xlabel('Hours')
    plt.ylabel('Score')
    plt.show()


def fit_regression_model(df):
    y = df['score']
    x = df[['hours']]
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    print(model.summary())
    return model


def print_residual_plot(model):
    fig = plt.figure(figsize=(8, 6))
    fig = sm.graphics.plot_regress_exog(model, 'hours', fig=fig)
    plt.show()
    return


def get_r_squared(model):
    return model.rsquared


def get_st_err_of_the_fit(model):
    mse_resid = model.mse_resid
    return np.sqrt(mse_resid)
