import pandas as pd

def create_example():
    """
    Return a data frame example
    """
    data = pd.DataFrame({
        'Produto' : ['café' , 'chocolate' , 'arroz'],
        'Preços' : [6 , 5 , 8],
        'Quatity' : [1 , 10 , 2]
    })
    return data