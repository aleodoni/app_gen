#!/usr/bin/env node

import fs from 'file-system'

import { createDirectoryContents } from './lib/createdir'
import { Answers, Question, prompt } from 'inquirer'

const CURR_DIR = process.cwd()

const CHOICES = fs.readdirSync(`${__dirname}/templates`)

const QUESTIONS: Question[] = [
  {
    name: 'project-choice',
    type: 'list',
    message: 'What project template would you like to generate ?',
    choices: CHOICES
  },
  {
    name: 'project-name',
    type: 'input',
    message: 'Project name:',
    validate: function (input: string) : string|boolean {
      if (/^([A-Za-z\-\d])+$/.test(input)) return true
      else {
        return 'Project name may only include letters, numbers, underscores and hashes.'
      }
    }
  }
]

const _prompt = prompt(QUESTIONS)

_prompt.then((answers: Answers) : void => {
  const projectChoice = answers['project-choice']
  const projectName = answers['project-name']
  const templatePath = `${__dirname}/templates/${projectChoice}`

  fs.mkdirSync(`${CURR_DIR}/${projectName}`)
  createDirectoryContents(templatePath, projectName, projectChoice, CURR_DIR)
})
