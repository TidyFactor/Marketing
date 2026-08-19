#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/* Lightweight Zero-Dependency ANSI formatting */
const chalk = {
  cyan: (str) => `\x1b[36m${str}\x1b[0m`,
  green: (str) => `\x1b[32m${str}\x1b[0m`,
  yellow: (str) => `\x1b[33m${str}\x1b[0m`,
  red: (str) => `\x1b[31m${str}\x1b[0m`,
  bold: (str) => `\x1b[1m${str}\x1b[0m`,
  dim: (str) => `\x1b[2m${str}\x1b[0m`,
};

const PACKAGE_ROOT = path.resolve(__dirname, '..');
const targetDir = process.cwd();
const skillDestDir = path.join(targetDir, '.agents', 'skills', 'tidyfactor-marketing');

console.log(chalk.cyan(`\nInjecting TidyFactor Marketing Skill into: ${targetDir}...`));

fs.mkdirSync(skillDestDir, { recursive: true });

const copyDir = (src, dest) => {
  fs.mkdirSync(dest, { recursive: true });
  for (const item of fs.readdirSync(src)) {
    const srcItem = path.join(src, item);
    const destItem = path.join(dest, item);
    if (fs.statSync(srcItem).isDirectory()) {
      copyDir(srcItem, destItem);
    } else {
      fs.copyFileSync(srcItem, destItem);
    }
  }
};

// Copy references and root files
const filesToCopy = ['SKILL.md', 'package.json', 'README.md', 'README.ar.md', 'LICENSE', 'brand.json', '.tidyfactor'];
for (const f of filesToCopy) {
  const srcFile = path.join(PACKAGE_ROOT, f);
  if (fs.existsSync(srcFile)) {
    fs.copyFileSync(srcFile, path.join(skillDestDir, f));
  }
}

if (fs.existsSync(path.join(PACKAGE_ROOT, 'references'))) {
  copyDir(path.join(PACKAGE_ROOT, 'references'), path.join(skillDestDir, 'references'));
}

console.log(chalk.bold(chalk.green(`✅ TidyFactor Marketing Skill injected successfully into .agents/skills/tidyfactor-marketing!\n`)));
