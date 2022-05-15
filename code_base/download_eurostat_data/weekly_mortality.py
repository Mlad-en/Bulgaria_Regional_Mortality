import pathlib
import os
import pandas as pd


if __name__ == '__main__':
    file = r'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&file=data%2Fdemo_r_mweek3.tsv.gz'
    df = pd.read_csv(file, sep='\t')
    save_loc = pathlib.Path(f'{pathlib.Path(__file__).parent.resolve()}/../../raw_data/demo_r_mweek3.tsv')
    df.to_csv(save_loc, index=False)
    print('Weekly Regional Mortality downloaded successfully.')