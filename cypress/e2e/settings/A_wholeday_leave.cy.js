describe('Settings - Import Approved Whole Day Leave', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should import approved whole day leave CSV file', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#imports > a'
        ]);

        cy.get(':nth-child(24) > .ibox > .ibox-title', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('[style="position:relative;"] > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        const fileName = 'A_WholeDay_Leave.csv';
        cy.fixture(fileName).then(fileContent => {
            const blob = new Blob([fileContent], { type: 'text/csv' });
            cy.get('input[type="file"]').then(subject => {
                const el = subject[0];
                const testFile = new File([blob], fileName);
                const dataTransfer = new DataTransfer();
                dataTransfer.items.add(testFile);
                el.files = dataTransfer.files;
                cy.wrap(subject).trigger('change', { force: true });
            });
        });

        cy.get('.actions > .pull-right', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('.actions > .pull-right', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
