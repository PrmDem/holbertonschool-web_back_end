// Returns an array of objects filtered by city
export default function getStudentsByLocation(studentsList, city) {
  const byCity = studentsList.filter((stdn) => stdn.location === city);
  return byCity;
}
