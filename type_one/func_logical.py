import datetime

def calc_time_failure(a):
    '''
    This func calculated summary time of failures for selected stations, 
    which passed in the arg 'a'. 
    '''
    s = datetime.timedelta(0,0)
    list_of_delt_time = []
    for object in a:
        list_of_delt_time.append(object.delt_time)
    for delt_time in list_of_delt_time:
        s = s + delt_time
    return s