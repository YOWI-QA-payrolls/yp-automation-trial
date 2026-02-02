import 'cypress-file-upload';

describe('login', () => {
    beforeEach(() => {
        cy.fixture('credentials').then(credentials => {
            const { url, email, pass } = credentials;

            cy.visit(url);
            cy.get('#email').type(email);
            cy.get('#password').type(pass);
            cy.get('#signin-button').click();
        });
    });

    describe('settings', () => {
        it.skip('profile', () => {
            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('[heading="Memo/Certificates/Agreement"] > .nav-link').click();
            cy.wait(2000);
            cy.get('.active > .panel-body > .ibox-content .form-group .btn').click();
            cy.get('[ng-if="is_seminar_training || main.is_company_attachment"] > :nth-child(1) > .form-control').type('title_testng');

            cy.wait(5000);

            cy.fixture('company.png').then((fileContent) => {
                cy.get('#attachment_transaction').then((input) => {
                    const blob = Cypress.Blob.base64StringToBlob(fileContent, 'image/png');
                    const file = new File([blob], 'company.png', { type: 'image/png' });
                    const dataTransfer = new DataTransfer();
                    dataTransfer.items.add(file);
                    input[0].files = dataTransfer.files;

                    // Trigger the 'change' event to simulate the file upload
                    cy.get('#attachment_transaction').trigger('change', { force: true });
                });
            });
        });

        // cy.get('[ng-hide="!main.is_company_attachment"]').click();
    });
}); 
