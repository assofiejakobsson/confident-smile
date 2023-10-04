Welcome to Confident Smile, the go-to online store built with the Django web framework, specializing in organic and fluoride-free teeth whitening products. Designed for health-conscious consumers, eco-friendly shoppers, individuals with sensitivities to fluoride, and tech-savvy enthusiasts who appreciate a user-friendly platform, our offerings cater to those looking for natural, environmentally friendly dental care solutions.

## **[Live site](https://confident-smile-9920989d7786.herokuapp.com/)    |    [Repository](https://github.com/assofiejakobsson/confident-smile.git)**

![Confident Smile](media/readme/confident-smile-homepage-screenshot.png)

## Table of Contents
- [**Live site    |    Repository**](#live-site--------repository)
- [Table of Contents](#table-of-contents)
- [User Experience (UX)](#user-experience-ux)
- [Agile Methodology](#agile-methodology)
  - [User Stories](#user-stories)
    - [EPIC | Product details and information](#epic--product-details-and-information)
    - [EPIC | Shopping cart and checkout](#epic--shopping-cart-and-checkout)
    - [EPIC | Order management and analytics](#epic--order-management-and-analytics)
    - [EPIC | Product management](#epic--product-management)
    - [Epic: Customer suport and marketing](#epic-customer-suport-and-marketing)
  - [The following user stories where labelled as "could have" and "Won't Have" on my project board on Github.](#the-following-user-stories-where-labelled-as-could-have-and-wont-have-on-my-project-board-on-github)
    - [EPIC | Order management and analytics](#epic--order-management-and-analytics-1)
    - [Epic: Customer suport and marketing](#epic-customer-suport-and-marketing-1)
    - [Colour Scheme](#colour-scheme)
- [Facebook](#facebook)
- [Wireframes](#wireframes)
- [Security Features and Defensive Design](#security-features-and-defensive-design)
  - [User Authentication](#user-authentication)
  - [Database Security](#database-security)
- [Testing](#testing)
- [Manual Testing](#manual-testing)
  - [Header](#header)
  - [Product Mangement](#product-mangement)
  - [Profile](#profile)
  - [Wishlist](#wishlist)
  - [Register page](#register-page)
  - [Login page](#login-page)
  - [Logout page](#logout-page)
  - [Home page](#home-page)
  - [Shoping page](#shoping-page)
  - [Product page](#product-page)
  - [Review page](#review-page)
  - [Shopping bag](#shopping-bag)
  - [Checkout page](#checkout-page)
  - [Fotter](#fotter)
  - [Admin page](#admin-page)
- [Validator Testing](#validator-testing)
  - [HTML](#html)
  - [CSS](#css)
  - [Javascript](#javascript)
  - [Python](#python)
  - [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Bugs](#bugs)
- [Deploy the App to Heroku](#deploy-the-app-to-heroku)
- [Languages](#languages)
- [Credits](#credits)


## User Experience (UX)

The typical visitor to this webshop is an individual who is both health- and environmentally-conscious, actively seeking quality products that reflect these values, and is willing to invest in organic and fluoride-free teeth whitening solutions to maintain a healthy and radiant smile.

## Agile Methodology

Github projects was used to manage the development process using an agile approach. The link to my project board is [here.](https://github.com/users/assofiejakobsson/projects/28)



### User Stories

#### EPIC | Product details and information
 - As a customer, I want to view a variety of teeth whitening products that are organic and fluoride-free, so I can choose the one that best suits my needs
 - As a customer, I want to view detailed product descriptions, including ingredients, benefits, and usage instructions, to make an informed decisions.
 - As an administrator, I want to manage product inventory, including adding new products, updating product details, and removing discontinued items.

#### EPIC | Shopping cart and checkout
 - As a customer, I want to securely proceed to checkout and provide shipping and payment information to complete my purchase.
 - As a customer, I want to receive confirmation emails with order details and shipment tracking information after making a purchase.
 - As a customer, I want to create an account, which allows me to save my shipping addresses, track previous orders, and easily make future purchases.


#### EPIC | Order management and analytics
 - As a customer, I want to add products to my cart and have the ability to adjust the quantities or remove items if needed. 
 - As an administrator, I want to have access to an admin panel where I can manage user accounts, and oversee overall website functionality. 
 

#### EPIC | Product management 
 - As a customer, I want to search for specific teeth whitening products by name, category, or specific features. 
 - As a customer, I want to read reviews and ratings from other customers to help me make a more informed decision about a particular product.


####  Epic: Customer suport and marketing 
 - As a customer, I want to receive promotional offers or discounts via email newsletters, providing me with incentives to make repeat purchases.


### The following user stories where labelled as "could have" and "Won't Have" on my project board on Github.

#### EPIC | Order management and analytics
 - As an administrator, I want to generate sales reports and analytics to monitor the performance of the teeth whitening products and identify areas for improvement or marketing strategies.
 - As an administrator, I want to track and manage customer orders, including order fulfillment, shipping, and cancellations if necessary.


####  Epic: Customer suport and marketing 
 - As a customer, I want to have access to a customer support contact or live chat feature to ask questions or get assistance with product selection or any issues I encounter.

#### Colour Scheme
<small><i><a href='https://coolors.co/ffffff-000000-98dff6-5fcafb-1ab2ff-0096ff-4176f8'>Colour palette from Coolors</a></i></small>

![Colour Palette](media/readme/colour palete.png)

The colour scheme of the site is mainly linear-gradient. The rest is boostrap.

The colors are designed with ease of use in mind. 

## Facebook

 <summary>Home Page</summary>

![Facebook](media/readme/Facebook.png)
</details>


## Wireframes

<details>

 <summary>Home Page</summary>

![Home Page](media/readme/homepage_wierframs.png)
</details>


## Security Features and Defensive Design

### User Authentication

User Authentication

Users are securely verified when they sign up and log in.
User passwords are safely stored in a coded format to keep them secure.
Users can log in using their social media accounts safely.
Secure Form Submissions

Protection against unauthorized form submissions is in place.
Password Reset

A secure process is used for resetting passwords.
Custom User Data

User information is kept secure with a customized system.
Encrypted Communication

Data transmission is encrypted to protect user information.
Regular Updates

Frequent updates maintain security and stability.
Security Checks

Regular audits ensure adherence to the latest security standards.
Responsible Reporting

Encouraging responsible reporting of vulnerabilities for timely resolution.
CSRF Protection and Object Retrieval:

The CSRF tokens and middleware are built-in Django mechanisms to handle CSRF protection and mitigate the risks associated with CSRF attacks.
The 'get_object_or_404' function is used to handle object retrieval from the database. This function retrieves an object but raises a 404 HTTP response if the object is not found. This helps avoid exposing sensitive information or potential security vulnerabilities.

### Database Security

 - The database url and secret key are stored in the env.py file to prevent unwanted connections to the database.

## Testing

## Manual Testing




### Header
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Header                 |            |                                                                             |           |
| Site Name (logo)       | Click      | Redirect to home                                                            | Pass      |
| Register Link          | Click      | Visible when the user is not logged in and redirect to the register page.   | Pass      |
| Log In Link            | Click      | Visible when the user is not logged in and redirect to the register page.   | Pass      |
| Log Out Link           | Click      | Visible when the user is logged in and a confirm messages sign out pop up.  | Pass      |
| Sign out               | Click      | Sing out Success message.                                                   | Pass      |
| Seartch                | Click      | Redirect to the product that is entered.                                    | Pass      |
| Shoppingbag            | Click      | Redirect to the shoppingbag page.                                           | Pass      |
| My Account             | Click      | Dropdown menu.                                                              | Pass      |
| Burger menu            | Click      | Dropdown menu (appears on smaller screens)                                  | Pass      |
| Product mangement link     | Display      | If loggedin as admin                                           | Pass      |
| Product mangement link             | Click      | Redirect to Product mangement page                                                              | Pass      |
| Profile link           | Display      | If the user is loggedin                                | Pass      |
| Profile  link          | Click      | redirect to the profile page                               | Pass      |
| Wishlist link           | Display      | If the user is loggedin                                | Pass      |
| Wishlist link            | Click      | redirect to the wishlist page page                               | Pass      |


### Product Mangement
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Product Mangement                 |            |                                                                             |           |
| Product Mangement        | Display      | Product form Whit inputfield for all product information and a fil uplode                                                           | Pass      |
| Cancel btn         | Click      | Redirect to product page.   | Pass      |
| Add Product btn            | Click      | If evrything is enterd correct the new product adds to the product page   | Pass      |



### Profile
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Profile                 |            |                                                                             |           |
| Profile        | Display      | User information and order history                                                            | Pass      |
| Uppdate information btn         | Click      | The information enterd in the userinformation form uppdates and a success messages pop up  | Pass      |
| Order number Link          | Click      | Redirect to order history details  | Pass      |
| BACK TO PROFILE            | Click      | Redirect to profile  | Pass      |


### Wishlist
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Wishlist                 |            |                                                                             |           |
| Wishlist      | Display      | View wishlist                                                           | Pass      |
| Remove from vishlist link          | Click      | The product was removed   | Pass      |
| Add to wishlist btn            | Click      | Product added to the wishlist and the user redirect to the wishlist if the user is loggedin else it will redirekt to sign in  | Pass      |
| SHOP NOW btn            | Click      | Redirect to shopping page   | Pass      |



### Register page 
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Register page          |            |                                                                             |           |
| Register form          | Display    | Inputfields for username, password, register btn. sign in link              | Pass      |
| Register(btn)          | Click      | If everything is correct. The user get a messages to verify the email adress and a confirm messages on the email pop up.        | Pass      |
| confirm email on the email             | Click      | Redirect to the websait whit a confirm message                                                 | Pass      |
| confirm btn             | Click      | Redirect to the login page and a success messages for confirm the email pop up                                                | Pass      |


### Login page 
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Login page             |            |                                                                             |           |
| Login form             | Display    | sign up link, Inputfields for login, password, remember me checkbox, signe in btn. forgot password link                | Pass      |
| sign in (btn)             | Click      |if the login information is correct, Redirects to the home page as logdein whit a success messages                                      | Pass      |
| sign up lik          | Click      | Redirect to the register page                                               | Pass      |
| forget password          | Click      | Redirect to resetpassword whit a confirm messages that we sent a email                                               | Pass      |
| Reset passwor link on email          | Click    | Redirect to resetpassword whit input field for new password and a change btn              | Pass      |
| change btn          | click    | If evrything is correct a confirm and success messages pop up              | Pass      |



### Logout page 
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Logout page          |            |                                                                             |           |
| Logout link          | Display    | If user are loggdein             | Pass      |
| Logout link           | Click      |     Sign out messages pop out whit Sign Out btn to confirm if the user want to logout    | Pass      |
| Sign Out btn             | Click      | Redirect to the home page as logged out whit a succes message                                                 | Pass      |
                                               

### Home page
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Home page              |            |                                                                             |           |
| Welcome and About information      | Display    |                                                                             | Pass      |
| Shop Now btn          | Click      | Redirect to the shopping page                                               | Pass      |
| Subscribe btn          | Click      | It pop up a messages that says if the email are signe up to newsletter                                              | Pass      |


### Shoping page
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Shoping page         |            |                                                                             |           |
| Sort product         | Click      | Dropdown menu whit By price, rating, category or all products                                                   | Pass      |
| By price link          | Click    | Then the cheapest product comes first                                     | Pass      |
| By rating         | Click      | Then the products with the highest rating will come first                                                 | Pass      |
| All products | Click      | Then all products come up                                                  | Pass      |
| Product  | Click      | Redirect to the product page for details and add to buy                                                   | Pass      |


### Product page 
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Product page              |            |                                                                             |           |
| product details           | Display    | View products title, description, reviews.        | Pass      |
| + - (btn)            | Click      | Press plus or minus to get the desired number of products                                                | Pass      |
| ADD TO BAG(btn)              | Click      | The number of products user has chosen adds to the shoping bag and a success messaes pop up                                               | Pass      |
| KEEP SHOPING(btn)            | Click      | Redirect to the shoping page                                                 | Pass      |
| WRITE A REVIEW link              | Click      | If loggdein redirect to review page else login                                              | Pass      |
| EDIT(btn)              | Click      | If loggde in  redirect to the product maneger else it will be no EDIT btn                                             | Pass      |
| DELETE(btn)              | Click      | The product will be deleted if loggedin as admin else it will not be any delete btn                                             | Pass      |
| GO TO SECURE CHECKOUT btn              | Click      | Redirect to the shoping bag.                                             | Pass      |


### Review page 
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Review page              |            |                                                                             |           |
| Review form           | Display    | inputfield for title an textarea for discription and a dropdown menu to rate fom 1-5        | Pass      |
| Submit Review(btn)            | Click      | Redirect to the product page whit the new review                                                | Pass      |


### Shopping bag 
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Shopping bag               |            |                                                                             |           |
| Update link           | Click    | The added number of products will be updated         | Pass      |
| Remove link            | Click      | The products will be removed from the shopping bag                                                 | Pass      |
| KEEP SHOPPING(btn)              | Click      | Redirect to the todo list page                                              | Pass      |
| + - (btn)            | Click      | Press plus or minus to get the desired number of products    | Pass      |
| Secure Checkout           | Click    | Redirect to the checkout page         | Pass      |



### Checkout page 
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Checkout page              |            |                                                                             |           |
| Checkout page           | Display    | View the added products and a checkout form         | Pass      |
| Complete Order(btn)            | Click      | If evrything is correct enterd thene it pop up a thank you and order detail and a success messages and a order conformation to the user email.                                                 | Pass      |
| Adjust Bag(btn)              | Click      | Redirect to the shoppingbag                                              | Pass      |


### Fotter
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Fotter                 |            |                                                                             |           |
| Site Name (logo)       | Click      | Redirect to home                                                            | Pass      |
| Contact information    | Display    | View contact info as email and Phone number and media                                | Pass      |
| Privacy policy  link  | Click    | Redirect to privacy policy information                                | Pass      |
| FAQS    | Click    | Redirect to FAQS page whit info about profile and password                               | Pass      |
| Facebook icon    | Click    | Redirect to the facebookpage                               | Pass      |



### Admin page 
| Element                | Action     | Expected Result                                                             | Pass/Fail |
|------------------------|------------|-----------------------------------------------------------------------------|-----------|
| Admin page              |            |                                                                             |           |
| Admin page            | Display    | As an inloggde admin I can access the admin page else I cant access it  | Pass      |
| Users        | Click      | view all users, change as primary, verified, delete and add users                           | Pass      |
| Orders          | Click      | Change order and delete order                                                             | Pass      |
| Categories      | Click      | Add and delete categories                                                   | Pass      |
| Products              | Click      | Add and delete products                                           | Pass      |
| faqs          | Click      | Change, add or delete faqs                                                            | Pass      |



## Validator Testing

### HTML 


 Not done whit this i have some error most related to the django.


### CSS

The web app was Validate by URI [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) And it was no errors or warnings. See the images below.


![W3C CSS Validator](media/readme/css-validator.png)



### Javascript

7 Five warnings which seems to have with which version I have and the redden seems to be from the fact that they are baked into my django code



<summary>Jshint</summary>

![Jshint](media/readme//stripe_elements.png)
![Jshint](media/readme/js-base.html.png)


### Python

  CI Python Linter

![Python](media/readme/python-linter-context.py.png)
![Python](media/readme/python-linter-urls.py.png)
![Python](media/readme/python-linter-view-bag.py.png)
![Python](media/readme/python-linter-admin-checkout.py.png)
![Python](media/readme/python-linter-checkout-models.py.png)
![Python](media/readme/python-linter-signal.py.png)




### Lighthouse

![Lighthouse](media/readme/lighthous.png)

Lighthouse validation was run on all pages (both mobile and desktop) in order to check accessibility, performance, Best Practices and SEO. At first I received issues for my lables for name. And this is the result after I fixed it.

## Browser Testing
- I have tested the web app on Google Chrome, Firefox, Safari and Edge browsers without more problems than I already recorded. .


## Device Testing
- The web app was viewed on a variety of devices such as Laptop, iPad, samsung s21, s9, zflip 4 and motorola g8 plus. to ensure responsiveness on various screen sizes and bugs. Its responsive.


## Bugs 


I am receiving this error message when I try to edit the account pages for login, log out, and register. I have sought help from a tutor, but they have not seen this before, so there's a risk of damaging many other things. They believe that the problem might be due to having the 'code anywhere' template in Gitpod. The accounts are working, but they lack CSS and a cancel button.

![edit_error](media/readme/edit_error.png)

I have now solved the bug above using tutor, was done a copy of the allauth files using the following command.

![copy_allauth_command](media/readme/copy_allauth_command.png)


I also have a bug in the order history, as it is only visible on the admin page and not on the profile page as it should be. I don't know why, as I haven't had a chance to look into it yet.

My favicon is not showing, and that's because I uploaded it as a zip file in my bucket on Amazon. I haven't had a chance to fix this yet.

I am also missing some CSS due to a lack of time, so it's not a bug

## Deploy the App to Heroku

To deploy your app to Heroku, follow these steps:


 ##Create a new external database.
 - Log in to your ElephantSQL account.
 - Copy the DATABASE_URL located in Config Vars in the Settings Tab.
 - Click "Create New Instance" and follow the steps outlined in the instructions.
 - Copy the ElephantSQL database URL.


##Create the Heroku App.
 - Log in to Heroku or create a new account if you don't have one.
 - On the main page, click the "New" button in the top right corner and select "Create New App" from the drop-down menu.
 - Choose a unique and meaningful app name.
 - Select the region that is closest to your target audience.
 - Click on the "Create App" button.
 - Open the settings tab and click "Reveal Config Vars."
 - Add a config var called DATABASE_URL and paste the ElephantSQL database URL as the value.

##Prepare the environment and settings.py file
 - In your local development environment, create an env.py file in the main directory of your project.
 - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
 - Update the settings.py file to import the env.py file and configure the SECRET_KEY and DATABASE_URL.
 - Comment out the default database configuration in the settings.py file.
 - Save the files and run the necessary migrations.
 - Configure the STATIC files settings using Amazon for static and media files, including the URL, storage path, directory path, root - - path, media URL, and default file storage path.
 - Link the file to the templates directory in Heroku.
 - Change the templates directory variable to TEMPLATES_DIR.
 - Add the Heroku app URL to the ALLOWED_HOSTS list, using the format ['app_name.heroku.com', 'localhost'].
 - Create files/directories:
 - Create requirements.txt file.
 - Create three directories in the main directory; assets, static, and templates.
 - Create a file named "Procfile" in the main directory and add the following: web: gunicorn ConfidentSmile.wsgi.
 - Update Heroku Config Vars:

##Add the following Config Vars in Heroku,

 - SECRET_KEY value.
 - Amazon configuration for handling static and media files.
 - PORT = 8000.


##Deploy,
 - Make sure that the DEBUG setting in your Django settings is set to False.
 - In the Heroku Dashboard, go to the "Deploy" tab of your app.
 - Connect your app to your GitHub repository by selecting the repository and branch.
 - Scroll down to the deployment options and choose whether to enable automatic deploys or deploy manually by clicking the "Deploy Branch" button.
 - Wait for the deployment process to complete.
 - Click View to view the deployed site.
 - The site is now live.

##Forking this repository,
 - Locate the repository at this link Confident Smile.
 - At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
 - A copy of the repository is now created.

##Cloning this repository

 - To clone this repository, follow the below steps,
 - Go to the repository at this link Confident Smile.
 - Under the "Code" button, select your preferred cloning option (HTTPS, SSH, or GitHub CLI) and copy the provided URL.
 - Open your Terminal or command-line interface.
 - Navigate to the directory where you want to clone the repository.
 - Type git clone and then paste the URL you copied from GitHub.
 - Press "Enter" to create the local clone of the repository.


## Languages

- Python
- HTML
- CSS
- Javascript

## Credits

- images to the shop are taken frome amazone.
- This repository was created using the template provided by Code Institute. [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template)
- To get the Django framework installed and set up I followed the Code institutes [Boutique Ado](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+2021_T1/courseware/eb05f06e62c64ac89823cc956fcd8191/40cc2543c48643fda09351da6fa90579/)
- My starting code I get from [Boutique Ado](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopmentecomm)from Code Institut.
- I have received a lot of help from tutors at Code Institute.
- I have had a lot of help from this page when trying to understand what to do and why.[w3schools](https://www.w3schools.com/django/index.php)
- I have used this to create my favicon.[favicon](https://favicon.io/favicon-generator/)
- For my background i have used a gardient and I created that here. [gardient](https://mycolor.space/gradient?ori=to+bottom&hex=%23401EDB&hex2=%231282EB&sub=1)

[Back to Table of contents](#table-of-contents)

