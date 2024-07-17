import pandas as pd
TABS = ["AR comp","RT2657","RT2665","RT2702","RT2721","RT2789","RT2791"]

if __name__=="__main__":
    num_tabs = 2
    final_df = None
    for i in range(num_tabs):
        skip = 0 if i == 0 else 1
        df = pd.read_csv("test.csv", usecols=[3* i +skip], skiprows=1)
        df.columns =["gene"]
        
        df[TABS[i]] = 1
        print(df)

        final_df = df if final_df is None else pd.merge(final_df, df, how="outer", on="gene")
    final_df.fillna(0, inplace=True)
    final_df["overlap_counts"] = final_df[final_df.columns[1:]].sum(axis = 1)
    print(final_df)
    final_df.to_csv("overlap_summary.csv")




