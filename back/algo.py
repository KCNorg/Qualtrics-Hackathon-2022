from back.constans import reverse_parser
from back.data_loader import get_dataframe_from_json


def calculate_result(row, problem, satisfaction_threshold):
    return 1 if satisfaction_threshold > row[problem] else 0


def calculate_score(df, params, problems, satisfaction_threshold):
    query_string = ""

    for param in params:
        query_string += reverse_parser[param] + "=='" + param + "'and "

    query_string = query_string[:-4]
    df_queried = df.query(query_string)

    score = 0

    for problem in problems:
        score += sum(df_queried.apply(lambda row: calculate_result(row, problem, satisfaction_threshold), axis=1))

    return score


params = ["Male", "Business"]
problems = ["wifiService", "onboardService"]
satisfaction_threshold = 3

df = get_dataframe_from_json()
calculate_score(df, params, problems, satisfaction_threshold)
