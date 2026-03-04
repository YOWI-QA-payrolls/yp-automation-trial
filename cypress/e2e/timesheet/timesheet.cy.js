describe('Timesheet - Daily Logs', () => {
    beforeEach(() => {
        cy.on('uncaught:exception', () => false);
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Create Manual Timesheet Entry', () => {
        it('should navigate to daily logs and create a timesheet entry with manual schedule', () => {
            cy.navigateMenu([
                '#timesheets',
                '#daily_logs > a'
            ]);

            cy.get('tbody', { timeout: 30000 }).should('exist');

            cy.window().then((win) => {
                // Block ALL $uibModalStack.dismiss calls for the entire test.
                // Both the employee ui-select and the schedule type select2 render
                // their dropdowns in document.body; clicking them triggers the
                // $uibModalStack document-level click listener which calls dismiss().
                // The modal closes via stack.close() on successful submission, so
                // blocking dismiss() does not affect the intended close path.
                // Must be patched BEFORE clicking Create so residual document events
                // from preceding tests cannot auto-dismiss the modal.
                try {
                    const injector = win.angular.element(win.document.body).injector();
                    const stack = injector.get('$uibModalStack');
                    stack.dismiss = () => {};
                } catch (e) { /* ignore if service not found */ }
            });

            cy.get('.page-heading .col-sm-4 button', { timeout: 15000 })
                .first()
                .should('be.visible')
                .click({ force: true });

            cy.get('.modal.in', { timeout: 15000 }).should('be.visible');
            cy.get('.modal.in .form > :nth-child(1) input').first().then(($el) => {
                $el.val('03/05/2026').trigger('input').trigger('change');
            });
            cy.get('.modal.in .panel-body form div:nth-child(5) .select2-arrow.ui-select-toggle', { timeout: 10000 })
                .should('exist').first().click({ force: true });
            cy.get('.select2-drop-active .select2-input', { timeout: 10000 }).first().type('aria');
            cy.get('.ui-select-choices-row', { timeout: 10000 }).first().click({ force: true });
            cy.wait(1000);

            cy.get('.modal.in').should('be.visible');
            cy.get('.modal.in .form > :nth-child(6) > .form-control').clear({ force: true }).type('manual', { force: true });
            cy.select2First('.modal.in .form > :nth-child(7) > .ui-select-container > .select2-choice > .select2-arrow > b');
            cy.get('.hours > .form-control').should('be.visible').type('8');
            cy.get('.minutes > .form-control').should('be.visible').type('30');
            cy.get('.pull-right > .btn-success').should('not.be.disabled').click();
        });
    });
});
