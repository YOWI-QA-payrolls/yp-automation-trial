describe('Employee Schedule - Group Schedule', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should create a group schedule with day assignments', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#employeeschedule > a',
        ]);
        cy.get('.navbar > .nav > :nth-child(2) > a', { timeout: 15000 }).should('be.visible').click({ force: true });

        cy.get('.col-sm-2 > .btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('.form-control').type('testing');
        cy.select2First('.select2-chosen.ng-binding');

        // Assign schedule to each day of the week
        const daySelectors = [
            '[ng-repeat="sorted_day in main.sorted_days_of_the_week"]:first .ui-select-container .select2-choice .select2-chosen.ng-binding',
            ':nth-child(5) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding',
            ':nth-child(6) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding',
            ':nth-child(7) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding',
            ':nth-child(8) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding',
            ':nth-child(9) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding',
            ':nth-child(10) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding',
        ];

        daySelectors.forEach((selector) => {
            cy.get(selector, { timeout: 10000 }).click();
            cy.get('.select2-highlighted > .select2-result-label > [ng-bind-html="schedule.name | highlight: $select.search"]', { timeout: 10000 })
                .should('be.visible')
                .click();
        });

        cy.get('.btn-success').click();
    });
});
