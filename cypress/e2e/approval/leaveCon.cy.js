describe('Approval - Leave Conversion', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Leave Conversion Approval Workflow', () => {
        it('should navigate to leave conversion approval, filter, and create conversion form', () => {
            cy.navigateMenu([
                '#approval_list > a',
                '#leave_conversion > a'
            ]);

            cy.get('body').then($body => {
                if ($body.find('[ng-click="main.open_date(\'filter_date_from\')"]').length > 0) {
                    cy.get('[ng-click="main.open_date(\'filter_date_from\')"]').click();
                    cy.get('.uib-datepicker-popup .uib-left').click();
                    cy.get('.uib-datepicker-popup').contains('11').click();
                }
                if ($body.find('[ng-model="filters.date_to"]').length > 0) {
                    cy.get('[ng-model="filters.date_to"]').clear().type('01/30/2024');
                }
            });

            cy.get('tbody', { timeout: 30000 }).should('exist');

            cy.get('#advance-filter-btn', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('tbody', { timeout: 30000 }).should('exist');
            cy.get('#advance-search').should('be.visible').click();

            cy.get('body').then($body => {
                if ($body.find('.btn-group > .btn').length > 0) {
                    cy.get('.btn-group > .btn').should('be.visible').click();
                    cy.get('.col-sm-3 > .ui-select-container > .select2-choice > .select2-arrow > b')
                        .should('be.visible')
                        .click();

                    cy.get('body').then($innerBody => {
                        if ($innerBody.find('.select2-highlighted > .select2-result-label > .ng-binding').length > 0) {
                            cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
                            cy.get(':nth-child(2) > .ui-select-container > .select2-choice > .select2-arrow > b').click();
                            cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
                            cy.get('#no_of_days').should('be.visible').type('5');
                            cy.get(':nth-child(4) > .input-group > .input-group-btn > .btn').should('be.visible').click();
                            cy.get('.btn-info').should('not.be.disabled').click();
                            cy.get('.col-sm-1 > .btn').should('not.be.disabled').click();
                            cy.get('tbody', { timeout: 30000 }).should('exist');
                            cy.get('.btn-success').should('not.be.disabled').click();
                        }
                    });
                }
            });
        });
    });
});
