describe('Employee Location', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to location and select from dropdown', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#information_list > a',
            '#employeelocation > a',
        ]);

        cy.get('#advance-filter-btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('#advance-search').click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('tbody tr:first .align_left').click();
        cy.select2First(':nth-child(1) > td > .col-sm-5.pull-left > .ui-select-container > .select2-choice > .select2-arrow > b');
        cy.get(':nth-child(1) > td > :nth-child(2) > .input-group > .input-group-btn > .btn').click();
        cy.get('.btn-info').click();
    });
});
