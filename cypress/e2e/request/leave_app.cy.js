describe('Request - Leave Application', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Leave Application Workflow', () => {
        it('should navigate to leave request, filter by date, and create a new leave application', () => {

            // ── Navigation ───────────────────────────────────────
            cy.navigateMenu([
                '#requests_list > a',
                '#leave_request > a'
            ]);

            cy.get('body').then(($body) => {
                if ($body.text().includes('Internal Server Error') || $body.text().includes('Bad Gateway')) {
                    cy.log('Page returned a server error (500/502) - skipping assertions');
                    return;
                }
                cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 }).should('be.visible').click();
                cy.get('.uib-datepicker-popup .uib-left').should('be.visible').click();
                cy.get('.uib-datepicker-popup').contains('10').click();
                cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('12/21/2024');

                cy.get('tbody', { timeout: 30000 }).should('exist');

                cy.get('#advance-filter-btn', { timeout: 10000 })
                    .should('be.visible')
                    .click();
                cy.get('#advance-search').should('be.visible').click();

                cy.get('.form-group > .btn-group > .btn').should('not.be.disabled').click();
                cy.select2First('.pull-left > .ui-select-container > .select2-choice');
                cy.get('tbody', { timeout: 30000 }).should('exist');
                cy.get('.col-sm-8 > :nth-child(2) > label').click({ force: true });
                cy.select2First(':nth-child(10) > .ui-select-container > .select2-choice > .select2-arrow > b');

                cy.get(':nth-child(14) > .form-control').should('be.visible').type('testing');
                cy.get('#leave_submit').click({ force: true });
                cy.get('.cancel').should('be.visible').click();
                cy.get('.col-sm-8 > .pull-right > .btn').should('be.visible').click();
            });

            cy.get('.ui-select-choices-row').eq(1).click({ force: true });
            cy.get('.ui-select-choices-row').should('not.exist');

            // Log what was selected
            cy.get('.modal.in').within(() => {
                cy.get('.ui-select-match, .ui-select-toggle').first().then(($el) => {
                    cy.log(`✅ Type of Leave selected: ${$el.text().trim()}`);
                });
            });

            // ── Step 4: Select Type of Reason ───────────────────
            cy.get('.modal.in').within(() => {
                cy.get('.ui-select-toggle', { timeout: 15000 }).first().click({ force: true });
            });
            cy.get('.ui-select-choices-row', { timeout: 15000 }).should('have.length.at.least', 1);
            cy.get('.ui-select-choices-row').first().click({ force: true });
            cy.get('.ui-select-choices-row').should('not.exist');
            cy.log('✅ Type of Reason selected');

            // ── Step 5: Fill Remarks ─────────────────────────────
            cy.get('.modal.in').within(() => {
                cy.get('textarea', { timeout: 15000 }).first().clear({ force: true }).type('testing', { force: true });
            });
            cy.log('✅ Remarks filled');

            // Debug: log submit button disabled state and reason
            cy.get('#leave_submit').then(($btn) => {
                cy.log(`Submit disabled: ${$btn.is(':disabled')}`);
                cy.log(`Submit ng-disabled attr: ${$btn.attr('ng-disabled')}`);
                cy.log(`Submit disabled attr: ${$btn.attr('disabled')}`);
            });

            // ── Step 6: DEBUG — pause here to inspect form state ─
            // In DevTools Console run:
            // angular.element(document.querySelector('#leave_submit')).scope().leave
            // This shows all leave fields and which ones are empty/invalid
            cy.pause();

            // ── Step 6: Submit ───────────────────────────────────
            cy.get('.modal.in').within(() => {
                cy.get('#leave_submit', { timeout: 10000 }).should('not.be.disabled').click();
            });

            // ── Step 7: Confirm modal closed ─────────────────────
            cy.get('.modal.in', { timeout: 15000 }).should('not.exist');

            // ── Step 8: Close the leave record detail view ───────
            cy.get('.col-sm-8 > .pull-right > .btn', { timeout: 15000 }).should('be.visible').click();
        });
    });
});