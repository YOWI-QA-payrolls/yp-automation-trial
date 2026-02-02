module.exports = {
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
  reporter: 'mocha-junit-reporter',
  reporterOptions: {
    mochaFile: 'results/results-[hash].xml',
    toConsole: true,
  },
};
