# West Ivy Interiors 

![Responsive Design](static/images/testing/iamresponsive.png)

[View the deployed website](https://ms4-cc-west-ivy.herokuapp.com/)

## Table of Content 
1. [Project Goals](#project-goals)
2. [User Experience](#user-experience)
    1. [User Stories](#user-stories)
    2. [Design choices](#design-choices)
    3. [Fonts](#fonts)
    4. [Colours](#colours)
    5. [Wireframes](#wireframes)
3. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Features left to Implement](features-left-to-implement)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [Accessibility](#accessibility)
    4. [Performance](#performance)
    5. [Javascript](#javascript)
    6. [Python](#python)
    7. [Testing user stories from UX section](#testing-user-stories-from-ux-section)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [How to run this project locally](#how-to-run-this-project-locally)
9. [Credits](#credits)
    1. [Code](#code)
    4. [Media](#media)
    5. [Text](#text)
    6. [Acknowledgements](#acknowledgements)

## Project Goals
### Developer and Business Goals
* Create a professional website which is userfriendly, innovative and stylish.
* All frameworks used to be fully functioning. 
* To add this to my portfolio and be proud of the work I have created.
* All pages to be functioning properly
* The site to be fully responsive.
* User enjoy their shopping experience and return to the website.
* User to love our products.
* Users to follow our social media pages.

## User Experience
### User Stories 

| User Story | As A/An  | I want to be able to | So that I can |
|---|---|---|---|
| 1 | Site User | Easy to view a total of my purchases | Keep tabs on spending |
| 2 | Site User | View individual product details | Learn more about the product |
| 3 | Site User | View a list of products  | Choose what I would like to purchase |
| 4 | Site User | Easily register for an account | Be able to view my recent purchases and sign in when I return |
| 5 | Site User | Easily login and out | Access my purchase history and ensure easier checkout for next time |
| 6 | Site User | Receive email confirmation after registering  | Verify my registration  |
| 7 | Site User | Sort through products easily | Find the product I am looking for quickly |
| 8 | Site User | Search for a product by using name and description | Find a specific product |
| 9 | Site User | View items in my bag | View total cost of my bagged items. |
| 10 | Site User | Adjust the quantity of items in my bag | Easily make changes to my shopping bag |
| 11 | Site User | Easily and securely enter my payment information  | Checkout quickly and safely |
| 12 | Site User | Receive confirmation email after checkout | Verify my order |
| 13 | Store Owner | Edit and update product details | Change product prices, images and description  |
| 14 | Store Owner | Add a product | Add a new item to my website |
| 15 | Store Owner | Delete a product | Remove items from my website that are no longer on sale |


### Design choices 
* I chose a simple design for my website with a white background to ensure all images took center stage so the user can clearly see which product they like. 
* The font I chose was simple yet easy to read and eligant, in black to ensure good all uses can read the writing clearly. 

### Images 
* Images for my website are taken from [Pexels](https://www.pexels.com/) and [Soho home](https://www.sohohome.com/inspiration/shop-the-look/living-room). They suit the theme of the website and I am happy with the look and feel.

### Wireframes 
Select each of the below to view my wireframes: 

* [Base](static/images/testing/wireframes/basewf.png)
* [Products ](static/images/testing/wireframes/productswf.png)
* [Product Detail](static/images/testing/wireframes/product-detailwf.png)
* [Dining inspiration](static/images/testing/wireframes/dininginspwf.png)
* [Lighting inspiration](static/images/testing/wireframes/lightinginspwf.png)
* [Home Decor inspiration](static/images/testing/wireframes/homeinspwf.png)
* [Profile](static/images/testing/wireframes/profilewf.png)
* [Our Story](static/images/testing/wireframes/outstorywf.png)
* [Contact us](static/images/testing/wireframes/contactuswf.png)
* [Product Management](static/images/testing/wireframes/pmwf.png)
* [Login](static/images/testing/wireframes/loginwf.png)
* [Logout](static/images/testing/wireframes/logoutwf.png)
* [Register](static/images/testing/wireframes/registerwf.png)
* [Edit Products](static/images/testing/wireframes/editproductwf.png)


## Technologies Used 

### Languages 
* HTML 
* CSS 
* Python 
* JavaScript

### Frameworks, Programs and Libraries
* [Google Fonts](https://https://fonts.google.com/) has been used for my fonts.
* [Font awesome](https://fontawesome.com/) has been used throughout my wesbite.
* [Bootstrap](https://getbootstrap.com/)
* [GitHub](https://github.com/) used as primary for my code.
* [Balsamiq](https://balsamiq.com/) used to create wireframes.
* [jQuery](https://jquery.com/)
* [SQLite](https://www.sqlite.org/index.html) database used during development.
* [Django](https://www.djangoproject.com/) used to build site.
* [Heroku](https://dashboard.heroku.com/) used to host deployed site.
* [Stripe](https://stripe.com/) used for the payments functionality
* [Random Key Gen](https://randomkeygen.com/) used to generate secret keys across site.
* [Favicon](https://favicon.io/) used to my favicon. 
* [AWS S3](https://aws.amazon.com/) - used for storage of static and media files on the deployed site.
* [Autoprefixer](https://autoprefixer.github.io/) - used for adding CSS vendor prefixes to increase compatibility across browsers.
* [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/).


## Features
### Existing Features 
* Responsive front end design.
* Repsonsive navbar taking users to the requested page.
* User profiles, including order history and delivery details.
* Signin, register, login, logout functionality.
* Toasts, which tell the user what action has been done in the top right corner of the screen.
* Automatic emails.
* Links on home page to the 4 different product categories. 
* Best sellers on the home page with link to that product's details.
* Product filtering.
* Bag total and ability for the user to update the shopping bag.
* Checkout page with form for the user to complete with the option to store their data.
* Payment using Stripe.
* Our inspiration page, to give user's inspiration about their home interiors.
* Links to social media page's at the bottom of the screen.
* Contact us and about us pages to give the users a better understanding out West Ivy.

### Features left to implements
* Adding the option for users to remove their profile.
* Create social media accounts for West Ivy and add the link to the footer.

## Testing

### HTML Validation
The [W3 Validator](https://validator.w3.org/#validate_by_input) was used to test my HTML. All passed with warning apart from the pages using crsipy field which some errors occured. I have researched these errors and they will not affect my project. See below evidence:
* [Base HTML](static/images/testing/basehtml.png)
* [Bag HTML](static/images/testing/baghtml.png)
* [Checkout HTML](static/images/testing/checkouthtml.png)
* [Contact us HTML](static/images/testing/contactushtml.png)
* [Dining Inspiration HTML](static/images/testing/dininginspohtml.png)
* [Edit Product HTML](static/images/testing/editproducthtml.png)
* [Home Inspiration HTML](static/images/testing/homeinspohtml.png)
* [Lighting Inspiration HTML](static/images/testing/lightinginspohtml.png)
* [Login HTML](static/images/testing/loginhtml.png)
* [Order Success HTML](static/images/testing/ordersuccesshtml.png)
* [Our Story HTML](static/images/testing/ourstoryhtml.png)
* [Product Detail HTML](static/images/testing/product-detailhtml.png)
* [Product HTML](static/images/testing/producthtml.png)
* [Product Management HTML](static/images/testing/productmanagehtml.png)
* [Profile HTML](static/images/testing/profilehtml.png)
* [Register HTML](static/images/testing/registerhtml.png)
* [Sign out HTML](static/images/testing/signouthtml.png)

### CSS Validation
The [W3C Validator Service](https://jigsaw.w3.org/css-validator/#validate_by_uri) was used to test my CSS. All passed using direct input, see evidence below:
* [Base CSS](static/images/testing/basecss.png)
* [Checkout CSS](static/images/testing/checkoutcss.png)
* [Profile CSS](static/images/testing/profilecss.png)

### Performance 
[Google lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test my performance. See [here](static/images/testing/performance.png) for evidence and below for details:
* Performance 71 
* Accessibility 100
* Best Practices 70
* SEO 83

### Javascript
[JS Hint](https://jshint.com/) was used to test my JS. All passed with a few warnings, see below for evidence:
[JS](static/images/testing/js.png)

### Python
[Pep 8](http://pep8online.com/) used to check for errors. All passed with no errors or warning, please select each of the below option with a screenshot containing evidence for all pages in that folder. Any errors I have left are no from code I have written.

* [Bag](static/images/testing/bagpython.png)
* [Checkout](static/images/testing/checkoutpython.png)
* [Home](static/images/testing/homepython.png)
* [MS4_CC_WEST_IVY](static/images/testing/westivypython.png)
* [Products](static/images/testing/productspython.png)
* [Profiles](static/images/testing/profilespython.png)
* [Project Level](static/images/testing/projectlevelpython.png)


### Testing user stories from UX section 
| Feature | Action | Expected Result | Actual Result | Evidence |
|---|---|---|---|---|
| 1. Easy view a total of my purchases | Keep tabs on spending | Users should see a pop up with the total of all items in back when an item is added. User should be able to access the checkout at anytime to view a list of purchases | Works as expected | ![ALT](/static/images/testing/bagux.png) ![ALT](/static/images/testing/bag1ux.png) |
| 2. View individual product details | Learn more about the product | User is able to select an image which will take them to a screen displaying the product and more information about it | Works as expected | ![ALT](/static/images/testing/productux.png) |
| 3. View a list of products | Choose what I would like to purchase | User is able to select view products easily but selecting the 'view products' button on the home page or 'All products' on the menu bar under 'Products | Works as expected | ![ALT](/static/images/testing/productsux.png) |
| 4. Easily register for an account | Be able to view my recent purchases and sign in when I return | User is able to register for an account and sign in when they return | Works as expected | ![ALT](/static/images/testing/registerux.png) |
| 5. Easily login and out | Access my purchase history and ensure easier checkout for next time | User is able to login to to their profile and see their details and a list of recent purchases | Works as expected | ![ALT](/static/images/testing/loginux.png) |
| 6. Receive email confirmation after registering | Verify my registration | User registers and received a confirmation email | Works as expected | ![ALT](static/images/testing/registeremailux.png) |
| 7. Sort through products easily | Find the product I am looking for quickly | User is able to sort products on the website in order to find what they are looking for. | Works as expected | ![ALT](/static/images/testing/sortux.png) |
| 8. Search for a product by using name and description | Find a specific product | User is able to use the search bar to find a specific product | Works as expected | ![ALT](static/images/testing/searchux.png) |
| 9. View items in my bag | View total cost of my bagged items. | User is able to view shopping bag and see a list of all items in the bag with description, price and quantity | Works as expected | ![ALT](/static/images/testing/bag2ux.png) |
| 10. Adjust the quantity of items in my bag | Easily make changes to my shopping bag | User is able to add, remove and change the quantity of items in their shopping bag | Works as expected | ![ALT](/static/images/testing/changesux.png) |
| 11. Easily and securely enter my payment information | Checkout quickly and safely | User is able to checkout knowing their details are secure | Works as expected | ![ALT](/static/images/testing/checkoutux.png) |
| 12. Edit and update product details | Change product prices, images and description | Site owner is able to edit, update and remove product details  | Works as expected | ![ALT](/static/images/testing/adminux.png) |
| 13. Add a product | Add a new item to my website | Site owner is able to add products to the website | Works as expected | ![ALT](/static/images/testing/addux.png) |
| 14. Delete a product | Remove items from my website that are no longer on sale | Site owner is able to delete a product from the website when it is no longer required | Works as expected | ![ALT](/static/images/testing/deleteux.png) |

### Devices Used for Testing
Tested on Macbook Pro and iPhone xs.

## Bugs found and fixed during development 
* Removing items from the shopping bag was not working with the below code: 
```
$('.remove-item').click(function(e) {
        var csrfToken = "{{ csrf_token }}";
        var itemId = $(this).attr('id').split('remove_')[1];
        var url = `/bag/remove/${itemId}/`;

        $.post(url, data)
         .done(function() {
             location.reload();
         });
    })
```
with the help of student support we realised I had missed off ```var data = {'csrfmiddlewaretoken': csrfToken}; ``` once this was added into the JS, the delete button worked perfectly.

* My toasts were not closing when the cross was selected with the below code:
```
<script type="text/javascript">
          $('.toast').toast('show');
        </script>
```
with the help of Sean at tutor support I amended the code with a more up to date JS code and it works correctly. Code below:
```
let toastElList = [].slice.call(document.querySelectorAll('.toast'))
          let toastList = toastElList.map(function (toastEl) {
            return new bootstrap.Toast(toastEl)
          });
          toastList.forEach(toast => toast.show());
          const buttonClose = document.querySelectorAll('.btn-close');
          buttonClose.forEach(btn => btn.addEventListener('click', event => {
          const toast = document.querySelector('.toast.custom-toast.fade.show');
          toast.classList.remove('show');
          toast.classList.add('hide')
          }))
```

* Shopping bag was not repsonsive for mobile devices. I added to below code for screen 700px and below:
```
@media screen and (max-width: 700px) {
    .checkout-items {
        display: block !important;
    }
    .checkout-subheadings {
        display: none;
    }
}
```
This code worked and the shopping back is now responsive. 

## Deployment
The IDE chosen was Gitpod and deployment to Heroku.

### How to run this project locally
1. From my project's repo on [GitHub](https://github.com/carolinecole25/MS4_CC_west_ivy), download the files by clicking on "Code" and getting the zip folder.
2. Open the project's folder and install all the requirements from the requirements.txt file with the below command:
```
pip3 install -r requirements.txt.
```
3 Set up your environment variables in an env.py file, ensuring you add env.py to gitignore as per below:
```
os.environ["DEVELOPMENT"] = "True"
os.environ('STRIPE_PUBLIC_KEY', 'YOUR_STRIPE_PUBLIC_KEY')
os.environ('STRIPE_SECRET_KEY', 'YOUR_STRIPE_SECRET_KEY')
os.environ('STRIPE_WH_SECRET', 'YOUR_STRIPE_WH_SECRET')
os.environ('SECRET_KEY', 'YOUR_DJANGO_SECRET_KEY') 
```
4. Migrate the models with the below commands in this same order:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
5. Set up the database by loading the fixtures which can be found in MS4_CC_west_ivy/products/fixtures in the following order:
```
python3 manage.py loaddata categories

python3 manage.py loaddata products
```
6. Create a superuser for yourself so you can do admin tasks using the below command:
```
python3 manage.py createsuperuser
```
7. Run the project locally with the below command:
```
python3 manage.py runserver
```

### Deployment to Heroku
1. Set up you [AWS account](https://aws.amazon.com/) which is where your static and media files will be hosted for your deployed site.
2. Add a public access S3 basket, more informaiton [here ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html).
3. Connect this to your Django application, more information [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).
4. Login to Heroku and create your new app and select the region closest to you.
5. In your IDE, add a Procfile with the below code:
```
web: gunicorn bojeaux.wsgi:application
```
6. In Heroku, under settings, add your Config Vars which should include the below:
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* DATABASE_URL
* SECRET_KEY
* STRIPE_PUBLIC_KEY
* STRIPE_SECRET_KEY
* STRIPE_WH_SECRET
* USE_AWS - set to `True`
7. In settings file, add in the below code:
```
ALLOWED_HOSTS = ['your-app-url', 'localhost']
```
8. In settings file, replace DATABASES with the below code:
```
DATABASES = {
 'default': dj_database_url.parse('your-url-goes-here')
}
```
9. Git add, commit and push code to GitHub.
10. On Heroku under the deploy tab, connect to github and choose your git repository then select auto deploy. This will take a few minutes to load, once loaded a link for your deployed site will appear. 
11. Now you can set up with your email account for sending emails. Create an email account and ensure you have 2-step verification turn and generate an App Password under settings. Add the passwork to Config Vars along with Email host pass, see below:
* EMAIL_HOST_PASS
* EMAIL_HOST_USER
10. Your site should now be deployed and functioning. 

## Credits
* [Code institute](https://codeinstitute.net/) [Boutique Ado mini project](https://github.com/Code-Institute-Solutions/boutique_ado_v1) which my site was based on and adapted to fit my sites requirements. 

### Code
* [Code institute](https://codeinstitute.net/) course material, particularly the Boutique Ado mini project, from which I have reused code for several functionalities.
* [Django documentation](https://docs.djangoproject.com/en/3.2/) for deeper understanding on how models, views and urls come together to build apps.
* [Bootstrap](https://getbootstrap.com/) code for many templates throughout the site.
* [Stripe](https://stripe.com/docs) documentation for better understanding on how webhooks work.

### Media
1. Images for shopping bag and home page taken from [Pexels](https://www.pexels.com/)
2. Images for inspiration pages taken from [Soho home](https://www.sohohome.com/inspiration/shop-the-look/living-room)

### Design
* Design Inspiations taken from [SOHO Home](https://www.sohohome.com/new), [H&M Home](https://www2.hm.com/en_gb/home.html), [Nkuku](https://www.nkuku.com/).

### Acknowledgements 
* Tutor support, thank for your support for helping fix bugs and any issues which occurred. 
* Mo, my mentor thanks for your support on this project.

