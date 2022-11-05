const url = "";

export async function fetchTypes() {
  const res = await fetch(url + "/types");
  return await res.json();
}

export default { fetchTypes };
