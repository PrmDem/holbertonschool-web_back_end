import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const pathToDB = process.argv[2];

    readDatabase(pathToDB)
      .then((data) => {
        let output = 'This is the list of our students\n'; // To have the full response body in one variable

        const sortedFields = Object.keys(data).sort((a, b) => {
          const stdn1 = a.toLowerCase();
          const stdn2 = b.toLowerCase();
          if (stdn1 < stdn2) {
            return -1;
          }
          if (stdn1 > stdn2) {
            return 1;
          }

          return 0;
        }); // ensures proper sorting throughout various tests

        sortedFields.forEach((spec, index) => {
          const studentsList = data[spec].join(', '); // Getting field property's value for manipulation
          output += `Number of students in ${spec}: ${data[spec].length}. List: ${studentsList}`;

          if (index < sortedFields.length - 1) {
            output += '\n';
          } // avoids unnecessary new line at the end
        });

        res.status(200).send(output);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    const pathToDB = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return; // Stop & exit method on wrong value
    }

    readDatabase(pathToDB)
      .then((data) => {
        const byMajor = data[major];
        res.status(200).send(`List: ${byMajor.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
