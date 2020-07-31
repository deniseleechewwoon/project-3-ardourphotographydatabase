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
 
* [Landing Page] (https://dlcw-ardour-photography.herokuapp.com/)
    1. Animated Page, slides in together with Company Logo from top of page - Brings some life to the static page.
    2. The use of a landing page is to welcome the users before they enter the gallery page with informative content.

* [Add Page- Create] (https://dlcw-ardour-photography.herokuapp.com/photo/create)
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

* [View Gallery Page - Read] (https://dlcw-ardour-photography.herokuapp.com/photos)
    1. Clear Nav Bar stack to the top of the page to allow user to navigate to other Pages
    2. Search Bar feature on top of page to allow user to search through gallery Database by category and searh terms
    3. Once the page is scroll down, a "Return to Top" Button appears at the buttom right hand corner of the page to help user navigate easily back to the top of the page.
    4. For each photgraphy entry, the image uploaded can be seen clearly on the left and with the right displaying photography techqniques used. With this, it will clearly allow users to get essential information about the photgraphy entry. At the far right of each entry, there are three simple icons, namely, 1)view more, 2)edit and 3)delete to allow easy navigation to view more or make other changes to the entry. In order to ensure that it is foolproof, the tooltip function was added upon hovering over the icons to ensure that users understand what each icon allow them to do. To increase interativeness, the icon will also animate upon hover.
    5. Each photograph will be displayed in a simple lightbox with toggle click feature.
    6. Basically, from this page, users may navigate to a) create new entries by clicking Add form Navbar, b) read all the entries by scrolling through the page and click on the eye icon to view more information and comments, c) update each entry by clicking on the pencil icon and d) delete entry by clicking on the bin icon.

* [Edit Page - Update] (https://dlcw-ardour-photography.herokuapp.com/photo/update/5f1a5c06b99c35e5d6863573)
    1. Edit all details of the photography entry
    2. Upload new photograph

* [Delete Page - Delete] (https://dlcw-ardour-photography.herokuapp.com/photo/delete/5f1a5c06b99c35e5d6863573)
    1. Delete the photography entry
    2. A confirmation message shown on top of the page to reassure the user's intent to delete
    3. Show the photography entry details to the users again
    4. If user select cancel, it will bring them back to the view gallery page

* [View Photo Entry Page] (https://dlcw-ardour-photography.herokuapp.com/photo/details/5f1a5c06b99c35e5d6863573)
    1. View more details of each entry
    2. Each photograph will be displayed in a simple lightbox with toggle click feature.
    3. Comments section included with CRUD feature for the comments as well.

* [Photography Genre Page] (https://dlcw-ardour-photography.herokuapp.com/photos/genre) 
    1. Feature the different types of photography with images to illustrate
    2. Allow users to gain some knowledge in types of photography available

### Features left to be implemented
- Feature 1 - Login authentication and allow users to only make amendments to own uploaded work or comments
- Feature 2 - Implement more complex search features stack to allow users to search more areas. For instance, Camera Make used to take the photograph
- Feature 3 - Like or Share the photography entries to user's social media profile

## Technologies Used
In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
## Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.
Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.
For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:
1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.
You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.
If this section grows too long, you may want to split it off into a separate file and link to it from here.
## Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).
In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.
## Credits
### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
### Media
- The photos used in this site were obtained from ...
### Acknowledgements
- I received inspiration for this project from X
