const url = "http://localhost:5000";

export const sendResult = async (result) => {
  const res = await fetch(url + "/types", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify(result),
  });
  return await res.text();
};

export default { sendResult };
