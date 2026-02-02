/// <reference types="cypress" />

describe("Self-Service Setup Phase 1", () => {
  beforeEach(() => {
    cy.visit("https://staging-yp.yahshuasupport.com/wizard/first-phase/");
    cy.get('img[src="/static_cdn/new-ui/img/yplogin.png"]').should("be.visible");
    cy.get('input[placeholder="Email"]').type("qa.automation@gmail.com");
    cy.get('input[placeholder="Password"]').type("Qa_12345");
    cy.contains("button", "Sign In").click();
    cy.contains("div", "Signing In...").should("be.visible");
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
  });

  it.skip("Check response after clicking sign - in", () => {
    cy.visit("https://staging-yp.yahshuasupport.com/wizard/first-phase/");
    cy.get('img[src="/static_cdn/new-ui/img/yplogin.png"]').should("be.visible");
    cy.get('input[placeholder="Email"]').type("qa.automation@gmail.com");
    cy.get('input[placeholder="Password"]').type("Qa_12345");
    cy.contains("button", "Sign In").click();
    cy.contains("div", "Logging In...").should("be.visible");
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
  });

  it.skip("Check response when clicking “Be right back” button", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('a', 'Be right back')
      .should('be.visible')
      .click()
      cy.get('img[src="/static_cdn/new-ui/img/yplogin.png"]').should("be.visible");
  });

  it.skip("Check response when clicking “Im ready!” button", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');
  });

  it.skip("Check response when clicking “Add Location” button without inputted location name", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');
    cy.contains('div', 'Add Location')
      .should('be.visible')
      .click()
    cy.contains('div', 'Please enter Location.').should('be.visible');
  });

  it.skip("Check response when clicking “Add Location” button with inputted location name", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');
    cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
      .type('test')
    cy.contains('div', 'Add Location')
      .should('be.visible')
      .click()
  });

  it.skip("Check response when adding duplicate location name", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');
    cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
      .type('test')
    cy.contains('div', 'Add Location')
      .should('be.visible')
      .click()
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
      .type('test')
    cy.contains('div', 'Add Location')
      .should('be.visible')
      .click()
    cy.get('#toast-container > div > div > div > div.toast-title').should('be.visible');
  });

  it.skip("Check response when clicking “Edit” button", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');
    cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
      .type('test')
    cy.contains('div', 'Add Location')
      .should('be.visible')
      .click()
    cy.get('#tableeee > tbody > tr:nth-child(3) > td:nth-child(2) > button.btn.btn-md.btn-success.btn-outline > i').click()
  });

  it.skip("Check response when clicking “Delete” button and clicking “Cancel” button", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');
    cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
      .type('test')
    cy.contains('div', 'Add Location')
      .should('be.visible')
      .click()
    cy.get('#tableeee > tbody > tr:nth-child(3) > td:nth-child(2) > button.btn.btn-md.btn-danger.btn-outline.ng-scope').click()
    cy.contains('h2', 'Are you sure you want to delete the data?').should('be.visible')
    cy.get('#page-top > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.cancel')
      .click()
    cy.get('#tableeee > tbody > tr:nth-child(3) > td.ng-binding').invoke('text').then((text) => {
      expect(text).to.equal('test');
    });
    
  });

  it.skip("Check response when clicking “Delete” button and clicking “Yes” button", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');
    cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
      .type('test')
    cy.contains('div', 'Add Location')
      .should('be.visible')
      .click()
    cy.get('#tableeee > tbody > tr:nth-child(3) > td:nth-child(2) > button.btn.btn-md.btn-danger.btn-outline.ng-scope').click()
    cy.contains('h2', 'Are you sure you want to delete the data?').should('be.visible')
    cy.get('#page-top > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm')
      .click()
    // wrong success message compared to blueprint
  });

  it.skip("Check response when clicking Download Template", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');
    cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(1) > div:nth-child(2) > span > a').click()
    cy.checkFileExists('\Users\Ej\Downloads\Settings - Locations.csv').should('eq', true); // File not found
    });

  it.skip("Check response when clicking the next button in the pagination", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');

    function performActionNTimes(count) {
      if (count <= 0) {
        return; // Exit the recursion
      }
      // Perform your action here
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
        .type('test' + count)
      cy.contains('div', 'Add Location')
          .should('be.visible')
          .click()
      // Call the function recursively with the reduced count
      performActionNTimes(count - 1);
    }
    performActionNTimes(5); // Perform the action 5 times
    
    cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > div > ul > li.pagination-next.ng-scope > a').click();
    cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > div > ul > li.pagination-next.ng-scope > a').should('not.be.enabled');
    });

  it.skip("Check response when clicking the back button in the pagination", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');

    function performActionNTimes(count) {
      if (count <= 0) {
        return; // Exit the recursion
      }
      // Perform your action here
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
        .type('test' + count)
      cy.contains('div', 'Add Location')
          .should('be.visible')
          .click()
      // Call the function recursively with the reduced count
      performActionNTimes(count - 1);
    }
    performActionNTimes(5); // Perform the action 5 times
    
    cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > div > ul > li.pagination-next.ng-scope > a').click();
    cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > div > ul > li.pagination-prev.ng-scope > a').click()
    cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > div > ul > li.pagination-prev.ng-scope > a').should('not.be.enabled');
    });


    it.skip("Check response when clicking “Record per Page” selection box", () => {
      cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
      cy.contains('button', "I'm Ready!")
        .should('be.visible')
        .click()
      cy.contains('h1','Phase I | Location').should('be.visible');

      cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > span.col-sm-1.pull-right > div').click()
      cy.get('#ui-select-choices-row-0- > a > div').should('be.visible')
      });


  it.skip("Check response when selecting “10” in the Record per page", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');

    function performActionNTimes(count) {
      if (count <= 0) {
        return; // Exit the recursion
      }
      // Perform your action here
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
        .type('test' + count)
      cy.contains('div', 'Add Location')
          .should('be.visible')
          .click()
      // Call the function recursively with the reduced count
      performActionNTimes(count - 1);
    }
    performActionNTimes(5); // Perform the action 5 times

    cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > span.col-sm-1.pull-right > div').click()
    cy.get('#ui-select-choices-row-0- > a > div').eq(1).click()
    cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > span.col-sm-1.pull-right > div > div > span > span.ui-select-match-text.pull-left > span').invoke('text').should('eq', '10')
    });

  it.skip("Check response when clicking “Next” button (currently in the Location page)", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');
    cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click()
    cy.contains('h1', 'Phase I | Department').should('be.visible');
    });

  it.skip("Check response when clicking “Location” selection box - Department Set up", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');
    cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
      .type('test location')
    cy.contains('div', 'Add Location')
      .should('be.visible')
      .click()
    cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click()
    cy.contains('h1', 'Phase I | Department').should('be.visible');
    cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > div > div > ul > li > input').click()
    cy.get('#ui-select-choices-row-1- > div > div').eq(2).invoke('text').should('eq', 'test location')
    });

    it.skip("Check response when clicking “Select All” button - Department Set up", () => {
      cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
      cy.contains('button', "I'm Ready!")
        .should('be.visible')
        .click()
      cy.contains('h1','Phase I | Location').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
        .type('test location')
      cy.contains('div', 'Add Location')
        .should('be.visible')
        .click()
      cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click()
      cy.contains('h1', 'Phase I | Department').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > button:nth-child(5)').click()
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > div > div > ul > span > li:nth-child(1) > span > span').should('be.visible')
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > div > div > ul > span > li:nth-child(3) > span > span').should('be.visible')
      });  

    it.skip("Check response when clicking “Deselect All” button - Department Set up", () => {
      cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
      cy.contains('button', "I'm Ready!")
        .should('be.visible')
        .click()
      cy.contains('h1','Phase I | Location').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
        .type('test location')
      cy.contains('div', 'Add Location')
        .should('be.visible')
        .click()
      cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click() // To click next going to department setup
      cy.contains('h1', 'Phase I | Department').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > button:nth-child(5)').click()
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > div > div > ul > span > li:nth-child(1) > span > span').should('be.visible')
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > div > div > ul > span > li:nth-child(3) > span > span').should('be.visible')
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > button:nth-child(6)').click()
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > div > div > ul > span > li:nth-child(1) > span > span').should('not.exist')
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > div > div > ul > span > li:nth-child(3) > span > span').should('not.exist')
      });  


  it.skip("Check response when clicking “Edit” button - Department Set up", () => {
    cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
    cy.contains('button', "I'm Ready!")
      .should('be.visible')
      .click()
    cy.contains('h1','Phase I | Location').should('be.visible');
    cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
        .type('test location')
      cy.contains('div', 'Add Location').click()
      cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click() // To click next going to department setup
      cy.contains('h1', 'Phase I | Department').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(1) > input') //To type in Name field
          .type('Test department')
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > div > div > ul > li > input')
          .click()
      cy.get('#ui-select-choices-row-1- > div')
          .eq(2).click()
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-2 > button')
          .click()
      cy.get('#tableeee > tbody > tr:nth-child(2) > td:nth-child(3) > button.btn.btn-md.btn-success.btn-outline').click() //to click edit button
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(1) > input').invoke('val').should('eq', 'Test department')//To check field
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > div > div > ul > span > li > span > span').invoke('text').should('eq', 'test location')
    });

    it.skip("Check response when clicking “Delete” button and clicking “Cancel” button - Department Set up", () => {
      cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
      cy.contains('button', "I'm Ready!")
        .should('be.visible')
        .click()
      cy.contains('h1','Phase I | Location').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-4 > input')
          .type('test location')
        cy.contains('div', 'Add Location').click()
        cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click() // To click next going to department setup
        cy.contains('h1', 'Phase I | Department').should('be.visible');
        cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(1) > input') //To type in Name field
            .type('Test department')
        cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > div > div > ul > li > input')
            .click()
        cy.get('#ui-select-choices-row-1- > div')
            .eq(2).click()
        cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-2 > button')
            .click() // To click save button
        cy.get('#tableeee > tbody > tr:nth-child(2) > td:nth-child(3) > button.btn.btn-md.btn-danger.btn-outline.ng-scope').click() // To click delete button
        cy.get('#page-top > div.sweet-alert.showSweetAlert.visible').should('be.visible')
        cy.contains('button', 'Cancel').click()
        cy.get('#page-top > div.sweet-alert.showSweetAlert.visible').should('not.be.visible') //Not working
      });

    it.skip("Check response when clicking “Next” button (currently in the Department page) - Department Set up", () => {
      cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
      cy.contains('button', "I'm Ready!")
        .should('be.visible')
        .click()
      cy.contains('h1','Phase I | Location').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click() // To click next going to department setup
      cy.contains('h1', 'Phase I | Department').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click()
      cy.contains('h1', 'Phase I | Position').should('be.visible');
      });

    it.skip("Check response when clicking the back button in the pagination (Department Page) - Department Set up", () => {
      cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
      cy.contains('button', "I'm Ready!")
        .should('be.visible')
        .click()
      cy.contains('h1','Phase I | Location').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click() // To click next going to department setup
      cy.contains('h1', 'Phase I | Department').should('be.visible');
      function performActionNTimes(count) {
        if (count <= 0) {
          return; // Exit the recursion
        }
        // Perform your action here
        cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(1) > input')
          .type('test' + count)
        cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > button:nth-child(5)')
            .click()
        cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-2 > button').click()
        // Call the function recursively with the reduced count
        performActionNTimes(count - 1);
      }
      performActionNTimes(5); // Perform the action 5 times

      cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > div > ul > li.pagination-next.ng-scope > a').click() // To click next button(Pagination)
      cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > div > ul > li.pagination-prev.ng-scope > a').click(); // To click prev button(Pagination)
      cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > div > ul > li.pagination-prev.ng-scope > a').should('not.be.enabled');
      });

    it.skip("Check response when clicking the next button in the pagination (Department Page) - Department Set up", () => {
      cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
      cy.contains('button', "I'm Ready!")
        .should('be.visible')
        .click()
      cy.contains('h1','Phase I | Location').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click() // To click next going to department setup
      cy.contains('h1', 'Phase I | Department').should('be.visible');
      function performActionNTimes(count) {
        if (count <= 0) {
          return; // Exit the recursion
        }
        // Perform your action here
        cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(1) > input')
          .type('test' + count)
        cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > button:nth-child(5)')
            .click()
        cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div.col-sm-2 > button').click()
        // Call the function recursively with the reduced count
        performActionNTimes(count - 1);
      }
      performActionNTimes(5); // Perform the action 5 times

      cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > div > ul > li.pagination-next.ng-scope > a').click() // To click next button(Pagination)
      cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > div > ul > li.pagination-next.ng-scope > a').should('not.be.enabled');
      });

    it.skip("Check response when clicking “Record per Page” selection box (Department Page) - Department Set up", () => {
      cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
      cy.contains('button', "I'm Ready!")
        .should('be.visible')
        .click()
      cy.contains('h1','Phase I | Location').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click() // To click next going to department setup
      cy.contains('h1', 'Phase I | Department').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > span.col-sm-1.pull-right > div').click()
      cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > span.col-sm-1.pull-right > div > ul').should('be.visible')
      });

    it.skip(" Check response when selecting “10” in the Record per page - Department Set up", () => {
      cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
      cy.contains('button', "I'm Ready!")
        .should('be.visible')
        .click()
      cy.contains('h1','Phase I | Location').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click() // To click next going to department setup
      cy.contains('h1', 'Phase I | Department').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > span.col-sm-1.pull-right > div').click()
      cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > span.col-sm-1.pull-right > div > ul').should('be.visible')
      cy.get('#ui-select-choices-row-2- > a > div').eq(1).click()
      cy.get('#page-wrapper > div > div > div > div:nth-child(2) > div > div.row > div > span.col-sm-1.pull-right > div > div > span > span.ui-select-match-text.pull-left > span').invoke('text').should('eq', '10')
      });

    it(" Check response when clicking “Department” selection box - Position Set up", () => {
      cy.contains('h1', 'WELCOME TO YAHSHUA').should('be.visible');
      cy.contains('button', "I'm Ready!")
        .should('be.visible')
        .click()
      cy.contains('h1','Phase I | Location').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click() // To click next going to department setup
      cy.contains('h1', 'Phase I | Department').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div.footer > div > div > div:nth-child(2) > button').click() // To click next going to position setup
      cy.contains('h1', 'Phase I | Position').should('be.visible');
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > div > div > ul > li > input').click()
      cy.get('#page-wrapper > div > div > div > div:nth-child(1) > div > div.row > div:nth-child(4) > div:nth-child(3) > div > div > div > ul')
        .should('be.visible')
      });


    // yes me


  });
