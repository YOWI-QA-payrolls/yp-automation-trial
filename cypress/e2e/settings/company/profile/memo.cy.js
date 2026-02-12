describe('Settings - Company Profile - Memo/Certificates/Agreement', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should create a memo with title and file attachment', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#profiles > a'
        ]);

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('[heading="Memo/Certificates/Agreement"] > .nav-link', { timeout: 10000 })
            .should('be.visible')
            .click({ force: true });

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('.active > .panel-body > .ibox-content .form-group .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('[ng-if="is_seminar_training || main.is_company_attachment"] > :nth-child(1) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('title_testng');

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.fixture('company.png').then((fileContent) => {
            cy.get('#attachment_transaction').then((input) => {
                const blob = Cypress.Blob.base64StringToBlob(fileContent, 'image/png');
                const file = new File([blob], 'company.png', { type: 'image/png' });
                const dataTransfer = new DataTransfer();
                dataTransfer.items.add(file);
                input[0].files = dataTransfer.files;
                cy.get('#attachment_transaction').trigger('change', { force: true });
            });
        });
    });
});
