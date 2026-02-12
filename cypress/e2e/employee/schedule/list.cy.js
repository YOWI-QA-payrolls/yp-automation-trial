describe('Employee Schedule - Schedule List', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should create a schedule entry with time selections', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#employeeschedule > a',
        ]);

        cy.get(':nth-child(7) > .btn', { timeout: 15000 }).should('be.visible').click();
        cy.get(':nth-child(1) > .checkbox > label').click();
        cy.get('[ng-if="set_schedule.is_group && !set_schedule.use_date_to"] > .form-control').type('1');
        cy.select2First(':nth-child(6) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.select2First(':nth-child(7) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
    });
});
