describe('Settings - General Settings - Minimum Wage', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should create a new minimum wage entry', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(16) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('[ng-click="minimum_wage.locations = all_locations"] > .fa', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('.input-group-btn > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('.btn-info', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(3) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('556');

        cy.get('.btn-success', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
