describe('Request - Cash Advance', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Cash Advance Request Workflow', () => {
        it('should navigate to cash advance request, filter, search, and create a new cash advance', () => {
            cy.navigateMenu([
                '#requests_list > a',
                '#cash_advance_request > a'
            ]);

            cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 }).should('be.visible').click();
            cy.get('.uib-datepicker-popup .uib-left').should('be.visible').click();
            cy.get('thead > :nth-child(1) > :nth-child(3) > .btn').should('be.visible').click();
            cy.get('.uib-datepicker-popup').contains('8').click();
            cy.get('tabletoolsdaterange3 > .input-group > .form-control.ng-pristine').clear().type('01/08/2024');

            cy.get('tabletoolstrans > .input-group > .form-control').should('be.visible').type('caleb');

            cy.get('tbody', { timeout: 30000 }).should('exist');

            cy.get('#advance-filter-btn', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('#advance-search').should('be.visible').click();

            cy.get('.form-group > .btn').should('not.be.disabled').click();
            cy.select2First('.align_left > :nth-child(1) > .col-sm-3 > .ui-select-container > .select2-choice > .select2-arrow > b');

            cy.select2First('[ng-if="main.record.cash_advance_type == \'regular\' || !main.record.id"] > :nth-child(1) > :nth-child(1) > .ui-select-container > .select2-choice > .select2-arrow > b');

            cy.get('#input_list_amount').should('be.visible').type('1500');

            cy.get(':nth-child(3) > .input-group > .input-group-btn > .btn').should('be.visible').click();
            cy.get('#page-top div.modal.fade.in div.panel-body table tbody tr:nth-child(2) td div div:nth-child(1) div:nth-child(3) p div ul')
                .contains('21').click();
            cy.get('#input_list_amount_to_').should('be.visible').type('testing');
            cy.get('.radio > label').should('be.visible').click();
            cy.get('.col-sm-3.form-group > :nth-child(4) > label').should('be.visible').click();
            cy.get('.col-sm-5 > .form-control').should('be.visible').type('500');
            cy.get('.col-sm-12 > :nth-child(1) > .input-group > .input-group-btn > .btn').should('be.visible').click();
            cy.get('.btn-group > .btn-info').should('not.be.disabled').click();
            cy.get('.btn-success').should('not.be.disabled').click();
        });
    });
});
