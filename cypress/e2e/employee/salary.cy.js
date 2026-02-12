describe('Employee Salary & Rate Status', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to salary page and set salary details', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#information_list > a',
            '#employee_salary > a',
        ]);

        cy.get('#advance-filter-btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('#advance-search').click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('tbody > :nth-child(2) > :nth-child(2)').click();
        cy.select2First(':nth-child(1) > td > .col-sm-4.form-group > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.get('#salary').type('25000');
        cy.get(':nth-child(1) > td > .col-sm-3 > .input-group > .input-group-btn > .btn').click();
        cy.get(':nth-child(3) > .btn > .glyphicon').click();
        cy.get('#page-top')
            .find('div.modal.fade.ng-scope.ng-isolate-scope.in')
            .find('div.panel-body')
            .find('div.row.table-responsive.custom-responsive-div')
            .find('table tbody tr:nth-child(1) td div.col-sm-3.form-group p div ul')
            .contains('29')
            .click();
    });
});
