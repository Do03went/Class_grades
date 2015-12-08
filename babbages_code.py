Python 2.7.10 |Anaconda 2.3.0 (64-bit)| (default, May 28 2015, 16:44:52) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def statistics(grades):
    
    import numpy as np 
    
    mean = np.mean(grades)
    std = np.std(grades)
    high = np.max(grades)
    low = np.min(grades)
    

    return mean,std,high,low
