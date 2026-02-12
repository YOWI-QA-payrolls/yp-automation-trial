describe('Timesheet Reports - Manpower Analysis Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Manpower Analysis Report with Department and Period Tabs', () => {
        it('should navigate to manpower analysis, search by department, change views, and configure period tab', () => {
            cy.navigateMenu([
                '#timesheetreports_list > [href="#"]',
                '#manpower_analysis_report > a'
            ]);

            cy.get(':nth-child(2) > .input-group > .form-control', { timeout: 15000 })
                .should('be.visible')
                .click();

            cy.get('.select2-search-field > .select2-input').should('be.visible').type('MAIN {enter}');

            cy.get(':nth-child(3) > .ui-select-container > .select2-choice > .select2-arrow > b', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get(':nth-child(2) > .select2-result-label > .ng-binding').should('be.visible').click();
            cy.get('tbody', { timeout: 30000 }).should('exist');
            cy.get(':nth-child(3) > .ui-select-container > .select2-choice > .select2-arrow > b')
                .should('be.visible')
                .click();
            cy.get(':nth-child(1) > .select2-result-label > .ng-binding').should('be.visible').click();
            cy.get('tbody', { timeout: 30000 }).should('exist');

            cy.get('[select="change_tab(\'period\')"] > .nav-link', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('[ng-model="filters.date_from"]').should('be.visible').clear().type('12/10/2023');
            cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('12/26/2023');
            cy.get('.input-group > .hand_cursor').should('be.visible').click();
            cy.get('.input-group > .ui-select-container > .select2-choice > .select2-arrow > b')
                .should('be.visible')
                .click();
            cy.get(':nth-child(2) > .select2-result-label > .ng-binding').should('be.visible').click();
            cy.get('div.pull-right > [type="button"]').should('not.be.disabled').click();
        });
    });
});
