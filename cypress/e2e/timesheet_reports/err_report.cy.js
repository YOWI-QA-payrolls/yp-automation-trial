describe('Timesheet Reports - Erroneous Timesheet Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Erroneous Timesheet Report Filtering and Delete', () => {
        it('should navigate to erroneous timesheet, filter by date, and delete a record', () => {
            cy.navigateMenu([
                '#timesheetreports_list > a',
                '#erroneous_timesheet > a'
            ]);

            cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 }).should('be.visible').click();
            cy.get('.uib-datepicker-popup .uib-left').should('be.visible').click();
            cy.get('.uib-datepicker-popup').contains('29').click();
            cy.get('.hand_cursor').should('be.visible').click();

            cy.wait(2000);
            cy.get('body').then(($body) => {
                if ($body.find(':nth-child(11) > .btn').length > 0) {
                    cy.get(':nth-child(11) > .btn').first().click();
                    cy.get('fieldset > input').should('be.visible').type('test');
                    cy.get('.confirm').should('be.visible').click();
                }
            });
        });
    });
});
