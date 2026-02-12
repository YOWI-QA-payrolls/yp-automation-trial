describe('Settings - General Settings - Kiosk Configuration', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure kiosk display and access settings', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(11) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get('#show_payslip_not_viewed', { timeout: 10000 })
            .should('exist');

        cy.get('#is_show_legend_daily_logs', { timeout: 10000 })
            .should('exist');

        cy.get('#is_kiosk_user_disable_request', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_use_schedule_code', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_sort_leave_type_by_code', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_hide_overtime', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_hide_undertime', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_hide_workonholiday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_hide_workonrestday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_hide_leave', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_hide_officialbusiness', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#hide_cash_advance', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#show_calendar', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_timekeeping_module', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#show_certificates', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#has_timein_out_access', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('[ng-if="kiosk_settings.has_timein_out_access"]:first .col-sm-8 .ui-select-container .select2-choices .select2-search-field .select2-input', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('.select2-results', { timeout: 10000 }).then($results => {
            const visibleResults = $results.find('.select2-result-label:visible');
            if (visibleResults.length > 0) {
                cy.wrap(visibleResults.first()).click();
            }
        });

        cy.get(':nth-child(4) > .col-sm-8 > .ui-select-container > .select2-choices > .select2-search-field > .select2-input', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('.select2-results', { timeout: 10000 }).then($results => {
            const visibleResults = $results.find('.select2-result-label:visible');
            if (visibleResults.length > 0) {
                cy.wrap(visibleResults.first()).click();
            }
        });

        cy.get('#has_project_timekeeping', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
