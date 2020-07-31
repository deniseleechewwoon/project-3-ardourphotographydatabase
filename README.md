<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

# Ardour Photography Database

# Code Institute - Data Centric Development Milestone Project (3)

This Web Application functions as a Photography Database Gallery to showcase impressive photography works shared by Photographers to users including aspiring photographers and the general public. For aspiring photographers, the purpose will be to learn camera techniques or functions used by others through this cloud sharing platform. For the general public, it will be a leisure platform to view nice photography works and also an avenue for them to explore and hire good photographers.

The website aims to stimulate the photography ecosystem and allow photographers to be noticed through their works and for users to discover photography talents for their projects.

This website is inspired by my [User Centric Frontend Development Milestone Project (1)](https://deniseleechewwoon.github.io/project-1-ardourphotography/index.html) where it features Adour Photography - a fictitious Photography company that has existing photography talents. Hence, Adour Photography Database will be mandatory or highly encouraged to be used by Adour Photography's photographers to showcase their work to the general public. At the same time, it gives other colleagues a platform to share photography techniques.


The live site for this Project-Ardour Photography Database may be viewed [here](https://dlcw-ardour-photography.herokuapp.com/).

 
## UX

The target audience for the website will be
* Photography enthusiasts
* General public doing leisure browsing or looking for photography talents
 
In order to achieve the intent of capturing the viewers attention to the photography works that are showcased, the website aims to portray a very simple and minimalist feel. The use of blank space and clean minimalist icons to allow the viewer attention to be focused mainly on the photography works. A five-colour palette scheme consisting of mostly warm colours was maintained throughout the whole website design. This is consistent and evident through the the wireframe. A copy of the wireframe me be viewed [here](https://drive.google.com/file/d/1ZPt-NCnP-v5vOl3gIXFhYpDju0n0uf9y/view?usp=sharing).

Besides the look, the website also ensure that it is user-friendly and interactive. When a user first enter the website, they will be greeted by a welcoming photo followed by three navigation buttons which clearly specifies the intent - view gallery, add a new entry and view various photography genre.

The use of minimal clicks the navigate the website allow users to have a good browsing experience when going through the website. Icons were placed with thought to allow users to intuitively click on them to navigate pages. Photography enthusiasists will enjoy the process of viewing other professional works and sharing of their own knowledge in photography. A commenting section was added to allow some degree of interaction among the enthusiasists and the general public. They may add, edit or event delete entries uploaded. For the general public,they will also find a joy in viewing the beautiful works of the photographers and can even be able to reach out to them for any projects opportunities. With this in mind, when viewers click view more, the details of each entry including email contact will be displayed.

Apart from that, the display of the photography entries differs form a desktop and mobile view to allow the same experience on all devices and platforms. All in all, the website is created with the intent to fulfil the users' needs in a straighforward and forthcoming approach.

## Features
### Existing Features
 
* [Landing Page](https://dlcw-ardour-photography.herokuapp.com/)
    1. Animated Page, slides in together with Company Logo from top of page - Brings some life to the static page.
    2. The use of a landing page is to welcome the users before they enter the gallery page with informative content.

* [Add Page- Create](https://dlcw-ardour-photography.herokuapp.com/photo/create)
    1. Create new Photography entry to the database comprising of the following
    - Title
    - Name of Photographer
    - Email contact
    - Location 
    - Database
    - Select a Photography Type
    - Photography Description
    - Photography Details (Camera Make and Model, Focal Length, Aperture, Shutter Speed and ISO used)
    - Upload Image via the Cloudinary Platform

* [View Gallery Page - Read](https://dlcw-ardour-photography.herokuapp.com/photos)
    1. Clear Nav Bar stack to the top of the page to allow user to navigate to other Pages
    2. Search Bar feature on top of page to allow user to search through gallery Database by category and searh terms
    3. Once the page is scroll down, a "Return to Top" Button appears at the buttom right hand corner of the page to help user navigate easily back to the top of the page.
    4. For each photgraphy entry, the image uploaded can be seen clearly on the left and with the right displaying photography techqniques used. With this, it will clearly allow users to get essential information about the photgraphy entry. At the far right of each entry, there are three simple icons, namely, 1)view more, 2)edit and 3)delete to allow easy navigation to view more or make other changes to the entry. In order to ensure that it is foolproof, the tooltip function was added upon hovering over the icons to ensure that users understand what each icon allow them to do. To increase interativeness, the icon will also animate upon hover.
    5. Each photograph will be displayed in a simple lightbox with toggle click feature.
    6. Basically, from this page, users may navigate to a) create new entries by clicking Add form Navbar, b) read all the entries by scrolling through the page and click on the eye icon to view more information and comments, c) update each entry by clicking on the pencil icon and d) delete entry by clicking on the bin icon.

