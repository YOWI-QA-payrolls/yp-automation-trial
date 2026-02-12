describe('Employee Department & Position', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to department page and click a row', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#information_list > a',
            '#employee_department > a',
        ]);

        cy.get('#advance-filter-btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('#advance-search').click();

        cy.waitForTableData();

        cy.get('tbody tr:first > :nth-child(3)').click();
        cy.get('body').then(($body) => {
            if ($body.find('[ng-click="create(department, \'edit\')"] > .fa').length > 0) {
                cy.get('[ng-click="create(department, \'edit\')"] > .fa').click();
            }
        });
    });
});
