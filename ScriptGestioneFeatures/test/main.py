from LinearRegression import *

if __name__ == '__main__':
    df = create_data_frame()
    print_scatter_plot(df)
    model = fit_regression_model(df)
    print_residual_plot(model)
    st_err_of_the_fit = get_st_err_of_the_fit(model)
    r_squared = get_r_squared(model)
    print('st_err_of_the_fit = ', st_err_of_the_fit)
    print('r_squared = ', r_squared)
