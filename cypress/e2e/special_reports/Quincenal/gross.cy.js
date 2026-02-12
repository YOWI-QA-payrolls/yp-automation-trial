describe('Special Reports - Quincenal Gross Earnings Register Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to Gross Earnings Register, select payroll period, and generate report', () => {
        cy.navigateMenu([
            '#dmpi_reports_list > [href="#"]',
            '#quincenal_list > a',
            '#gross_earnings_registers > a'
        ]);

        cy.select2First('.select2-search-field > .select2-input');

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(3) > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
