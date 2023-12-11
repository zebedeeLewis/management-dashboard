/* eslint-disable */
export default {
  displayName: 'frontend',
  preset: './jest.preset.js',
  transform: {
    '^(?!.*\\.(js|jsx|ts|tsx|css|json)$)': '@nx/react/plugins/jest',
    '^.+\\.[tj]sx?$': ['babel-jest', { presets: ['@nx/react/babel'] }],
  },
  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx'],
  coverageDirectory: './coverage/frontend',
  testMatch: [
    '<rootDir>/frontend/**/__tests__/**/*.[jt]s?(x)',
    '<rootDir>/frontend/**/*(*.)@(spec|test).[jt]s?(x)',
  ],
};
