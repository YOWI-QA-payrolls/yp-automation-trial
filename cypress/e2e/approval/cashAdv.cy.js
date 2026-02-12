describe('Approval - Cash Advance', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Cash Advance Approval Workflow', () => {
        it('should navigate to cash advance approval, filter by date, and process auto approval', () => {
            cy.navigateMenu([
                '#approval_list > a'
            ]);

            cy.intercept('POST', '**/cash_advance/read_pagination/**').as('loadData');
            cy.get('#cash_advance_approval > a', { timeout: 15000 }).should('exist').click({ force: true });

            cy.wait('@loadData');

            cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 })
                .should('be.visible')
                .click();
            cy.get('.uib-datepicker-popup .uib-left').should('be.visible').click();
            cy.get('.uib-datepicker-popup').contains('11').click();
            cy.get('[ng-model="main.filters.date_to"]').clear().type('01/30/2024');

            cy.get('tbody', { timeout: 30000 }).should('exist');

            cy.get('#advance-filter-btn', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('tbody', { timeout: 30000 }).should('exist');
            cy.get('#advance-search').should('be.visible').click();

            cy.get('[ng-model="main.auto_approval"] .select2-choice', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('body').then($body => {
                if ($body.find('#ui-select-choices-0 li').length > 0) {
                    cy.get('#ui-select-choices-0 li:nth-child(3)').click();
                    cy.get('#auto_approval').should('be.visible').click();
                    cy.get('[ng-click="main.submit_auto_approval()"]').should('not.be.disabled').click();
                    cy.get('.confirm').should('be.visible').click();
                } else {
                    cy.get('[ng-model="main.auto_approval"] .select2-choice').click();
                }
            });
        });
    });
});
