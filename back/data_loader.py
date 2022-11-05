import json
import pandas as pd


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
    return parse_to_dataframe(jdata)


if __name__ == '__main__':
    print(get_dataframe_from_json())
