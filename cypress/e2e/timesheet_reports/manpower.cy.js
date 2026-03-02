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

            cy.get('.select2-chosen:contains("Detailed")', { timeout: 15000 })
                .should('be.visible')
                .click();
            cy.get('.select2-results .ui-select-choices-row-inner', { timeout: 10000 })
                .contains('Detailed')
                .click();

            cy.get('input.select2-input[placeholder="Location"]', { timeout: 15000 })
                .should('be.visible')
                .click()
                .type('Cagayan De Oro{enter}');

            cy.get('button[ng-click="main.main_loader();"]', { timeout: 10000 })
                .first()
                .should('be.visible')
                .click();
            cy.get('tbody', { timeout: 30000 }).should('exist');
        });
    });
});
