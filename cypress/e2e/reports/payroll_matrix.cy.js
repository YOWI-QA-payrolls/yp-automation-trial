describe('Reports - Payroll Summary Matrix', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should select payroll and search matrix', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#payroll_summary_matrix > a']);
        cy.wait(1000);
        cy.get('.select2-choices input.select2-input', { timeout: 10000 })
            .first()
            .click({ force: true });
        cy.get('.ui-select-choices-row-inner', { timeout: 15000 })
            .should('be.visible')
            .first()
            .click({ force: true });

        cy.get('[ng-click="main.open_date(\'bugo_funding_date\')"]', { timeout: 10000 })
            .should('be.visible')
            .click();
        cy.get('.uib-datepicker-popup', { timeout: 10000 })
            .should('be.visible')
            .contains('button', '1')
            .click();

        cy.get('[ng-click="main.open_date(\'bugo_deposit_date\')"]', { timeout: 10000 })
            .should('be.visible')
            .click();
        cy.get('.uib-datepicker-popup', { timeout: 10000 })
            .should('be.visible')
            .contains('button', '1')
            .click();
    });
});
