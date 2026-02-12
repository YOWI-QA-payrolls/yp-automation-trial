describe('Employee Leave Monitoring', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to leave monitoring and interact with records', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#employee_leave_monitoring > a',
        ]);

        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 })
            .should('be.visible')
            .type('caleb');

        cy.get('#advance-filter-btn').click();
        cy.get('#advance-search', { timeout: 10000 }).click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('tr.ng-scope > :nth-child(3)').click();
        cy.get('.panel > .panel-footer > .pull-right > .btn').click();
    });
});
