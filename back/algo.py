from back.data_loader import get_dataframe_from_json
import pandas as pd


def calculate_weight(row, parameter, values):
    return values[str(row[parameter])]


def calculate_result(row, parameter, satisfactionThreshold):
    return row["weight"] * (1 if satisfactionThreshold > row[parameter] else 0)
    # return row["weight"] * max(satisfactionThreshold - row[parameter], 0)


def algo(params, satisfactionThreshold):
    df = get_dataframe_from_json()
    X = df.copy()
    X["weight"] = 0

    # print(XCopy["weight"])

    example_input_weights = params[0]
    example_input_problems = params[1]

    for key in example_input_weights.keys():
        X["weight"] += X.apply(lambda row: calculate_weight(row, key, example_input_weights[key]), axis=1)

    # print(XCopy["weight"])
    # print(sum(XCopy["weight"]))

    res = pd.DataFrame()
    # print(res)
    for problem in example_input_problems:
        res[problem] = X.apply(lambda row: calculate_result(row, problem, satisfactionThreshold), axis=1)

    # print(res)
    # print(sum(res["wifiService"]))


params = [{"gender": {"Female": 2, "Male": 1}, "travelClass": {"Eco Plus": 0, "Eco": 1, "Business": 4}},
          ["wifiService"]]

algo(params, 3)
