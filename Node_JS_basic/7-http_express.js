const express = require('express');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .filter((line) => line.trim() !== '');

      const students = lines.slice(1);
      const fields = {};
      const result = [];

      result.push(`Number of students: ${students.length}`);

      students.forEach((student) => {
        const [firstname, , , field] = student.split(',');

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      });

      Object.keys(fields).forEach((field) => {
        result.push(
          `Number of students in ${field}: ${fields[field].length}. List: ${
            fields[field].join(', ')
          }`,
        );
      });

      resolve(result.join('\n'));
    });
  });
}

const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const database = process.argv[2];

  countStudents(database)
    .then((data) => {
      res.type('text/plain');
      res.send(`This is the list of our students\n${data}`);
    })
    .catch((err) => {
      res.type('text/plain');
      res.send(`This is the list of our students\n${err.message}`);
    });
});

app.listen(1245);

module.exports = app;
