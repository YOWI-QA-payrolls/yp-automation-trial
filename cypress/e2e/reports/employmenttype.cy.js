describe('Reports - Certificate of Employment', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should generate certificate of employment', () => {
        // 1. Navigate
        cy.navigateMenu(['#reports_list > [href="#"]', '#certificate_of_employment > a']);

        // 2. Wait for page loaders to finish
        cy.get('.sk-loading, .main_page_loader', { timeout: 30000 }).should('not.exist');

        // 3. Click "Show inactive" 
        cy.contains('label', 'Show inactive').find('input').click({ force: true });

        // 4. WAIT for the Employee dropdown to be ready
        cy.get('.select2-chosen', { timeout: 20000 })
          .should('not.contain', 'Please wait...');

        // 5. Open the Employee Dropdown
        cy.get('.select2-container').first().click();

        // 6. Select the first visible employee
        cy.get('.ui-select-choices-row:visible', { timeout: 15000 })
          .first()
          .find('.select2-result-label')
          .click();

        // 7. Click Search
        cy.contains('.btn', 'Search', { timeout: 15000 })
          .should('be.visible')
          .should('not.be.disabled')
          .click();

        // 8. Wait for the report generation (XHR / Loaders)
        cy.get('.sk-loading', { timeout: 30000 }).should('not.exist');

        // 9. Type into the Purpose field (FIXED)
        // Since 'Purpose' is inside the box, it's a placeholder, not a label tag.
        cy.get('input[placeholder="Purpose"]', { timeout: 15000 })
          .should('be.visible')
          .clear() // Clear in case there is default text
          .type('Testing', { delay: 50 });

        // 10. Verify typing worked
        cy.get('input[placeholder="Purpose"]').should('have.value', 'Testing');
        
        // 11. Optional: Click the Action/Download button if needed
        cy.contains('.btn', 'Action').click();
    });
});