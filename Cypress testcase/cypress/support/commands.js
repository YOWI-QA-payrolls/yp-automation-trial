// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

Cypress.Commands.add('SaveData', (selector, variableName) => {
  cy.get(selector)
    .invoke('text')
    .then((text) => {
      cy.wrap(text).as(variableName); // Store the text in a variable
    });
  });

Cypress.Commands.add('checkFileExists', (filePath) => {
  return cy.task('checkFileExists', filePath);
  });
  

Cypress.Commands.add('openDatePicker', { prevSubject: 'element' }, (subject) => {
  subject[0].dispatchEvent(new Event('mousedown', { bubbles: true }));
  subject[0].dispatchEvent(new Event('mouseup', { bubbles: true }));
});

Cypress.Commands.add('login2', (username, password) => {
  cy.visit("https://staging-yp.yahshuasupport.com/signin/");
  cy.get('#root > div.bg-loginscreen > div.middle-box.text-center.loginscreen.wow.fadeIn.animated > div > div.logo.mb-3 > img').should("be.visible");
  cy.get('input[placeholder="Email"]').type(username);
  cy.get('input[placeholder="Password"]').type(password);
  cy.contains("button", "Sign In").click();
  cy.contains("div", "Signing in...").should("be.visible");
  cy.wait(5000)
  cy.contains("button", "Close").click({ force: true });
    // cy.contains('button', 'Close').click()
  cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-heading > div > div > button',{timeout: 5000}).click({multiple: true})
});

Cypress.Commands.add('dmpilogin', (username, password) => {
  cy.visit("https://staging-dmpi2.yahshuasupport.com/signin/");
  cy.get('#email').type(username);
  cy.get('#password').type(password);
  cy.contains("button", "Log in").click();
  cy.get('#page-top > div:nth-child(2) > div > div > div > div.panel-footer > div > div > button').click()
  cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > div > button').click()
  cy.contains("button", "Close").click({ force: true });
  // cy.contains('button', 'Close').click()
  // cy.get('@btn',{timeout: 5000}).click({multiple: true})
  cy.wait(2000)
});