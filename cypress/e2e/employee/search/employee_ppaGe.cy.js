describe('Employee Search - Per Page Filter', () => {
    beforeEach(() => {
        cy.login();
    });

    it('should filter daily logs by date range and employee page', () => {
        cy.navigateMenu([
            '#timesheets_list > a',
            '#daily_logs > a'
        ]);

        cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 }).click();
        cy.get('.uib-datepicker-popup').contains('13').click();
        cy.get('.input-group > :nth-child(5) > .btn').click();
        cy.get('.uib-datepicker-popup').contains('19').click();
        cy.get('.select2-choice').click();
        cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
        cy.get('.select2-choice').click();
        cy.get(':nth-child(1) > .select2-result-label > .ng-binding').click();
        cy.get('[ng-if="!main.no_search_button"]').click();
    });
});
