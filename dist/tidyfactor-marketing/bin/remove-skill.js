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

const targetDir = process.cwd();
const skillDestDir = path.join(targetDir, '.agents', 'skills', 'tidyfactor-marketing');

if (fs.existsSync(skillDestDir)) {
  fs.rmSync(skillDestDir, { recursive: true, force: true });
  console.log(chalk.bold(chalk.yellow(`\n🗑️ Removed TidyFactor Marketing Skill from .agents/skills/tidyfactor-marketing\n`)));
} else {
  console.log(chalk.dim(`\nNo TidyFactor Marketing Skill found at: ${skillDestDir}\n`));
}
