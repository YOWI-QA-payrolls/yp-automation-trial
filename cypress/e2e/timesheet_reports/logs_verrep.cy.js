describe('Timesheet Reports - Logs Verification Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Logs Verification Report Multi-Tab Workflow', () => {
        it('should navigate to logs verification, search, filter, and browse all tabs', () => {
            cy.navigateMenu([
                '#timesheetreports_list > [href="#"]',
                '#logs_verification_reports > a'
            ]);

            cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 }).should('be.visible').click();

            cy.get('tabletoolstrans > .input-group > .form-control').should('be.visible').type('Juan');

            cy.get('#advance-filter-btn', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('.btn-sm').should('be.visible').click();

            cy.get('.ui-select-match > .btn-default', { timeout: 10000 }).should('be.visible').click();
            cy.get(':nth-child(3) > .ui-select-choices-row-inner').should('be.visible').click();

            cy.select2First('#page-wrapper div.wrapper.wrapper-content.body div.tab-pane.ng-scope.active div.col-xs-6.col-sm-6.col-md-3.col-lg-2.pull-left a span.select2-arrow.ui-select-toggle');

            cy.get('[select="main._change_tab(\'summary_per_range\')"] > .nav-link', { timeout: 10000 })
                .should('be.visible')
                .click();

            cy.get('tabletoolstrans > .input-group > .form-control').should('be.visible').type('Juan');

            cy.get('#advance-filter-btn', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('.btn-sm').should('be.visible').click();
            cy.get('tbody', { timeout: 30000 }).should('exist');

            cy.get('.active > .nav-link', { timeout: 10000 }).should('be.visible').click();

            cy.get('tabletoolstrans > .input-group > .form-control').should('be.visible').type('Juan');

            cy.get('#advance-filter-btn', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('.btn-sm').should('be.visible').click();
            cy.get('tbody', { timeout: 30000 }).should('exist');

            cy.get('[select="main._change_tab(\'summary_per_classification\')"] > .nav-link', { timeout: 10000 })
                .should('be.visible')
                .click();

            cy.get('tabletoolstrans > .input-group > .form-control').should('be.visible').type('Juan');

            cy.get('#advance-filter-btn', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('.btn-sm').should('be.visible').click();

            cy.get('#select_payroll_period', { timeout: 10000 }).should('exist').click({ force: true });
            cy.select2First('.form-group > .ui-select-container > .select2-choice');
        });
    });
});
