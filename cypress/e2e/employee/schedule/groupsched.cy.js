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
        cy.intercept('POST', '**/group_schedules/read_pagination/**').as('groupScheduleData');
        cy.get('.navbar > .nav > :nth-child(2) > a', { timeout: 15000 }).should('be.visible').click({ force: true });

        // Group Schedule page to fully load before clicking the Create button
        cy.url().should('include', 'group_schedule');
        cy.wait('@groupScheduleData', { timeout: 20000 });

        cy.get('.col-sm-2 > .btn', { timeout: 20000 }).should('be.visible').click();
        cy.get('textarea[ng-model="main.group_schedule.description"]', { timeout: 20000 })
            .should('exist')
            .type('testing', { force: true });

        // Select Starting Day - click the dropdown trigger, then select first option
        cy.get('[ng-model="main.group_schedule.starting_day"] .select2-chosen', { timeout: 15000 })
            .first()
            .click({ force: true });
        cy.get('.select2-results .ui-select-choices-row', { timeout: 10000 })
            .first()
            .click({ force: true });

        // Wait for day assignment selectors to render after starting day selection
        cy.get('[ng-repeat="sorted_day in main.sorted_days_of_the_week"]', { timeout: 10000 })
            .should('have.length', 7);

        // Assign schedule to each day of the week
        cy.get('[ng-repeat="sorted_day in main.sorted_days_of_the_week"]').each(($day, index) => {
            cy.wrap($day).scrollIntoView();
            cy.wrap($day).find('.select2-chosen').first().click({ force: true });
            cy.get('.select2-results .ui-select-choices-row', { timeout: 10000 })
                .first()
                .click({ force: true });
            // This is to verify this day's selection registered before moving to next
            cy.wrap($day).find('.ui-select-container')
                .should('not.have.class', 'ng-empty');
        });

        cy.get('.btn-success').click();
    });
});
