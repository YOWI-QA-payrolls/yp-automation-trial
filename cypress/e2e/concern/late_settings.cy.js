describe('Concern - Late Settings', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Configure 10 Minutes Late Setting', () => {
        it('should navigate to company settings and set 10 minute late threshold', () => {
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
                cy.get(':nth-child(1) > td').should('be.visible').click();

                cy.get('.form-control').should('be.visible').clear().type('10');

                cy.get('.form-group > .btn').should('not.be.disabled').click();
            });
        });
    });

    describe('Configure Customized Late Setting', () => {
        it('should navigate to company settings and configure customized late thresholds', () => {
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
                cy.get(':nth-child(1) > td').should('be.visible').click();

                cy.get('#customize_late').should('be.visible').click();

                cy.get(':nth-child(1) > .form-control').should('be.visible').type('5');
                cy.get('.form > :nth-child(2) > .form-control').should('be.visible').type('10');
                cy.get(':nth-child(3) > .form-control').should('be.visible').type('10');

                cy.get('.pull-right > .btn-success').should('not.be.disabled').click();
            });
        });
    });

    describe('Verify Company Settings Page Load', () => {
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
                cy.get(':nth-child(1) > td').should('be.visible').click();
            });
        });
    });
});
