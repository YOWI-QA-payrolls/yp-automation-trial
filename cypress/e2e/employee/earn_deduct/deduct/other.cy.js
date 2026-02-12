describe('Employee Deductions - Other', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to other deductions and add a deduction', () => {
        cy.get('#employee_list > a').click();
        cy.get('#employee_income_deduction > a', { timeout: 15000 }).should('exist').click({ force: true });
        cy.get('#employee_deductions > a', { timeout: 15000 }).click({ force: true });
        cy.get('#employee_other_deductions_details > a', { timeout: 15000 }).click({ force: true });

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('tbody tr:first .align_left .ng-binding').click();
        cy.get('.col-sm-1 > .btn').click();

        cy.select2First('.align_left > .col-sm-3 > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.get('#otherdeduction_amount_select', { timeout: 10000 }).type('5000');
        cy.get(':nth-child(4) > .form-control').type('testing');
        cy.get(':nth-child(5) > .form-control').type('123test');
    });
});
