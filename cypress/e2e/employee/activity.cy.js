describe('Employee Activity', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to employee performance and search', () => {
        cy.navigateMenu([
            '#reports_list > a',
            '#employee_performance > a',
        ]);

        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 })
            .should('be.visible')
            .type('caleb');

        cy.get('#advance-filter-btn').click();
        cy.get('#advance-search', { timeout: 10000 }).click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('.hand_cursor > :nth-child(2)').click();
        cy.select2First(':nth-child(1) > td > :nth-child(1) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.get('.input-group-btn > .btn').click();
        cy.get('.btn-info').click();
    });
});
