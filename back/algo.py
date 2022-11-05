from data_loader import get_dataframe_from_json
import pandas as pd
from constans import inv_reviews, inv_info, reviews_reverse
from constans import reverse_parser
import itertools


def calculate_result(row, problem, satisfaction_threshold):
    return 1 if satisfaction_threshold >= row[problem] else 0


def calculate_score(df, params_list, problems, satisfaction_threshold):
    score_result = []
    for params in params_list:
        query_string = ""
        for param in params:
            query_string += reverse_parser[param] + "=='" + param + "'and "
        query_string = query_string[:-4]
        df_queried = df.query(query_string)

        score = 0
        for problem in problems:
            score += sum(df_queried.apply(lambda row: calculate_result(row, reviews_reverse[problem], satisfaction_threshold), axis=1))
        if df_queried.shape[0] > 0:
            score_result.append((score, df_queried.shape[0], params))
    return score_result


def parse_info(info):
    result = dict()
    for d in info:
        result[inv_info[d['name']]['name']] = d['values']

    return result


def get_filtered_df(params):
    df = get_dataframe_from_json()
    info, review = parse_info(params['info']), params['review']
    df = df.filter(items=[inv_reviews[x] for x in review] + list(info.keys()))

    for k, v in info.items():
        df = df[df[k].isin(v)]

    return df


def get_all_combinations(params):
    lists = [info['values'] for info in params['info']]
    lists = list(filter(lambda x: len(x) != 0, lists))
    return list(itertools.product(*lists))


def get_results(params):
    df = get_filtered_df(params)
    # print(get_all_combinations(params))
    result = calculate_score(df, get_all_combinations(params), params["review"], 3)
    result = sorted(result)[:10:-1]

    str_result = ['TOP 10 most dissatisfied groups']

    for i in range(len(result)):
        str_result.append(f'{i+1}. {result[i][3]}')

    return str_result
# =======
# params = ["Male", "Business"]
# problems = ["wifiService", "onboardService"]
# satisfaction_threshold = 3
#
# df = get_dataframe_from_json()
# calculate_score(df, params, problems, satisfaction_threshold)
# >>>>>>> 5e8089b327056e0d297e27cffab71cd616a4b545
