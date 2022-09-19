# Mindful Massage

![Multiple Device Demo](./docs/readme/images/multi-site-v1.png)

## Live Site

|Heroku|:|Render|
|--|-|--:|
|[Mindful Massage on Heroku](https://mindful-massage.herokuapp.com)|:|[Mindful Massage on Render](https://mindful-massage.onrender.com)|

## Repository

[GitHub hosted repository](https://github.com/DaveyJH/ci-portfolio-four)
***

## Table of Contents

- [Mindful Massage](#mindful-massage)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Table of Contents](#table-of-contents)
  - [Objective](#objective)
  - [Brief](#brief)
  - [UX &#8722; User Experience Design](#ux--user-experience-design)
    - [User Requirements](#user-requirements)
      - [First Time User](#first-time-user)
      - [Returning User](#returning-user)
        - [Client](#client)
        - [Staff](#staff)
      - [Owner](#owner)
      - [Developer](#developer)
    - [Initial Concept](#initial-concept)
      - [Wireframes](#wireframes)
        - [Samples from Mobile](#samples-from-mobile)
        - [Complete wireframes](#complete-wireframes)
      - [Colour Scheme](#colour-scheme)
        - [Contrast](#contrast)
      - [Typography](#typography)
        - [Headings](#headings)
        - [Body](#body)
      - [Imagery](#imagery)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
  - [Data Model](#data-model)
    - [PostgreSQL](#postgresql)
  - [Technologies Used](#technologies-used)
    - [Python Packages](#python-packages)
    - [Other Tech](#other-tech)
      - [*Instant Eyedropper*](#instant-eyedropper)
      - [*WebAIM Contrast Checker*](#webaim-contrast-checker)
      - [*Windows Snipping Tool*](#windows-snipping-tool)
      - [*Balsamiq*](#balsamiq)
      - [*Font Awesome*](#font-awesome)
      - [*Google Fonts*](#google-fonts)
      - [*Multi Device Mockup Generator*](#multi-device-mockup-generator)
      - [*W3C Markup Validation Service*](#w3c-markup-validation-service)
      - [*flake8*](#flake8)
      - [*Visual Studio Code*](#visual-studio-code)
      - [VSCode Extensions](#vscode-extensions)
  - [Testing](#testing)
  - [Bugs](#bugs)
    - [Current](#current)
    - [Resolved](#resolved)
  - [Development](#development)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)
    - [Personal Development](#personal-development)

***

## Objective

This site is to represent capabilities with the django framework. It should
employ full Create, Read, Update, Delete (CRUD) functionality.

The assessment checklist is available to view in the
[`docs/` directory](https://github.com/DaveyJH/ci-portfolio-four/tree/main/docs)
of the project repository.

***The needs within this project are not genuine and are made purely for the
purpose of completing my Code Institute fourth project***

***

## Brief

Mindful Massage : a massage therapist and therapies site. The site should show
the therapists employed at (the entirely made up) Mindful Massage Spa, as well
as the therapies offered. Users should be able to sign in and leave reviews, as
well as view reviews left by others.

Full CRUD functionality should be achievable through the front-end of the site,
with different levels of users having specific actions and interactions.

***

## UX &#8722; User Experience Design

### User Requirements

The original user stories were based on pseudo personas created for the project.
Due to time constraints and other priorities, the scope of the project has been
reduced from the initial conception and is well documented through version
control. The original user
[personas are viewable here.](https://github.com/DaveyJH/ci-portfolio-four/wiki/User-Personas)

[Epics](https://github.com/DaveyJH/ci-portfolio-four/issues?q=is%3Aissue+label%3A%22user+story%22+-label%3Atest+label%3Aepic+)
were created for the initial concepts that were to be included within the site.
Each epic issue consists of a user type, referencing the persona document linked
above, a required functionality and the benefit it provides. The original user
epics have been broken down into smaller issues for the development process.

As part of the testing procedure, I wrote very
[granular user stories](https://github.com/DaveyJH/ci-portfolio-four/issues?q=is%3Aissue+label%3A%22user+story%22+-label%3Aepic+-label%3Atest)
to ensure all functionality was as expected. Note that I have referenced this in
the [personal development](#personal-development) section at the end of this
document.

Below is a non-exhaustive list of some of the user stories:

#### First Time User

> *"As a potential customer, I would like to know what the site is about"*
>
> *"As a non-registered user, I would like to explore some of the site"*
>
> *"As a non-registered user, I would like to be able to sign up"*
>
> *"As a potential customer, I would like to view the main services offered"*

#### Returning User

##### Client

> *"As a returning user, I would like to be able to log in to my account"*
>
> *"As a returning user, I would like to be able to view reviews written by me"*
>
> *"As a returning user, I would like to be able to edit reviews written by me"*
>
> *"As a returning user, I would like to be able to delete reviews written by
> me"*

##### Staff

> *"As a staff member, I would like to be able to log in to my account"*
>
> *"As a staff member, I would like to be able to view reviews written about
> me in one location"*
>
> *"As a staff member, I would like other users to be able to view some
> information about me"*

#### Owner

> *"As the owner, I would like to be able to add therapists"*
>
> *"As the owner, I would like to be able to add therapies"*
>
> *"As the owner, I would like to be able to edit therapists"*
>
> *"As the owner, I would like to be able to edit therapies"*
>
> *"As the owner, I would like to be able to delete therapists"*
>
> *"As the owner, I would like to be able to delete therapies"*
>
> *"As the owner, I would like to be able to approve reviews"*
>
> *"As the owner, I would like to provide contact info for my business"*
>
> *"As the owner, I would like to be able to update the business info"*

#### Developer

> *"As the developer, I would like to ensure the site meets the essential user
> requirements"*

***

### Initial Concept

The initial idea of the site was to provide a digital booking system, combining
reviews and ratings, for a massage spa. Due to time constraints, a lot of the
functionality has been removed. As a result, the scope has been reassessed
throughout the development process to ensure a minimum viable product is
created.

In the 'ideal world', the site would have had unique booking slots available to
each therapist, allowing separate diaries for each. This would have allowed a
business advisor to review the types of bookings that are being made and could
lead to business adjustments to maximise profits. As stated, the time
constraints imposed by external factors meant that I decided very early to
negate the complexity of involving dates and times with regard to front-end
rendering. This allowed rapid development of more simplified functionality.

***

#### Wireframes

Initial wireframes were made for the original conception idea. As functionality
was reduced, these wireframes have also become guidelines for the more basic
functions and remain in place for future development. The wireframes were
designed using [Balsamiq](#balsamiq), with a mobile-first approach.

##### Samples from Mobile

|Home|Therapies|Therapists|
|:-:|:-:|:-:|
|![mobile home wireframe](./docs/readme/images/wireframe-mob-home.png)|![mobile home wireframe](./docs/readme/images/wireframe-mob-therapies-short.png)|![mobile home wireframe](./docs/readme/images/wireframe-mob-therapists.png)|

##### Complete wireframes

*[See main wireframes here](./docs/design/mindful_massage_wireframes.pdf)*

Other wireframes are viewable in the
[`docs/design/`](https://github.com/DaveyJH/ci-portfolio-four/tree/main/docs/design)
directory on GitHub. The original Balasmiq file is also available there which
has comments that describe some of the sections.

***

#### Colour Scheme

A light colour scheme was chosen to match the ersatz colour scheme of the Spa.
The light colours allow a good contrast with text and give a clean feel
throughout the site. Colours were checked with a contrast checker during the
design process to make sure they meet accessibility requirements.

![color scheme](./docs/design/mindful1.png)

##### Contrast

The chart shown below was generated via
[a site I produced](https://daveyjh.github.io/Color-Contrast-Checker/) that
allows multiple colours to be checked against each other in one action, rather
than having to input values repeatedly. The chart was referenced throughout the
design and styling process to ensure high contrasts were maintained. Some
transparency has been applied in places, and thus, the resulting colours have
been checked via the use of the [eye dropper tool](#instant-eyedropper),
mentioned in the technologies used section, and a
[one-hit contrast check](#webaim-contrast-checker).

![color scheme](./docs/design/mindful-contrast.png)

***

#### Typography

To maintain a relaxing and peaceful theme, the main font used throughout the
site is not complex. It allows easy reading and does not detract from the
overall feel of the site. To add a little more style, the headings and some
links/buttons have a slightly cursive font that still remains, largely, easy to
read.

Both fonts are from [Google fonts](#google-fonts), meaning they can be imported
via their API and giving wide coverage to keep the styling maintained across
various devices.

##### Headings

Grape Nuts  
![grape nuts google font](./docs/design/font-grape-nuts.png)

##### Body

Dosis  
![dosis google font](./docs/design/font-dosis.png)

<!-- typography -->
***

#### Imagery

The imagery used throughout the site is intended to maintain a peaceful,
calming nature. All static images are sourced through
[Pexels.com](https://www.pexels.com/) and are royalty-free. There is a list of
images used, and inspirational/trial images considered, available on the
[media wiki here](https://github.com/DaveyJH/ci-portfolio-four/wiki/Media-ideas).
At the time of writing, the images within the database also came from Pexels.

***

## Features

### Existing Features

<!-- - Feature 1 - allows users X to achieve Y, by having them fill out Z -->
<!-- 1. feature1
>*"User... **story quote**"*
- *explanation*-->
F1
***
<!-- - Feature 2 - allows users X to achieve Y, by having them fill out Z -->
<!-- 1. feature2
>*"User... **story quote**"*
- *explanation*
  ![imgName](imgURL)
-->
F2
***

### Features Left to Implement

<!-- features left to implement -->
<!-- 1. Explain desired feature 1
  - *Notes regarding feature*
  - Explanation of feature need etc. -->
<!-- 2. Explain desired feature 2
  - *Notes regarding feature*
  - Explanation of feature need etc. -->
***

## Data Model
<!-- todo add link to lucidchart in tech used -->

After the initial conceptualisation of the site, an entity relationship
diagram(ERD) was generated using LucidChart. Being my first project using a
relational database, this was a new concept to get to grips with and I suspect
has not been done in the best way.

![original entity relationship diagram](./docs/design/db_erd.png)

As the project developed and the scope changed, the ERD became less accurate to
the end model. It acted as brilliant guidance and helped me to get the base
structure of the database created at an early stage, however, it is not quite
accurate for the final database structure.

I was able to generate an ERD from the database as it has ended up, and I am
fairly happy with how similar my initial thoughts were to the end result. One
thing I note is that, due to using functions to generate the average ratings,
these are not present on the ERD. Many of the `all_auth` entities have been
excluded from this diagram as they are not being used. Another consideration is
that I have excluded the original booking entity as it does not feature in this
iteration of deployment.

![final entity relationship diagram](./docs/design/generated_erd.png)

PDF versions of the displayed original ERD and the generated ERD (including
bookings) are available in the
[`docs/erd/` directory](https://github.com/DaveyJH/ci-portfolio-four/tree/main/docs/design/erd)
in the GitHub repository.

### PostgreSQL
<!-- todo add link to postgresql -->
A relational database was needed for the site, and as such, PostgreSQL was
chosen. As a widely implemented database platform, the documentation available
for working with this is quite extensive and there are many extensions available
to assist with its use. Due to the use of `ArrayField`s within the models, I was
unable to use the generated `db.sqlite3` instance, that is installed when
initialising django, for development. Instead, I used a database hosted on
ElephantSQL and successfully transfered the majority of data from that
development database into the deployed database hosted on Heroku.

As the site
was deployed to two hosting platforms (due to uncertainty with the future of
free tiers available with Heroku) I have opted to maintain the Render instance
with the use of the development database, thus all 'test' entries have been
purged and 'real' data has been added. To ensure the two sites began with
similar data, I used a database cloning method as detailed in the
[deployment](#deployment) section below.

## Technologies Used

### Python Packages

|Package|Use|
|--:|--|
|[django](https://www.djangoproject.com/)|web framework that encourages rapiddevelopment and clean, pragmatic design|
|[dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/)|facilitates integration with Cloudinary|
|[cloudinary](https://pypi.org/project/cloudinary/)|easy uploading of images to Cloudinary|
|[django-crispy-forms](https://pypi.org/project/django-crispy-forms/)|allows DRY forms to be created rapidly through HTML templates|
|[django-summernote](https://pypi.org/project/django-summernote/)|allows use of text-rich editors for form inputs|
|[python-dotenv](https://pypi.org/project/python-dotenv/)|reads key-value pairs from a `.env` file. Negates the need to write a Python file for environment variables (as would be done in an `env.py` file)|
|[gunicon](https://pypi.org/project/gunicorn/)|natively suuports django to allow use of commands|
|[psycopg2](https://pypi.org/project/psycopg2/)|PostgreSQL database adapter for Python|
|[django-phonenumber-field](https://pypi.org/project/django-phonenumber-field/)|allows storing of configurable telephone numbers in django models|
|[whitenoise](https://pypi.org/project/whitenoise/)|allows easy implementation of static files|
|||

*For a full list of installed Python packages, see
[`requirements.txt`](.txthttps://github.com/DaveyJH/ci-portfolio-four/blob/main/requirements.txt)*

Most packages have relevant documentation hosted on the
[Python package index](https://pypi.org/) site. More expansive docs are found
for many of the packages at [Read the Docs](https://readthedocs.org/)

***

### Other Tech

#### *[Instant Eyedropper](http://instant-eyedropper.com/)*

A quick and simple application to obtain hex values from any colour on my
display. I downloaded this while playing around with my laptop layout/display
settings. I have the app set to run on startup and remain minimized in my
system tray. This allows quick access and if I click the colour, it
automatically copies the hex value to my clipboard.

#### *[WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)*

A basic contrast checking service for conformity to the Web Content
Accessibility Guidelines. The service allows input of a foreground and
background colour and displays the resulting contrast ratio, including a quick
reference to meeting WCAG AA / AAA standards. This was used for 'one-shot'
colour instances.

#### *[Windows Snipping Tool](https://support.microsoft.com/en-us/windows/use-snipping-tool-to-capture-screenshots-00246869-1843-655f-f220-97299b865f6b)*

A screenshot tool built in to Windows. It allows quick, partial screenshots
to be taken that can be saved as image files.

#### *[Balsamiq](https://balsamiq.com/)*

Balsamiq was used to create
[wireframes](./docs/design/mindful_massage_wireframes.pdf) for the project.

#### *[Font Awesome](https://fontawesome.com/)*

The project uses icons from Font Awesome version 6.2.0.

#### *[Google Fonts](https://fonts.google.com/)*

The fonts used in the website are imported from Google Fonts.

#### *[Multi Device Mockup Generator](https://techsini.com/multi-mockup/index.php)*

The image at the top of this document was created using a free service
provided by TechSini.&#8203;com

#### *[W3C Markup Validation Service](validator.w3.org)*

A service to check the HTML and CSS files for errors.
[HTML validation results here](#w3c-validator).

#### *[flake8](https://flake8.pycqa.org/en/latest/)*

A Python code validation service. View the [flake8 process here](#flake8)

#### *[Visual Studio Code](https://code.visualstudio.com/)*
  
A free, streamlined code editor. The [extensions](#vscode-extensions)
available have allowed me to customize my workspace and become more
efficient.

***

#### VSCode Extensions

Links to the VSCode marketplace for each extension used throughout this project:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
- [GitHub Pull Request and Issue Provider](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
- [Highlight Matching Tag](https://marketplace.visualstudio.com/items?itemName=vincaslt.highlight-matching-tag)
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
- [Reflow Markdown](https://marketplace.visualstudio.com/items?itemName=marvhen.reflow-markdown)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)

***

## Testing

<!-- explain testing
? item tested
? expected result
? how test was performed
? actual result
? differences
? action required
? re-test
- more detail and better format required compared with project 1
look at daisy's testing documentation and [webinar](https://us02web.zoom.us/rec/play/9FIKllHX2ZiQNFRhYPn_hBh_ZeA8964ZvIDLnhpKGAf1NLVc3_hBJ6zSL8Hv5Hx7ALnPtDmbg8CmFAs.YVsZ9LR_uI7OjEwH)-->

<!-- validation of html, css and script. -->
<!-- lighthouse testing -->

## Bugs

[Bugs](https://github.com/DaveyJH/ci-portfolio-four/issues?q=label%3Abug+) were
noted with a `bug` label on GitHub.

### Current

1. [Phone number does not convert to local format in Sweden.](https://github.com/DaveyJH/ci-portfolio-four/issues/97)

    *By utilising the `django-phonenumber-field` package, I had intended for the
    phone number supplied to display in local format for users in Sweden. A big
    thanks to @Jays-T for testing this, and reporting to me that it **does not**
    appear as intended. With the impact of this being so negligble, the bug
    remains in the deployed version.*

    Potential resolution:

- There are two likely causes of this issue. First, the package may need some
  initial configuration in its `__init__.py` file. However, after consideration,
  I suspect this is not the root cause as I have entered a telephone number in
  the local Swedish format (starting with a zero) in the database and it is
  rendering with the Swedish country dialling code in all instances.
- The second, and more likely, is that I have not specified in what way the
  phone number should render via the options within the package, or have
  misinterpreted the use of the `PHONE_NUMBER_DEFAULT_REGION` setting in
  `settings.py`. As I would be reliant on assistance from somebody in Sweden to
  test this, and it would need to be tested on the deployed version, I have
  decided not to risk causing further issues that may render the telephone
  number as 'local' in areas that are not Sweden.

2. [Therapy specialists do not populate as checked when editing a therapy.](https://github.com/DaveyJH/ci-portfolio-four/issues/90)

    *When a superuser opens the 'edit therapy' form, all data self populates
    **apart from the specialists**. The impact is minor on the user experience,
    and as it only effects superusers, I would be satisfied with detailing the
    issue, and need to ensure specialists are checked, in some handover
    documentation.*

### Resolved

1.
   [Lists are rendering in an unusual way in the admin section of the therapists page](https://github.com/DaveyJH/ci-portfolio-four/pull/49)

    *Commit -
    **[0ef646f](https://github.com/DaveyJH/ci-portfolio-four/pull/49/commits/0ef646f2ccf17298fc10b981a0b206b851c26ab2#diff-a34e70e0ddac5f02fba0410361c1a0c90d1417fb86059e0f289c46ce3a10a390R82-R83)**
    : During the process of modifying the lists in the admin section, an `</li>`
    tag was misplaced. Repositioning the tage resolved the issue.*
2.
   [Navbar button drops to a new line on some devices](https://github.com/DaveyJH/ci-portfolio-four/issues/76)
  
    *Commit -
    **[495e4c1](https://github.com/DaveyJH/ci-portfolio-four/commit/495e4c1654c7b31ea86d2e038e352d27b99de0a4)**
    : Due to the size of the `h1` element and the use of Bootstrap, a `nowrap`
    class is now toggled via JavaScript to prevent the layout shift.*
3.
   [Some FontAwesome icons are rendering with a different colour to the text](https://github.com/DaveyJH/ci-portfolio-four/issues/78)
  
    *Commit -
    **[606dc35](https://github.com/DaveyJH/ci-portfolio-four/commit/606dc3547e4a503d661ec4c6fc986e425586bfaa#diff-a5ea33c888430601a659bcbef2da1944097953737f2606282efc13ca6e5fbabaR148-R151)**
    : 3rd party style rules have been overridden in the CSS.*
4.
   [The site is far less user friendly if JavaScript is not enabled](https://github.com/DaveyJH/ci-portfolio-four/issues/79)
  
    *Commit -
    **[5cec5c7](https://github.com/DaveyJH/ci-portfolio-four/commit/5cec5c7246373dc31aeb7fd11e3eb35e82e4eaf3)**
    : A styled `noscript` element has been added to the site.*
5.
   [The bookings page causes a 404 error](https://github.com/DaveyJH/ci-portfolio-four/issues/88)
  
    *Commit -
    **[abb543a](https://github.com/DaveyJH/ci-portfolio-four/commit/abb543ac31002f738b5e44890b1169109b5199f1)**
    : On discovering this bug, it led to me finding I had left `/` off the URL
    pattern. I also changed the context variable name to avoid conflicts with
    the URL name. This did not resolve the issue.*

    *Commit -
    **[6b30a98](https://github.com/DaveyJH/ci-portfolio-four/commit/6b30a98a9d520d993de2e0c9155ba99163d7212d)**
    : Having tried the fix above, I realised I was viewing a database that had
    no `BookingInfo` object instances. As I had configured the site to raise an
    error if this were the case, the error was expected. However, I decided to
    alter the exception raised to a `500` error as it indicates to the user that
    the error is within the server/database.*
6.
   [When validating the HTML, an error was raised regarding an open element existing when trying to close a form element](https://github.com/DaveyJH/ci-portfolio-four/issues/89)
  
    *Commit -
    **[b0737fa](https://github.com/DaveyJH/ci-portfolio-four/commit/b0737fa72be8587c75250b6b528f7b62e4b94391#diff-46192b4b57fb419f7f8ce5009a659bbc36c5bbaaa481f4c5ea06e46df8b659f6R42)**
    : A closing `</div>` tag was added to the relevant HTML template.*
7.
   [A skipped heading level was reported by Wave accessibility checker](https://github.com/DaveyJH/ci-portfolio-four/issues/98)
  
    *Commit -
    **[6857133](https://github.com/DaveyJH/ci-portfolio-four/commit/6857133fc9d14366dec76bd9efb5a3ab181c5b62#diff-52a3585ac5621885b8c9fbdde0079453c1f917d189c54bde982de76f162fac52R35)**
    : The erroneous `h4` tags were replaced with `h3` tags.*
8.
   [The lower paragraph on the logout page was hard to read](https://github.com/DaveyJH/ci-portfolio-four/issues/99)
  
    *Commit -
    **[2736484](https://github.com/DaveyJH/ci-portfolio-four/commit/273648441f040b508084689777c50508cf406163)**
    : The paragraph was styled with CSS to make it more visible.*
9.
   [Any logged in user was able to view any user's profile](https://github.com/DaveyJH/ci-portfolio-four/issues/100)
  
    *Commit -
    **[2192c56](https://github.com/DaveyJH/ci-portfolio-four/commit/2192c56fd0a5225493a3509e51fa715fa263223a)**
    : A `UserPassesTestMixin` was added to the `UserProfileView`. It utilises a
    regex to retrieve the URL being visited and references it against the
    currently logged in user's id attribute. Yay for regex!*
9.
   [The active page was not indicated to the user](https://github.com/DaveyJH/ci-portfolio-four/issues/117)
  
    *Commit -
    **[e71d9bf](https://github.com/DaveyJH/ci-portfolio-four/commit/e71d9bf757b1d63266353989a470eb71d53a004d)**
    : Logic was added to the `base.html` template to check the current URL path
    against the list of URL pattern names.*




***

## Development

<!-- section missed in first project. 
!describe development process -->

## Deployment

<!-- !check this section, may need adjusting as using additional languages -->

<!-- **Github Pages**
- Navigate to the relevant GitHub Repository [here](github repo URL)
- Select "Settings" from the options below the name of the repository

![Settings Snip](./readme-content/images/github-settings.png)
- Select "Pages" from the left hand menu

![Pages Snip](./readme-content/images/pages-select.png)
- Select "Branch: main" as the source and leave the directory as "/(root)"

![Source Snip](./readme-content/images/pages-source.png)

- Click the Save button

- Take note of the URL provided

![URL Snip](./readme-content/images/pages-url.png)

- GitHub takes a short while to publish the page. The bar turns green if you refresh the pages tab and the page has been deployed

![Confirmed Deployment Snip](./readme-content/images/pages-deployed.png)
- Click the link or copy the URL to a browser to reach the deployed page
https://daveyjh.github.io/ci-portfolio-one-v4/

The site is now live and operational -->
***

## Credits

### Content
<!-- - the a comes from b -->
<!-- - the c comes from d -->
### Media
<!-- - the a comes from b -->
<!-- - the c comes from d -->
### Acknowledgements
<!-- - acknowledge a, found at [b](bURL), for c -->
<!-- - acknowledge d, found at [e](eURL), for f -->
***

### Personal Development

As mentioned in this document, the time to achieve this project was very
limited. In total, I had just over 2 weeks to design, develop and deploy the
site, bar some initial conceptual ideas from a long time ago. Working full time
and then continuing to work with this site has meant I have worked very long
hours. Considering the circumstances, I am very happy with the outcome. I
learned a lot about django from their documentation and would like to explore it
further when I have less time pressure.

With regard to the agile process, I worked in the best way I could without
delaying myself by exploring the many features of GitHUb and the project board.
It has come to my attention that there is an iteration feature within the
project board, and this would have been far better suited than the approach I
took toward sprints. I have used the 'Milestones' as general groupings rather
than for epics. This allowed me to keep track, efficiently, of my project, but
does leave a somewhat confusing organisational structure for other
visitors/potential collaborators.

Having 'found my feet' through this project, there are many things I would do
differently from the initial setup right through to the final stages:

- I would like to utilise `.yml` templates for issues in the future. They allow
  rapid creation of similarly formatted issues, which would allow a more
  granular dissection of the user stories at an early stage.
- I intend to explore the full capabilities of the project boards available
  through GitHub; for a free service, they are very impressive and have a wide
  array of functionality.
- Now I have a better understanding of django and the relationships available, I
  would be comfortable diving into more intricate Models and database
  structures. This would allow me to create more accurate and detailed ERDs from
  the start.
- Finding the astounding number of predefined classes within django and its
  related packages has made me realise that a great deal can be achieved through
  a fairly small amount of Python code. The OOP pillars feature heavily
  throughout the framework and my time working with this project, and the
  exploration done in my current role, have led to an eagerness to push these
  concepts.
- As much as I am happy with the layout across all device types, my original
  design did allow more of a layout shift between device types. However, with
  such a short time available to me to complete the responsive side of the
  design, I have had to limit the differences. As much as I appreciated that
  consistency is a benefit for users, I do not think that users necessarily
  anticipate that consistency across all devices. Having explored the simple
  implementation of Bootstrap, I would like to delve further into the
  configurable settings within the framework, as well as exploring other similar
  options such as Tailwind.
- Work in a test driven development(TDD) approach. I am fairly confident with
  how to create a multitude of tests for this site, but do not have the time.
  Had I worked via TDD, I would have far less testing to do at these final
  stages and would have thorough documentation to provide. This would also help
  ensure no bugs were created along the way.

Finally, having put in over **110 hours** of screen time **within 7 days**, I
will certainly look to work on projects over a longer time period in future.
