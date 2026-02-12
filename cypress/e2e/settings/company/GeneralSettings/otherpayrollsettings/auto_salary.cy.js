describe('Settings - General Settings - Auto Salary Increment', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should toggle auto salary increment setting', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(10) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(7) > td', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('#is_auto_salary_increment', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('exist');
    });
});
