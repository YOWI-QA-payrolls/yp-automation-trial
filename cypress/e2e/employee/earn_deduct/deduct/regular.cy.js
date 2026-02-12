describe('Employee Deductions - Regular', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to regular deductions and add a deduction', () => {
        cy.get('#employee_list > a').click();
        cy.get('#employee_income_deduction > a', { timeout: 15000 }).should('exist').click({ force: true });
        cy.get('#employee_deductions > a', { timeout: 15000 }).click({ force: true });
        cy.get('#employee_regular_deductions_details > a', { timeout: 15000 }).click({ force: true });

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('tbody tr:first .align_left .ng-binding').click();
        cy.get('.col-sm-1 > .btn').click();

        cy.select2First(':nth-child(1) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.get('#input_list_amount', { timeout: 10000 }).type('5000');
        cy.get(':nth-child(3) > .input-group > .input-group-btn > .btn').click();
        cy.get('.btn-info').click();
        cy.get('#input_list_amount_to_').type('testing');
    });
});
