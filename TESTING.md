# Easy Keyboard Maker Testing 

![Absolut Zero am i responsive]()

Developer: [Erik Guldbrand](https://github.com/Tossan99) <br>
[Live webpage](https://absolut-zero-9622981fe97d.herokuapp.com/)<br>
[Project Repository](https://github.com/Tossan99/absolut-zero)<br>


## Table of Content

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

[Back to top ⇧](#table-of-contents)

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

