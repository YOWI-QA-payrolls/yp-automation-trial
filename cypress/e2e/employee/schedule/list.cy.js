describe('Employee Schedule - Schedule List', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
        // Wait for any modal to disappear before proceeding
        cy.get('.modal').should('not.exist');
    });

    it('should create a schedule entry with time selections', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#employeeschedule > a',
        ]);

        cy.get(':nth-child(7) > .btn', { timeout: 15000 }).should('be.visible').click();
        cy.get(':nth-child(1) > .checkbox > label').click();
        cy.get('[ng-if="set_schedule.is_group && !set_schedule.use_date_to"] > .form-control').type('1');
        // Debug: log the DOM to help inspect if the select2 elements are present
        cy.get('.modal-content').then($modal => {
            cy.log($modal.html());
        });

        // Use a more robust selector for select2 dropdowns
        cy.get('.modal-content .ui-select-container', { timeout: 10000 }).should('have.length.at.least', 2);
        cy.select2First('.modal-content .ui-select-container:eq(0) .select2-choice');
        cy.select2First('.modal-content .ui-select-container:eq(1) .select2-choice');
    });
});
