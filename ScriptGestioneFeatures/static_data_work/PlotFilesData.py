import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import IsolationForest
import PreparazioneFile


def prepare_arrays(masses_X, means_y, std_dev = '0'):

    masses_X = [[masses_X[i]] for i in range(len(masses_X))]
    masses_X = np.array(masses_X)
    means_y = np.array(means_y)

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
    regr.fit(masses_X, means_y)

    # Make predictions using the testing set
    means_y_pred = regr.predict(masses_X)


    reg_coeff = regr.coef_
    mean_squared_er = mean_squared_error(means_y, means_y_pred)
    det_coeff = r2_score(means_y, means_y_pred)


    # The coefficients
    print("Coefficients: \n", reg_coeff)
    # The mean squared error
    print("Mean squared error: %f" % mean_squared_er)
    # The coefficient of determination: 1 is perfect prediction
    print("Coefficient of determination: %f" % det_coeff)

    # Plot outputs
    plt.scatter(masses_X, means_y, color="black")
    plt.plot(masses_X, means_y_pred, color="blue", linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()
