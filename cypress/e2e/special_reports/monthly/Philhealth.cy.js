describe('Special Reports - Monthly PhilHealth Remittances Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to PhilHealth Monthly Remittances, select payroll period, and generate report', () => {
        cy.navigateMenu([
            '#dmpi_reports_list > [href="#"]',
            '#monthlies_list > a',
            '#phic_monthly_remittances > a'
        ]);

        cy.get('#select_payroll_period', { timeout: 15000 })
            .should('exist')
            .click({ force: true });

        cy.select2First(
            '.col-sm-4.ng-scope > .form-group > .ui-select-container > .select2-choices > .select2-search-field > .select2-input'
        );

        cy.get('.col-sm-1 > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
