describe('Employee Search - Daily Log Search', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should search for an employee in daily logs', () => {
        cy.navigateMenu([
            '#timesheets_list > a',
            '#daily_logs > a'
        ]);

        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).type('juan');
        cy.get('[ng-if="!main.no_search_button"]').click();
    });
});
