describe('Settings - General Settings - Deduction Settings', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure deduction settings and select dropdown option', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(10) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(1) > td', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(6) > :nth-child(14) > .my-ui-select > .select2-choice > .select2-arrow > b', { timeout: 10000 })
            .should('be.visible')
            .click();
    });
});
