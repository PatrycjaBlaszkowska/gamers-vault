/**
 * @jest-environment jsdom
 */

const { fireEvent } = require('@testing-library/dom');
require('@testing-library/jest-dom');

describe('Contact Form Related Order Visibility', () => {
    let queryTypeField;
    let relatedOrderContainer;

    beforeEach(() => {
        // Simulate the HTML structure where the JavaScript is embedded
        document.body.innerHTML = `
            <div class="container">
                <form method="POST" action="" class="p-4 border mt-4 mb-4">
                    <select name="query_type">
                        <option value="general">General Inquiry</option>
                        <option value="order">Order Inquiry</option>
                    </select>
                    <div id="related-order-container" style="display: none;">
                        <label for="order">Related Order:</label>
                        <input type="text" id="order" name="order">
                    </div>
                </form>
            </div>
        `;

        queryTypeField = document.querySelector('select[name="query_type"]');
        relatedOrderContainer = document.getElementById('related-order-container');

        // Manually add the event listener to simulate what happens on page load
        queryTypeField.addEventListener('change', function() {
            if (this.value === 'order') {
                relatedOrderContainer.style.display = 'block'; // Show related order field
            } else {
                relatedOrderContainer.style.display = 'none'; // Hide related order field
            }
        });
    });

    test('should show related order field when "order" is selected', () => {
        // Simulate selecting 'order'
        fireEvent.change(queryTypeField, { target: { value: 'order' } });

        // Expect related order container to be visible
        expect(relatedOrderContainer).toBeVisible();
    });

    test('should hide related order field when other option is selected', () => {
        // Set to 'order' first
        fireEvent.change(queryTypeField, { target: { value: 'order' } });
        expect(relatedOrderContainer).toBeVisible();

        // Simulate selecting 'general'
        fireEvent.change(queryTypeField, { target: { value: 'general' } });

        // Expect related order container to be hidden
        expect(relatedOrderContainer).not.toBeVisible();
    });
});
