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

        cy.waitForSettingsTable();
        cy.clickSettingsRow('Employee Cost');

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
