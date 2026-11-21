import { execSync } from 'child_process';

export function getCommitEpoch(): number {
  const epoch = execSync('git log -1 --pretty=%ct', { encoding: 'utf8' }).trim();
  return parseInt(epoch, 10);
}

