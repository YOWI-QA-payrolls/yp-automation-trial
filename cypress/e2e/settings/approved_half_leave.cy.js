describe('login', () => {
    beforeEach(() => {
      cy.viewport(1280, 900);
      cy.fixture('credentials').then(credentials => {
        const { url, email, pass } = credentials;
        cy.visit(url);
        cy.get('#email').type(email);
        cy.get('#password').type(pass);
        cy.get('#signin-button').click();
      });
    });
  
    describe('import', () => {
      it('new features', () => {
        cy.get('#settings_list > a').click();
        cy.get('#imports > a').click();
        cy.get(':nth-child(22) > .ibox > .ibox-title').click();
        cy.wait(3000);
  
        // Button for uploading
        cy.get('[style="position:relative;"] > .btn').click();
  
        // File upload step
        const fileName = 'A_HalfDay_Leave_.csv';
        cy.fixture(fileName).then(fileContent => {
          const blob = new Blob([fileContent], { type: 'text/csv' });
          const testFile = new File([blob], fileName);
          cy.get('input[type="file"]').then(subject => {
            const el = subject[0];
            const testFile = new File([blob], fileName);
            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(testFile);
            el.files = dataTransfer.files;
            cy.wrap(subject).trigger('change', { force: true });
          });
        });

        cy.get('.actions > .pull-right').click();
        cy.get('.actions > .pull-right').click();
        
      });
    });
  });
  