* [Edit Page - Update](https://dlcw-ardour-photography.herokuapp.com/photo/update/5f1a5c06b99c35e5d6863573)
    1. Edit all details of the photography entry
    2. Upload new photograph

* [Delete Page - Delete](https://dlcw-ardour-photography.herokuapp.com/photo/delete/5f1a5c06b99c35e5d6863573)
    1. Delete the photography entry
    2. A confirmation message shown on top of the page to reassure the user's intent to delete
    3. Show the photography entry details to the users again
    4. If user select cancel, it will bring them back to the view gallery page

* [View Photo Entry Page](https://dlcw-ardour-photography.herokuapp.com/photo/details/5f1a5c06b99c35e5d6863573)
    1. View more details of each entry
    2. Each photograph will be displayed in a simple lightbox with toggle click feature.
    3. Comments section included with CRUD feature for the comments as well.

* [Photography Genre Page](https://dlcw-ardour-photography.herokuapp.com/photos/genre) 
    1. Feature the different types of photography with images to illustrate
    2. Allow users to gain some knowledge in types of photography available

### Features left to be implemented
- Feature 1 - Login authentication and allow users to only make amendments to own uploaded work or comments
- Feature 2 - Implement more complex search features stack to allow users to search more areas. For instance, Camera Make used to take the photograph
- Feature 3 - Like or Share the photography entries to user's social media profile

## Technologies Used
* [HTML](https://www.w3schools.com/html/) - standard markup language for creating web pages
    - HTML is basically used throughout the whole document to construct the various segments and putting things together

* [CSS](https://www.w3schools.com/css/) - describes the style of the HTML document
    - CSS is important to maintain the look, style and feel of the website

* [Bootstrap 4.4](https://getbootstrap.com/docs/4.4/getting-started/introduction/) - popular framework for building responsive, mobile-first sites
    - Bootstrap framework makes things easier to have basic features and minimised the use of css styling with bootstrap features

* [Javascript](https://www.youtube.com/watch?v=gnDOjWUSHks)
    - Javascript is used to create a responsive lightbox - modal image gallery
    - Javascript is used for the uploading of images from Cloudinary

* [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

* [Python](https://www.python.org/)
    - General-purpose coding language used with Flask Application in this project

* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    - Text-based template language and thus can be used to generate any markup as well as source code. The Jinja template engine allows customization of tags, filters, tests, and globals.

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - Web application framework used for the project

* [MongoDB](https://www.mongodb.com/cloud/atlas/lp/try2?utm_source=google&utm_campaign=gs_apac_singapore_search_brand_atlas_desktop&utm_term=mongodb%20atlas&utm_medium=cpc_paid_search&utm_ad=e&gclid=EAIaIQobChMI_-Ga0cSh6gIVWX8rCh1YWQCzEAAYASAAEgKjNvD_BwE)
    - Database to be updated for CRUD features

* [Google Fonts](https://fonts.google.com/)
    - Used of appropriate fonts for website theme

## Testing
The site is manually tested on a macbook pro, windows laptop, andriod mobile device (Samsung note 9) and ipad to ensure the responsiveness and that all the links work well.

* Page content fits device width and is responsive on all devices
* Text on the page is readable
* Links and tap targets are sufficiently large and touch-friendly
* The navbar to access all the Sections (View Gallery > Add > Photography Genre) is tested to ensure it works well

On all platforms, the following were tested

1. Landing Page
    - The animated graphics in effect of the page works well with every refresh
    - The button is able to bring the users to the main section works well
2. Gallery Page
    - The graphics show up without error on every refresh
    - Navbar links work well
    - Searchbar: Selected a photography category and enter a blank search term displays all entries of the search term
    - Searchbar: Selected a photography catergory with a specific search term return a result of only "search term" within that category
    - Upon click on image, it displayed well in a lightbox
    - Side icons on each entry display tooltip well and brings users to respective pages well. Animated icon also work well.
    - Return to top shows up with scrolling of page and upon click return to top of page
3. View Entry Page
    - Details were displayed well with click from main gallery page
    - CRUD works well for each commenting
    - Added a comment, edited and deleted it, works well
4. Edit Entry Page
    - Details displayed were of selected entry from main gallery page
    - Tried to update all fields and uploaded a new image and it displays well and reeturn to main gallery page
5. Delete Entry Page
    - Details displayed were of selected entry from main gallery page
    - Click on Delete and Entry was deleted and return to main gallery page
    - Click on cancel and entry was not deleted and return to main gallery page
6. Photography Genre Page
    - The graphics and description show up without error on every refresh

The site was manually tested on different browsers (Chrome, Safari, Morzilla Firefox and Internet Explorer).
The site works well on all browsers.

The site was also tested using online platform [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) and results show that page is mobile friendly and easy to use on a mobile device.

## Deployment
This site is hosted by Heroku and directly deployed from the master branch and Github. A repository was firstly created using github and commits were pushed to the master branch. Materials are pushed to the GitHub repository with git add, git commit, git push and git push heroku master
Eventually, the deployed site will be updated automatically upon any new commits on heroku. 

## Credits

### Content
- The text for the various sections were taken and modified from the following websites

### Media
- The photos used in this site were all obtained from [freepik](https://www.freepik.com/home) - a stock image library. Please refer to the full credits and link for each image [here](https://drive.google.com/open?id=1RW7ISUwm2yo8boamNulaxKoPbtTykVB8).

### Acknowledgements
- CSS Styling by [Bootstrap4](https://getbootstrap.com/).
- All fonts used for this site are obtained from [google fonts](https://fonts.google.com/).


### This website created is for educational use.