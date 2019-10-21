let numericals = s => {
  let obj = {};
  return [...s].map(c => (obj[c] = (obj[c] || 0) + 1).toString()).join("");
}