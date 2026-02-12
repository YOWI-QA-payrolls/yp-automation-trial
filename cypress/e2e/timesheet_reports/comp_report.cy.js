describe('Timesheet Reports - Complete Timesheet Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Complete Timesheet Report Filtering and Actions', () => {
        it('should navigate to complete timesheet report, filter by date, toggle columns, and send email', () => {
            cy.navigateMenu([
                '#timesheetreports_list > a',
                '#complete_timesheet > a'
            ]);

            cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 }).should('be.visible').click();
            cy.get('.uib-datepicker-popup').contains('10').click();
            cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('12/29/2023');

            cy.get('#advance-filter-btn', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('.btn-sm').should('be.visible').click();

            cy.get('span.ng-scope > .btn', { timeout: 10000 }).should('be.visible').click();
            cy.get('.row > :nth-child(1) > .checkbox > label').should('be.visible').dblclick();
            cy.get('span.ng-scope > .btn').should('be.visible').click();

            cy.get('div.pull-right > .dropdown-toggle', { timeout: 10000 }).should('be.visible').click();
            cy.get('[ng-if="main.has_send_mail"] > .ng-scope').should('be.visible').click();
            cy.get('.cancel').should('be.visible').click();
        });
    });
});
