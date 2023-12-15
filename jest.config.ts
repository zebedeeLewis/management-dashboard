/* eslint-disable */
export default {
  displayName: 'app_frontend',
  preset: './jest.preset.js',
  transform: {
    '^(?!.*\\.(js|jsx|ts|tsx|css|json)$)': '@nx/react/plugins/jest',
    '^.+\\.[tj]sx?$': ['babel-jest', { presets: ['@nx/react/babel'] }],
  },
  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx'],
  coverageDirectory: './coverage/app_frontend',
  testMatch: [
    '<rootDir>/src/app/webui/**/__tests__/**/*.[jt]s?(x)',
    '<rootDir>/src/app/webui/**/*(*.)@(spec|test).[jt]s?(x)',
  ],
};
