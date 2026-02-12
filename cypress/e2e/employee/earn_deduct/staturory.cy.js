describe('Employee Statutory Contributions', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to statutory and add a contribution', () => {
        cy.get('#employee_list > a').click();
        cy.get('#employee_income_deduction > a', { timeout: 15000 }).should('exist').click({ force: true });
        cy.get('#employee_statutory > a', { timeout: 15000 }).click({ force: true });

        cy.select2First('.select2-search-field > .select2-input');
        cy.get('.form-group > .btn').click();
        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).type('caleb');

        cy.get('#advance-filter-btn').click();
        cy.get('#advance-search', { timeout: 10000 }).click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('.align_left > .ng-binding').click();
        cy.get('.col-sm-1 > .btn').click();
        cy.select2First('.align_left > .col-sm-3 > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.get('#contribution_amount_select').type('1000');
        cy.get('.col-sm-4 > .form-control').type('testing');
        cy.get('.panel > .panel-footer > .pull-right > .btn').click();
    });
});
