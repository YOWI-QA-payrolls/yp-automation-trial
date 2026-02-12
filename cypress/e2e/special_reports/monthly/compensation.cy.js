describe('Special Reports - Monthly Compensation Items Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to Compensation Items, toggle checkbox, select payroll period, and generate report', () => {
        cy.navigateMenu([
            '#dmpi_reports_list > [href="#"]',
            '#monthlies_list > a',
            '#compensation_items > a'
        ]);

        cy.get('label > .ng-pristine', { timeout: 10000 })
            .should('exist')
            .click();

        cy.select2First('.select2-choices');

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(3) > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
