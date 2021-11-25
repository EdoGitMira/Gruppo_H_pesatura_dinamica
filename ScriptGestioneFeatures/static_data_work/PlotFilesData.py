import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from math import *


def prepare_arrays(masses_X, masses_value_y, std_dev = '0'):

    masses_X = [[masses_X[i]] for i in range(len(masses_X))]

    masses_X = np.array(masses_X)
    masses_value_y = np.array(masses_value_y)

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
    mean_squared_er = round(mean_squared_error(masses_value_y, means_y_pred),20)
    dev_std = sqrt(mean_squared_er)
    det_coeff = round(r2_score(masses_value_y, means_y_pred),20)


    # The coefficients
    print("Coefficients: \n", reg_coeff)
    # The mean squared error
    print(f"Mean squared error: {mean_squared_er}" )
    print(f"stddev: {dev_std}" )
    # The coefficient of determination: 1 is perfect prediction
    print(f"Coefficient of determination: {det_coeff}" )

    # Plot outputs
    plt.scatter(masses_X, masses_value_y, color="black")
    plt.plot(masses_X, means_y_pred, color="blue", linewidth=3)

    #plt.xticks()
    #plt.yticks()

    plt.xlabel('grams')
    plt.ylabel('Voltage')
    plt.title('Taratura Statica')
    plt.show()
