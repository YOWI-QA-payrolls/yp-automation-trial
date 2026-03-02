describe('Special Reports - Quincenal Carried Forward Deductions Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to Carried Forward Deductions, select payroll period, and generate report', () => {
        cy.navigateMenu([
            '#dmpi_reports_list > [href="#"]',
            '#quincenal_list > a',
            '#carried_forward_deductions > a'
        ]);

        cy.select2First('.select2-search-field > .select2-input');

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('.btn.btn-success', { timeout: 15000 })
            .first()
            .should('not.be.disabled')
            .click({ force: true });
    });
});
