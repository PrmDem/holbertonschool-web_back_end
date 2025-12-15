/* Provided with an array of new grades in this format:
{ studentId: 31, grade: 78 }
 Updates the grades of students from a specified city.
 If newGrade is empty, the final grade will be 'N/A'. */

export default function updateStudentGradeByCity(studentList, city, newGrades) {
  return studentList
    .filter(stdn => stdn.location === city)
    .map(stdn => {
      const found = newGrades.find(grade => grade.studentId === stdn.id);
      return {
        ...stdn,
        grade: found ? found.grade : 'N/A'
      };
    })
}
