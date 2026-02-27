describe('Reports - Edit/Delete Timesheet', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should edit and delete a timesheet entry', () => {
        cy.get('#timesheets').click();
        cy.get('#daily_logs > a', { timeout: 15000 }).click();

        // -------- DATE FILTER (FROM/TO) --------
        cy.get('body', { timeout: 30000 }).then(($body) => {
            const fromSel =
                $body.find('#filter_date_from').length
                    ? '#filter_date_from'
                    : 'input[name="filter_date_from"], input[id*="filter_date_from"], input[ng-model*="date_from"], input[placeholder*="From"]';

            const toSel =
                $body.find('#filter_date_to').length
                    ? '#filter_date_to'
                    : 'input[name="filter_date_to"], input[id*="filter_date_to"], input[ng-model*="date_to"], input[placeholder*="To"]';

            cy.get(fromSel, { timeout: 30000 }).first().should('be.visible').click({ force: true });

            cy.get('body').then(($b) => {
                const popupSel =
                    $b.find('.uib-datepicker-popup').length
                        ? '.uib-datepicker-popup'
                        : ($b.find('.ui-datepicker').length ? '.ui-datepicker' : null);

                if (popupSel) {
                    cy.get(popupSel, { timeout: 15000 }).contains(/^11$/).first().click();
                    cy.get('.input-group > :nth-child(5) > .btn').first().click();
                    cy.get(popupSel, { timeout: 15000 }).contains(/^12$/).first().click();
                    cy.get('.hand_cursor:visible').first().click();
                } else {
                    cy.get(fromSel).first().then(($el) => {
                        const type = ($el.attr('type') || '').toLowerCase();
                        const val = type === 'date' ? '2026-02-23' : '02/23/2026';
                        cy.wrap($el).clear({ force: true }).type(val, { force: true });
                    });

                    cy.get(toSel).first().then(($el) => {
                        const type = ($el.attr('type') || '').toLowerCase();
                        const val = type === 'date' ? '2026-02-24' : '02/24/2026';
                        cy.wrap($el).clear({ force: true }).type(val, { force: true });
                    });
                }
            });
        });

        // -------- SEARCH --------
        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).type('juan');
        cy.get('[ng-if="!main.no_search_button"]').click();
        cy.get('tbody', { timeout: 30000 }).should('exist');

        // -------- EDIT (opens modal) --------
        const editSel = ':nth-child(6) > .ng-binding.ng-scope > [ng-if="user_employee != record.employee"] > [ng-click="edit_timesheet_dialog(record,typee.short_code)"]';
        cy.get('body').then(($body) => {
            if ($body.find(editSel).length > 0) {
                cy.get(editSel).first().click();

                // Reason field (textarea)
                cy.get('.form > :nth-child(1) > .form-control').first().clear().type('testing');

                // fill required TIME in modal to avoid "Please indicate Time."
                cy.get('.modal:visible').within(() => {
                    cy.get('input[placeholder="HH"]').first().clear().type('08');
                    cy.get('input[placeholder="MM"]').first().clear().type('30');
                });

                cy.get('.pull-right > .btn-success').click();

                // -------- DELETE --------
                cy.get(':nth-child(19) > .btn').first().click();
                cy.get('.confirm', { timeout: 10000 }).should('be.visible').click();

                cy.get('td[ng-if="user_employee != record.employee"] > .btn').first().click();
                cy.get('fieldset > input').first().clear().type('testing');
                cy.get('.confirm', { timeout: 10000 }).should('be.visible').click();
            }
        });
    });
});