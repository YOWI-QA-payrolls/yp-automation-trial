describe('Settings - General Settings - Auto Salary Increment', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should toggle auto salary increment setting', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.waitForSettingsTable();
        cy.clickSettingsRow('Other Payroll Settings');
        cy.clickSettingsRow('Salary');

        cy.get('#is_auto_salary_increment', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('exist');
    });
});
