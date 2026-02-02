/// <reference types="cypress" />

describe("Activate other setup for miscellaneous list", () => {
  beforeEach(() => {
    cy.visit("https://staging-yp4.yahshuasupport.com/signin/");
    cy.get('#root > div.bg-loginscreen > div.middle-box.text-center.loginscreen.wow.fadeIn.animated > div > div.logo.mb-3 > img')
      .should("be.visible");
    cy.get('input[placeholder="Email"]').type("admin_demo@gmail.com");
    cy.get('input[placeholder="Password"]').type("YP$taging30k");
    cy.contains("button", "Sign In").click();
    cy.contains("div", "Signing in...").should("be.visible");
    cy.wait(3000)

    // cy.get('#page-top > div:nth-child(2) > div > div > div > div.panel-footer > div > div > button').click()
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-heading > div > div > button', { timeout: 5000 }, {force: true}).click()
  });

  it("Settings setup - Check results hovering the cursor on the settings. other setup for miscellaneous list", () => {
    cy.get('#settings_list').click();
    cy.wait(1000)
    cy.get('#company_list').click();
    cy.get('#companies_general_settings').click();
    cy.contains("h2", "Company | General Settings").should('be.visible');
    cy.contains('h3', 'Other Payroll Settings').click(); // to click other payroll settings
    cy.contains('h3', 'Employee information Settings').click() // to click employee information settings
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div.row > div.col-sm-8 > div > label').trigger('mouseover'); // to hover mouse over settings
    cy.wait(1000)
    cy.contains('.tooltip-inner', 'This is a one-to-one setup of Departments, Positions, Sections, Units, and Sub-units.')
      .should('be.visible')
  })

  it("Check results clicking the checkbox and saving.", () => {
    cy.get('#settings_list').click();
    cy.wait(1000)
    cy.get('#company_list').click();
    cy.get('#companies_general_settings').click();
    cy.contains("h2", "Company | General Settings").should('be.visible');
    cy.contains('h3', 'Other Payroll Settings').click(); // to click other payroll settings
    cy.contains('h3', 'Employee information Settings').click() // to click employee information settings
    cy.wait(2000)
    cy.get('#is_activate_other_setup_misc_list').check(); // to activate settings
    cy.get('#is_activate_other_setup_misc_list').should('be.checked');
    cy.contains('button', 'Save').click() // to click save button

    cy.get('#misc_lists').click() // to click miscellaneous list module
    cy.contains('h2', 'Settings | Miscellaneous Lists').should('be.visible')

    //- The “Locations” field in the miscellaneous list  “Create Department” dialog box should be hidden.
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(2) > div.ibox-content.ng-scope > div:nth-child(3) > div')
      .should('not.exist') 
    cy.contains('span', 'Location').should('not.be.visible')
    cy.wait(1000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(2) > div.ibox-content.ng-scope > div.col-sm-1.pull-right > div > button')
      .click() // To click create button
    cy.get('h3.panel-title').should('be.visible')
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(2) > label')
      .should('not.exist') // To check the location field in "Create department" dialog.
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-heading > div > div > button').click()
    cy.wait(1000)

    // - The “Department” field in the miscellaneous list “Create Position” dialog box should be hidden.
    cy.contains('span', 'Department').should('not.be.visible')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(3) > div.ibox-content.ng-scope > div.col-sm-2.pull-right > div > button')
      .click()
    cy.get('h3.panel-title').should('be.visible')
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-heading > div > div > button').click()
    cy.wait(1000)

    // The “Departments” field in the miscellaneous list - “Create Section” dialog box should be hidden. 
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(9) > div.ibox-content.ng-scope > div:nth-child(3) > div')
      .should('not.exist')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(9) > div.ibox-content.ng-scope > div.col-sm-1.pull-right > div > button')
      .click() // To click create section 
    cy.get('h3.panel-title').should('be.visible')
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(2)')
      .should('not.exist')
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-white').click() // To close dialog box

    // The “Section” field in the miscellaneous list - “Create Unit” dialog box should be hidden. 
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(10) > div.ibox-content.ng-scope > div:nth-child(3) > div')
      .should('not.exist') // To check if the Section field is not visible
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(10) > div.ibox-content.ng-scope > div.col-sm-1.pull-right > div > button')
      .click() // To click create unit 
    cy.get('h3.panel-title').should('be.visible')
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(2)')
      .should('not.exist')
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-white').click() // To close dialog box


    // The “Unit” field in the miscellaneous list - “Create Sub Unit” dialog box should be hidden. 
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(11) > div.ibox-content.ng-scope > div.col-sm-2.pull-right > div > button')
      .click() // To click create sub unit 
    cy.get('h3.panel-title').should('be.visible')
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(2)')
      .should('not.exist')
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-white').click() // To close dialog box

    // Creation of Payroll (Location & Department) should have no restriction

    // SETUP for payroll location and department field testing.
    // To create new Location and Department
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(5) > div.ibox-content.ng-scope > div.col-sm-2.pull-right > div > button').click()
    // Set a string in an alias to create a new location and department
    var NewLocation = "Location Automation"
    var NewDepartment = "Department Automation"

    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div > input').type(NewLocation)
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success').click() // To click save and create the new Location
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(2) > div.ibox-content.ng-scope > div.col-sm-1.pull-right > div > button').click()
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(1) > input').type(NewDepartment)
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button').click() // To click save and create the new Department

    // cy.get('#payroll_default > a > span').click() // To click the payroll module 
    // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > div > label').should('be.visible')
    // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.btn-group.pull-right > button').click() // To click create payroll
    // cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-heading > h3 > span').should('be.visible')
    // cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div.form-group > div > a > span.select2-chosen.ng-binding').click() // To click payroll schedule
    // cy.contains('#ui-select-choices-row-3- > div > div', 'Quincenal').click()
    // cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(3) > div > ul > li > input').type('Automation location')
    // cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(6) > div > ul > li > input').click() // To click the department field.

    // User > Accounts > Create (Location and department) should have no restriction
    cy.get('#users_list').click() // To click the Users module
    cy.get('#accounts').click() // To click the Accounts module
    cy.contains('h2', 'Users').should('be.visible')
    cy.wait(2000)
    cy.contains('button', 'Create').click() // To click the create new user button
    cy.wait(2000)
    cy.contains('h3', 'Create/Edit Account').should('be.visible')
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(6) > div > ul > li > input')
      .type(NewLocation)
      .type('{enter}')
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(8) > div > div > ul > li > input')
      .type(NewDepartment)
      .type('{enter}')
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(8) > div > div > ul')
      .invoke('text')
      .should('eq', NewDepartment + ' ');
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-white').click() // To close the create new user dialog box

// To delete the created setup (Department and Location)

    cy.get('#settings_list').click()
    cy.get('#misc_lists').click() // to click miscellaneous list module
    cy.contains('h2', 'Settings | Miscellaneous Lists').should('be.visible')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(2) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > input')
      .type(NewDepartment)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(2) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > div > div > button')
      .click()
    cy.get('#tableee > tbody > tr.hand_cursor.ng-scope > td')
      .trigger('contextmenu');
    cy.get('body > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(3) > a').click() // To click delete
    cy.get('body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click() // To click delete confirmation button

    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(5) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > input')
      .type(NewLocation)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(5) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > div > div > button > i')
      .click()
    cy.get('#tableeee > tbody > tr.hand_cursor.ng-scope > td').trigger('contextmenu');
    cy.get('body > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(3) > a').click()
    cy.get('body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click() // To click delete confirmation button

    })

  it("Check results creating a duplicate name of department in the miscellaneous settings.", () => {
    cy.get('#settings_list').click()
    cy.get('#misc_lists').click() // to click miscellaneous list module
    cy.contains('h2', 'Settings | Miscellaneous Lists').should('be.visible')
    var NewDepartment = "Department Automation"
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(2) > div.ibox-content.ng-scope > div.col-sm-1.pull-right > div > button').click()
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(1) > input').type(NewDepartment)
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button').click() // To click save and create the new Department
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(2) > div.ibox-content.ng-scope > div.col-sm-1.pull-right > div > button').click()
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(1) > input').type(NewDepartment)
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button').click() // To click save and create the new Department
    cy.contains('div', 'This Department already exists.').should('be.visible')

    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > div').click() // To close the create department dialog box
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(2) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > input')
      .type(NewDepartment)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(2) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > div > div > button')
      .click()
    cy.get('#tableee > tbody > tr.hand_cursor.ng-scope > td')
      .trigger('contextmenu');
    cy.get('body > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(3) > a').click() // To click delete
    cy.get('body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click() // To click delete confirmation button


  })

  it("Check results creating a duplicate name of position in the miscellaneous settings.", () => {
    cy.get('#settings_list').click()
    cy.get('#misc_lists').click() // to click miscellaneous list module
    cy.contains('h2', 'Settings | Miscellaneous Lists').should('be.visible')
    var NewPosition = "Position Automation"
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(3) > div.ibox-content.ng-scope > div.col-sm-2.pull-right > div > button').click()
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(1) > input').type(NewPosition)
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success').click() // To click save and create the new Position
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(3) > div.ibox-content.ng-scope > div.col-sm-2.pull-right > div > button').click()
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(1) > input').type(NewPosition)
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success').click() // To click save and create the new Position
    cy.contains('div', 'This Position already exists.').should('be.visible')
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-white').click() // To close the position dialog box
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(3) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > input')
      .type(NewPosition);
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(3) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > div > div > button')
      .click()
    cy.get('#tablee > tbody > tr.hand_cursor.ng-scope > td')
      .trigger('contextmenu');
    cy.get('body > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(3) > a').click()
    cy.get('body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click()
  })

  it("Check results creating a new “Department” in the miscellaneous settings.", () => {
    cy.get('#settings_list').click()
    cy.get('#misc_lists').click() // to click miscellaneous list module
    cy.contains('h2', 'Settings | Miscellaneous Lists').should('be.visible')
    var NewDepartment = "Department Automation"
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(2) > div.ibox-content.ng-scope > div.col-sm-1.pull-right > div > button').click()
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(1) > input').type(NewDepartment)
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button').click() // To click save and create the new Department
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(2) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > input')
      .type(NewDepartment)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(2) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > div > div > button')
      .click()
    cy.get('#tableee > tbody > tr.hand_cursor.ng-scope > td > div > small').should('be.visible') // To check if the date created is visible
    cy.get('#tableee > tbody > tr.hand_cursor.ng-scope > td')
      .trigger('contextmenu');
    cy.get('body > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(3) > a').click() // To click delete
    cy.get('body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click() // To click delete confirmation button
  })

  it("Check results creating a new “Position” in the miscellaneous settings.", () => {
    cy.get('#settings_list').click()
    cy.get('#misc_lists').click() // to click miscellaneous list module
    cy.contains('h2', 'Settings | Miscellaneous Lists').should('be.visible')
    var NewPosition = "Position Automation"
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(3) > div.ibox-content.ng-scope > div.col-sm-2.pull-right > div > button').click()
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(1) > input').type(NewPosition)
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success').click() // To click save and create the new Position
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(3) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > input')
      .type(NewPosition) // To search create position
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(3) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > div > div > button > i')
      .click() // To click search button
    cy.get('#tablee > tbody > tr.hand_cursor.ng-scope > td > div > small').should('be.visible') // To check if the date created is visible
    cy.get('#tableee > tbody > tr.hand_cursor.ng-scope > td')
      .trigger('contextmenu');
    cy.get('body > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(3) > a').click() // To click delete
    cy.get('body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click() // To click delete confirmation button
  })

  it("Check results creating a new “Location” in the miscellaneous settings.", () => {
    cy.get('#settings_list').click()
    cy.get('#misc_lists').click() // to click miscellaneous list module
    cy.contains('h2', 'Settings | Miscellaneous Lists').should('be.visible')
    var NewLocation = "Location Automation"
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(5) > div.ibox-content.ng-scope > div.col-sm-2.pull-right > div > button').click()
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div > input').type(NewLocation)
    cy.get('body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success').click() // To click save and create the new Location
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(5) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > input')
      .type(NewLocation) // To search create Location
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div:nth-child(5) > div.ibox-content.ng-scope > div.col-sm-4.pull-right > tabletoolstrans > div > div > div > button')
      .click() // To click search button
    cy.get('#tableeee > tbody > tr.hand_cursor.ng-scope > td > div > small').should('be.visible') // To check if the date created is visible
    cy.get('#tableeee > tbody > tr.hand_cursor.ng-scope')
      .trigger('contextmenu');
    cy.get('body > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(3) > a').click() // To click delete
    cy.get('body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click() // To click delete confirmation button
  })
})
