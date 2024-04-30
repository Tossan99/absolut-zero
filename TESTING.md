# Easy Keyboard Maker Testing 

![Absolut Zero am i responsive]()

Developer: [Erik Guldbrand](https://github.com/Tossan99) <br>
[Live webpage](https://absolut-zero-9622981fe97d.herokuapp.com/)<br>
[Project Repository](https://github.com/Tossan99/absolut-zero)<br>


## Table of Content

- [Easy Keyboard Maker Testing](#easy-keyboard-maker-testing)
  * [Table of Content](#table-of-content)
  * [Code Validation](#code-validation)
    + [HTML Validation](#html-validation)
    + [CSS Validation](#css-validation)
    + [PYTHON Validation](#python-validation)
  * [Performance](#performance)
  * [Browser compatibility](#browser-compatibility)
  * [Automated Testing](#automated-testing)
  * [Manual Testing](#manual-testing)
    + [Responsiveness](#responsiveness)
    + [Full Testing](#full-testing)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


[Back to top ⇧](#table-of-contents)

## Code Validation

### HTML Validation

W3C Markup Validation is a service offered by W3C, which enables you to assess the compliance of your HTML code with the official standards. This service identifies syntax errors, improper tag usage, and other issues that might impact the structure and meaning of your web pages. By utilizing W3C Markup Validation, you can ensure that your HTML code is well-structured and conforms to established web standards.

Google Chrome web browser and the 'Inspect' function were used to capture the HTML page from the webb applications templates, which was then validated against the W3C Validator.


| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
| **Home App** |
|index.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-index.JPG)</details>| ✅
| **Products App** |
|products.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-products.JPG)</details>| ✅
|product_details.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-product-details.JPG)</details>| ✅
| **Shopping Cart App** |
|shopping_cart.html| All clear, no errors found. | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-cart.JPG)</details>| ✅
| **Checkout App** |
|checkout.html| One warning for empty heading for the loading spinner and one error for the placeholder text on the select element. No good solution could be found to fix the two problems due to lack of time. | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-checkout.JPG)</details>| ❌
|checkout_success.html| All clear, no errors found. | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-success.JPG)</details>| ✅
| **Profiles App** |
|profile.html| All clear, no errors found. | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-profile.JPG)</details>| ✅
| **About App** |
|about.html| All clear, no errors found. | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-about.JPG)</details>| ✅
| **FAQ App** |
|faq.html| All clear, no errors found. | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-faq.JPG)</details>| ✅

### CSS Validation
[W3C Jigsaw](https://jigsaw.w3.org/css-validator/) is a tool provided by the World Wide Web Consortium (W3C) that allows you to validate and check the correctness of your HTML and CSS code. It helps ensure that your web pages comply with the standards set by the W3C, promoting interoperability and accessibility.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|base.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-basecss.JPG)</details>| ✅
|about.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-aboutcss.JPG)</details>| ✅
|checkout.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-checkoutcss.JPG)</details>| ✅
|faq.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-faqcss.JPG)</details>| ✅
|home.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-homecss.JPG)</details>| ✅
|products.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-productscss.JPG)</details>| ✅
|profile.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-profilecsss.JPG)</details>| ✅
|shopping-cart.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](documentation\validator_images\validator-shopping-cartcss.JPG)</details>| ✅


### PYTHON Validation 
[PEP 8](https://pep8ci.herokuapp.com/) serves as a comprehensive style guide for writing Python code, emphasizing consistency and readability as its core principles. It offers guidance on code formatting, variable and function naming conventions, and various best practices. Adhering to PEP 8 principles contributes to enhancing code quality, making it more readable and maintainable.

During all validation of the python files the "line too long error" was ignored due to lack of time. this will be fixed in the future.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
| **Home App** |
|views.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-homeview.JPG)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-homeurls.JPG)</details>| ✅
| **Products App** |
|views.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-productsviews.JPG)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-productsurls.JPG)</details>| ✅
|models.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-productsmodels.JPG)</details>| ✅
|forms.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-productsforms.JPG)</details>| ✅
| **Shopping Cart App** |
|views.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-cartviews.JPG)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-carturls.JPG)</details>| ✅
| **Checkout App** |
|views.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-checkoutviews.JPG)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-checkouturls.JPG)</details>| ✅
|models.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-checkoutmodels.JPG)</details>| ✅
|forms.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-checkoutforms.JPG)</details>| ✅
|webhooks.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep-checkoutwh.JPG)</details>| ✅
|webhook_handler.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-checkoutwhh.JPG)</details>| ✅
| **Profiles App** |
|views.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-profilesviews.JPG)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-profilesurls.JPG)</details>| ✅
|models.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-profilesmodels.JPG)</details>| ✅
|forms.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](documentation\validator_images\pep8-profilesforms.JPG)</details>| ✅


