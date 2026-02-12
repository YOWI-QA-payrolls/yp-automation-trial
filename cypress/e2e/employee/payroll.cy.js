describe('Employee Payroll Schedule', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to payroll schedule and interact with records', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#employee_payroll_schedule > a',
        ]);

        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 })
            .should('be.visible')
            .type('caleb');

        cy.get('#advance-filter-btn').click();
        cy.get('#advance-search', { timeout: 10000 }).click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('tr.ng-scope > :nth-child(3)').click();
        cy.select2First(':nth-child(1) > td > .col-sm-5.pull-left > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.get(':nth-child(1) > td > :nth-child(2) > .input-group > .input-group-btn > .btn').click();
        cy.get('.btn-info').click();
    });
});
