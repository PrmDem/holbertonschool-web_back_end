export default class HolbertonCourse {
  constructor(name, length, students) {
    // Verify name param is a string
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    // Verify length param is a number
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    // Verify student param is an array
    if (!Array.isArray(students) || !students.every(s => typeof s === 'string')) {
      throw new TypeError('Students must be an array');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Every setter must verify type for new input
  // getting & setting for 'name' attr
  get name() {
    return this._name;
  }
  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName;
  }

  // getting & setting for 'length' attr
  get length() {
    return this._length;
  }
  set length(newLength) {
    if (typeof newLength !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = newLength;
  }

  // getting & setting for 'students' attr
  get students() {
    return this._students;
  }
  set students(newStudents) {
    if (!Array.isArray(newStudents) || !newStudents.every(s => typeof s === 'string')) {
      throw new TypeError('Students must be an array');
    }
    this._students = newStudents;
  }
}
