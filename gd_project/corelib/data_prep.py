import numpy as np
import pandas as pd

def reduce_mem_usage(df, verbose=True):
    """
    Reduce numeric 
    
    Parameters
    ----------
    :param df: pandas data frame
        pd.DataFrame object

    Return
    ------

    Pandas data frame object

    Future
    ------

    - optimisation by transfer float to int
    - reduce objects
    """
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    start_mem = df.memory_usage().sum() / 1024**2

    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
                    
    end_mem = df.memory_usage().sum() / 1024**2
    if verbose: print('Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)'.format(end_mem, 100 * (start_mem - end_mem) / start_mem))
    
    return df


def reduce_obj_mem_usage(df, verbose=True):
    """
    Reduce object. Return new data frame, containing only columns with dtype object.
    Columns with number of unique values, that is no more than 50%, recieve subtype category
    
    Parameters
    ----------

    :param df: 
    Pandas data frame
        pd.DataFrame object

    Return
    ------

    New pandas data frame, which contains only object and categorial dtype columns.
    All other columns is droped.

    Future
    ------

    - all columns return
    """
    df = df.select_dtypes(include=['object']).copy()

    df.describe()
    start_mem = df.memory_usage().sum() / 1024**2

    converted = pd.DataFrame()

    for col in df.columns:
        unic = len(df[col].unique())
        total = len(df[col])
        if unic / total < 0.5:
            converted.loc[:,col] = df[col].astype('category')
        else:
            converted.loc[:,col] = df[col]

    converted.describe()
    end_mem = converted.memory_usage().sum() / 1024**2

    if verbose: print('Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)'.format(end_mem, 100 * (start_mem - end_mem) / start_mem))

    return converted


def search_func(data, *cols):
    """
    Function return dictionary of the form: 'value': index, that can be used for
    mapping in ordered feature encoding estimators
    
    Parameters
    ----------

    :param data: 
    Pandas data frame
        pd.DataFrame object
    
    :param cols: 
    List of columns, where function search for unical ordered value
        list, tuple

    Return
    ------

    List of dicts, where keys are names of values for ordered encoding, and values are position in order    
    """
    full_map = []

    for i in cols:
        mapping = {}
        for idx, val in enumerate(pd.unique(sorted(data[i]))):
            mapping[val] = idx
        full_map.append(mapping)
        
    return full_map