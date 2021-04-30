import os
import pandas as pd

def process(path):
    files = [os.path.join(path, f) for f in os.listdir(path)]
    for file in files:
        print(file)
        df = pd.read_csv(file, sep=' ')
        df['height(nm)'] = df['height(nm)'].apply(lambda s: float(str(s)[:-2]))
        df['period(mkm)'] = df['period(mkm)'].apply(lambda s: float(str(s)[:-3]))
        df['expose(nm)'] = df['expose(nm)'].apply(lambda s: float(str(s)[:-2]))

        df.to_excel(file.replace('.txt', '.xlsx'), index=False)


process(r'/TXT')
