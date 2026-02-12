describe('Special Reports - Quincenal Loans Register Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to Loans Register, select payroll period, and generate report', () => {
        cy.navigateMenu([
            '#dmpi_reports_list > [href="#"]',
            '#quincenal_list > a',
            '#loans_register > a'
        ]);

        cy.select2First('.form-group > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');

        cy.get(':nth-child(4) > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
