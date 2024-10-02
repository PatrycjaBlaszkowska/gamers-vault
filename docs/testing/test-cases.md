# Test Cases

## Test Case 1: Access Home Page
**Objective:** Verify that the home page loads correctly for all users.

**Steps:**
1. Navigate to the [home page URL](http://gamers-vault-72a0e73da873.herokuapp.com/).
2. Wait for the page to fully load.

**Expected Result:**  
The home page should load without errors, displaying all sections correctly.

**Screenshot:**  
![Home page](/docs/images/test-case-1-results.png)

<hr>

## Test Case 2: Browse Products
**Objective:** Ensure that users can browse available products.

**Steps:**
1. From the home page, scroll down to the products section.
2. Click on a product image or name to view product details.

**Expected Result:**  
The product detail page should load, showing all relevant product information (images, description, price).

**Screenshot:**  
![Product detail](/docs/images/product-detail-desktop.png)

<hr>

## Test Case 3: Search for Products
**Objective:** Test the search functionality.

**Steps:**
1. Locate the search bar at the top of the home page.
2. Enter a product name (e.g., "shoes") and press Enter or click the search icon.

**Expected Result:**  
The search results page should display products matching the search criteria.

**Screenshot:**  
![Search results](/docs/images/test-case-3-results.PNG)

<hr>

## Test Case 4: Guest Checkout Process
**Objective:** Validate the guest checkout functionality.

**Steps:**
1. Browse products and add an item to the cart.
2. Click on the cart icon to view the cart.
3. Click on the "Proceed to Checkout" button.
4. Select the guest checkout option.
5. Fill in the required delivery information fields (name, address, etc.).
6. Choose a payment method and complete the purchase.

**Expected Result:**  
The order confirmation page should display a thank-you message, order details, and a confirmation email should be sent.

**Screenshot:**  


<hr>

## Test Case 5: User Registration
**Objective:** Ensure that new users can successfully register.

**Steps:**
1. From the home page, click on the "Sign Up" or "Register" link.
2. Fill in the registration form with valid details (username, email, password).
3. Click the "Register" button.

**Expected Result:**  
The user should be redirected to a success page or the home page, and a confirmation email should be sent.

**Screenshot:**  

<hr>

## Test Case 6: User Login
**Objective:** Verify that existing users can log in.

**Steps:**
1. Click on the "Login" link on the home page.
2. Enter valid credentials (email and password).
3. Click the "Login" button.

**Expected Result:**  
The user should be redirected to the home page with a success message, and their profile should be accessible.

**Screenshot:**  
Capture a screenshot of the home page after logging in.

<hr>

## Test Case 7: Add Item to Wishlist
**Objective:** Ensure users can add items to their wishlist.

**Steps:**
1. Navigate to a product page.
2. Click on the "Add to Wishlist" button.

**Expected Result:**  
The item should be successfully added to the user's wishlist, and a confirmation message should be displayed.

**Screenshot:**  


<hr>

## Test Case 8: Contact Us Form Submission
**Objective:** Validate that users can submit inquiries through the Contact Us page.

**Steps:**
1. Click on the "Contact Us" link in the footer or header.
2. Fill in the contact form (Name, Email, Query Type, Message).
3. Click the "Send Message" button.

**Expected Result:**  
The user should be redirected to a thank you page, confirming the message was sent.

**Screenshot:**  


<hr>

## Test Case 9: View Order History
**Objective:** Ensure users can view their order history after logging in.

**Steps:**
1. Log in to the user account.
2. Click on the "Profile" link in the navigation menu.
3. Select the "Order History" section.

**Expected Result:**  
The order history should display a list of past orders with details (order number, date, items).

**Screenshot:**  


<hr>

## Test Case 10: Update Profile Information
**Objective:** Verify that users can update their profile information.

**Steps:**
1. Log in to the user account.
2. Click on the "Profile" link.
3. Edit the delivery information fields (e.g., address, phone number).
4. Submit the updated information.

**Expected Result:**  
A success message should be displayed, confirming that the profile has been updated.

**Screenshot:**  

