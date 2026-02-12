describe('Settings - General Settings - Approval Settings', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure approval hierarchy and request settings', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(4) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get('#has_approval_hierarchy', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_allow_bypass_approval', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#allowed_credit_adjustment', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#auto_request_overtime', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
