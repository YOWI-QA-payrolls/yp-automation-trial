describe('Timesheet - Complete Timesheet', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Create Complete Timesheet by Date Range', () => {
        it('should navigate to daily logs and create a complete timesheet entry', () => {
            cy.navigateMenu([
                '#timesheets_list > a',
                '#daily_logs > a'
            ]);

            cy.get('tbody', { timeout: 30000 }).should('exist');

            cy.get(':nth-child(3) > .btn-group > .btn', { timeout: 15000 })
                .should('be.visible')
                .click();
            cy.get('.btn-group > .dropdown-menu > li > a').should('be.visible').click();
            cy.get('#by_date_range').should('be.visible').click();
            cy.get(':nth-child(3) > .form-control').should('be.visible').type('manual');
            cy.get('[ng-click="complete_timesheet.employees = filter_employees2;get_employee_schedule(complete_timesheet)"] > .fa')
                .should('be.visible')
                .click();
            cy.get(':nth-child(9) > :nth-child(3) > label').should('be.visible').click();
            cy.get('.pull-right > .btn-success').should('not.be.disabled').click();
        });
    });
});
