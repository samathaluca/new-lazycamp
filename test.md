![README ](/README.md)

## Validation Services
The following validation services and linter were used to check the validity of the website code.

[W3C Markup Validation](https://validator.w3.org/) was used to validate HTML.

[W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.

[JSHint](https://jshint.com/) was used to validate JavaScript.

[Chrome Devtools](https://developers.google.com/web/tools/chrome-devtools/) to test responsivitiy throughout.

[Firefox Devtools](https://developer.mozilla.org/en-US/docs/Tools) to test responsivitiy throughout. 

[HTML and CSS Beautifier](https://www.freeformatter.com/html-formatter.html) use format selection in beautify code

[AutoPrefixer](https://autoprefixer.github.io/) -This project used AutoPrefixer to make sure the css code is valid for all browsers.

[Markdown live-preview](https://markdownlivepreview.com/) -This project used markdown previewer to check the rendering of the readme.md file content.

[PEP8 online](http://pep8online.com/)- Not secure but ok for testing console errors.
    
[VSC code extensions](https://code.visualstudio.com/)- To test code when gitpod was not working well.

[IDLE](https://www.python.org/)- to check python code
    


## Manual Testing

Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected.

Due to the incompatability between gitpod IDE and gmail all send email manual tests could only be carried out once the project had been deployed.
FB messenger will not work in the IDE and needs to be deployed to test.

Aside from the email and messenger manual tests, all commits to the github repository were preceded by changes that had been tested and proved to run successfully in the IDE.
After each new commit the deployed app was tested to check the changes were successful.

After each change proved to work well in a particular screen size responsive design manual tests were completed using both chrome and Firefox dev tools. Each test was carried out in both browsers in both local and deployed versions.

Periodically extensive manual testing was carried out using 2 desktop screen sizes, 3 laptops, 2 tablets and 7 different mobile phones. Knowledge that testing responsive design in dev tools is not always 100% accurate, true rendering on the physical devices was relied upon through development.  

#### Devices tested

##### Mobile phones

Samsung S9,
Iphone 6
Iphone 7
Iphone 7S plus,
Sony XA2
Sony X3
Blackberry Priv

##### Tablets tested

Ipad 2 early IOS did not show datepicker correctly.
LNBEI 10 inch Android tablet

##### Laptop tested

MacBook pro,
Sony Vaio
HP Pavillion DV6

##### Desktop 

(unbranded Windows 7 OS) with different monitors 21 and 24inch.

#### Browsers 
Between devices the browsers tested were as follows:
Google Chrome,
Opera,
Firefox,
Microsoft Edge,
Safari,
Android Brower,
Samsung Browser

### Final Testing Plan and Guide.

#### Elements on every page

1. Navbar

* Click on Logo returns to home on desktop. Mobile version is styled so logo appears above search and on click reveals the search input.
* Tests on both mobile menu dropdown icon and desktop dropdown menus all link to the correct page. 
* Confirm My account is visible and that when clicked the logged out the options "Register" and "Log in" are visible and that "Campspot Management", "My Profile" and "Log out" are not.
* When Logged in the site, confirm that options "Campspot Management", "My Profile" and "Log out" are visible and that "Register" and "Log in" are not.
* Add a booking to the session and, confirm that the total expenditure appears under the shopping icon with the correct price displayed in £ as a float with two decimal places.
* Delete all items from the booking, confirm that the price of £0.00 is displayed in the navbar.
* Click the "price" link in the navbar, confirm that booking is empty or that all bookings are listed. 
* In mobile versions search input bar is not dispayed until the search icon is clicked. 
* The input search box is  set up to drive traffic to the online booking section. Manual tests confirm that 
on each page in which it is displayed the search lists campspots available to book online. The best results are achieved by searching by Welsh County currently because all campspots added have one added. 
* Check that on the products.html page the search box is hidden on desktop versions.
* Check that on mobiles and tablets the search icon is displayed but that the placeholder notifies the divert to online booking. This may be disable following peer review if it is raised as a point of confusion. Previous testing by friends and family have not commented on this as. 

#### Home page (index.html)

1.  Hero Image displays well in all browsers on all screen sizes tested.
2.  Call to action Book Now button is obvious, well positioned and on click lists all the campspots that are available to book immediateley online. 

#### Campspot Page (campspot.html)

1. Sorting options

* Select the different sorting options from the top navigation menu one by one, confirm that the campspots are sorted in to the categories selected.
For example, Click on peaceful selects all Beach, Woodland or Forest and Nature Retreats. 
Check each category is displayed and that the categories can be resorted individually. If sorting option displays multiple categories each can be reselected individually.

* From the Lazy choices or Campspot/pitches category dropdown choices, the results can be sorted in to order that most suits the user.

For example 

If Gwent is inputed in search bar.
The results of the search can then be sorted in to price, rating, name or category.
There is scope for adding in different choices from the model fields so, for example,the county search could be further sorted in to postcode option.

This is deemed to be important in the future when there are more campspots in the data base. 

2. Up arrow postioned in the bottom right of page and jumps users back to the page top when clicked

3. Campspot cards -available section

* Hover over product cards, confirm the hover effect works as expected on bottom button.
* Confirm that the link to campspot details works from both campspot image and Book online Now button. 
* Confirm that the photos, Location and prices displayed are correct.
* Confirm that all image sizes are correct.
* Check that no cards are misaligned. 
* Click multiple campspots, confirm that the user is taken to the correct campspot page if available.
* Check that when the category name is clicked that all other campspots in the same category are displayed with invitation to "Book Online Now".

4. Campspot cards - Not currently available section

* Check that all fully booked campspots (that have been unticked as False in Boolean add/edit campspot checkbox by admin or the user) are displayed in the currently unavailable section underneath all the available sites and marked as "Fully Booked".

* Check that all recently added campspots, by admin or authorised user have been added and are displayed in the currently unavailable section underneath all the available sites and marked as "Coming Soon".

* Check that there are no duplicates or missing products

#### Campspot Detail Page (campspot_detail.html)

* Click on image brings up large image in new tab.

* If logged in user is either a superuser or is the authorised site owner they will have the option to edit or delete. Check that the edit and delete coloured text is displayed when logged in. If they edit and delete text is visible, check that the edit campspot links to the correct campspot id. 

* If not logged in or on a campspot page for which you do not have the authority to edit or delete, check that the edit and delete options are not visible. 

* Check that the Number of adults and Number of nights input boxes move up and down as expected. 

* Check that the datepicker is revealed on click and the chosen date is selected.

* Click on Book Now button and the number of adults, date and number of nights selected is revealed in a success toast with the message "added date and campspot name to book. 

* If more than one booking is made check that they are all added in the campspot_detail booking success toast and that the total price is updated. 

* If more than one booking is made for the same campspot, ensure that these bookings are added together and reflect the sum of the two bookings. Check that this is revealed in the success toast. 

* Test that the keep looking link gives the option to add additional bookings.

* "check your date!" tooltip is revealed on hover over the book now button.

*  Check that the "Go to Secure Checkout" link on the success toast correctly renders the booking session on the book.html page.

#### Booking page (book.html)

* On the bookings page check

* all details are correct

* the image links to campspot_detail page
*  the remove option deletes the booking from session and page

*  the amend option deletes the booking and redirects the user to the same campspot and reminds the user to rebook in a toast

* The grand total to pay for the booking is displayed.

* The two links to secure checkout or backwards to keep looking both take to the expected pages


#### Checkout page (checkout.html)

* Confirm checkout form is displayed.
* Confirm that failure to fill out required fields will reveal an error e.g. Please enter an email address or please fill in this field.
* Confirm that the cursor returns to the empty required field.
* Confirm that the test card number 4242 4242 4242 4242 424 42424 process the order.
* Confirm spinner is revealed as payment is processed.
* Confirm that incorrect test card number has error message  "Your card number is incomplete."
* Confirm that all correct booking details are on the checkout page with the correct total being shown and advised that "Your card will be charged £ Total due"
* Confirm that both the "adjust booking" and "complete order" links work. 

#### Checkout success (checkout.html)

* Check stripe payment has succeeded and is shown in the dahsboard.
* Check confirmation emails have been sent to business owner , admin and user
* Check order is in admin if authorised.
* Check order appears on user profile page.
* Check the link to "Now click out the latest Events is working. 


#### Product Page (product.html)- In summer this promotes events.

* Check that the aim of the products page is immediately obvious. The products displayed on this page will differ seasonally. 
* Currently and in future summers this page will promote scheduled events and campspots near festivals.

In the Winter it will promote Christmas event and camping kits gifts

In The Spring this page will promote camping kits and European events.

In the Autumn this page will promote Southern Mediterranean festivals and events alongside European roadtrip and camping kits recommended for different climates. In British Summer camping in Greece, Southern Italy, Southern Spain and Croatia is not recommended by Lazycamp. 

1. Sorting options

* Select the different sorting options from the menu one by one, confirm that the products are sorted in the orders selected.

* The details of search sorting options are the same as for campspot page. 
There is flexibility and scope to attract different types of customers. 

DIFFERENT APPEAL to older and experienced campers used to booking by phone versus younger, dynamic online savvy users who may expect to find and book what they want online with secure payment without needing to pick up the phone. 

* Up arrow postioned in the bottom right of page and jumps users back to the page top when clicked

2. Product cards

* Hover over product cards, confirm the hover effect works as expected on bottom button.
* Confirm that the link to product details works from both product image and Telephone number button. 
Once this site has working payment in place the telephone number will that if the product owner/supplier. 
* Confirm that the photos, Location and prices displayed are correct.
* Confirm that all image sizes are correct.
* Check that no cards are misaligned. 
* Click multiple products, confirm that the user is taken to the correct product page.

#### Product Detail Page (product_detail.html)

* Click on image brings up large image in new tab.

* Confirm that for a logged in user the email address field has already been populated.

* If logged in user is either a superuser or is the authorised site owner they will have the option to edit or delete. Check that the edit and delete coloured text is displayed when logged in. If they edit and delete text is visible, check that the edit product links to the correct product id. 

* If not logged in or on a product page for which you do not have the authority to edit or delete, check that the edit and delete options are not visible. 

* Test the product enquiry form reveals a toast with the success message "Your email was sent Successfully!" when completed and submitted. NOTE: this can only be tested in the deployed version due to gitpod and gmail incompatibility.

* Test the "Please fill in this field" tooltip is revealed if the email is attempted to be sent without completion of all the required fields.

* Test the links to the products.html Events and the separate link to campspots.html Online Camps bookings work.

#### Contact Us Dropdown.

##### Contact Page (contact.html)

* Get to the contact page from the Contact Us dropdown in the navigation menu. Click on enquiry.
* Confirm that the contact form is laid out as expected.
* Confirm that for a logged in user the email address field has already been populated.
* Confirm that for a user who is not logged in the email address field is blank.
Try to send the form with no fields filled in, confirm that the user is alerted to fill in the required fields.
* Try to enter a non-email address into the email field, confirm that the user is alerted to fill in an email address.
* Send a complete form, confirm that the message is sent with all the information included. NOTE: this can only be tested in the deployed version due to incompatibility betweeb gitpod and heroku.

* check phone number link works to direct dial from mobile and computers with skype or calling option 

* Check links to continue browsing work well. 

##### Other Contact option in contact us dropdown. 

1. Quickfire email 

Check email link works immediately on mobile phones and computers with email client. 

2. Check that messenger chat option in contact us dropdown links to messenging.html page.

3. Phone/text in dropdown 

Check direct dial from all mobiles with network and credit is achieved. 
Check calls can be made from computers who have e.g. skype calls enabled or computer calling tools or apps installed. 

#### Chat Messenger page ( messenging.html)

* Test that Facebook messenger icon appears automatically in bottom right of the page (FB recommended that you do not try to reposition this). 
If you have FB account already on logged in to mobile or desktop the messenger icon will automatically open in to a chat box which then sends messages to Lazycamp FB messenger. 
* Check sent messages appear in lazycamp FB messenger.
* Facebook and Instagram fa-icons are present and linking to lazycamp pages.. 

#### My account dropdown 

#### Register Page
* Log out then go to the register page again. Confirm that the register form is displayed as expected.
* Fill in the form with a username already in the database, confirm that the user is informed that the username already exists.
* Fill in a form with email address already in the data base and check that the user will be informed " A user is already registered with this email address. 
* Fill in the email input with a non-email address, confirm the user is shown an error asking the to use an email address.
* Fill in the form with two different passwords, confirm the error is caught and the user is informed of their mistake.
Fill in the registration form correctly, confirm that the user is automatically directed to the login page, and the message "Your account has been created <username>. You can now log in." is displayed above the login page.
* Fill in password that is less than 8 characters and check the response will be " This password is too short. It must contain at least 8 characters."
* link to messenger chat to discuss host verified sign up is visible and working.  

#### Login Page
* Reload the login page, confirm that the message for a new account is not visible.
* Attempt to log in with a username not in the database, confirm the relevant error message is shown.
* Attempt to log in with a correct username but wrong password, confirm the relevant error message is shown.
* Log in with a correct username and password, confirm that the user is logged in and that they are redirected to their cart page.
* Try to return to the login page url when already logged in, confirm that the user is redirected to the cart page.
* Reset password. Works correctly and the message is sent to the email supplied. 


#### Profile Page
* Go to the profile page of a newly created user. Confirm that the profile info form is populated with the users username and email address.
* Confirm that the first name and last name fields are also available.
* Fill in the form with a non-email address, confirm that the applicable error is shown to the user
* Fill in the form correctly, confirm that the "Your account info has been updated." message is shown to the user and that the reloaded form is now populated with the new data.
* Confirm that a user with no previous orders has the "no orders to show" text in the Orders section.
* Make 2 separate orders on the website.
* Return to the profile page, confirm that the orders are displayed in the Orders section of the profile page. With the top order being the most recent and open to show the full details. Confirm that all orders after it in the list are closed accordions, but that can be opened with a click.
* Confirm that all data in the orders on the profile page is accurate.
* Go into the admin panel, check all users are in the user section of the database.
* Check if the email is verified or not. 

#### Logout Page

* confirm option to cancel is working.

* Confirm sign out works and redirects to home page. With success message "You have signed out".


#### Campspot management

1. Add campspot

This is only allowed for logged in superusers from the my account dropdown or staff in admin.

Check added campspot is added to the correct section of the campspot page and appears in admin on the correct date. 

2. Edit Campspots check updated version is now in the campspot page

This is only allowed for superusers and the owner of the site.
The link to edit will only appear on the campspot_detail.html page if the user is both authorised and logged in as superuser or product owner. 

3. Delete campspot 

This is currenly only allowed for superusers.


#### Event management

1. Add Event

This is only allowed for logged in superusers from the my account dropdown or staff in admin.

Once the add_product.html form is completed, check it has been added to product page and in admin. The most recently added will be at the top of the admin products.

2. Edit Events

This is only allowed for superusers and the owner of the site.
The link to edit will only appear on the products_detail.html page if the user is both authorised and logged in as superuser or product owner. 

3. Delete Events from the link in the products_detail.html page. 

This is only allowed for superusers.

#### Admin checks.
Check order is present
Check latest campspots and product events are shown at the top of the page so all new additions can be seen in the database immediately 

#### Each time a new order payment is made and so is added check stripe.

#### Check that all the latest static and media versions have been uploaded to S3 bucket.
Check all the recently added images in events and campspots are in s3 bucket. 

## ALL TEST WORK WELL


### Bugs mended

1. When two campspot bookings for the same date at the same venue were made previously, each booking was displayed separately yet if you attempted to delete one then both were deleted.

Also if two bookings were made on the same date they were stored separately. There are now added together and updated with a toast advising the user as such.

Both were an issue. The first may confuse and frustrate users who may then not make the effort to rebook. The second meant that duplicate bookings could confuse the business hosts and admin plus lead to queries made to stripe as to why two charges had been made. 

The solution was found by deleting products with the same id by date not just by id.

2. When project was submitted for peer review on slack MPia_lead noticed that the main links were not working. 
I hunted through all the python code, then html making changes and reverting to previous versions.
I was confused that I had not notice but on emptying cache I duplicated the error.

I uninstalled imagekit remembering that I had noticed the links on the mobile version were shwoing some errors when I installed imagekit and at the same time added the Facebook messenger Javascript to the messenging.html page.
I then methodically checked all the javascript for discrepancies between the most recent versions and versions prior to adding ImageKit.  

Using Dev tools I found that the error was triggered at screen size 650px. I searched gitpod IDE
and found a media queries for max-screen size 650px in base.css. When I commented this out the error disappeared and all links began working correctly. 

3. Adding messenger to pages with included javascript did not work. 

I made a fresh messenging.html page without any template inheritance and no other JS to make it work reliably,

4. Imagekit worked perfectly in gitpod but not I was not able to replicate the success in the deployed version. Research revealed an unresolved incompatility betweem django-imagekit and AWS S3 buckets on which I am relying for static and media file storage. 
I initially commented out all reference to imagekit and was planning to leave in place in the interest of agile design planning to find an alernative media and storage system. 
When I found the bug effecting the mobile screen size links I uninstalled imagekit to see if that could be the issue.

In the interest of defensive design allowing campspot owners and event organisers to add images to the site themselves is risky. For this reason I have removed the image URL as an option knowing that it can be confusing and often the page and not the image URL will be added. 

As a temporary solution I have set the max-height of all added images to 250 px in base.css for campspot then inline max-height of 200px in campspot.html and products.html page respectively to test alternatives. 

## Bugs # TODO 

orders are being replicated in the profile and admin section. This is caused by the webhook handler.
Temporary message to user stating that they will only be charged once. 

found that if the user mistakenly adds two conflicting bookings for the same site on different dates it is possible to delete them but not amend one of them. I will attempt to resolve this before submission if all documentation is up to date and code quality has been validated, formatted and re-checked thoroughly enough with a review of all comments. 

realised no easy access to the event management product/add page. 
Code had already been added to the product view and templates had been made. 
An option added "event management" to my account caused as error in heroku build. 
The subsequent efforts to run the  heroku app in chrome failed for 3 hours despite refresh and clear session selected. Heroku worked well in all other browsers on desktop and all mobile devices tested. After 3 1/2 hour lapse Chrome loaded heroku app as expected and tests resumed. 


### User Stories Testing

#### ALL USER STORIES CHECKED AND SATSFIED. Nothing outstanding.

The project providing an easy and straightforward way for the users to achieve each of their goals.


### Responsive Design - LazyCamp is fully responsive;


Debug = False check 404 page 


# Automated testing 

I attempted to use Django's built-in testing framework.

After writing tests, I ran ```python3 manage.py test```

This command checks all of the apps for filenames that begin with the word test and runs all of the methods in that file that begin with test_

In the terminal,  running ```python3 manage.py test``` worked well before beginning to use the postgres database.

After switching to postgres database from sqlite3 the tests would not run. 

As I tried to develop automated tests repeated errors were thrown in the database as follows. 
```
gitpod /workspace/new-lazycamp/book $ cd ..
gitpod /workspace/new-lazycamp $ python3 manage.py test products
Creating test database for alias 'default'...
/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/postgresql/base.py:294: RuntimeWarning: Normally Django will use a connection to the 'postgres' database to avoid running initialization queries against the production database when it's not needed (for example, when running tests). Django was unable to create a connection to the 'postgres' database and will use the first PostgreSQL database instead.
  warnings.warn(
Got an error creating the test database: permission denied to create database
```

Following Django test documentation,
I added a test to books.py which threw an error in the database.
I then added test database in lazycamp settings.py file.
In the terminal, python3 manage.py test products --settings=lazycamp.test_settings
still had problems so I set up a separate test.settings.py file in product app to test the models function
I tested with self.name() and passed the test.py file. When the self.name() was commented out the test failed.
To added a test to products app and I ran command 
python3 manage.py test products --settings=lazycamp.test_settings in the terminal
I tried to correct this with the command python3 manage.py test products --settings=test_settings.

```from django.test import TestCase

from campspots.models import Category

The following test in campspots and test.py file works well. All other tests in the project have not worked so will be deleted for submission. 


class TestCategory(TestCase):
    def setUp(self):
        Category.objects.create(name='catone', friendly_name='First Category')
        Category.objects.create(name='cattwo', friendly_name='cattwo')

    def test_get_friendly_name(self):
        catone = Category.objects.get(name='catone')
        cattwo = Category.objects.get(name='cattwo')
        self.assertEqual(catone.get_friendly_name(), 'First Category')
        self.assertEqual(cattwo.get_friendly_name(), 'cattwo')```

