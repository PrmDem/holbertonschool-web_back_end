export default function hasValuesFromArray(set, array) {
  const setArray = new Set(array); // Set can only be compared to Set-like objects
  return set.isSupersetOf(setArray);
}
