import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    weight_more_than_100 = pd.DataFrame(animals[animals['weight']>100].sort_values(by="weight", ascending=False)['name'])
    # weight_more_than_100_sorted = weight_more_than_100.sort_values(by="weight", ascending=False)
    # names = weight_more_than_100_sorted['name']
    # print(names)

    return weight_more_than_100