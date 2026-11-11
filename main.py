# Noah Shuldberg
# Program that reads a cfb dataset and displays teams that vary
# by number of wins by season.

import pandas as pd

# Read cfb file
cfb_data = pd.read_csv("cfb.csv")
while True:  
    # Validate user's season input  
    try:
        # Prompt user for their desired season.
        season = int(input("Which season would you like to view?: "))
        if season not in cfb_data["Season"].values:
            raise KeyError("The season you selected is not available. Please try again.")
        df_season = cfb_data[cfb_data["Season"] == season]
        
        # Define each group's list depending on # of wins
        ten_plus_wins = df_season.loc[df_season["Win"] >= 10, "Team"].tolist()
        eight_nine_wins = df_season.loc[(df_season["Win"] >= 8) & (df_season["Win"] <= 9), "Team"].tolist()
        six_seven_wins = df_season.loc[(df_season["Win"] >= 6) & (df_season["Win"] <= 7), "Team"].tolist()
        six_less_wins = df_season.loc[df_season["Win"] < 6, "Team"].tolist()

        teams = { "10 or more wins": ten_plus_wins,
                    "8-9 wins": eight_nine_wins,
                    "6-7 wins": six_seven_wins,
                    "Less than 6 wins": six_less_wins
        }

        # Display wins by category
        print("\n10 OR MORE WINS:")
        print("=================")
        print("\n".join(teams["10 or more wins"]))
        print("\n8-9 WINS:")
        print("=================")
        print("\n".join(teams["8-9 wins"]))
        print("\n6-7 WINS:")
        print("=================")
        print("\n".join(teams["6-7 wins"]))
        print("\nLESS THAN 6 WINS:")
        print("=================")
        print("\n".join(teams["Less than 6 wins"]))
        break
    except KeyError as e:
        print(e)