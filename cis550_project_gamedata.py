from datetime import datetime as dt
import pandas as pd

dir_path = "/home/chemenggiitm/workspace/upenn_workspace/fall21_cis550/data/raw/retrosheet"

prcsd_dir_path = "/home/chemenggiitm/workspace/penn/data/processed/data"

prcsd_dir_path2 = "/home/chemenggiitm/workspace/penn/data/processed/tables/v1"

df = pd.read_csv(dir_path + "/game_data.csv")

cols = list(df.columns)

cols_df = pd.DataFrame()
cols_df["col_name"] = cols
cols_df["required"] = False
cols_df.to_csv(dir_path + "/game_data_cols.csv", index=False)

# Manual processing

MANUAL_DONE = 1

if MANUAL_DONE:

    req_cols_df = pd.read_csv(dir_path + "/req_game_data_cols.csv")
    req_cols = req_cols_df.loc[req_cols_df["required"], "col_name"].values
    req_df = df[req_cols]

    cond = req_df["GAME_ID"].apply(lambda x: 2011 <= int(x[3:7]) <= 2015)

    req_df = req_df[cond].sort_values(["GAME_DT", "GAME_ID"]).reset_index(drop=True)
    req_df.reset_index(inplace=True)
    req_df.rename(columns={"index": "ID"}, inplace=True)
    req_df["ID"] = req_df["ID"] + 1

    req_df.to_csv(dir_path + "/req_game_data.csv", index=False)

    req_df[["GAME_ID", "ID"]].rename(columns={"GAME_ID": "GameID"}).\
        to_csv(prcsd_dir_path + "/gameID.csv", index=False)
    req_df.drop(columns=["GAME_ID"], inplace=True)

    team_id_df = pd.read_csv(prcsd_dir_path + "/teamretroID.csv")

    team_id_dict = dict()
    for indx, row in team_id_df.iterrows():
        team_id_dict[row["teamIDretro"]] = row["ID"]

    rretroIDMap = {
        "WSN": "WAS",
        "ANA": "LAA",
    }

    req_df["AWAY_TEAM_ID"] = req_df["AWAY_TEAM_ID"].apply(lambda x: team_id_dict[x if x in team_id_dict else rretroIDMap[x]])
    req_df["HOME_TEAM_ID"] = req_df["HOME_TEAM_ID"].apply(lambda x: team_id_dict[x if x in team_id_dict else rretroIDMap[x]])

    park_id_df = pd.read_csv(prcsd_dir_path + "/parkID.csv")

    park_id_dict = dict()
    for indx, row in park_id_df.iterrows():
        park_id_dict[row["ParkID"]] = row["ID"]

    req_df["PARK_ID"] = req_df["PARK_ID"].apply(lambda x: park_id_dict[x])

    req_df["GAME_DT"] = req_df["GAME_DT"].apply(lambda x: dt.strptime(str(x), "%Y%m%d"))
    req_df["GAME_DT"] = req_df["GAME_DT"].apply(lambda x: dt.strftime(x, "%Y-%m-%d"))

    req_cols_order = ['ID', 'PARK_ID', 'HOME_TEAM_ID', 'AWAY_TEAM_ID', 'HOME_SCORE_CT',
                      'AWAY_SCORE_CT', 'GAME_DT', 'ATTEND_PARK_CT', 'MINUTES_GAME_CT',
                      'INN_CT',  'HOME_HITS_CT', 'AWAY_HITS_CT', 'HOME_ERR_CT',
                      'AWAY_ERR_CT', 'HOME_LOB_CT', 'AWAY_LOB_CT', 'OUTS_CT']

    req_df = req_df[req_cols_order]

    req_df.columns = ['ID', 'Park', 'HomeTeam', 'AwayTeam', 'HomeScore', 'AwayScore',
                      'Date', 'Attendance', 'Minutes', 'Innings',  'HomeHits', 'AwayHits',
                      'HomeErr', 'AwayErr', 'HomeLob', 'AwayLob', 'Outs']

    req_df.to_csv(prcsd_dir_path + "/game.csv", index=False)
    req_df.to_csv(prcsd_dir_path2 + "/game.csv", index=False)
