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

function createDirectoryContents(templatePath, projectName, projectChoice) {
  const filesToCreate = fs.readdirSync(templatePath);

  filesToCreate.forEach(file => {
    const origFilePath = `${templatePath}/${file}`;
    const stats = fs.statSync(origFilePath);

    if (stats.isFile()) {
      const contents = fs.readFileSync(origFilePath, "utf8");

      if (file === ".npmignore") file = ".gitignore";

      const writePath = `${CURR_DIR}/${projectName}/${file}`;

      const [fileName, fileExtension] = file.split('.')
      if (fileExtension === 'ejs') {
        generateFileByTemplate(projectName, `${CURR_DIR}/${projectName}/`,fileName, contents, projectChoice)
      }
      else {
        fs.writeFileSync(writePath, contents, "utf8");
      }
    } else if (stats.isDirectory) {
      fs.mkdirSync(`${CURR_DIR}/${projectName}/${file}`);

      createDirectoryContents(
        `${templatePath}/${file}`,
        `${projectName}/${file}`,
        projectChoice
      );
    }
  });
}

function generateFileByTemplate(projectName, path, file, contents, projectChoice) {
  let fileType
  let fileName
  const dataForTemplate = {
    'projectName': projectName
  }

  if (projectChoice === 'drf') fileType = fileTypeDfr
  const newContent = ejs.render(contents, dataForTemplate)

  Object.keys(fileType).forEach(key => {
    if (key == file) {
      fileName = `${key}.${fileType[key]}`
    }
  })

  fs.writeFileSync(`${path}${fileName}`, newContent, "utf8")
  
}
