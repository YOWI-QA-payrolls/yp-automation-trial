describe('Employee Activity', () => {
  beforeEach(() => {
    cy.viewport(1280, 900);
    cy.login();
  });

  it('should navigate to employee performance and search', () => {
    cy.intercept('GET', '**/common/popover_advance_filter/**').as('advanceFilterTpl');

    cy.navigateMenu([
      '#reports_list > a',
      '#employee_performance > a',
    ]);

    // wait for loaders
    cy.get('.sk-loading', { timeout: 30000 }).should('not.exist');
    cy.get('.main_page_loader', { timeout: 30000 }).should('not.exist');

    // type into the search input (robust)
    cy.get('input[type="search"], tabletoolstrans input.form-control, input.form-control', { timeout: 20000 })
      .filter(':visible')
      .first()
      .should('be.visible')
      .clear()
      .type('caleb');

    // open advance filter popover
    cy.get('#advance-filter-btn')
      .should('be.visible')
      .click();

    cy.wait('@advanceFilterTpl');

    // click Search in popover
    cy.get('.wrapper.modalibox', { timeout: 20000 })
      .should('be.visible')
      .within(() => {
        cy.contains('button', 'Search')
          .should('be.visible')
          .click();
      });

    // wait results
    cy.get('.sk-loading', { timeout: 30000 }).should('not.exist');
    cy.get('.main_page_loader', { timeout: 30000 }).should('not.exist');

    // ensure we have rows
    cy.get('tbody tr', { timeout: 30000 })
      .should('have.length.greaterThan', 0);

    // click the first row (or 2nd column if you prefer)
    cy.get('tbody tr')
      .first()
      .as('firstRow');

    cy.get('@firstRow')
      .should('be.visible')
      .click();


  });
});