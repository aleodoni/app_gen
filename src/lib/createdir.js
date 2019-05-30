import fs from 'fs'
import { generateFileByTemplate } from './createfile'
import SimpleStore from '../store'

export function createDirectoryContents(store, templatePath, projectName, projectChoice) {
    
  const filesToCreate = fs.readdirSync(templatePath);

  filesToCreate.forEach(file => {
    const origFilePath = `${templatePath}/${file}`;
    const stats = fs.statSync(origFilePath);

    if (stats.isFile()) {
      const contents = fs.readFileSync(origFilePath, "utf8");

      if (file === ".npmignore") file = ".gitignore";

      const writePath = `${store.getContent().CURR_DIR}/${projectName}/${file}`;

      const [fileName, fileExtension] = file.split('.')
      if (fileExtension === 'ejs') {
        generateFileByTemplate(projectName, `${store.getContent().CURR_DIR}/${projectName}/`,fileName, contents, projectChoice)
      }
      else {
        fs.writeFileSync(writePath, contents, "utf8");
      }
    } else if (stats.isDirectory) {
      fs.mkdirSync(`${store.getContent().CURR_DIR}/${projectName}/${file}`);

      createDirectoryContents(
        store,
        `${templatePath}/${file}`,
        `${projectName}/${file}`,
        projectChoice
      );
    }
  });
}