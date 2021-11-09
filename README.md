# West Ivy Interiors 

![Responsive Design]()

[View the deployed website]()

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
    7. [Testing client stories from UX section](#testing-client-stories-from-ux-section)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [How to run this project locally](#how-to-run-this-project-locally)
9. [Credits](#credits)
    1. [HTML](#html)
    2. [CSS](#css)
    3. [Javascript](#javascript)
    4. [Python](#python)
    4. [Media](#media)
    5. [Text](#text)
    6. [Acknowledgements](#acknowledgements)

## Project Goals


### Developer and Business Goals


## User Experience
### User Stories 

#### Site Users


#### Site Owner 


### Design choices 


### Images 


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
* [jQuery]()
* [SQLite]() database used during development.
* [Django]() used to build site.
* [Heroku]() used to host deployed site.
* [Stripe]() used for the payments functionality
* [Random Key Gen](https://randomkeygen.com/) used to generate secret keys across site.
* [Favicon](https://favicon.io/) used to my favicon. 

### Resources
* 

## Features
### Existing Features 


### Features left to implements


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
* Best Practices 80
* SEO 83

### Javascript
[JS Hint](https://jshint.com/) was used to test my JS. All passed with a few warnings, see below for evidence:
[JS](static/images/testing/js.png)

### Python
[Pep 8](http://pep8online.com/) used to check for errors. All passed but some with a few warnging. Select [here](static/images/testing/python.png) for evidence for no warnings or errors.

### Testing client stories from UX section 

#### Site Users
Tables 


#### Site Owner 
Tables 

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

## Deployment

### Requirements 


### How to run this project locally
 

### Deployment to Heroku


## Credits
* [Code institute](https://codeinstitute.net/) [Boutique Ado mini project](https://github.com/Code-Institute-Solutions/boutique_ado_v1) which my site was based on and adapted to fit my sites requirements. 


### HTML


### CSS


### Javascript


### Python 


### Media
1. Images for shopping bag and home page taken from [Pexels](https://www.pexels.com/)
2. Images for inspiration pages taken from [Soho home](https://www.sohohome.com/inspiration/shop-the-look/living-room)

### Design
* Design Inspiations taken from [SOHO Home](https://www.sohohome.com/new), [H&M Home](https://www2.hm.com/en_gb/home.html), [Nkuku](https://www.nkuku.com/).

### Acknowledgements 
* Tutor support for helping fix bugs and any issues which occurred. 

