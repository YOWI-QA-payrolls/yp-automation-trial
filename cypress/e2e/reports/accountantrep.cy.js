// cypress/e2e/reports/accountantrep.cy.js

describe('Reports - Accountant Reports', () => {
  beforeEach(() => {
    cy.viewport(1280, 900);
    cy.login();
  });

  it('should view accountant report', () => {
    cy.navigateMenu(['#reports_list > [href="#"]', '#accountant_reports > a']);

    // 1. Wait for loaders to disappear
    cy.get('.sk-loading, .main_page_loader', { timeout: 30000 }).should('not.exist');

    // 2. Identify the Payroll Period group
    cy.contains('label', 'Payroll Period', { timeout: 20000 })
      .should('be.visible')
      .closest('.form-group')
      .as('payrollGroup');

    // 3. Open the dropdown
    // Added .first() here to solve the "2 elements" error
    cy.get('@payrollGroup')
      .find('.ui-select-match, .select2-choice, .select2-selection, input.select2-input, .form-control')
      .filter(':visible')
      .first() 
      .click();

    // 4. Select the first "Real" option (ignoring "Select all")
    cy.get('.ui-select-choices-row, .select2-results__option, .select2-result-selectable')
      .filter(':visible')
      .filter((index, el) => {
        const text = el.innerText.toLowerCase();
        return text.trim() !== '' && 
               !text.includes('select all') && 
               !text.includes('deselect all');
      })
      .first() // Ensures we only try to click one option
      .click({ force: true });

    // 5. Click Search
    // Added .first() just in case there are multiple search buttons on the page
    cy.contains('button', 'Search', { timeout: 20000 })
      .should('be.visible')
      .first()
      .click();

    // 6. Assert results loaded
    cy.get('tbody tr', { timeout: 30000 })
      .should('have.length.greaterThan', 0);
  });
});