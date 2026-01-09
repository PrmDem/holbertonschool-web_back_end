import fs from 'node:fs';

function readDatabase(pathToFile) {
  return new Promise((resolve, reject) => {
    fs.readFile(pathToFile, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database from utils'));
        return;
      }

      const lines = data.trim().split('\n');
      const students = lines.slice(1);

      const lists = {};

      students.forEach((stdn) => {
        // eslint-disable-next-line no-unused-vars
        const [first, _last, _age, field] = stdn.split(',');
        if (!lists[field]) {
          lists[field] = []; // add as 'lists' object properties, value is a list
        }
        lists[field].push(first); // adds first name to the corresponding list
      });
      resolve(lists);
    });
  });
}

export default readDatabase;
