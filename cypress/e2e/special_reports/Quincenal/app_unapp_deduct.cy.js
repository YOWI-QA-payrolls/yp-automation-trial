describe('Special Reports - Quincenal Applied/Unapplied Deductions Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to Applied/Unapplied Deductions, select payroll period, and generate report', () => {
        cy.navigateMenu([
            '#dmpi_reports_list > [href="#"]',
            '#quincenal_list > a',
            '#applied_unapplied_deductions > a'
        ]);

        cy.select2First('.select2-input');

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(3) > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
