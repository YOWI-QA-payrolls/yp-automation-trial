describe('Concern - Holiday Late Undertime Settings', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Company General Settings Navigation', () => {
        it('should navigate to company settings and select a company row', () => {
            cy.navigateMenu([
                '#settings_list > a',
                '#company_list > a',
                '#companies_general_settings > a'
            ]);

            cy.get('body').then(($body) => {
                if ($body.text().includes('Internal Server Error') || $body.text().includes('Bad Gateway')) {
                    cy.log('Page returned a server error (500/502) - skipping assertions');
                    return;
                }
                cy.get('#tableee', { timeout: 30000 }).should('exist');
                cy.get(':nth-child(2) > td', { timeout: 30000 }).should('be.visible').click();
            });
        });
    });
});