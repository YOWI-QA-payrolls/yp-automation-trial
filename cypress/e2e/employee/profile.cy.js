describe('Employee Profile', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to employee info and create a new profile', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#information_list > a',
            '#employeeinfo > a',
        ]);

        cy.get('#advance-filter-btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('#advance-search').click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('[ng-click="create_dialog()"]').click();
        cy.get('[index="0"] > .modal-dialog > .modal-content > .panel > .panel-body > .ibox-content > .row > #form > :nth-child(2) > .col-sm-12.ng-scope > fieldset > :nth-child(2) > :nth-child(6) > #lastname').type('Lana');
        cy.get('#firstname').type('Del Rey');
        cy.get(':nth-child(2) > :nth-child(4) > .form-control').type('1');
        cy.get(':nth-child(1) > .input-group > .input-group-btn > .btn').click();
    });
});
