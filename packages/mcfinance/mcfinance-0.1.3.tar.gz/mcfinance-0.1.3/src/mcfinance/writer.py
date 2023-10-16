import pandas as pd

def excel_writer(daf, words, filepath, years) -> None:
    '''Write dataframe into pandas dataframe or excel file'''
    web, name, info = words[1], words[0], words[3]
    if filepath != "":
        filepath += "/"
    fdf = daf.drop(daf.iloc[:, years+1:],axis = 1)
    writer = pd.ExcelWriter(filepath+web+'_'+name+'_'+info+'.xlsx')
    fdf.to_excel(writer)
    writer.close()
    print(f'{name} {info} data is written successfully to Excel File.')
    
def df_writer(daf, years) -> pd.DataFrame:
    fdf = daf.drop(daf.iloc[:, years+1:],axis = 1)
    return fdf