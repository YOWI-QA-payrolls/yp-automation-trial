describe('Timesheet Reports - Break Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Break Report Filtering and View Options', () => {
        it('should navigate to break report, filter by date, search, and change view options', () => {
            cy.navigateMenu([
                '#timesheetreports_list > [href="#"]',
                '#break_reports > a'
            ]);

            cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 })
                .should('be.visible')
                .click();
            cy.get('.uib-datepicker-popup .uib-left').should('be.visible').click();
            cy.get('.uib-datepicker-popup').contains('10').click();
            cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('12/10/2023');

            cy.get('tabletoolstrans > .input-group > .form-control').should('be.visible').type('Juan');
            cy.get('#advance-search').should('be.visible').click();

            cy.get('#advance-filter-btn', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('tbody', { timeout: 30000 }).should('exist');
            cy.get('.btn-sm').should('be.visible').click();

            cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div.col-sm-2 > div > div > a > span.select2-arrow.ui-select-toggle', { timeout: 10000 })
                .should('be.visible')
                .click({ multiple: true });
            cy.get('.select2-highlighted > .select2-result-label').should('be.visible').click();
            cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div.col-sm-2 > div > div > a > span.select2-arrow.ui-select-toggle')
                .should('be.visible')
                .click({ multiple: true });
            cy.get(':nth-child(2) > .select2-result-label').should('be.visible').click();
            cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div.col-sm-2 > div > div > a > span.select2-arrow.ui-select-toggle')
                .should('be.visible')
                .click({ multiple: true });
            cy.get(':nth-child(3) > .select2-result-label > .ng-binding').should('be.visible').click();

            cy.get('.ui-select-match > .btn-default', { timeout: 10000 }).should('be.visible').click();
            cy.get(':nth-child(3) > .ui-select-choices-row-inner').should('be.visible').click();
        });
    });
});
