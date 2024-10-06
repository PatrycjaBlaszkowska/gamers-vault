/**
 * @jest-environment jsdom
 */

const $ = require('jquery');

// The jQuery function to handle file selection
function setupFileInputHandler() {
    $('#id_image').change(function() {
        const file = this.files[0]; // Get the selected file
        if (file) {
            $('#filename').text(`Image will be set to: ${file.name}`); // Update filename display
        } else {
            $('#filename').text('No file selected'); // Default text if no file
        }
    });
}

// Quantity input handler
function setupQuantityHandlers() {
    // Disable +/- buttons outside 1-99 range
    function handleEnableDisable(itemId) {
        const currentValue = parseInt($(`#id_qty_${itemId}`).val());
        const minusDisabled = currentValue <= 1; // Changed from < 2 to <= 1
        const plusDisabled = currentValue >= 99; // Changed from > 98 to >= 99
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }

    // Ensure proper enabling/disabling of all inputs on page load
    const allQtyInputs = $('.qty_input');
    for (let i = 0; i < allQtyInputs.length; i++) {
        const itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function () {
        const itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Increment quantity
    $('.increment-qty').click(function (e) {
        e.preventDefault();
        const closestInput = $(this).closest('.input-group').find('.qty_input')[0];
        const currentValue = parseInt($(closestInput).val());
        
        if (currentValue < 99) { // Ensure we do not exceed 99
            $(closestInput).val(currentValue + 1);
            const itemId = $(this).data('item_id');
            handleEnableDisable(itemId);
        }
    });

    // Decrement quantity
    $('.decrement-qty').click(function (e) {
        e.preventDefault();
        const closestInput = $(this).closest('.input-group').find('.qty_input')[0];
        const currentValue = parseInt($(closestInput).val());

        if (currentValue > 1) { // Ensure we do not go below 1
            $(closestInput).val(currentValue - 1);
            const itemId = $(this).data('item_id');
            handleEnableDisable(itemId);
        }
    });
}

// Sort Selector Handler
function setupSortSelectorHandler() {
    $('#sort-selector').change(function() {
        const selector = $(this);
        const currentUrl = new URL(window.location.href);
        const selectedVal = selector.val();
        
        if (selectedVal !== "reset") {
            const [sort, direction] = selectedVal.split("_");
            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);
            window.location.replace(currentUrl); 
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");
            window.location.replace(currentUrl); 
        }
    });
}

// Jest tests for the image file input functionality
describe('Image File Input', () => {
    beforeAll(() => {
        // Set up the HTML environment for testing
        document.body.innerHTML = `
            <input type="file" id="id_image" />
            <span id="filename" class="text-muted">No file selected</span>
        `;
        
        // Initialize the change event
        setupFileInputHandler(); // Call this function to set up the event handler
    });

    test('should update filename when a file is selected', () => {
        // Create a fake File object
        const file = new File([''], 'test-image.jpg', { type: 'image/jpeg' });

        // Set the input's files property to the fake file
        const input = document.getElementById('id_image');
        Object.defineProperty(input, 'files', {
            value: [file],
            writable: false, // Make it non-writable
        });

        // Trigger the change event
        $(input).change(); // jQuery change event

        // Assert that the filename is updated correctly
        expect($('#filename').text()).toBe('Image will be set to: test-image.jpg');
    });
});

// Jest tests for the quantity input functionality
describe('Quantity Input Functionality', () => {
    beforeEach(() => {
        // Set up the HTML environment for testing
        document.body.innerHTML = `
            <div class="input-group">
                <div class="input-group-prepend">
                    <button class="decrement-qty btn btn-green" data-item_id="1" id="decrement-qty_1" disabled>
                        <span class="icon"><i class="fas fa-minus"></i></span>
                    </button>
                </div>
                <input class="form-control qty_input" type="number" name="quantity" value="1" min="1" max="99" data-item_id="1" id="id_qty_1">
                <div class="input-group-append">
                    <button class="increment-qty btn btn-green" data-item_id="1" id="increment-qty_1">
                        <span class="icon"><i class="fas fa-plus"></i></span>
                    </button>
                </div>
            </div>
        `;

        // Initialize the quantity handlers
        setupQuantityHandlers();
    });

    test('should disable decrement button when quantity is 1', () => {
        const decrementButton = $('#decrement-qty_1');
        const quantityInput = $('#id_qty_1');
        expect(decrementButton.prop('disabled')).toBe(true);
        
        // Change the input to 2 and check again
        quantityInput.val(2).change(); // Trigger change event
        expect(decrementButton.prop('disabled')).toBe(false);
    });

    test('should disable increment button when quantity is 99', () => {
        const incrementButton = $('#increment-qty_1');
        const quantityInput = $('#id_qty_1');
        expect(incrementButton.prop('disabled')).toBe(false); // Initially enabled
        
        // Set input to 99 and check again
        quantityInput.val(99).change(); // Trigger change event
        expect(incrementButton.prop('disabled')).toBe(true); // Should be disabled now
    });

    test('should increment the quantity when the increment button is clicked', () => {
        const incrementButton = $('#increment-qty_1');
        const quantityInput = $('#id_qty_1');

        // Simulate click
        incrementButton.click(); 
        expect(quantityInput.val()).toBe('2'); // Check if value has incremented
    });

    test('should decrement the quantity when the decrement button is clicked', () => {
        const decrementButton = $('#decrement-qty_1');
        const quantityInput = $('#id_qty_1');

        // First increment to 2
        $('#increment-qty_1').click();
        
        decrementButton.click(); // Simulate click
        expect(quantityInput.val()).toBe('1'); // Check if value has decremented
    });

    test('should not go below 1 when decrementing', () => {
        const decrementButton = $('#decrement-qty_1');
        const quantityInput = $('#id_qty_1');

        decrementButton.click(); // Simulate click
        expect(quantityInput.val()).toBe('1'); // Check if still 1
    });

    test('should not go above 99 when incrementing', () => {
        const incrementButton = $('#increment-qty_1');
        const quantityInput = $('#id_qty_1');

        // Set to 99
        quantityInput.val(99).change();
        incrementButton.click(); // Simulate click
        expect(quantityInput.val()).toBe('99'); // Check if still 99
    });
});

// Jest tests for the selector functionality
describe('Sort Selector Functionality', () => {
    beforeAll(() => {
        // Set up the HTML environment for testing
        document.body.innerHTML = `
            <div class="col-12 col-md-6 my-auto order-md-last d-flex justify-content-center justify-content-md-end">
                <div class="sort-select-wrapper w-50">
                    <select id="sort-selector" class="custom-select custom-select-sm rounded-0 border black">
                        <option value="reset" selected>Sort by...</option>
                        <option value="price_asc">Price (low to high)</option>
                        <option value="price_desc">Price (high to low)</option>
                        <option value="rating_asc">Rating (low to high)</option>
                        <option value="rating_desc">Rating (high to low)</option>
                        <option value="name_asc">Name (A-Z)</option>
                        <option value="name_desc">Name (Z-A)</option>
                        <option value="category_asc">Category (A-Z)</option>
                        <option value="category_desc">Category (Z-A)</option>
                    </select>
                </div>
            </div>
        `;
        
        // Initialize the change event
        setupSortSelectorHandler();
    });

    beforeEach(() => {
        delete window.location;
        window.location = { 
            href: 'http://example.com', 
            replace: jest.fn(), 
            searchParams: new URLSearchParams()
        };
    });

    test('should set sort and direction in URL when a valid option is selected', () => {
        $('#sort-selector').val('price_asc').change(); // Simulate change event
        
        const expectedUrl = 'http://example.com/?sort=price&direction=asc';
        
        // Log for debugging
        console.log('Expected:', expectedUrl);
        console.log('Received:', window.location.replace.mock.calls[0][0].toString()); // Convert to string for comparison

        // Use toEqual for better diagnostics
        expect(window.location.replace.mock.calls[0][0].toString()).toEqual(expectedUrl); // Convert to string
    });

    test('should reset sort and direction in URL when reset option is selected', () => {
        $('#sort-selector').val('reset').change(); // Simulate change event
        
        const expectedUrl = 'http://example.com/';
        
        // Log for debugging
        console.log('Expected:', expectedUrl);
        console.log('Received:', window.location.replace.mock.calls[0][0].toString()); // Convert to string for comparison
        
        expect(window.location.replace.mock.calls[0][0].toString()).toEqual(expectedUrl); // Convert to string
    });
});


