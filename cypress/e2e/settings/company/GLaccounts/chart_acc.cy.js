describe('Settings - GL Accounts - Chart of Accounts', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should create a new chart of account entry', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#profiles > a',
            '#gl_accounts > a'
        ]);

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('.form > :nth-child(1) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('testingcode123');

        cy.get(':nth-child(2) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('testingcode');
    });
});
