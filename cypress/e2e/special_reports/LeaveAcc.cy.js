describe('Special Reports - Leave Accruals Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to Leave Accruals report, select leave type, and generate it', () => {
        cy.navigateMenu([
            '#dmpi_reports_list > [href="#"]',
            '#leave_accruals > a'
        ]);

        cy.get('[ng-click="filter.leave_type = leave_types"] > .fa', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
