import json
import pandas as pd
constants=[]
def decoder_func():

    file = 'WOConfigApp.xlsx'
    data = pd.ExcelFile(file)
    sheets=data.sheet_names
    for sheet in sheets:
        df = data.parse(sheet)
        ht=df.to_dict()
        c={}
        if ht:
            for i in range(len(ht)):
                if i!=2:
                    if len(ht)>=2 and i==0:
                        key=[*ht]
                        a=[y.encode("ascii", "ignore") for y in ht[key[0]].values() if type(y)!=float and type(y)!=int]

                    elif len(ht)>=2 and i==1:
                        key=[*ht]
                        b=[y.encode("ascii", "ignore")   for y in ht[key[1]].values() if type(y)!=float and type(y)!=int]
            for a,b in zip(a,b):
                a=a.decode()
                b=b.decode()
                c[a]=b  
            sheet=sheet.encode("ascii", "ignore").decode()
            insert_dic={sheet:c}
            constants.append(insert_dic)
    with open('output.json','w') as file:

        file.write(json.dumps(constants,indent=2))
    return constants
decoder_func()
