
import ejs from 'ejs'
import fs from 'fs'
import { fileTypes as fileTypeDfr } from '../filetypes/drf'

export function generateFileByTemplate (projectName: string, path: string, file: string, contents: string, projectChoice: string) : void {
  let fileType: object
  let fileName: string

  const dataForTemplate = {
    'projectName': projectName
  }

  if (projectChoice === 'drf') fileType = fileTypeDfr
  const newContent = ejs.render(contents, dataForTemplate)

  Object.keys(fileType).forEach((key): void => {
    if (key === file) {
      if (key === 'travis') {
        fileName = `.${key}.${fileType[key]}`
      } else {
        fileName = `${key}.${fileType[key]}`
      }
    }
  })

  fs.writeFileSync(`${path}${fileName}`, newContent, 'utf8')
}
