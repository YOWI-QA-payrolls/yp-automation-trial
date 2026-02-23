describe('Special Reports - Monthly CEAP Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to CEAP report, select payroll period, and generate report', () => {
        cy.navigateMenu([
            '#dmpi_reports_list > [href="#"]',
            '#monthlies_list > a',
            '#ceap > a'
        ]);

        cy.get('#select_payroll_period', { timeout: 15000 })
            .should('exist')
            .click({ force: true });

        cy.select2First(
            '.col-sm-4.ng-scope > .form-group > .ui-select-container > .select2-choices > .select2-search-field > .select2-input'
        );

        cy.get('.btn.btn-success', { timeout: 15000 })
            .first()
            .should('not.be.disabled')
            .click({ force: true });
    });
});
