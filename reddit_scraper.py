
import praw
import pandas as pd
import numpy as np

user_agent = "Scraper 1.0 by /u/lukas877"
reddit = praw.Reddit(
    client_id='s9KPZPL-Eme_mhpBmLjXYg',
    client_secret='vf79sdMvrsyET0Vamaw74yzjWPDaxg',
    user_agent=user_agent
)

subreddit_list = [
    'rapefantasies',
    'Slut',
    'needysluts',
    'barelylegalteens',
    'amihot',
    'Selfie',
    'xsmallgirls',
    'Nude_Selfie',
    'DadWouldBeProud',
    'Femdomdenial',
    'horny',
    'UnderwearGW',
    'DaughterTraining',
    'GirlsGW',
    'faces',
    'SchoolgirlsXXX',
    'slutsofsnapchat',
    'smallboobs',
    'SmallCutie',
    'naturaltitties',
    'Shawties',
    'TotalPackage',
    'Babes',
    'womenarethings',
    'HungryButts',
    'OnlyFansBlonde',
    'OnlyFansPetite',
    'PetiteTits',
    'Censoredforbetas',
    'raceplay',
    'forcedbreeding',
    'RealCute',
    'ClothedForPrejacs',
    'BabesNSFW',
    'dommes',
    'Selfie_Heaven',
    'SexyButClothed',
]

dataset = pd.DataFrame({'subreddit': [], 'title': [], 'score': []})
print(f"BEFORE {dataset}")
for subreddit in subreddit_list:
    print(f"Start subreddit {subreddit.upper()}")
    for submission in reddit.subreddit(subreddit).top(limit=100):
        new_datapoint = {'subreddit': subreddit, 'title': submission.title, 'score': submission.score}
        if np.isnan(dataset.index.max()):
            dataset.loc[0] = new_datapoint
        dataset.loc[dataset.index.max() + 1] = new_datapoint
print(f"AFTER {dataset}")

dataset.to_csv("dataset_100.csv")