const { test } = require('node:test');
const assert = require('node:assert');

test('passing assertion', () => {
  assert.strictEqual(1 + 1, 2);
});
