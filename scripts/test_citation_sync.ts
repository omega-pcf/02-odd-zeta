import { syncCitationMetadata } from './tasks/citation.js';

async function test() {
    const testVersion = '1.6.0-test';
    console.log(`Testing syncCitationMetadata for version ${testVersion}...`);
    try {
        syncCitationMetadata(testVersion);
        console.log('Test completed successfully!');
    } catch (error) {
        console.error('Test failed:', error);
        process.exit(1);
    }
}

test();
