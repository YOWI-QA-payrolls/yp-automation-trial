describe('Employee Location', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to location and select from dropdown', () => {
        cy.intercept('POST', '**/employees/locations/read_pagination/**').as('loadLocationData');
        cy.navigateMenu([
            '#employee_list > a',
            '#information_list > a',
            '#employeelocation > a',
        ]);

        cy.get('#advance-filter-btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('#advance-search').click();

        cy.wait('@loadLocationData').its('response.statusCode').should('eq', 200);

        cy.get('tbody > :nth-child(1) > :nth-child(2)').first().click();
        cy.waitForLoading();
        cy.select2First(':nth-child(1) > td > .col-sm-5.pull-left > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.get(':nth-child(1) > td > :nth-child(2) > .input-group > .input-group-btn > .btn').click();
        cy.get('.btn-info').click();
    });
});
