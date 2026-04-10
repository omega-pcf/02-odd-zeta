import { execSync } from 'child_process';

export function getCommitEpoch(): number {
  try {
    const epoch = execSync('git log -1 --pretty=%ct', { encoding: 'utf8' }).trim();
    if (!epoch) return Math.floor(Date.now() / 1000);
    return parseInt(epoch, 10);
  } catch (error) {
    return Math.floor(Date.now() / 1000);
  }
}

