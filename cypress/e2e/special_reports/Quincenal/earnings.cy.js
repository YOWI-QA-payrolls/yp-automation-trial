describe('Special Reports - Quincenal Earnings and Deductions Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to Earnings and Deductions, select payroll period, and generate report', () => {
        cy.navigateMenu([
            '#dmpi_reports_list > [href="#"]',
            '#quincenal_list > a',
            '#earnings_and_deductions > a'
        ]);

        cy.select2First('.select2-search-field > .select2-input');

        cy.get('.btn.btn-success', { timeout: 15000 })
            .first()
            .should('not.be.disabled')
            .click({ force: true });
    });
});
