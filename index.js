#!/usr/bin/env node
import { fileTypes as fileTypeDfr } from './filetypes/drf'
const inquirer = require("inquirer");
const fs = require("fs");
const ejs = require("ejs");
const CURR_DIR = process.cwd();

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

  fs.mkdirSync(`${CURR_DIR}/${projectName}`);
  createDirectoryContents(templatePath, projectName, projectChoice);
});

function createDirectoryContents(templatePath, newProjectPath, projectChoice) {
  const filesToCreate = fs.readdirSync(templatePath);

  filesToCreate.forEach(file => {
    const origFilePath = `${templatePath}/${file}`;
    const stats = fs.statSync(origFilePath);

    if (stats.isFile()) {
      const contents = fs.readFileSync(origFilePath, "utf8");

      if (file === ".npmignore") file = ".gitignore";

      const writePath = `${CURR_DIR}/${newProjectPath}/${file}`;

      const [fileName, fileExtension] = file.split('.')
      if (fileExtension === 'ejs') {
        generateFileByTemplate(`${CURR_DIR}/${newProjectPath}/`,fileName, contents, projectChoice)
      }
      else {
        fs.writeFileSync(writePath, contents, "utf8");
      }
    } else if (stats.isDirectory) {
      fs.mkdirSync(`${CURR_DIR}/${newProjectPath}/${file}`);

      createDirectoryContents(
        `${templatePath}/${file}`,
        `${newProjectPath}/${file}`,
        projectChoice
      );
    }
  });
}

function generateFileByTemplate(path, file, contents, projectChoice) {
  let fileType
  let fileName
  const dataForTemplate = {
    'projectName': 'zaca'
  }

  if (projectChoice === 'drf') fileType = fileTypeDfr
  const newContent = ejs.render(contents, dataForTemplate)
  for (let [key, value] of Object.entries(fileType)) {
    if (key === file) {
      fileName = `${key}.${value}`
      break
    }
  }
  fs.writeFileSync(`${path}${fileName}`, newContent, "utf8")
  
}
