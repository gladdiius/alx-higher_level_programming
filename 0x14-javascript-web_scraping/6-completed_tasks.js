#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const todos = JSON.parse(body);

      // Initialize an object to store completed tasks count per user
      const completedTasksCount = {};

      // Filter completed tasks and count them for each user
      todos.forEach(todo => {
        if (todo.completed) {
          if (completedTasksCount[todo.userId] === undefined) {
            completedTasksCount[todo.userId] = 1;
          } else {
            completedTasksCount[todo.userId]++;
          }
        }
      });

      // Print the result
      console.log(completedTasksCount);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
