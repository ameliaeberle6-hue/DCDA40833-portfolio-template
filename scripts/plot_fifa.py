#
#!/usr/bin/env python3
#
"""Generate static preview charts for FIFA ranking dataset.
#

#
Creates two PNGs in the `images/` folder:
#
- `fifa_time_series.png`: total_points over time for selected top teams
#
- `fifa_top10_latest.png`: horizontal bar chart of top 10 teams by total_points at the latest date
#
"""
#
import pandas as pd
#
import matplotlib.pyplot as plt
#
import os
#

#
IN_FILE = "data/clean/fifa_ranking_clean.csv"
#
OUT_DIR = "images"
#
os.makedirs(OUT_DIR, exist_ok=True)
#

#
def time_series(df):
#
    # pick a handful of prominent teams
#
    teams = ["Brazil", "Germany", "Argentina", "Italy", "France", "Spain"]
#
    df_ts = df[df['country_full'].isin(teams)].copy()
#
    df_ts['rank_date'] = pd.to_datetime(df_ts['rank_date'])
#
    plt.figure(figsize=(10,5))
#
    for team in teams:
#
        sub = df_ts[df_ts['country_full'] == team].sort_values('rank_date')
#
        if sub.empty:
#
            continue
#
        plt.plot(sub['rank_date'], sub['total_points'].astype(float), label=team)
#
    plt.legend()
#
    plt.title('FIFA total points over time — selected teams')
#
    plt.xlabel('Date')
#
    plt.ylabel('Total points')
#
    plt.tight_layout()
#
    out = os.path.join(OUT_DIR, 'fifa_time_series.png')
#
    plt.savefig(out)
#
    plt.close()
#
    print('Wrote', out)
#

#
def top10_latest(df):
#
    df['rank_date'] = pd.to_datetime(df['rank_date'])
#
    latest = df['rank_date'].max()
#
    df_latest = df[df['rank_date'] == latest]
#
    # Some datasets may have multiple entries per country for same date; take top by total_points
#
    df_latest = df_latest.sort_values('total_points', ascending=False).drop_duplicates('country_full')
#
    top10 = df_latest.head(10).iloc[::-1]
#
    plt.figure(figsize=(8,6))
#
    plt.barh(top10['country_full'], top10['total_points'].astype(float), color='tab:blue')
#
    plt.title(f'Top 10 countries by total points — {latest.date()}')
#
    plt.xlabel('Total points')
#
    plt.tight_layout()
#
    out = os.path.join(OUT_DIR, 'fifa_top10_latest.png')
#
    plt.savefig(out)
#
    plt.close()
#
    print('Wrote', out)
#

#
def main():
#
    df = pd.read_csv(IN_FILE)
#
    time_series(df)
#
    top10_latest(df)
#

#
if __name__ == '__main__':
#
    main()
