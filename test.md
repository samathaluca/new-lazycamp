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

Due to the incompatability between gitpod IDE and gmail all sent email manual tests could only be carried out once the project had been deployed.
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

Unitests ran successfully before changing tp Postgres database. I did not gain enough confidence in my ability to write automated tests to negate the need for the manual tests. 
I understand that automated tests and TDD and essential when numerous people are working on the same project but as the sole contributor to the project my preference was reliance on manual testing.
I also believe that in development work few customers are willing to pay for time taken to write the tests on their code so after grasping the basics of writing automated tests I concentrated efforts on user stories and testing that would reveal bugs the user will see when browsing. 

Travis. Having successfully run Travis using the old version of the Full stack Developer module, I noted that Travis was no longer included in the updated videos. After some issue with Travis continuing to run lazycamp instead of new-lazycamp respository and even when successfully switching, Travis reverted back and ran tests on old repository, I was advised by the tutors that Travis had been  deprecated along with the use of Django 1 in projects along with Travis.. 

### Final Testing before Submission.

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

2. Campspot cards - Not currently available section

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


#### Checkout page 

Checkout success 

Check stripe
Check confirmation emails have been sent to business owner , admin and user


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

* Test the links to the products.html Events and the separate link to campspots.html Online Camps bookings 


#### Contact Page (contact.html)
* Go to the contact page from the Contact dropdown in the navigation menu. 

* Confirm that the contact form is laid out as expected.
* Confirm that for a logged in user the email address field has already been populated.
* Confirm that for a user who is not logged in the email address field is blank.
Try to send the form with no fields filled in, confirm that the user is alerted to fill in the required fields.
* Try to enter a non-email address into the email field, confirm that the user is alerted to fill in an email address.
* Send a complete form, confirm that the message is sent with all the information included. NOTE: this can only be tested in the deployed version due to incompatibility betweeb gitpod and heroku.

* check phone number link works to direct dial from mobile and computers with skype or calling option 





* Check links to continue browsing work well. 

Quickfire email 
check email link works to direct dial from mobile and computers with 





Quickfire email 
* Checked that email link works to direct dial from mobile and computers with e.g. skype call and email client





skype or calling option 
messenger chat in organise events too
phone link 


### My account dropdown 

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


#### Campspot managements 

1. Add campspot

check added to correct section of the campspot page 
2. Edit Campspots check updated version is now in the campspot page

Delete campspot 


#### Event managements 

1. Add Event

check added to product page

2. Edit Events

Delete

#### Admin checks.
Check order is present
Check latest campspots and product events are shown at the top of the page so all new additions can be seen in the database immediately 

#### Each time a new order payment is made and so is added check stripe.

#### Check that all the latest static and media versions have been uploaded to S3 bucket.
Check all the recently added images in events and campspots are in s3 bucket. 


Debug = False check 404 page 


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

Early development testing.

Responsive Design - LazyCamp is fully responsive;

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. 
A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


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
```
gitpod /workspace/new-lazycamp/book $ python3 experiment.py 
gitpod /workspace/new-lazycamp/book $ python3 experiment.py 
7
gitpod /workspace/new-lazycamp/book $ python3 experiment.py 
7
gitpod /workspace/new-lazycamp/book $ python3 experiment.py 
8
gitpod /workspace/new-lazycamp/book $ python3 experiment.py 
8
Traceback (most recent call last):
  File "experiment.py", line 9, in <module>
    test()
  File "experiment.py", line 7, in test
    assert(add(3,4)==7)
AssertionError
gitpod /workspace/new-lazycamp/book $ python3 experiment.py 
7
```
I added a new test in products app which I ran in the terminal. 

```
gitpod /workspace/new-lazycamp $ python3 manage.py test products
Creating test database for alias 'default'...
/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/postgresql/base.py:294: RuntimeWarning: Normally Django will use a connection to the 'postgres' database to avoid running initialization queries against the production database when it's not needed (for example, when running tests). Django was unable to create a connection to the 'postgres' database and will use the first PostgreSQL database instead.
  warnings.warn(
Got an error creating the test database: permission denied to create database

gitpod /workspace/new-lazycamp $ python3 manage.py test products
Creating test database for alias 'default'...
/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/postgresql/base.py:294: RuntimeWarning: Normally Django will use a connection to the 'postgres' database to avoid running initialization queries against the production database when it's not needed (for example, when running tests). Django was unable to create a connection to the 'postgres' database and will use the first PostgreSQL database instead.
  warnings.warn(
Got an error creating the test database: permission denied to create database

``` 

I tried to correct this with the command python3 manage.py test products --settings=test_settings

