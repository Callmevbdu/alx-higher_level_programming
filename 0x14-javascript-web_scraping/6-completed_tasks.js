#!/usr/bin/node
// a script that computes the number of tasks completed by user id.

const request = require('request');
const completedTasks = {};

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasks = JSON.parse(body);

  tasks.forEach((task) => {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  });
