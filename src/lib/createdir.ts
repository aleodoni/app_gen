import fs from 'file-system'
import { generateFileByTemplate } from './createfile'

export function createDirectoryContents (templatePath: string, projectName: string, projectChoice: string, currDir: string) : void {
  const filesToCreate = fs.readdirSync(templatePath)

  filesToCreate.forEach(function (file) : void{
    const origFilePath = `${templatePath}/${file}`
    const stats = fs.statSync(origFilePath)

    if (stats.isFile()) {
      const contents = fs.readFileSync(origFilePath, 'utf8')

      if (file === '.npmignore') file = '.gitignore'

      const writePath = `${currDir}/${projectName}/${file}`

      const [fileName, fileExtension] = file.split('.')
      if (fileExtension === 'ejs') {
        generateFileByTemplate(projectName, `${currDir}/${projectName}/`, fileName, contents, projectChoice)
      } else {
        fs.writeFileSync(writePath, contents, 'utf8')
      }
    } else if (stats.isDirectory) {
      fs.mkdirSync(`${currDir}/${projectName}/${file}`)

      createDirectoryContents(
        `${templatePath}/${file}`,
        `${projectName}/${file}`,
        projectChoice,
        currDir
      )
    }
  })
}
