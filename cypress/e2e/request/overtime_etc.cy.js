describe('Request - Overtime and Business Trip', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Overtime Request and Business Trip Workflow', () => {
        it('should navigate to overtime request and create a business trip request', () => {
            cy.navigateMenu([
                '#requests_list > a',
                '#undertime_overtime_request > a'
            ]);

            cy.get('#request_tab > :nth-child(5) > a', { timeout: 15000 })
                .should('be.visible')
                .click();

            cy.get('tbody', { timeout: 30000 }).should('exist');

            cy.get('#advance-filter-btn', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('#advance-search').should('be.visible').click();

            cy.get('.col-sm-3 > .pull-right > .btn').should('not.be.disabled').click();
            cy.select2First('.select2-chosen.ng-binding');
            cy.get('[ng-show="official_business.employee"] > .col-sm-8 > :nth-child(2)').should('exist');
            cy.get('#whole_day').should('be.visible').click();
            cy.get(':nth-child(8) > .form-control').should('be.visible').type('testing');
            cy.get('.pull-right > .btn-success').should('not.be.disabled').click();
            cy.get('.cancel').should('be.visible').click();
            cy.get('.col-sm-8 > .pull-right > .btn').should('be.visible').click();
        });
    });
});
