describe('Timesheet Reports - Incomplete Timesheet Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Incomplete Timesheet Report Filtering', () => {
        it('should navigate to incomplete timesheet, filter by date, search, and apply advanced filter', () => {
            cy.navigateMenu([
                '#timesheetreports_list > [href="#"]',
                '#incomplete_timesheet > a'
            ]);

            cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 })
                .should('be.visible')
                .click();
            cy.get('.uib-datepicker-popup .uib-left').should('be.visible').click();
            cy.get('.uib-datepicker-popup').contains('10').click();
            cy.get('.hand_cursor').should('be.visible').click();

            cy.get('tabletoolstrans > .input-group > .form-control').should('be.visible').type('Juan');

            cy.get('#advance-filter-btn', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('.btn-sm').should('be.visible').click();
        });
    });
});
