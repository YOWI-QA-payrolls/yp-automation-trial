describe('Employee Bank Accounts', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to bank accounts and add account details', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#employeebankaccounts > a',
        ]);

        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 })
            .should('be.visible')
            .type('caleb');

        cy.get('#advance-filter-btn').click();
        cy.get('#advance-search', { timeout: 10000 }).click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('tr.ng-scope > :nth-child(3)').click();
        cy.get('#account_number').type('12345678');
        cy.get('#transaction_reference').type('123testing');
        cy.get('.input-group-btn > .btn').click();
        cy.get('.btn-info').click();
        cy.select2First('.select2-chosen.ng-binding');
    });
});
