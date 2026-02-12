describe('Timesheet - Daily Logs', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Create Manual Timesheet Entry', () => {
        it('should navigate to daily logs and create a timesheet entry with manual schedule', () => {
            cy.navigateMenu([
                '#timesheets',
                '#daily_logs > a'
            ]);

            cy.get('tbody', { timeout: 30000 }).should('exist');

            cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > div > button', { timeout: 15000 })
                .should('be.visible')
                .click();

            cy.get('.form > :nth-child(1) > .input-group > .input-group-btn > .btn')
                .should('be.visible')
                .click();
            cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(1) > p.input-group > div')
                .contains('5').click();

            cy.select2First('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(5) > div > a > span.select2-arrow.ui-select-toggle');

            cy.get(':nth-child(6) > .form-control').should('be.visible').clear().type('manual');
            cy.select2First('.form > :nth-child(7) > .ui-select-container > .select2-choice');
            cy.get('.hours > .form-control').should('be.visible').type('8');
            cy.get('.minutes > .form-control').should('be.visible').type('30');
            cy.get('.pull-right > .btn-success').should('not.be.disabled').click();
        });
    });
});
