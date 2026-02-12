describe('Employee Search - Calendar Search', () => {
    beforeEach(() => {
        cy.login();
    });

    it('should filter daily logs by date range', () => {
        cy.navigateMenu([
            '#timesheets_list > a',
            '#daily_logs > a'
        ]);

        cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 }).click();
        cy.get('.uib-datepicker-popup').contains('11').click();
        cy.get('.input-group > :nth-child(5) > .btn').click();
        cy.get('.uib-datepicker-popup').contains('12').click();
        cy.get('.hand_cursor').click();
    });
});
