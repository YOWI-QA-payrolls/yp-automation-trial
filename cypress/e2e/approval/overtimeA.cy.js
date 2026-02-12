describe('Approval - Overtime/Undertime', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Business Trip Tab Approval Workflow', () => {
        it('should navigate to overtime approval and process business trip tab', () => {
            cy.navigateMenu([
                '#approval_list > a',
                '#undertime_overtime_approval > a'
            ]);

            cy.get('#approval_tab > :nth-child(5) > a', { timeout: 15000 })
                .should('be.visible')
                .click();

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

            cy.dismissToast();

            cy.get('tbody', { timeout: 30000 }).should('exist');

            cy.get('body').then($body => {
                if ($body.find('#advance-filter-btn').length > 0) {
                    cy.get('#advance-filter-btn').should('be.visible').click();
                    cy.get('tbody', { timeout: 30000 }).should('exist');
                    cy.get('#advance-search').should('be.visible').click();
                }
            });

            cy.get('body').then($body => {
                if ($body.find('[ng-model="ot_request.auto_approval_option"] .select2-choice').length > 0) {
                    cy.get('[ng-model="ot_request.auto_approval_option"] .select2-choice').click();

                    cy.get('body').then($innerBody => {
                        if ($innerBody.find('#ui-select-choices-0 li:nth-child(3)').length > 0) {
                            cy.get('#ui-select-choices-0 li:nth-child(3)').click();
                            cy.get('#auto_approval').click();
                            cy.get('#apply_status_btn').should('not.be.disabled').click();
                            cy.get('.confirm').should('be.visible').click();
                        }
                    });
                }
            });

            cy.dismissToast();

            cy.get('body').then($body => {
                if ($body.find('tbody tr:first > :nth-child(4)').length > 0) {
                    cy.get('tbody tr:first > :nth-child(4)').click();
                    cy.get('span.ng-scope > :nth-child(1) > label').should('be.visible').click();
                    cy.get('.pull-right > .btn-success').should('not.be.disabled').click();
                    cy.get('tbody', { timeout: 30000 }).should('exist');
                    cy.dismissToast();
                    cy.get('.confirm').should('be.visible').click();
                }
            });
        });
    });
});
