/// <reference types="cypress" />

describe("Testings for other deductions in miscellaneous list", () => {
  beforeEach(() => {
    cy.visit("https://staging-yp4.yahshuasupport.com/signin/");
    cy.get('#root > div.bg-loginscreen > div.middle-box.text-center.loginscreen.wow.fadeIn.animated > div > div.logo.mb-3 > img')
      .should("be.visible");
    cy.get('input[placeholder="Email"]').type("admin_demo@gmail.com");
    cy.get('input[placeholder="Password"]').type("YP$taging30k");
    cy.contains("button", "Sign In").click();
    cy.contains("div", "Signing in...").should("be.visible");
    cy.wait(3000)

    cy.get('#page-top > div:nth-child(2) > div > div > div > div.panel-footer > div > div > button').click()
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-heading > div > div > button', { timeout: 5000 }, {force: true}).click()
  
  });

  it("Check results creating other deductions with Remittance Loan checkbox checked.", () => {
    cy.get('#settings_list').click();
    cy.wait(1000);
    cy.get('#misc_lists').click();
    cy.contains("h2", "Settings | Miscellaneous Lists").should('be.visible');
    cy.get('#App2').click();
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(7) > div.ibox-content.ng-scope > div.col-sm-2.pull-right > div > button')
      .click() // To click create other deductions
    var OtherDeductionCode = 'Automation other'
    var OtherDeductionName = 'Automation other name'
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(1) > input')
      .type(OtherDeductionCode) // To input Othe deduction code
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(2) > input')
      .type(OtherDeductionName) // To input Other deduction name
    cy.get('#is_remittance_loan').check() // To check the remittance loan checkbox
    cy.get('#is_remittance_loan').should('be.checked')
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // To save created other deductions

    cy.get('#reports_list > a').click() // To click reports module
    cy.get('#contribution_reports').click() // To click contributions report module
    cy.contains('h2', 'Contribution/Loan Reports').should('be.visible')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > nav > ul > li:nth-child(4)').click() // To click remittances loan tab
    cy.wait(5000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.row > div:nth-child(3) > div > div')
      .type(OtherDeductionName)
      .type('{enter}')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.row > div:nth-child(3) > div > div')
      .invoke('text').then((text) => {
        const actualText = text.trim(); // Remove extra whitespace and newline characters
        expect(actualText).to.equal(OtherDeductionName);
      });
    
    // To Delete created other deductions
    cy.get('#settings_list').click();
    cy.wait(1000);
    cy.get('#misc_lists').click();
    cy.contains("h2", "Settings | Miscellaneous Lists").should('be.visible');
    cy.get('#App2').click();
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(7) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > input')
      .type(OtherDeductionName)
      .type('{enter}')
    cy.get('#tableeeee > tbody > tr.hand_cursor.ng-scope > td:nth-child(2)').trigger('contextmenu') 
    cy.get('body > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(3) > a').click()
    cy.get('body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click()
  })

  it("Check results creating other deductions with Remittance Loan checkbox unchecked.", () => {
    cy.get('#settings_list').click();
    cy.wait(1000);
    cy.get('#misc_lists').click();
    cy.contains("h2", "Settings | Miscellaneous Lists").should('be.visible');
    cy.get('#App2').click();
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(7) > div.ibox-content.ng-scope > div.col-sm-2.pull-right > div > button')
      .click() // To click create other deductions
    var OtherDeductionCodes = 'Automation others'
    var OtherDeductionNames = 'Automation others name'
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(1) > input')
      .type(OtherDeductionCodes) // To input Othe deduction code
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(2) > input')
      .type(OtherDeductionNames) // To input Other deduction name
    cy.get('#is_remittance_loan').should('not.be.checked')
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // To save created other deductions

    cy.get('#reports_list > a').click() // To click reports module
    cy.get('#contribution_reports').click() // To click contributions report module
    cy.contains('h2', 'Contribution/Loan Reports').should('be.visible')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > nav > ul > li:nth-child(4)').click() // To click remittances loan tab
    cy.wait(3000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.row > div:nth-child(3) > div > div')
      .type(OtherDeductionNames)
      .type('{enter}')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.row > div:nth-child(3) > div > div')
      .invoke('text')
      .should('eq', '')
    
    // To Delete created other deductions
    cy.get('#settings_list').click();
    cy.wait(1000);
    cy.get('#misc_lists').click();
    cy.contains("h2", "Settings | Miscellaneous Lists").should('be.visible');
    cy.get('#App2').click();
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(7) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > input')
      .type(OtherDeductionNames)
      .type('{enter}')
    cy.get('#tableeeee > tbody > tr.hand_cursor.ng-scope > td:nth-child(2)').trigger('contextmenu') 
    cy.get('body > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(3) > a').click()
    cy.get('body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click()
  })


  it("Check results editing other deductions. - Check the Remittance Loan checkbox.", () => {
    cy.get('#settings_list').click();
    cy.wait(1000);
    cy.get('#misc_lists').click();
    cy.contains("h2", "Settings | Miscellaneous Lists").should('be.visible');
    cy.get('#App2').click();
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(7) > div.ibox-content.ng-scope > div.col-sm-2.pull-right > div > button')
      .click() // To click create other deductions
    var OtherDeductionCode = 'Automation others'
    var OtherDeductionName = 'Automation others name'
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(1) > input')
      .type(OtherDeductionCode) // To input Othe deduction code
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(2) > input')
      .type(OtherDeductionName) // To input Other deduction name
    cy.get('#is_remittance_loan').should('not.be.checked')
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // To save created other deductions
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(7) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > input')
    .type(OtherDeductionName)
    .type('{enter}')
    cy.get('#tableeeee > tbody > tr.hand_cursor.ng-scope > td:nth-child(2)').click()
    cy.get('#is_remittance_loan').check()
    cy.get('#is_remittance_loan').should('be.checked')
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // To save created other deductions


    

    cy.get('#reports_list > a').click() // To click reports module
    cy.get('#contribution_reports').click() // To click contributions report module
    cy.contains('h2', 'Contribution/Loan Reports').should('be.visible')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > nav > ul > li:nth-child(4)').click() // To click remittances loan tab
    cy.wait(2000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.row > div:nth-child(3) > div > div')
      .type(OtherDeductionName)
      .type('{enter}')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.row > div:nth-child(3) > div > div')
      .invoke('text').then((text) => {
        const actualText = text.trim(); // Remove extra whitespace and newline characters
        expect(actualText).to.equal(OtherDeductionName);
      });
    
    // To Delete created other deductions
    cy.get('#settings_list').click();
    cy.wait(1000);
    cy.get('#misc_lists').click();
    cy.contains("h2", "Settings | Miscellaneous Lists").should('be.visible');
    cy.get('#App2').click();
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(7) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > input')
      .type(OtherDeductionName)
      .type('{enter}')
    cy.get('#tableeeee > tbody > tr.hand_cursor.ng-scope > td:nth-child(2)').trigger('contextmenu') 
    cy.get('body > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(3) > a').click()
    cy.get('body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click()
  })

})
