import './commands';

// Hide chat widget that overlaps test elements
beforeEach(() => {
    cy.on('window:before:load', (win) => {
        const style = win.document.createElement('style');
        style.innerHTML = '.abba-widget-bubble, .abba-widget-container { display: none !important; }';
        win.document.head.appendChild(style);
    });
});