[Back to top ⇧](##table-of-contents)

## Performance
I conducted a comprehensive evaluation of The Absolut Zero website using [Google Lighthouse in Google Chrome Developer Tools](https://developer.chrome.com/docs/lighthouse/). This evaluation was performed in Google Chrome browser's incognito mode to eliminate all potential impacts from other addons and cached files.

| **Tested** | **Performance Score** | **View Result** | **Pass** |
--- | --- | --- | :---:
| **Home App** |
|index.html| 73 / 100 |<details><summary>Screenshot of result</summary>![Result](documentation\lighthouse\lighthouse-home.JPG)</details> | ✅
| **Products App** |
|product_details.html| 73 / 100 | <details><summary>Screenshot of result</summary>![Result](documentation\lighthouse\lighthouse-product-details.JPG)</details>| ✅
|products.html| 69 / 100 | <details><summary>Screenshot of result</summary>![Result](documentation\lighthouse\lighthouse-products.JPG)</details>| ✅
| **Shopping Cart App** |
|shopping_cart.html| 74 / 100 | <details><summary>Screenshot of result</summary>![Result](documentation\lighthouse\lighthouse-cart.JPG)</details>| ✅
| **Checkout App** |
|checkout.html| 70 / 100 | <details><summary>Screenshot of result</summary>![Result](documentation\lighthouse\lighthouse-checkout.JPG)</details>| ✅
| **Profiles App** |
|profile.html| 75 / 100 | <details><summary>Screenshot of result</summary>![Result](documentation\lighthouse\lighthouse-profile.JPG)</details>| ✅

The tests indicate a performance issue with the website, likely stemming from the presence of a large background heading image. This issue will be addressed in future updates, and subsequent tests will be conducted to monitor improvements.

[Back to top ⇧](#table-of-contents)

## Browser compatibility
The website was tested on the following:

<ins>Browsers</ins>
1. Microsoft Edge
2. Google Chrome 	
3. Mozilla Firefox 	
4. Safari

[Back to top ⇧](#table-of-contents)

## Automated Testing

Due to lack of time no automated testing has been implemented.

[Back to top ⇧](#table-of-contents)


## Manual Testing

### Responsiveness

- All sections of the website has been rigorously tested for responsiveness from 350px width, 650px height and up.
  
- No images are stretched or pixelated.
  
- No element overlap each other

### Full Testing

**`Navbar unauthorized user`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo | Redirects to index.html page | Clicked on logo | Index page loads | ✅ |
| Home | Redirects to the index page | Clicked on the link "Home" | Index page loads | ✅ |
| Products category links | Redirect to product view of the link | Clicked on the links of different product category  | Page reloads and displaying the correct products | ✅ |
| Search | Get search query render | Typed "ale" | Different ales was showing | ✅ |
| About | Redirect to the Article post page | Clicked on the link "About" | About page loads | ✅ |
| FAQ | Redirects to the support page | Clicked on the link "FAQ" | FAQ page loads | ✅ |
| Login | Redirects to the login page | Clicked on the link "Login" | Login page loads and form displays | ✅ |
| Sign up | Redirects to the sign up page and form | Clicked on the link "Sign up" | Sign-up page loads and the form displays | ✅ |


**`Navbar authorized user`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo | Redirects to index.html page | Clicked on logo | Index page loads | ✅ |
| Products category links | Redirect to product view of the link | Clicked on the links of different product category  | Page reloads and displaying the correct products | ✅ |
| About | Redirect to the Article post page | Clicked on the link "About" | About page loads | ✅ |
| FAQ | Redirects to the support page | Clicked on the link "FAQ" | FAQ page loads | ✅ |
| Profile icon | Triggers the dropdown menu | Clicked on the image | The dropdown menu is displayed | ✅ |

**`Index page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Browse Products | Redirects to the page displaying all products | Clicked on the "Browse Products" button | Successfully redirected to the page displaying all products | ✅ |
| My Profile | Redirects to the page displaying users profile | Clicked on the "My Profile" button | Successfully redirected to the page displaying the users profile| ✅ |
| Footer navigation links | Redirects to different information pages | Clicked on all links in the footer | Successfully user redirection to correct pages/templates | ✅ |

**`Sign up page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Username | Field is required and should be a valid username format | Tested with an empty field, invalid format | Error message is displayed prompting the user to provide a valid username | ✅ |
| Email | Field is required and should be a valid email format | Tested with an empty field, or invalid format | Error message displayed prompting the user to provide a valid email address | ✅ |
| Password | Field is required and should meet password criteria | Tested with an empty field, invalid criteria | Error message displayed prompting the user to provide a valid password | ✅ |
| Password confirmation | Field is required and should match the entered password | Tested with empty field, mismatched passwords | Error message displayed prompting the user to confirm the password correctly | ✅ |
| Sign up button | If the form is valid, the user is redirected to the profile page with a flash message confirming successful registration. If the form is not valid, an error message is displayed. | Clicked the button with valid and non-valid formats | The button functions as expected, redirecting to the appropriate page and displaying the corresponding messages | ✅ |
| Login text link | Redirects to the login page | Clicked on the "Login" link | The login page and form were successfully loaded | ✅ |

**`Log in page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Username | The user enters a username | Tested with valid and invalid username input | The username field accepts and saves the valid input. If invalid, it displays an error message | ✅ |
| Password | The user enters a password | Tested with valid and invalid password input | The password field functions correctly, allowing the user to input a valid password and displays an error message when not valid | ✅ |
| Sign up text link | Clicking the text link redirects to the sign-up page | Clicked on the "Sign up" text link | Successfully redirected to the sign-up page with the registration form | ✅ |
| Login | If the login form is valid, the user is logged in and redirected to the appropriate page. If the form is not valid, an error message is displayed. | Tested with valid and invalid login form input | The login button functions correctly, logging in the user with valid credentials and displaying error messages for invalid credentials | ✅ |

**`Profile page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Update shipping information | Able to update the shipping inputs directly on the page |  Clicked on the "Update" button | Page reloads and displays successful toast message of update was successful | ✅ |

**`Product page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Product add to cart button | Product is added to the cart with a successful message | Clicked on the "add to cart" button | Successfully clicked on the button link and the product was added to the cart with successful message indicating success | ✅ |
| Product name link | Redirect to product detail page | Clicked on product name link | Successfully redirected to product detail page | ✅ |
| Sort by list | Sort product by the desirable value | Clicked in the sort by dropdown for testing all values | Product was decending and acending depending on the value from the sort by | ✅ |

**`Product Review`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Review a product| Write review with a successfully submission | Write review and clicked submit | Review is submitted and displayed | ✅ |
| Rate a product | Rate a product with a successfully submission | Rate a product | Rating is submitted and displayed with review average of star | ✅ |

**`Product Detail page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Quantity buttons | Minus or Plus button for adding additional product quantity in the cart | Clicked on the minus or plus button | Product is added or removed from cart depending on the quantity buttons successfully | ✅ |
| Keep shopping button | Redirect user back to all product page | Clicked on the keep shopping button | Successfully redirected to product page were product are displayed | ✅ |
| Add to cart button | Product is added to the cart with a successful message | Clicked on the "add to cart" button | Successfully clicked on the button link and the product was added to the cart with successful message indicating success | ✅ |


**`403, 404, 405, 500 Page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Go home button | Correct "error message" displays and redirects the user to index.html page | Edited a non-URL path in the web browser and then clicked on the Go home button | Correct error handling message was displayed for the user, and when the Go home button was clicked, the user was redirected to the index page | ✅ |

[Back to top ⇧](#table-of-contents)

