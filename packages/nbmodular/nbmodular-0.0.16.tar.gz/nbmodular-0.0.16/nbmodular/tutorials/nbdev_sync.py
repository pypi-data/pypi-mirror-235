def first_function():
    a = 3 
    print ('a', a)
    return a
def second_function():
    b = 4
    c = a+b
    print (a, b, c)
    return c,b

def nbdev_sync_pipeline (test=False, load=True, save=True, result_file_name="nbdev_sync_pipeline"):

    # load result
    result_file_name += '.pk'
    path_variables = Path ("nbdev_sync") / result_file_name
    if load and path_variables.exists():
        result = joblib.load (path_variables)
        return result

    a = first_function ()
    c, b = second_function ()

    # save result
    result = Bunch (c=c,a=a,b=b)
    if save:    
        path_variables.parent.mkdir (parents=True, exist_ok=True)
        joblib.dump (result, path_variables)
    return result
