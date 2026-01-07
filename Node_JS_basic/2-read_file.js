const fs = require('node:fs');

function countStudents(pathToFile) {
  try {
    const data = fs.readFileSync(pathToFile, 'utf8');
    const lines = data.trim().split('\n'); // Turn csv into Array obj, removing blank spaces
    const students = lines.slice(1); // students are now separate from fields

    console.log(`Number of students: ${students.length}\n`);

    const lists = {};

    students.forEach((stdn) => {
      // eslint-disable-next-line no-unused-vars
      const [first, _last, _age, field] = stdn.split(',');
      if (!lists[field]) {
        lists[field] = []; // add as 'lists' object properties, value is a list
      }
      lists[field].push(first); // adds first name to the corresponding list
    });

    for (const spec in lists) {
      if (Object.hasOwn(lists, spec)) { // for eslint 'guard for in'
        const specList = lists[spec]; // Getting field property's value for manipulation
        console.log(`Number of students in ${spec}: ${specList.length}. List: ${specList.join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
