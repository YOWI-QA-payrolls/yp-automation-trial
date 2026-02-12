import 'cypress-file-upload';

// Reusable login command - logs in and verifies dashboard loaded
Cypress.Commands.add('login', () => {
    cy.fixture('credentials').then(({ url, email, pass }) => {
        cy.visit(url);
        cy.get('#email').type(email);
        cy.get('#password').type(pass);
        cy.get('#signin-button').click();
        cy.get('#side-menu', { timeout: 20000 }).should('be.visible');
    });
});

// Navigate to a sidebar menu item by clicking its parent chain
// Waits for each submenu level to expand before proceeding
Cypress.Commands.add('navigateMenu', (menuPath) => {
    menuPath.forEach((selector) => {
        cy.get(selector, { timeout: 15000 }).should('exist').click({ force: true });
    });
});

// Wait for a table to finish loading and have data rows
Cypress.Commands.add('waitForTableData', (tableSelector = 'tbody', timeout = 20000) => {
    cy.get(tableSelector, { timeout }).should('exist');
    cy.get(`${tableSelector} tr`, { timeout }).should('have.length.greaterThan', 0);
});

// Wait for loading spinner/state to disappear
Cypress.Commands.add('waitForLoading', () => {
    cy.get('.sk-loading', { timeout: 20000 }).should('not.exist');
    cy.get('table.table_loading').should('not.exist');
});

// Select the first option from a select2 dropdown (handles ui-select hidden containers)
Cypress.Commands.add('select2First', (triggerSelector) => {
    cy.get(triggerSelector, { timeout: 10000 }).should('exist').click({ force: true });
    cy.get('.select2-results', { timeout: 10000 }).should('exist');
    cy.get('.select2-results .select2-result-label', { timeout: 10000 })
        .first()
        .click({ force: true });
});

// Dismiss any toast notifications if present
Cypress.Commands.add('dismissToast', () => {
    cy.get('body').then(($body) => {
        if ($body.find('.toast').length > 0) {
            cy.get('.toast').click({ multiple: true, force: true });
        }
    });
});
