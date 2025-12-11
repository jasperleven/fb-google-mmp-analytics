import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

### --- SETTINGS ---
days = 14
campaigns_fb = [
    ("FB_Install_1", 101),
    ("FB_Optimization_2", 102),
    ("FB_Retargeting_3", 103),
]
campaigns_google = [
    ("GGL_UAC_1", 201),
    ("GGL_Install_2", 202),
    ("GGL_Prospecting_3", 203),
]

def gen_ad_data(campaigns, source):
    data = []
    for name, cid in campaigns:
        for i in range(days):
            date = (datetime.today() - timedelta(days=i)).strftime("%Y-%m-%d")
            
            impressions = np.random.randint(2000, 15000)
            clicks = int(impressions * np.random.uniform(0.01, 0.05))
            spend = round(clicks * np.random.uniform(0.15, 0.70), 2)
            installs = int(clicks * np.random.uniform(0.10, 0.35))

            data.append([date, cid, name, impressions, clicks, spend, installs, source])

    return pd.DataFrame(data, columns=[
        "date", "campaign_id", "campaign_name", 
        "impressions", "clicks", "spend", "installs", "source"
    ])

### --- GENERATE FB + GOOGLE ---
fb_df = gen_ad_data(campaigns_fb, "Facebook")
google_df = gen_ad_data(campaigns_google, "Google")

fb_df.to_csv("fb_ads.csv", index=False)
google_df.to_csv("google_ads.csv", index=False)

### --- GENERATE MMP (Adjust/AppsFlyer aggregated) ---
def gen_mmp_data(ad_df):
    data = []
    grouped = ad_df.groupby(["date", "campaign_id", "campaign_name"], as_index=False)\
                   .agg({"installs": "sum"})

    for _, row in grouped.iterrows():
        inst = row.installs
        
        d1_rev = round(inst * np.random.uniform(0.2, 0.8), 2)
        d7_rev = round(inst * np.random.uniform(0.5, 1.5), 2)

        data.append([
            row.date,
            row.campaign_id,
            row.campaign_name,
            inst,
            d1_rev,
            d7_rev
        ])
    
    return pd.DataFrame(data, columns=[
        "date", "campaign_id", "campaign_name", 
        "installs", "d1_revenue", "d7_revenue"
    ])

mmp_df = gen_mmp_data(pd.concat([fb_df, google_df]))

mmp_df.to_csv("mmp_data.csv", index=False)

print("Готово: fb_ads.csv, google_ads.csv, mmp_data.csv")

