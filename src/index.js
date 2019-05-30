#!/usr/bin/env node
import fs from 'fs'

import SimpleStore from './store'
import { createDirectoryContents } from './lib/createdir'

let store = new SimpleStore()
const inquirer = require("inquirer");
const CURR_DIR = process.cwd();

store.push({'CURR_DIR': process.cwd()})

const CHOICES = fs.readdirSync(`${__dirname}/templates`);

const QUESTIONS = [
  {
    name: "project-choice",
    type: "list",
    message: "What project template would you like to generate ?",
    choices: CHOICES
  },
  {
    name: "project-name",
    type: "input",
    message: "Project name:",
    validate: function(input) {
      if (/^([A-Za-z\-\_\d])+$/.test(input)) return true;
      else
        return "Project name may only include letters, numbers, underscores and hashes.";
    }
  }
];

inquirer.prompt(QUESTIONS).then(answers => {
  const projectChoice = answers["project-choice"];
  const projectName = answers["project-name"];
  const templatePath = `${__dirname}/templates/${projectChoice}`;

  store.push({'projectChoice': projectChoice})
  store.push({'projectName': projectName})
  store.push({'templatePath': templatePath})

  fs.mkdirSync(`${CURR_DIR}/${projectName}`);
  createDirectoryContents(store, templatePath, projectName, projectChoice);
});

