import json
import pandas as pd
import random
from constans import age_to_group, flight_distance_to_group


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
    df = pd.DataFrame(data)
    for col in df.columns:
        if (str(df[col][0][0]).isdigit()):
            df[col] = pd.to_numeric(df[col])

    df['arrivalDelayInMinutes'].fillna(round(df['arrivalDelayInMinutes'].mean(), 1), inplace=True)
    df.loc[df['travelType'] == 'Business travel', 'travelType'] = 'Business Travel'
    df.loc[df['type'] == 'disloyal Customer', 'type'] = 'Disloyal Customer'

    return df


def get_dataframe_from_json(filename='airline_passenger_satisfaction_dataset.json'):
    jdata = get_json_from_filename(filename)
    df = parse_to_dataframe(jdata)
    df = add_airlines(df)
    df = replace_age_with_age_groups(df)
    df = replace_flight_distance(df)

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

    return df


def replace_age_with_age_groups(df):
    age_groups_values = [age_to_group(age) for age in df["age"]]
    df["age"] = age_groups_values

    return df


def replace_flight_distance(df):
    flight_distance_groups_values = [flight_distance_to_group(flight_distance) for flight_distance in
                                     df["travelDistance"]]
    df["travelDistance"] = flight_distance_groups_values

    return df


if __name__ == '__main__':
    df = get_dataframe_from_json()
    print(df.info())
    print(df.head())