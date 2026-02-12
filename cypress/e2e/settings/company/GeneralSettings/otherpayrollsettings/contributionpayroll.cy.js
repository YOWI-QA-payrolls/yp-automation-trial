describe('Settings - General Settings - Contribution Payroll', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure contribution payroll settings', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(10) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(3) > td', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('#exclude_contribution_employment_type', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('[ng-click="main.excluded_employment_type_contribution = main.employmenttypes2"] > .fa', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('exist');
    });
});
