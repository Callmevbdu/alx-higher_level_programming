#!/usr/bin/node
// a script that computes the number of tasks completed by user id.

const request = require('request');
const completedTasks = {};

request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  body.forEach((task) => {
    if (task.completed) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 1;
      } else {
        completedTasks[task.userId] += 1;
      }
    }
  });
  console.log(completedTasks);
});
