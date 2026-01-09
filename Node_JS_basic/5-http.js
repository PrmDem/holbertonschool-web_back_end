const http = require('node:http');
const fs = require('node:fs');

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n'); // Need to add \n manually with res.write

    fs.readFile(process.argv[2], 'utf8', (err, data) => {
      if (err) {
        res.statusCode = 500;
        res.end('Cannot load the database');
        return; // stops & exits function if no database is found or data cannot be read
      }

      const lines = data.trim().split('\n');
      const students = lines.slice(1);

      res.write(`Number of students: ${students.length}\n`);

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
          const specList = lists[spec];
          res.write(`Number of students in ${spec}: ${specList.length}. List: ${specList.join(', ')}\n`);
        }
      }

      res.end();
    });
  }
});

app.listen(1245);

module.exports = app;
