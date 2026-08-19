#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const readline = require('readline');

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
const pkg = require(path.join(PACKAGE_ROOT, 'package.json'));

console.log(chalk.bold(chalk.cyan(`\n======================================================`)));
console.log(chalk.bold(chalk.cyan(`  TidyFactor Marketing Engine — CLI Setup (v${pkg.version})`)));
console.log(chalk.bold(chalk.cyan(`======================================================\n`)));

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const ask = (query, defaultVal) =>
  new Promise((resolve) => {
    rl.question(chalk.yellow(`${query} `) + (defaultVal ? chalk.dim(`[${defaultVal}]: `) : ''), (answer) => {
      resolve(answer.trim() || defaultVal);
    });
  });

async function main() {
  const targetDirInput = await ask('1. Target Directory to initialize marketing engine:', './');
  const targetDir = path.resolve(process.cwd(), targetDirInput);

  console.log(chalk.cyan('\nSelect Primary Target Market:'));
  console.log('  1) Global / Western (English Direct Response)');
  console.log('  2) MENA / GCC (Arabic Modern Standard + Regional Payments)');
  console.log('  3) Dual Bilingual (English + Arabic Parity)');
  const marketChoice = await ask('Select market (1-3):', '3');

  console.log(chalk.cyan('\nSelect Primary Growth Focus:'));
  console.log('  1) B2B SaaS & Enterprise (LinkedIn, Cold InMail, Demo Funnels)');
  console.log('  2) E-Commerce & DTC (Meta/TikTok Ads, Abandoned Cart, UGC)');
  console.log('  3) High-Ticket Services / Info-Products (Webinars, VSLs, Email Drips)');
  console.log('  4) Full 360° Growth Suite (All 7 Pillars)');
  const focusChoice = await ask('Select focus (1-4):', '4');

  console.log(chalk.green(`\nInitializing TidyFactor Marketing Engine in: ${targetDir}...`));

  // Copy references and SKILL.md to target directory .agents/skills/tidyfactor-marketing
  const skillDestDir = path.join(targetDir, '.agents', 'skills', 'tidyfactor-marketing');
  fs.mkdirSync(skillDestDir, { recursive: true });

  const filesToCopy = ['SKILL.md', 'package.json', 'README.md', 'README.ar.md', 'LICENSE', 'brand.json', '.tidyfactor'];
  for (const f of filesToCopy) {
    const srcFile = path.join(PACKAGE_ROOT, f);
    if (fs.existsSync(srcFile)) {
      fs.copyFileSync(srcFile, path.join(skillDestDir, f));
    }
  }

  // Copy references recursively
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

  copyDir(path.join(PACKAGE_ROOT, 'references'), path.join(skillDestDir, 'references'));

  console.log(chalk.bold(chalk.green('\n✅ TidyFactor Marketing Engine installed successfully!')));
  console.log(chalk.dim(`Installed at: ${skillDestDir}`));
  console.log(chalk.cyan('\n🚀 Available Slash Commands:'));
  console.log('  - /marketing strategy      -> Brand Positioning & Launch Plans');
  console.log('  - /marketing content       -> Multi-Platform Content & SEO Topic Clusters');
  console.log('  - /marketing social        -> LinkedIn B2B & Instagram/TikTok Hooks');
  console.log('  - /marketing email         -> Welcome Drips & Cart Recovery Flows');
  console.log('  - /marketing ads           -> 3-Angle Ad Copy Matrices & CRO Audits');
  console.log('  - /marketing promo         -> 72-Hour Flash Sales & Decoy Pricing');
  console.log('  - /marketing growth        -> Retention, Churn Reduction & Referral Loops\n');

  rl.close();
}

main().catch((err) => {
  console.error(chalk.red(`\n❌ Error: ${err.message}`));
  rl.close();
  process.exit(1);
});
