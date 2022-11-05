import { useEffect, useState } from "react";
import { sendResult } from "../apis/backend";

const Dashboard = () => {
  const [types, setTypes] = useState({
    info: [
      {
        name: "Travel Type",
        values: ["Personal Travel", "Business Travel"],
      },
      { name: "Travel Class", values: ["Business", "Eco", "Eco Plus"] },
      {
        name: "Travel Distance",
        values: ["Short", "Middle", "Long"],
      },
      { name: "Gender", values: ["Female", "Male"] },
      {
        name: "Passenger Type",
        values: ["Loyal Customer", "Disloyal Customer"],
      },
      {
        name: "Age",
        values: ["Child", "Young Adult", "Mid Adult", "Elder"],
      },
    ],
    review: [
      "Wifi Service",
      "Time Convenient",
      "Booking Ease",
      "Gate Location",
      "Food",
      "Boarding",
      "Seat Comfort",
      "Entertainment",
      "Onboard Service",
      "Leg Room Service",
      "Baggage Handling",
      "CheckinService",
      "Inflight Service",
      "Cleanliness",
      "Departure Delay In Minutes",
      "Arrival Delay In Minutes",
    ],
  });
  const [chosenTypes, setChosenTypes] = useState({
    info: [
      {
        name: "Travel Type",
        values: ["Personal Travel", "Business Travel"],
      },
      { name: "Travel Class", values: ["Business", "Eco", "Eco Plus"] },
      {
        name: "Travel Distance",
        values: ["Short", "Middle", "Long"],
      },
      { name: "Gender", values: ["Female", "Male"] },
      {
        name: "Passenger Type",
        values: ["Loyal Customer", "Disloyal Customer"],
      },
      {
        name: "Age",
        values: ["Child", "Young Adult", "Mid Adult", "Elder"],
      },
    ],
    review: [
      "Wifi Service",
      "Time Convenient",
      "Booking Ease",
      "Gate Location",
      "Food",
      "Boarding",
      "Seat Comfort",
      "Entertainment",
      "Onboard Service",
      "Leg Room Service",
      "Baggage Handling",
      "CheckinService",
      "Inflight Service",
      "Cleanliness",
      "Departure Delay In Minutes",
      "Arrival Delay In Minutes",
    ],
  });
  const [submitted, setSubmitted] = useState(false);
  const [result, setResult] = useState("Result");

  const infoClick = (type, value) => {
    if (
      chosenTypes.info
        .filter((info) => info.name === type.name)[0]
        .values.filter((value_name) => value_name === value).length > 0
    ) {
      const test = chosenTypes.info.map((chosenType) => {
        return {
          ...chosenType,
          values: chosenType.values.filter(
            (values_name) => values_name !== value
          ),
        };
      });
      setChosenTypes({
        info: test,
        review: chosenTypes.review,
      });
    } else {
      const test = chosenTypes.info.map((chosenType) => {
        if (chosenType.name === type.name) {
          return {
            ...chosenType,
            values: [...chosenType.values, value],
          };
        } else {
          return chosenType;
        }
      });
      setChosenTypes({
        info: test,
        review: chosenTypes.review,
      });
    }
  };

  const reviewClick = (type) => {
    if (chosenTypes.review.includes(type)) {
      setChosenTypes({
        info: chosenTypes.info,
        review: chosenTypes.review.filter((review) => type !== review),
      });
    } else {
      setChosenTypes({
        info: chosenTypes.info,
        review: [...chosenTypes.review, type],
      });
    }
  };

  const submitData = async (e) => {
    e.preventDefault();
    const response = await sendResult(chosenTypes);
    console.log(result);
    setResult(response);
    setSubmitted(true);
  };

  return (
    <>
      {!submitted && (
        <div className={"dashboard-container"}>
          <div className={"dashboard-info"}>
            {types.info.map((type) => (
              <div className={"dashboard-info-type"}>
                <p>{type.name}</p>
                {type.values.map((value, index) => (
                  <label>
                    <input
                      key={index}
                      type={"checkbox"}
                      defaultChecked={true}
                      onClick={() => infoClick(type, value)}
                    />
                    {value}
                  </label>
                ))}
              </div>
            ))}
          </div>
          <div className={"dashboard-reviews"}>
            {types.review.map((type) => (
              <label>
                <input
                  key={type}
                  value={"on"}
                  type={"checkbox"}
                  defaultChecked={true}
                  onClick={() => reviewClick(type)}
                />
                {type}
              </label>
            ))}
          </div>
          <a
            className={"btn btn-primary"}
            href={"/results"}
            onClick={(e) => submitData(e)}
          >
            Submit
          </a>
        </div>
      )}
      {submitted && (
        <div className={"dashboard-result"}>
          <h1>Your results</h1>
          <h2>{result}</h2>
        </div>
      )}
    </>
  );
};

export default Dashboard;
