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

        cy.wait(1000);
        cy.get('.select2-choices input.select2-input', { timeout: 10000 })
            .first()
            .click({ force: true });
        cy.get('.ui-select-choices-row-inner', { timeout: 15000 })
            .should('be.visible')
            .first()
            .click({ force: true });

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('.btn.btn-success', { timeout: 10000 })
            .first()
            .should('not.be.disabled')
            .click({ force: true });
    });
});
