import json
import pandas as pd
import random
from sklearn.preprocessing import MinMaxScaler


def get_json_from_filename(filename):
    def parse_to_one_dict(airline_res: dict):
        result = dict()
        for k in airline_res:
            if type(airline_res[k]) == dict:
                for k2 in airline_res[k]:
                    result[k2] = airline_res[k][k2]
            else:
                result[k] = airline_res[k]

        return result

    with open(filename, 'r') as file:
        jdata = json.load(file)

    return [parse_to_one_dict(one_airline_data) for one_airline_data in jdata]


def parse_to_dataframe(data: list[dict]):
    travel_classes = {'Eco Plus': 0, "Eco": 1, "Business": 2}
    df = pd.DataFrame(data)
    df.satisfaction = [1 if x == "satisfied" else 0 for x in df.satisfaction]
    df.travelType = [1 if "Business" in x else 0 for x in df.travelType]
    df.gender = [1 if x == "Male" else 0 for x in df.gender]
    df.type = [1 if "Loyal" in x else 0 for x in df.type]
    df.travelClass = [travel_classes[x] for x in df.travelClass]

    for col in df.columns:
        df[col] = pd.to_numeric(df[col])

    df['arrivalDelayInMinutes'].fillna(round(df['arrivalDelayInMinutes'].mean(), 1), inplace=True)
    return df


def get_dataframe_from_json(filename='airline_passenger_satisfaction_dataset.json'):
    jdata = get_json_from_filename(filename)
    df = parse_to_dataframe(jdata)
    df = add_airlines(df)
    df = replace_age_with_age_groups(df)

    return df


def add_airlines(df):
    airlines = ["Qatar Airways", "Singapore Airlines", "Emirates", "ANA All Nippon Airways", "Qantas Airways",
                "Japan Airlines", "Turkish Airlines", "Air France", "Korean Air", "Swiss International Air Lines"]
    N = len(airlines)

    airlines_vals = []
    for i in range(N):
        _N = df.shape[0] // N if i < N - 1 else df.shape[0] - len(airlines_vals)
        airlines_vals += [airlines[i] for _ in range(_N)]

    random.shuffle(airlines_vals)
    df["airline"] = airlines_vals
    df = pd.get_dummies(data=df, columns=["airline"])

    return df


def replace_age_with_age_groups(df):
    def age_to_age_group(age):
        if age < 18:
            return "child"
        elif age < 35:
            return "young adult"
        elif age < 50:
            return "mid adult"
        else:
            return "elder"

    age_groups_values = [age_to_age_group(age) for age in df["age"]]
    df["age"] = age_groups_values
    df = pd.get_dummies(data=df, columns=["age"])

    return df


def scale_all(df):
    scaler = MinMaxScaler()
    scaler.fit(df)
    X = scaler.transform(df)

    return X


if __name__ == '__main__':
    df = get_dataframe_from_json()
    print(df.info())
    X = scale_all(df)
    print(X)
