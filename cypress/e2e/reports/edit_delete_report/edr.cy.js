describe('Reports - Edit/Delete Timesheet', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should edit and delete a timesheet entry', () => {
        cy.get('#timesheets').click();
        cy.get('#daily_logs > a', { timeout: 15000 }).click();

        cy.get('#filter_date_from', { timeout: 15000 }).should('be.visible').click();
        cy.get('.uib-datepicker-popup').contains('11').click();
        cy.get('.input-group > :nth-child(5) > .btn').click();
        cy.get('.uib-datepicker-popup').contains('12').click();
        cy.get('.hand_cursor').click();

        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).type('juan');
        cy.get('[ng-if="!main.no_search_button"]').click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(6) > .ng-binding.ng-scope > [ng-if="user_employee != record.employee"] > [ng-click="edit_timesheet_dialog(record,typee.short_code)"]')
            .first()
            .click();

        cy.get('.form > :nth-child(1) > .form-control').clear().type('testing');
        cy.get('.pull-right > .btn-success').click();

        cy.get(':nth-child(19) > .btn').click();
        cy.get('.confirm', { timeout: 10000 }).should('be.visible').click();

        cy.get('td[ng-if="user_employee != record.employee"] > .btn').click();
        cy.get('fieldset > input').clear().type('testing');
        cy.get('.confirm', { timeout: 10000 }).should('be.visible').click();
    });
});
