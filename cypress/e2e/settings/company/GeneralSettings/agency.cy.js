describe('Settings - General Settings - Agency Configuration', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure agency settings with name and fee', () => {
        // Delay read_pagination by 8s so the server can't reset has_agency before we interact
        cy.intercept('POST', /agency_settings.*read_pagination/, (req) => {
            req.continue((res) => {
                res.delay = 8000;
            });
        });

        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.waitForSettingsTable();
        cy.clickSettingsRow('Agency');

        cy.get('#has_agency', { timeout: 10000 }).should('exist').then($el => {
            if (!$el.is(':checked')) {
                cy.wrap($el).check({ force: true });
            }
        });

        // Force Angular to set agency.has_agency = true by walking the scope tree
        cy.window().then(win => {
            const el = win.document.getElementById('has_agency');
            if (!el) return;
            let scope = win.angular.element(el).scope();
            while (scope && scope.agency === undefined) {
                scope = scope.$parent;
            }
            if (scope && scope.agency !== undefined) {
                try {
                    scope.$apply(() => { scope.agency.has_agency = true; });
                } catch (e) {
                    scope.agency.has_agency = true;
                    scope.$evalAsync(() => {});
                }
            }
        });

        cy.get('[ng-if="agency.has_agency"] .form-control', { timeout: 10000 })
            .first()
            .type('{selectAll}testname', { force: true });

        cy.get('[ng-if="agency.has_agency"] .form-control', { timeout: 10000 })
            .eq(1)
            .type('{selectAll}500', { force: true });

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
