describe('login', () => {
    // This code will run before each test case in this describe block
    beforeEach(() => {
        // Load login credentials from the fixture file
        cy.fixture('credentials').then(credentials => {
            const { url, email, pass } = credentials;
 
            // Login
            cy.visit(url);
            cy.get(':nth-child(1) > .form-control').type(email);
            cy.get(':nth-child(2) > .form-control').type(pass);
            cy.get('.custom-mb').click();
        });
    });

    describe('settings', () => {
        it('customized late', () => {
            
            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('#companies_general_settings > a').click();

            cy.get(':nth-child(10) > td').click();

            cy.get(':nth-child(5) > td').click();

            // duct

            cy.get('[ng-repeat-start="(idx,record) in main.records2"][style=""] > td > .align_left > a > [ng-show="!static_key"] > .btn').click();

            cy.get('[ng-repeat-end=""][style=""] > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(1) > .input-group > .input-group-btn > .btn').click();
            cy.get('.btn-info').click();

            cy.get('[ng-repeat-end=""][style=""] > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(2) > .input-group > .input-group-btn > .btn').click();
            cy.get('.uib-datepicker-popup').contains('15').click();

            cy.get('[ng-repeat-end=""][style=""] > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(3) > .input-group > .input-group-btn > .btn').click();

            cy.get('.uib-datepicker-popup').contains('30').click();

            cy.get('[ng-repeat-end=""][style=""] > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(4) > .input-group > .input-group-btn > .btn').click();
            cy.get('.uib-datepicker-popup').contains('15').click();

            cy.get('[ng-repeat-end=""][style=""] > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(5) > .input-group > .input-group-btn > .btn').click();
            cy.get('.uib-datepicker-popup').contains('30').click();

            // cy.get('.form-group > .btn').click(); save

            // late

            cy.get(':nth-child(4) > td > .align_left > a > [ng-show="!static_key"] > .btn').click();

            cy.get(':nth-child(5) > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(1) > .input-group > .input-group-btn > .btn').click();
            cy.get('.btn-info').click();

            cy.get(':nth-child(5) > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(2) > .input-group > .input-group-btn > .btn').click();
            cy.get('.uib-datepicker-popup').contains('15').click();

            cy.get(':nth-child(5) > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(3) > .input-group > .input-group-btn > .btn').click();
            cy.get('.uib-datepicker-popup').contains('30').click();


            cy.get(':nth-child(5) > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(4) > .input-group > .input-group-btn > .btn').click();
            cy.get('.uib-datepicker-popup').contains('15').click();


            cy.get(':nth-child(5) > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(5) > .input-group > .input-group-btn > .btn').click();
            cy.get('.uib-datepicker-popup').contains('30').click();

            // cy.get('.form-group > .btn').click(); save








            // cy.get('[ng-repeat-end=""][style=""] > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(2) > .input-group > .form-control').type('05/15/2024');


 
        }); // Closing it('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')