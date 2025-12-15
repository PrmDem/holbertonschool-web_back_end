// Returns the sum of all student ids
export default function getStudentIdsSum(studentsList) {
  return studentsList.reduce(
    (acc, student) => acc + student.id, 0);
}
