import pandas as pd

from sklearn.model_selection import StratifiedKFold

import config

def create_fold(folds:int = 5):
    df:pd.DataFrame = pd.read_csv(config.TRAIN_FILE)
    # shuffle
    df = df.sample(frac=1, random_state=0).reset_index(drop=True)

    kf:StratifiedKFold = StratifiedKFold(n_splits=folds, shuffle=True, random_state=0)

    X = df.drop(config.TARGET_NAME, axis= 1).values
    y = df[config.TARGET_NAME].values

    for f, (train_idx, test_idx) in enumerate(kf.split(X=X, y=y)):
        df.loc[test_idx, 'kfold'] = f
    df.to_csv(config.TRAIN_KFOLDS_FILE, index=False)

if __name__ == '__main__':
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--fold', default=5)

    args = ap.parse_args()
    create_fold(int(args.fold))