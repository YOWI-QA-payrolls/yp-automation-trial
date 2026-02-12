describe('Settings - General Settings - Employee Cost', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to employee cost settings and save', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(6) > td > :nth-child(1) > a', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
