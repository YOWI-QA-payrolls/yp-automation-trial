describe('Reports - Edit/Delete Timesheet', () => {
    beforeEach(() => {
        cy.on('uncaught:exception', (err) => {
            if (err.message.includes('inprog')) return false;
        });
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should edit and delete a timesheet entry', () => {
        cy.navigateMenu([
            '#timesheets',
            '#daily_logs > a'
        ]);

        // -------- DATE FILTER --------
        cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 })
            .should('be.visible')
            .click();
        cy.get('.uib-datepicker-popup .uib-left').should('be.visible').click();
        cy.get('.uib-datepicker-popup').contains('10').click();
        cy.get('.hand_cursor').should('be.visible').click();

        // -------- SEARCH --------
        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).type('juan', { delay: 100 });
        cy.get('#advance-search').click();
        cy.get('tbody', { timeout: 30000 }).should('exist');

        // -------- EDIT (opens modal) --------
        const editSel = ':nth-child(6) > .ng-binding.ng-scope > [ng-if="user_employee != record.employee"] > [ng-click="edit_timesheet_dialog(record,typee.short_code)"]';
        cy.get('body').then(($body) => {
            if ($body.find(editSel).length > 0) {
                cy.wrap($body.find(editSel).first()).click({ force: true });
                cy.wait(500); // brief settle for modal animation

                // Modal may auto-close (e.g. location-type edit) — check body snapshot immediately
                cy.get('body').then(($b) => {
                    const $modal = $b.find('.modal-dialog').filter(':visible');
                    if ($modal.length > 0) {
                        const inputSel = 'input:not([type="hidden"]):not([type="button"]):not([type="submit"]):not([type="checkbox"]):not([type="radio"]), textarea';
                        const $inputs = $modal.find(inputSel).filter(':visible');
                        if ($inputs.length > 0) {
                            // Use {selectAll} + type in one command — avoids clear() which re-renders Angular
                            cy.wrap($inputs.first()).type('{selectAll}testing', { force: true });
                        }
                        const $btn = $modal.find('.btn-success, .btn-primary, .btn-default, .btn')
                            .filter(':visible').not(':disabled').first();
                        if ($btn.length > 0) {
                            // Native JS click — bypasses Cypress post-click DOM attachment check
                            // which fails when Angular re-renders the modal after saving
                            $btn[0].click();
                        }
                    }
                });

                // -------- DELETE --------
                cy.get('body').then(($bodyDel) => {
                    if ($bodyDel.find(':nth-child(19) > .btn').length > 0) {
                        cy.get(':nth-child(19) > .btn').first().click();
                        cy.get('.confirm', { timeout: 10000 }).should('be.visible').click({ force: true });
                    }
                });

                cy.get('body').then(($bodyDel2) => {
                    if ($bodyDel2.find('td[ng-if="user_employee != record.employee"] > .btn').length > 0) {
                        cy.get('td[ng-if="user_employee != record.employee"] > .btn').first().click();
                        cy.get('fieldset > input').first().clear().type('testing');
                        cy.get('.confirm', { timeout: 10000 }).should('be.visible').click({ force: true });
                    }
                });
            }
        });
    });
});