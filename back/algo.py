from data_loader import get_dataframe_from_json
import pandas as pd
from constans import inv_reviews, inv_info


def calculate_weight(row, parameter, values):
    return values[str(row[parameter])]


def calculate_result(row, parameter, satisfactionThreshold):
    return row["weight"] * (1 if satisfactionThreshold > row[parameter] else 0)
    # return row["weight"] * max(satisfactionThreshold - row[parameter], 0)


def parse_info(info):
    result = dict()
    for d in info:
        result[inv_info[d['name']]['name']] = d['values']
    print(result)

    return result


def get_filtered_df(params):
    df = get_dataframe_from_json()
    info, review = parse_info(params['info']), params['review']
    df = df.filter(items=[inv_reviews[x] for x in review] + list(info.keys()))

    for k, v in info.items():
        print(k, v)
        df = df[df[k].isin(v)]
        print(df)

    return df


# if __name__ == '__main__':
#     params = {'review': ['Food', 'Boarding'],
#               'info': [
#                   {
#                       "name": "Travel Type",
#                       "values": ["Personal Travel"]
#                   },
#                   {
#                       "name": "Travel Class",
#                       "values": ["Eco", "Eco Plus"]
#                   },
#                   {
#                       "name": "Travel Distance",
#                       "values": ["Middle", "Long"]
#                   },
#                   {
#                       "name": "Gender",
#                       "values": ["Female", "Male"]
#                   },
#                   {
#                       "name": "Passenger Type",
#                       "values": ["Loyal Customer", "Disloyal Customer"]
#                   },
#                   {
#                       "name": "Age",
#                       "values": ["Child", "Young Adult", "Mid Adult", "Elder"]
#                   }
#               ]
#               }
#
#     print(get_filtered_df(params))
