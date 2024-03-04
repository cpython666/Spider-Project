const code = `
var x = 'hello Python斗罗'
console.log('x', x)
`

const options = {
   compact: false,
    debugProtection: true,
}

const obfuscator = require('javascript-obfuscator')
function obfuscate(code, options) {
   return obfuscator.obfuscate(code, options).getObfuscatedCode()
}
var ob_str=obfuscate(code, options)
console.log(ob_str)

const path = require('path');
// 获取当前文件的完整路径
const fullPath = __filename;
// 使用path模块获取文件名
const fileName = path.basename(fullPath);
console.log('当前文件名:', fileName);
const fs = require('fs');
// 新文件名
const newFileName = fileName.replace(/(\.js)$/, '_ob$1');
// 将内容写入文件
fs.writeFile(newFileName, ob_str, (err) => {
  if (err) {
    console.error('写入文件时出错：', err);
    return;
  }
  console.log('内容已成功写入到文件:', newFileName);
});