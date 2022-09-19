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
  - [Technologies Used](#technologies-used)
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
designed using 
<!-- todo add link -->
Balsamiq, with a mobile-first approach.

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
been checked via the use of the eye dropper tool,
<!-- todo link to eyedropper/tech used -->
mentioned in the technologies used section, and a one-hit contrast check.

![color scheme](./docs/design/mindful-contrast.png)

***

#### Typography

To maintain a relaxing and peaceful theme, the main font used throughout the
site is not complex. It allows easy reading and does not detract from the
overall feel of the site. To add a little more style, the headings and some
links/buttons have a slightly cursive font that still remains, largely, easy to
read.

Both fonts are from Google fonts, meaning they can be imported via their API and
giving wide coverage to keep the styling maintained across various devices.

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

## Technologies Used

<!-- tech used -->
<!-- - *[techNameOne](techURL)*
       - Description -->
<!-- - *[techNameTwo](techURL)*
       - Description -->

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

### Current

<!-- current bugs -->

<!-- - bugOne explanation

*notes on explanation* -->
***
<!-- - bugTwo explanation

*notes on explanation* -->
***

### Resolved

<!-- resolved bugs -->
<!-- 1. bugOne

![bugOneImg](bugOneImgURL)

*Commit - **[sha](commit link with highlighted lines)** - explanation of fix* -->
***
<!-- 1. bugTwo

![bugTwoImg](bugTwoImgURL)

*Commit - **[sha](commit link with highlighted lines)** - explanation of fix* -->
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
