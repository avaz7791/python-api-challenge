# module to caputure functions to use in our application
import scipy.stats as st

def lregression(x, y):

    # Calculate linear regression this function requieres 
    
    (slope, intercept, rvalue, pvalue, stderr) = st.linregress(x, y)
    lreg_values = x * slope + intercept
    line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
        
    plt.scatter(x, y)
    plt.plot(x, lreg_values, "r-")

    return line_eq


