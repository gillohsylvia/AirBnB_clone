# AirBnB clone - Web static
# Concepts
For this project, we expect you to look at these concepts:

* [HTML/CSS](HTML-CSS.md)
* [The trinity of front-end quality](trinity.md)

# Background Context
## Web static, what?
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

* Create simple HTML static pages
* Style guide
* Fake contents
* No Javascript
* No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, please fork or clone the repository `AirBnB_clone` from your partner if you were not the owner of the previous project.

# Resources
Read or watch:

* [Learn to Code HTML & CSS (until “Creating Lists” included)](https://learn.shayhowe.com/html-css/)
* [Inline Styles in HTML](https://www.codecademy.com/article/html-inline-styles)
* [Specifics on CSS Specificity](https://css-tricks.com/specifics-on-css-specificity/)
* [CSS SpeciFishity](https://www.standardista.com/cgi-sys/suspendedpage.cgi)
* [Introduction to HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
* [MDN](https://developer.mozilla.org/en-US/)
* [center boxes](https://css-tricks.com/centering-css-complete-guide/)
# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* What is HTML
* How to create an HTML page
* What is a markup language
* What is the DOM
* What is an element / tag
* What is an attribute
* How does the browser load a webpage
* What is CSS
* How to add style to an element
* What is a class
* What is a selector
* How to compute CSS Specificity Value
* What are Box properties in CSS

# Tasks

## Inline styling
Write an HTML page that displays a header and a footer.

Layout:

* Body:
  * no margin
  * no padding
* Header:
  * color #FF0000 (red)
  * height: 70px
  * width: 100%
* Footer:
  * color #00FF00 (green)
  * height: 60px
  * width: 100%
  * text `Best School` center vertically and horizontally
  * always at the bottom at the page
Requirements:

* You must use the `header` and `footer` tags
* You are not allowed to import any files
* You are not allowed to use the `style` tag in the `head` tag
* Use inline styling for all your tags

![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/ec27ac4a-fc6d-4735-9733-da98bff3e8be)

#### File: 0-index.html

## Head styling
Write an HTML page that displays a header and a footer by using the style tag in the head tag (same as 0-index.html)

Requirements:

* You must use the `header` and `footer` tags
* You are not allowed to import any files
* No inline styling
* You must use the `style` tag in the `head` tag

The layout must be exactly the same as `0-index.html`



![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/121cb68e-9ccd-499c-a7b5-75ff3b219114)

#### File: 1-index.html

## CSS files
Write an HTML page that displays a header and a footer by using CSS files (same as 1-index.html)

Requirements:

* You must use the `header` and `footer` tags
* No inline styling
* You must have 3 CSS files:
  * `styles/2-common.css`: for global style (i.e. the `body` style)
  * `styles/2-header.css`: for header style
  * `styles/2-footer.css`: for footer style

The layout must be exactly the same as `1-index.html`
#### File: 2-index.html, styles/2-common.css, styles/2-header.css, styles/2-footer.css

## Zoning done

Write an HTML page that displays a header and footer by using CSS files (same as `2-index.html`)

Layout:

* Common:
  * no margin
  * no padding
  * font color: #484848
  * font size: 14px
  * font family: `Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;`
  * [icon](![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/c644ac0b-1b44-423c-a8b8-7acbd9d3db6d))
 in the browser tab
* Header:
  * color: white
  * height: 70px
  * width: 100%
  * border bottom 1px #CCCCCC
  * [logo](![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/e1ac4b7a-e6f0-4407-84eb-e6b0ec0ab781))
 align on left and center vertically (20px space at the left)
* Footer:
  * color white
  * height: 60px
  * width: 100%
  * border top 1px #CCCCCC
  * text `Best School` center vertically and horizontally
  * always at the bottom at the page
  
Requirements:

* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 3 CSS files:
  * styles/3-common.css: for the global style (i.e body style)
  * styles/3-header.css: for the header style
  * styles/3-footer.css: for the footer style

![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/7e7e46c6-4861-4abb-bf08-fcd6fdf6ce8e)


#### File: 3-index.html, styles/3-common.css, styles/3-header.css, styles/3-footer.css, images/
  
## Search!

Write an HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on `3-index.html`)

* Container:
  * between `header` and `footer` tags, add a `div`:
    * classname: `container`
    * max width 1000px
    * margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot)
    * center horizontally
* Filter section:
  * tag `section`
  * classname `filters`
  * inside the `.container`
  * color white
  * height: 70px
  * width: 100% of the container
  * border 1px #DDDDDD with radius 4px
* Button search:
  * tag `button`
  * text `Search`
  * font size: 18px
  * inside the section filters
  * background color #FF5A5F
  * text color #FFFFFF
  * height: 48px
  * width: 20% of the section filters
  * no borders
  * border radius: 4px
  * center vertically and at 30px of the right border
  * change opacity to 90% when the mouse is on the button

Requirements:

* You must use: `header, footer, section, button` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 4 CSS files:
  * `styles/4-common.css`: for the global style (`body` and `.container` styles)
  * `styles/3-header.css`: for the header style
  * `styles/3-footer.css`: for the footer style
  * `styles/4-filters.css`: for the filters style
* `4-index.html` won’t be W3C valid, don’t worry, it’s temporary

![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/cbd2b5aa-1703-4c41-84fe-7e5f4bf45bb1)


#### File: 4-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/4-filters.css, images/
  
## More filters

Write an HTML page that displays a header, footer and a filters box.

Layout: (based on `4-index.html`)

* Locations and Amenities filters:
  * tag: `div`
  * classname: `locations` for location tag and `amenities` for the other
  * inside the section filters (same level as the `button` Search)
  * height: 100% of the section filters
  * width: 25% of the section filters
  * border right #DDDDDD 1px only for the first left filter
  * contains a title:
    * tag: `h3`
    * font weight: 600
    * text `States` or `Amenities`
  * contains a subtitle:
    * tag: `h4`
    * font weight: 400
    * font size: 14px
    * text with fake contents
   

Requirements:

* You must use: `header, footer, section, button, h3, h4` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 4 CSS files:
  * `styles/4-common.css`: for the global style (`body` and `.container` styles)
  * `styles/3-header.css`: for the header style
  * `styles/3-footer.css`: for the footer style
  * `styles/5-filters.css`: for the filters style

![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/cde5d1f1-0df0-4461-85d4-6cc60ff2f53f)


#### File: 5-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/5-filters.css, images/
  
## It's (h)over
Write an HTML page that displays a header, footer and a filters box with dropdown.

Layout: (based on `5-index.html`)

* Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter `div`:
  * tag `ul`
  * classname `popover`
  * text should be fake now
  * inside each `div`
  * not displayed by default
  * color #FAFAFA
  * width same as the `div` filter
  * border #DDDDDD 1px with border radius 4px
  * no list display
  * Location filter has 2 levels of `ul/li`:
    * state -> cities
    * state name must be display in a `h2` tag (font size 16px)

Requirements:

* You must use: `header, footer, section, button, h3, h4, ul, li` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 4 CSS files:
  * `styles/4-common.css`: for the global style (`body` and `.container` styles)
  * `styles/3-header.css`: for the header style
  * `styles/3-footer.css`: for the footer style
  * `styles/6-filters.css`: for the filters style
 
![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/868216d5-5e1d-46c3-859f-423a7d275787)


#### File: 6-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, images/
  
# Display results

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on `6-index.html`)

* Add Places section:
  * tag: `section`
  * classname: `places`
  * same level as the filters section, inside `.container`
  * contains a title:
    * tag: `h1`
    * text: `Places`
    * align in the top left
    * font size: 30px
  * contains multiple “Places” as listing (horizontal or vertical) describe by:
    * tag: `article`
    * width: 390px
    * padding and margin 20px
    * border #FF5A5F 1px with radius 4px
    * contains the place name:
      * tag: `h2`
      * font size: 30px
      * center horizontally
     
  
Requirements:

* You must use: `header, footer, section, article, button, h1, h2, h3, h4, ul, li` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 5 CSS files:
  * `styles/4-common.css`: for the global style (i.e. `body` and `.container` styles)
  * `styles/3-header.css`: for the header style
  * `styles/3-footer.css`: for footer style
  * `styles/6-filters.css`: for the filters style
  * `styles/7-places.css`: for the places style

![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/58e0435c-9c4d-42cb-a7f2-53eb74082554)


#### File: 7-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/7-places.css, images/
  
## More details

Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.

Layout: (based on `7-index.html`)

Add more information to a Place `article`:

* Price by night:
  * tag: `div`
  * classname: `price_by_night`
  * same level as the place name
  * font color: #FF5A5F
  * border: #FF5A5F 4px rounded
  * min width: 60px
  * height: 60px
  * font size: 30px
  * align: the top right (with space)
* Information section:
  * tag: `div`
  * classname: `information`
  * height: 80px
  * border: top and bottom #DDDDDD 1px
  * contains (align vertically):
    * Number of guests:
      * tag: `div`
      * classname: `max_guest`
      * width: 100px
      * fake text
      * [icon](![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/7da9f999-0001-4ff8-9b06-4dd826bc55d1))

    * Number of bedrooms:
      * tag: `div`
      * classname: `number_rooms`
      * width: 100px
      * fake text
      * [icon](![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/aec5ac35-9e4b-4a2f-b5a5-c9b674b08891))

    * Number of bathrooms:
      * tag: div
      * classname: number_bathrooms
      * width: 100px
      * fake text
      * [icon](![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/f8af0b77-5822-4ab3-b33e-746a7fd9a06b))

* User section:
  * tag: `div`
  * classname: `user`
  * text `Owner: <fake text>`
  * `Owner` text should be in bold
* Description section:
  * tag: `div`
  * classname: `description`

Requirements:


* You must use: `header, footer, section, article, button, h1, h2, h3, h4, ul, li` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 5 CSS files:
  * `styles/4-common.css`: for the global style (i.e. `body` and `.container` styles)
  * `styles/3-header.css`: for the header style
  * `styles/3-footer.css`: for the footer style
  * `styles/6-filters.css`: for the filters style
  * `styles/8-places.css`: for the places style

![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/f1d60e1d-179a-4539-8c23-51b8f6cf9639)


#### File: 8-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/8-places.css, images/
  
## Full details

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on `8-index.html`)

Add more information to a Place `article`:

* List of Amenities:
  * tag `div`
  * classname `amenities`
  * margin top 40px
  * contains:
    * title:
      * tag `h2`
      * text `Amenities`
      * font size 16px
      * border bottom #DDDDDD 1px
    * list of amenities:
      * tag `ul / li`
      * no list style
      * icons on the left: [Pet friendly](![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/c4efcb16-6ce8-4cab-a2cc-57ff30fc3676)), [TV](![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/b8106855-9fa5-4dee-ad8a-b972254623ac))
, [Wifi](![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/46aa0527-b319-42bf-b8e5-30ab68ea4141))
, etc… feel free to add more
* List of Reviews:
  * tag `div`
  * classname `reviews`
  * margin top 40px
  * contains:
    * title:
      * tag `h2`
      * text `Reviews`
      * font size 16px
      * border bottom #DDDDDD 1px
    * list of review:
      * tag `ul / li`
      * no list style
      * a review is described by:
        * `h3` tag for the user/date description (font size 14px). Ex: “From Bob Dylan the 27th January 2017”
        * `p` tag for the text (font size 12px)
       
    
Requirements:

* You must use: `header, footer, section, article, button, h1, h2, h3, h4, ul, li` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 5 CSS files:
  * `styles/4-common.css`: for the global style (`body` and `.container` styles)
  * `styles/3-header.css`: for the header style
  * `styles/3-footer.css`: for the footer style
  * `styles/6-filters.css`: for the filters style
  * `styles/100-places.css`: for the places style

![image](https://github.com/gillohsylvia/AirBnB_clone/assets/104779232/efbafdc4-d07f-4693-8e11-1e4b45d20d52)


#### File: 100-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/100-places.css, images/
  
## Flex

Improve the Places section by using [Flexible boxes](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) for all Place articles

[Flexbox Froggy](https://flexboxfroggy.com/)


#### File: 101-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/101-places.css, images/
  
## Responsive design

Improve the page by adding [responsive design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design) to display correctly in mobile or small screens.

Examples:

* no horizontal scrolling
* redesign search bar depending of the width
* etc.

#### File: 102-index.html, styles/102-common.css, styles/102-header.css, styles/102-footer.css, styles/102-filters.css, styles/102-places.css, images/
  
12. Accessibility

Improve the page by adding [Accessibility support](https://developer.mozilla.org/en-US/docs/Learn/Accessibility)

Examples:

* Colors contrast
* Header tags
* etc.

#### File: 103-index.html, styles/103-common.css, styles/103-header.css, styles/103-footer.css, styles/103-filters.css, styles/103-places.css, images/
