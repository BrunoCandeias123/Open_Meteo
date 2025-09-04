import pandas as pd
import logging

def write_csv_pandas(list_all_rows, out_path):
    df_list_all_rows = pd.DataFrame(list_all_rows)
    
    if df_list_all_rows.empty:
        logging.info("No rows to write.")
        return
    df_list_all_rows.to_csv(out_path, index=False)
    logging.info("Wrote %d rows × %d columns to %s", df_list_all_rows.shape[0], df_list_all_rows.shape[1], out_path)
