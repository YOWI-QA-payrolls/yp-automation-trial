describe('login', () => {
    // This code will run before each test case in this describe block
    beforeEach(() => {
        // Load login credentials from the fixture file
        cy.fixture('credentials').then(credentials => {
            const { url, email, pass } = credentials;
 
            // Login
            cy.visit(url);
            cy.get('#email').type(email);
            cy.get('#password').type(pass);
            cy.get('#signin-button').click();
        });
    });
 
    describe('settings', () => {
        it('profile', () => {
            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > ul > li:nth-child(1) > a').click();

            // Click on the button to upload an image
            cy.get('.active > .panel-body > .ibox-content > :nth-child(2) > .form-group > .btn').click();
            cy.wait(5000);

            cy.fixture('company.png').then((fileContent) => {
                cy.get('#emp-image').then((input) => {
                  const blob = Cypress.Blob.base64StringToBlob(fileContent, 'image/png');
                  const file = new File([blob], 'company.png', { type: 'image/png' });
                  const dataTransfer = new DataTransfer();
                  dataTransfer.items.add(file);
                  input[0].files = dataTransfer.files;
          
                  // Trigger the 'change' event to simulate the file upload
                  cy.get('#emp-image').trigger('change', { force: true });
                });
            });

            cy.get('.form > :nth-child(2) > .form-control').type('company123');
            cy.get(':nth-child(4) > .form-group > .form-control').type('address123');
            cy.get(':nth-child(5) > :nth-child(1) > .form-control').type('9200');
            cy.get('.col-sm-7 > .form-control').type('0912326545678');
            cy.get(':nth-child(5) > :nth-child(2) > .form-control').type('testrdo');
            // cy.get('.col-sm-7 > .form-control').type('company123');

            cy.get(':nth-child(8) > .form-control').type('1234567891');
            cy.get(':nth-child(9) > .form-control').type('123456789123');
            cy.get(':nth-child(10) > .form-control').type('123456789126');
            cy.get(':nth-child(11) > .form-control').type('123456789145');
            cy.get(':nth-child(12) > .form-control').type('employertest');

            // cy.get('.btn-success').click();

        }); // Closing it('profile') test case
    }); // Closing describe('settings')
}); // Closing describe('login')