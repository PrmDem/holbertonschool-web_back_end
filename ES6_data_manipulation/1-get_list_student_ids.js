/* Returns array of IDs from student list.
If the provided argument isn't an array,
function returns an empty array.*/

export default function getListStudentIds(studentsList) {
  if (!Array.isArray(studentsList)) return [];

  const idList = studentsList.map(stdn => stdn.id);
  return idList;
}
