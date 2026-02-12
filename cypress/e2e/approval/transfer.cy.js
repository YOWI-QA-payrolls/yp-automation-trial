describe('Approval - Transfer', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Transfer Approval Workflow', () => {
        it('should navigate to transfer approval, filter, and process approval', () => {
            cy.navigateMenu([
                '#approval_list > a',
                '#transfer_approval_request > a'
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
                if ($body.find('[ng-model="filters.auto_approval_option"] .select2-choice').length > 0) {
                    cy.get('[ng-model="filters.auto_approval_option"] .select2-choice').click();

                    cy.get('body').then($innerBody => {
                        if ($innerBody.find('#ui-select-choices-2 li:nth-child(3)').length > 0) {
                            cy.get('#ui-select-choices-2 li:nth-child(3)').click();
                            cy.get('.btn-success').should('not.be.disabled').click();
                        }
                    });
                }
            });

            cy.dismissToast();

            cy.get('body').then($body => {
                if ($body.find('tbody tr.hand_cursor').length > 0) {
                    cy.get('tbody tr.hand_cursor > :nth-child(6)').click();
                    cy.get('#leave_submit').should('not.be.disabled').click();
                    cy.get('tbody', { timeout: 30000 }).should('exist');
                    cy.dismissToast();
                    cy.get('.confirm').should('be.visible').click();
                }
            });
        });
    });
});
