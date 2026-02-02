/// <reference types="cypress" />

describe("Basic pay testcases", () => {
  beforeEach(() => {
    cy.dmpilogin("admin_dmpi@ypo.com", "DMPI$taging30k")
  });

  it("Check results opening/refreshing the page after creating a template.", () => {
    cy.get('#dmpi_reports_list').click(); // Click DMPI reports list
    cy.wait(1000)
    cy.get('#monthlies_list').click(); // Click monthlies reports list
    cy.get('#compensation_items').click(); // Click the compensation module
    cy.contains("h2", "DMPI Reports | Compensation Items").should('be.visible'); // Check if we are in the compensation module
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button')
      .click() // Click the advance filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span > div.ng-scope > div:nth-child(2) > div > div > a > span:nth-child(2)')
      .click() // Click the Rate status dropdown
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span > div.ng-scope > div:nth-child(2) > div > div > div > div > input')
      .type('Hourlies')
      .type('{enter}')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span > div.col-xs-12 > button.btn.btn-sm.btn-success.ng-scope')
      .click() // Click the "Save as template button"
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > fieldset > input[type=text]').type('Automation template')
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > div.sa-button-container > button.confirm').click()
    cy.wait(1000)
    cy.get('#page-top > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click() // Click Ok in confirmation dialog
    cy.wait(3000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button')
      .click() // Click the advance filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span > div.ng-scope > div:nth-child(1) > div > div')
      .click() // Click the Filter templates dropdown.
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span > div.ng-scope > div:nth-child(1) > div > div > div > div > input')
      .type('Automation template')
      .type('{enter}')
    cy.get('#ui-select-choices-row-13- > div > span.ng-binding.ng-scope > span').invoke('text')
      .then((text) =>{
        console.log(text)
      })
  })

  it("Check results creating a template.", () => {
    cy.get('#dmpi_reports_list').click(); // Click DMPI reports list
    cy.wait(1000)
    cy.get('#monthlies_list').click(); // Click monthlies reports list
    cy.get('#compensation_items').click(); // Click the compensation module
    cy.contains("h2", "DMPI Reports | Compensation Items").should('be.visible'); // Check if we are in the compensation module
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button')
      .click() // Click the advance filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span > div.ng-scope > div:nth-child(2) > div > div > a > span:nth-child(2)')
      .click() // Click the Rate status dropdown
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span > div.ng-scope > div:nth-child(2) > div > div > div > div > input')
      .type('Hourlies')
      .type('{enter}')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span > div.col-xs-12 > button.btn.btn-sm.btn-success.ng-scope')
      .click() // Click the "Save as template button"
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > fieldset > input[type=text]').type('Automation template')
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > div.sa-button-container > button.confirm').click()
    cy.wait(1000)
    cy.get('#page-top > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click() // Click Ok in confirmation dialog
    cy.wait(3000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button')
      .click() // Click the advance filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span > div.ng-scope > div:nth-child(1) > div > div')
      .click() // Click the Filter templates dropdown.
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span > div.ng-scope > div:nth-child(1) > div > div > div > div > input')
      .type('Automation template')
      .type('{enter}')
    cy.get('#ui-select-choices-row-13- > div > span.ng-binding.ng-scope > span').invoke('text')
      .then((text) =>{
        console.log(text)
      })
  })

  it("Check results clicking the “Save as template button” without changing the other fields.", () => {
    cy.get('#dmpi_reports_list').click(); // Click DMPI reports list
    cy.wait(1000)
    cy.get('#monthlies_list').click(); // Click monthlies reports list
    cy.get('#compensation_items').click(); // Click the compensation module
    cy.contains("h2", "DMPI Reports | Compensation Items").should('be.visible'); // Check if we are in the compensation module
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button')
      .click() // Click the advance filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span > div.col-xs-12 > button.btn.btn-sm.btn-success.ng-scope')
      .click() // Click the "Save as template button"
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > fieldset > input[type=text]').type('Automation template')
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > div.sa-button-container > button.confirm').click()
    cy.wait(1000)
    cy.get('#page-top > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click() // Click Ok in confirmation dialog
    cy.wait(3000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button')
      .click() // Click the advance filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span > div.ng-scope > div:nth-child(1) > div > div')
      .click() // Click the Filter templates dropdown.
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span > div.ng-scope > div:nth-child(1) > div > div > div > div > input')
      .type('Automation template')
      .type('{enter}')
    cy.get('#ui-select-choices-row-13- > div > span.ng-binding.ng-scope > span').invoke('text')
      .then((text) =>{
        console.log(text)
      })
  })

})
