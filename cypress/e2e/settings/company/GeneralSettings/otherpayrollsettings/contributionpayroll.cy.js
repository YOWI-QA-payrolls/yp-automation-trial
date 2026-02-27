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

        cy.waitForSettingsTable();
        cy.clickSettingsRow('Other Payroll Settings');
        cy.clickSettingsRow('Contribution');

        cy.get('#exclude_contribution_employment_type', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('exist');
    });
});
