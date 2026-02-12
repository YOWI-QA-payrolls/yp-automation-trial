describe('Request - Transfer', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Transfer Request Workflow', () => {
        it('should navigate to transfer request, filter, search, and create a new transfer', () => {
            cy.navigateMenu([
                '#requests_list > a',
                '#transfer_request > a'
            ]);

            cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 }).should('be.visible').click();
            cy.get('.uib-datepicker-popup .uib-left').should('be.visible').click();
            cy.get('thead > :nth-child(1) > :nth-child(3) > .btn').should('be.visible').click();
            cy.get('.uib-datepicker-popup').contains('8').click();
            cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('01/08/2024');

            cy.get('tabletoolstrans > .input-group > .form-control').should('be.visible').type('aria');

            cy.get('tbody', { timeout: 30000 }).should('exist');

            cy.get('#advance-filter-btn', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('#advance-search').should('be.visible').click();

            cy.get('.iCheck-helper').should('exist').click();
            cy.select2First('.select2-arrow > b');
            cy.select2First('.select2-arrow > b');

            cy.get('.form-group > .btn-group > .btn').should('not.be.disabled').click();
            cy.get(':nth-child(2) > .input-group > .input-group-btn > .btn').should('be.visible').click();
            cy.get('.btn-info').should('not.be.disabled').click();
            cy.select2First(':nth-child(5) > .ui-select-container > .select2-choice > .select2-arrow > b');
            cy.select2First('.select2-choices');

            cy.select2First('tr.ng-scope > :nth-child(1) > .ui-select-container > .select2-choice > .select2-arrow > b');
            cy.get('.col-sm-6 > .form-control').should('be.visible').type('testing');
            cy.get(':nth-child(2) > .ng-isolate-scope > .uib-timepicker > tbody > :nth-child(2) > .hours > .form-control')
                .should('be.visible').type('08');
            cy.get(':nth-child(2) > .ng-isolate-scope > .uib-timepicker > tbody > :nth-child(2) > .minutes > .form-control')
                .should('be.visible').type('30');
            cy.get(':nth-child(3) > .ng-isolate-scope > .uib-timepicker > tbody > :nth-child(2) > .hours > .form-control')
                .should('be.visible').type('17');
            cy.get(':nth-child(3) > .ng-isolate-scope > .uib-timepicker > tbody > :nth-child(2) > .minutes > .form-control')
                .should('be.visible').type('30');
            cy.get(':nth-child(6) > span > .btn').should('be.visible').click();
            cy.get('#leave_submit').should('not.be.disabled').click();
            cy.get('.cancel').should('be.visible').click();
            cy.get('.col-sm-8 > .pull-right > .btn').should('be.visible').click();
        });
    });
});
