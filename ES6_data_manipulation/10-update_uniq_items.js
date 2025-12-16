export default function updateUniqueItems(groceries) {
  if (!(groceries instanceof Map)) { // catches non-Map arguments
    throw new Error('Cannot process');
  }

  groceries.forEach((value, key) => { // (key, value) would not change values
    if (value === 1) { groceries.set(key, 100); }
  });
  return groceries;
}
