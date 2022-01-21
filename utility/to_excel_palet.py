import os
import pandas as pd

def process(path):
    files = [os.path.join(path, f) for f in os.listdir(path)]
    out_df = pd.DataFrame()

    for file in files:
        file = file.lower()
        print(file)
        df = pd.read_csv(file, sep=' ')
        df['angle(deg)'] = df['angle(deg)'].apply(lambda s: float(str(s)))
        df['period(mkm)'] = df['period(mkm)'].apply(lambda s: float(str(s)))
        df['expose(mkm)'] = df['expose(mkm)'].apply(lambda s: float(str(s))*1_000)

        df.columns = ['index', 'loc', 'angle(deg)', 'period(mkm)', 'expose(nm)']

        batch = file[file.rfind('\\') + 1:-4]
        df['batch'] = batch

        out_df = pd.concat([out_df, df])
        df.to_excel(file.replace('.txt', '.xlsx'), index=False)

    out_df.to_excel(path + '\\!master.xlsx', index=False, engine='openpyxl')

process(r'D:\work\python\fiddle\TXT')
