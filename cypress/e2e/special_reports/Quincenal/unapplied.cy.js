describe('Special Reports - Quincenal Unapplied Deductions Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to Unapplied Deductions, select payroll period, and generate report', () => {
        cy.navigateMenu([
            '#dmpi_reports_list > [href="#"]',
            '#quincenal_list > a',
            '#unapplied_deductions > a'
        ]);

        cy.select2First('.select2-input');

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('.btn.btn-success', { timeout: 15000 })
            .first()
            .should('not.be.disabled')
            .click({ force: true });
    });
});
