describe('Settings - General Settings - Other Payroll Settings', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure other payroll premium rate settings', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.waitForSettingsTable();
        cy.clickSettingsRow('Other Payroll Settings');
        cy.clickSettingsRow('Other Payroll Settings');

        cy.get('#no_holiday_pay', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.col-sm-4 > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('5');

        cy.select2First('.col-sm-8 > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');

        cy.get(':nth-child(5) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(2) > .select2-result-label > .ng-binding', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(6) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(7) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

    });
});
