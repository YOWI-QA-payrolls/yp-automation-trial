describe('Settings - General Settings - Agency Configuration', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure agency settings with name and fee', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(7) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get('#has_agency', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('[ng-if="agency.has_agency"]:first .input-group .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('testname');

        cy.get(':nth-child(3) > .input-group > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
