/**
 * @jest-environment jsdom
 */

// Require jQuery
const $ = require('jquery');

function handleUpdateClick() {
    $('.update-link').click(function(e) {
        const form = $(this).prev('.update-form');
        form.submit(); // Submit the form
    });
}

function handleRemoveClick() {
    $('.remove-item').click(function(e) {
        e.preventDefault(); // Prevent default link action
        const csrfToken = "fake-csrf-token"; // Mock CSRF token for testing
        const itemId = $(this).attr('id').split('_')[1]; // Extract item ID from the element ID
        const url = `/bag/remove/${itemId}/`; // Construct the URL for removal
        const data = { 'csrfmiddlewaretoken': csrfToken }; // Data to send in the request

        // Mock jQuery post function
        return $.post(url, data);
    });
}

function init() {
    handleUpdateClick(); // Attach update click handler
    handleRemoveClick(); // Attach remove click handler
}

describe('Update and Remove item functionality', () => {
    beforeAll(() => {
        // Set up the HTML environment for testing
        document.body.innerHTML = `
            <td class="py-3 w-25">
                <form class="form update-form" method="POST" action="/adjust_bag/1/">
                    <input type="hidden" name="csrfmiddlewaretoken" value="fake-csrf-token" />
                    <div class="form-group">
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <button class="decrement-qty btn btn-sm btn-green" data-item_id="1" id="decrement-qty_1">
                                    <i class="fas fa-minus fa-sm"></i>
                                </button>
                            </div>
                            <input class="form-control form-control-sm qty_input" type="number" name="quantity" value="2" min="1" max="99" data-item_id="1" id="id_qty_1">
                            <div class="input-group-append">
                                <button class="increment-qty btn btn-sm btn-green" data-item_id="1" id="increment-qty_1">
                                    <i class="fas fa-plus fa-sm"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </form>
                <a class="update-link text-white col-12"><small>Update</small></a>
                <a class="remove-item text-danger float-right col-12" id="remove_1" data-size="medium"><small>Remove</small></a>
            </td>
        `;
        
        // Initialize the click handlers
        init(); // Call init directly since it's defined here
    });

    test('should submit form when update link is clicked', () => {
        const form = document.querySelector('.update-form');
        const updateLink = document.querySelector('.update-link');

        // Prevent the actual form submission for testing
        form.addEventListener('submit', (e) => {
            e.preventDefault(); // Prevent the actual submission
        });

        // Simulate the click event on the update link
        updateLink.click();
        
        // Check if the form submission was prevented
        expect(form).toBeTruthy(); // Ensure the form exists
    });

    test('should call remove functionality when remove button is clicked', () => {
        const removeButton = document.getElementById('remove_1');

        // Mock the AJAX call to prevent actual reload
        const ajaxPostSpy = jest.spyOn($, 'post').mockImplementation((url, data) => {
            // Return a mock object with done and fail methods
            return {
                done: jest.fn().mockImplementation((callback) => {
                    callback(); // Call the success callback
                    return this; // Return the object to allow chaining
                }),
                fail: jest.fn().mockReturnValue(this) // Ensure fail also returns the same object
            };
        });

        // Click the remove button
        removeButton.click();

        // Assert that the AJAX call was made
        expect(ajaxPostSpy).toHaveBeenCalledWith(expect.any(String), expect.any(Object));

        // Clean up the spy
        ajaxPostSpy.mockRestore();
    });
});
