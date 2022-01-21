import os
import pandas as pd

def process(path):
    files = [os.path.join(path, f) for f in os.listdir(path)]
    out_df = pd.DataFrame()

    for file in files:
        file = file.lower()
        print(file)
        df = pd.read_csv(file, sep=' ')
        df['height(nm)'] = df['height(nm)'].apply(lambda s: float(str(s)[:-2]))
        df['period(mkm)'] = df['period(mkm)'].apply(lambda s: float(str(s)[:-3]))
        df['expose(nm)'] = df['expose(nm)'].apply(lambda s: float(str(s)[:-2]))

        batch = file[file.rfind('\\') + 1:-4]
        df['batch'] = batch

        out_df = pd.concat([out_df, df])
        df.to_excel(file.replace('.txt', '.xlsx'), index=False)

    out_df.to_excel(path + '\\!master.xlsx', index=False, engine='openpyxl')

process(r'D:\work\python\fiddle\TXT')
