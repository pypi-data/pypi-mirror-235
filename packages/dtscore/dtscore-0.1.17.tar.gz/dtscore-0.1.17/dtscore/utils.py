"""
    Utilties
"""

# -------------------------------------------------------------------------------------------------
#   Partition a list
#   - return a generator that applies a "window_size" moving window to the list
#   - for list a=[1,2,3,4,5,6], partition(a,2) will generate [1,2], [2,3]...[5,6]
def partition(aList:list, windows_size:int):
    for start in range(0,len(aList)-windows_size+1):
        yield aList[start:start+windows_size]


#---------------------------------------------------------------
#   do summary print of dataframe
# def quick_print(df:pd.DataFrame, head_size:int=5, do_info:bool=False, do_exit:bool=False):
#     print(df.head(head_size))
#     if do_info : print(df.info())
#     print('**********************\n')
#     if do_exit : exit()

