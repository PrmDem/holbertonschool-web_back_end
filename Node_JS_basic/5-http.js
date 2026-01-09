const http = require('http');
const countStudents = require('./3-read_file_async'); // Using past file as a module

const app = http.createServer(async (req, res) => {
  if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n'); // Need to add \n manually with res.write

    try {
      const data = await countStudents(process.argv[2]); // path to file given in command line
      res.end(data);
    } catch (err) {
      res.end(err.message);
    }
  } else { // So all other routes display message, not just '/'
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);

module.exports = app;