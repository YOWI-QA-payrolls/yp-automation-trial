describe('Settings - Company Profile', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should fill in company profile information with image upload', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#profiles > a'
        ]);

        cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > ul > li:nth-child(1) > a', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('.active > .panel-body > .ibox-content > :nth-child(2) > .form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.fixture('company.png').then((fileContent) => {
            cy.get('#emp-image').then((input) => {
                const blob = Cypress.Blob.base64StringToBlob(fileContent, 'image/png');
                const file = new File([blob], 'company.png', { type: 'image/png' });
                const dataTransfer = new DataTransfer();
                dataTransfer.items.add(file);
                input[0].files = dataTransfer.files;
                cy.get('#emp-image').trigger('change', { force: true });
            });
        });

        cy.get('.form > :nth-child(2) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('company123');

        cy.get(':nth-child(4) > .form-group > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('address123');

        cy.get(':nth-child(5) > :nth-child(1) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('9200');

        cy.get('.col-sm-7 > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('0912326545678');

        cy.get(':nth-child(5) > :nth-child(2) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('testrdo');

        cy.get(':nth-child(8) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('1234567891');

        cy.get(':nth-child(9) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('123456789123');

        cy.get(':nth-child(10) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('123456789126');

        cy.get(':nth-child(11) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('123456789145');

        cy.get(':nth-child(12) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('employertest');
    });
});