```
gitpod /workspace/new-lazycamp $ python3 manage.py test products --settings=test_settings
Traceback (most recent call last):
  File "manage.py", line 21, in <module>
    main()
  File "manage.py", line 17, in main
    execute_from_command_line(sys.argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 395, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/test.py", line 23, in run_from_argv
    super().run_from_argv(argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 320, in run_from_argv
    parser = self.create_parser(argv[0], argv[1])
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 294, in create_parser
    self.add_arguments(parser)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/test.py", line 44, in add_arguments
    test_runner_class = get_runner(settings, self.test_runner)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/test/utils.py", line 301, in get_runner
    test_runner_class = test_runner_class or settings.TEST_RUNNER
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/conf/__init__.py", line 76, in __getattr__
    self._setup(name)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/conf/__init__.py", line 63, in _setup
    self._wrapped = Settings(settings_module)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/conf/__init__.py", line 142, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
  File "/home/gitpod/.pyenv/versions/3.8.2/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'test_settings'
gitpod /workspace/new-lazycamp $ python3 manage.py test products --settings=lazycamp.test_settings
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.004s

OK
Destroying test database for alias 'default'...
gitpod /workspace/new-lazycamp $ python3 manage.py test products --settings=test_settings
Traceback (most recent call last):
  File "manage.py", line 21, in <module>
    main()
  File "manage.py", line 17, in main
    execute_from_command_line(sys.argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 395, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/test.py", line 23, in run_from_argv
    super().run_from_argv(argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 320, in run_from_argv
    parser = self.create_parser(argv[0], argv[1])
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 294, in create_parser
    self.add_arguments(parser)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/test.py", line 44, in add_arguments
    test_runner_class = get_runner(settings, self.test_runner)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/test/utils.py", line 301, in get_runner
    test_runner_class = test_runner_class or settings.TEST_RUNNER
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/conf/__init__.py", line 76, in __getattr__
    self._setup(name)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/conf/__init__.py", line 63, in _setup
    self._wrapped = Settings(settings_module)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/conf/__init__.py", line 142, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
  File "/home/gitpod/.pyenv/versions/3.8.2/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'test_settings'
gitpod /workspace/new-lazycamp $ python3 manage.py test products --settings=lazycamp.test_settings
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_get_friendly_name (products.tests.TestCategory)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/new-lazycamp/products/tests.py", line 14, in test_get_friendly_name
    self.assertEqual(cattwo.get_friendly_name(), 'cattwo')
AssertionError: '' != 'cattwo'
+ cattwo

----------------------------python3 manage.py test products --settings=lazycamp.test_settings------------------------------------------
Ran 1 test in 0.004s

FAILED (failures=1)
Destroying test database for alias 'default'...
gitpod /workspace/new-lazycamp $ 
gitpod /workspace/new-lazycamp $ 
gitpod /workspace/new-lazycamp $ 
gitpod /workspace/new-lazycamp $ python3 manage.py test products --settings=lazycamp.test_settings
Creating test database for alias 'default'...
Traceback (most recent call last):
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.OperationalError: no such column: products_product.owner_id

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "manage.py", line 21, in <module>
    main()
  File "manage.py", line 17, in main
    execute_from_command_line(sys.argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 395, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/test.py", line 23, in run_from_argv
    super().run_from_argv(argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 328, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 369, in execute
    output = self.handle(*args, **options)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/test.py", line 53, in handle
    failures = test_runner.run_tests(test_labels)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/test/runner.py", line 684, in run_tests
    old_config = self.setup_databases(aliases=databases)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/test/runner.py", line 604, in setup_databases
    return _setup_databases(
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/test/utils.py", line 169, in setup_databases
    connection.creation.create_test_db(
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/base/creation.py", line 80, in create_test_db
    self.connection._test_serialized_contents = self.serialize_db_to_string()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/base/creation.py", line 123, in serialize_db_to_string
    serializers.serialize("json", get_objects(), indent=None, stream=out)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/serializers/__init__.py", line 128, in serialize
    s.serialize(queryset, **options)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/serializers/base.py", line 90, in serialize
    for count, obj in enumerate(queryset, start=1):
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/base/creation.py", line 120, in get_objects
    yield from queryset.iterator()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/query.py", line 346, in _iterator
    yield from self._iterable_class(self, chunked_fetch=use_chunked_fetch, chunk_size=chunk_size)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/query.py", line 57, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1151, in execute_sql
    cursor.execute(sql, params)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.OperationalError: no such column: products_product.owner_id
gitpod /workspace/new-lazycamp $ python3 manage.py makemigrations --dry-run
Migrations for 'products':
  products/migrations/0008_product_owner.py
    - Add field owner to product

gitpod /workspace/new-lazycamp $ python3 manage.py test products --settings=lazycamp.test_settings
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.004s

OK
Destroying test database for alias 'default'...
gitpod /workspace/new-lazycamp $ 
```




travis 
[![Build Status](https://travis-ci.org/samathaluca/new-lazycamp.svg?branch=master)](https://travis-ci.org/samathaluca/new-lazycamp)





# LaZy Camp
## Lazy Camp
###### Lazy Camp
<hr>

*  Item 1
*  Item 2
*  Item 2a
*  Item 2b

1. Item 1
2. Item 2
3. Item 3
 * Item 3a
 * Item 3b

As Grace Hopper said:
> I’ve always been more interested
> in the future than in the past.

\*literal asterisks\*

```javascript```

![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)

https://new-lazycamp.herokuapp.com/ - automatic!
[GitHub](https://new-lazycamp.herokuapp.com/)

*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__
*You **can** combine them*

# LaZy Camp

<hr>

Quick guide
Home Page
About Page
Campspots Page
Individual Campspot Page
Register Page
Login Page
User Dashboard

To Add
Enquiry and contact PageBlog
Idea Page
Testiminial Page
Checkout Page









