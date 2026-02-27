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
                expect(
                    $body.text().includes('Internal Server Error') || $body.text().includes('Bad Gateway'),
                    'Page should not return a server error'
                ).to.be.false;
            });

            // ── Date Filter ──────────────────────────────────────
            cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 })
                .should('be.visible').click();
            cy.get('.uib-datepicker-popup .uib-left').should('be.visible').click();
            cy.get('.uib-datepicker-popup').contains('10').click();

            const date = new Date();
            date.setMonth(date.getMonth() - 1);
            const dynamicDate = `${String(date.getMonth() + 1).padStart(2, '0')}/21/${date.getFullYear()}`;
            cy.get('tabletoolsdaterange2 > .input-group > .form-control').first().clear().type(dynamicDate);

            cy.get('tbody', { timeout: 30000 }).should('exist');

            // ── Advance Filter ───────────────────────────────────
            cy.get('#advance-filter-btn', { timeout: 10000 }).should('be.visible').click();
            cy.wait(500);
            cy.get('#advance-search', { timeout: 10000 }).should('be.visible').click();

            // ── Open New Leave Modal ─────────────────────────────
            cy.get('.form-group > .btn-group > .btn').should('not.be.disabled').click();
            cy.get('.modal.in', { timeout: 15000 }).should('be.visible');

            // ── Step 1: Select Employee ──────────────────────────
            cy.get('.modal.in').within(() => {
                cy.get('.ui-select-toggle').first().click({ force: true });
            });
            cy.get('.ui-select-choices-row', { timeout: 15000 }).first().click({ force: true });
            cy.get('.ui-select-choices-row').should('not.exist');

            // Wait for leave balances and radios to render
            cy.get('label[for="whole_day"]', { timeout: 15000 }).should('be.visible');

            // ── Step 2: Click Whole Day ──────────────────────────
            cy.get('label[for="whole_day"]').click({ force: true });
            cy.get('#whole_day').should('be.checked');
            cy.log('✅ Whole Day radio is checked');

            // ── Step 3: Select Type of Leave ────────────────────
            cy.get('.modal.in').within(() => {
                cy.get('.ui-select-toggle', { timeout: 15000 }).first().click({ force: true });
            });
            cy.get('.ui-select-choices-row', { timeout: 15000 }).should('have.length.at.least', 1);

            // Log all available options so we can see what's in the dropdown
            cy.get('.ui-select-choices-row').each(($row, i) => {
                cy.log(`Leave type option ${i}: ${$row.text().trim()}`);
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