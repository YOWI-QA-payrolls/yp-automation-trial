describe('Employee Loan to Date', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to loans and add a loan entry', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#employee_loan_to_date > a',
        ]);

        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 })
            .should('be.visible')
            .type('juan');

        cy.get('#advance-filter-btn').click();
        cy.get('[ng-if="!main.no_search_button"]', { timeout: 10000 }).click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.dismissToast();

        cy.get('.btn-group > .btn', { timeout: 10000 }).should('not.be.disabled').click();
        cy.get('.input-group-btn > .btn').click();
        cy.get('.btn-info').click();
        cy.select2First('.col-sm-3.pull-left > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.select2First(':nth-child(2) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.get('#addtl_amount_select').type('500');
        cy.get('#addtl_principal_amount_select').type('1000');
    });
});
