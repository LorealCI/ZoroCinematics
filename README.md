# ZoroCinematics

## Introduction
ZoroCinematics is a movie review website. It allows users to be able to review any movie(s) they choose and be able to submit a request to add a movie that may not yet be on the site. This project is part of the Code Institute's Full-Stack Developer course and focuses on Django framework, database manipulation, and CRUD functionality.
(Responsive Homepage Image)

## Table of Contents
(insert table)
- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [UX - User Experience](#ux---user-experience)
    - [Design Inspiration](#design-inspiration)
    - [Colour Scheme](#colour-scheme)
    - [Font](#font)
- [Project Planning](#project-planning)
   - [Strategy Plane](#strategy-plane)
   - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
   - [MoSCoW Prioritisation](#moscow-prioritisation)
- [User Stories](#user-stories)
- [Scope Plane](#scope-plane)
- [Structural Plane](#structural-plane)

## Overview
ZoroCinematics is a movie review site that designed for users who want to give honest feedback on how they feel about a movie and for users who want to find a good movie to watch based on the reviews. Users can:
- Register and create a profile.
- See trending movies.
- Search for a movie.
- View information about the movie.
- Leave a review on a movie.
- Be able to edit and delete their review when needed.
- See recommended movies.

## UX User Experience
### Design Inspiration
My inspiration for ZoroCinematcs came from my love for movies, I have always enjoyed watching movies and know many others do to, this website is a great way for everyone to be able to determine what movie they would like to watch based on reviews of individuals who have already watched it. 

### Colour Scheme
For ZoroCinematics I went with a darker theme to emulate a cinematic experience. My two main chosen colours were:
- Black #000000: This plays off a dark cinema room.
- White #ffffff: I used white to counter balance the darkness of the site.

On my site you will see a few features that have a range of colours, as I felt my site needed some colour to make it stand out a bit more. 

### Font
For my main font I used Google Fonts in the style:

## Project Planning
The goal of my website was to create a simple easy to use platform. When planning my project I looked at a few other movie review sites for inspiration, I knew I wanted my site to have a 'sleeker' feel perfect for everyone to use. 

### Strategy Plane
The primary goal for ZoroCinematics is to create a easy-to-use movie review site, that is user friendly and not overwhelming. 
- Creates a user-friendly website.
- Provide an intuitive UI for efficient CRUD functionalities.
- Encourage users to leave honest reviews.
- Ensure consistent UX across mobile, tablet, and desktop devices.
- Allow to add future features.

### Agile Methodologies - Project Management
The development of ZoroCinematics follows Agile Methodologies, focusing on iterative improvements, flexibility, and user-centered design. My project was broken down into 'must have', 'should have' and 'could have' functionality to determine which features would deliver a functional minimum viable product (MVP). 

I utilized a GitHub Project Board to plan and track all of my work. This has been invaluable in keeping organised and keeping track of my goals for my project. It also helped in breaking down my project into manageable tasks, prioritising important features and keeping a steady workflow.

### MoSCoW Prioritisation
In my project board i chose to follow the MoSCow Prioritisation method, labelling my tasks into:
- **Must haves**: this is the required components for the project. Completing this helped me to reach my MVP (Minimum Viable Product) for this project.
- **Should haves**: this is the components that are valuable to the project beyond the scope of the MVP, you should ensure your must haves are completed before starting your should haves.
- **Could haves**: these are components that are a bonus to your project, components that are not vital to have but would be nice to have in the project, this should only be done after your must haves and should haves are completed.

## User Stories
User stories and features are recorded and managed on [GitHub Projects](<https://github.com/users/LorealCI/projects/8>)

(Insert User Stories)

## Scope Plane
As a Full Stack learner doing an individual capstone project at the Code Institute, I was careful to maintain full control over my project and not let my idea grow too big as I was using some new programming languages. My project uses technologies such as Django, SQL, Bootstrap, (and even AJAX due to an issue in my code!). To ensure I maintained the scope of my project and achieved my MVP, my features were prioritised into managable blocks. Following agile planning methodologies and user stories on my GitHub project board I was able to maintain project flow and keep on track of what tasks I needed to complete. 

The essential features of my project included:
- A visually appealing, accessible website that meets my users needs.
- Responsivity across mobiles, tablets, and desktop devices.
- User authentication and registration.
- Basic search functionality for movies.
- Movie page with necessary information.
- Review feature with full CRUD functionality.

My projects scope was planned throughly to ensure I could identify areas of importance for my MVP completion, satisfaction of assessment criteria, and the feasibility of implementation within the given timeframe. This approach allowed me to stay focused during my developmental stage and also allowed room for further improvements within this project.

## Structural Plane
The structural plan for ZoroCinematics encompasses several key components that work together to provide a seamless user experience. This structure is built around a fully responsive design ensuring accessibility across all devices. I implemented a captivating homepage, a page that fits all the movie search criteria, a detailed movie page that shows all the information for that particular movie, a review section for logged in users to be able to leave a review on a movie. This carefully planned structure allows for seamless navigation across the site. 

### Homepage
(insert images)

### Results Page
(insert images)

### Movie Page
(insert images)

### Authentication Pages
(insert images)

## Skeleton and Surface Planes
The wireframes for ZoroCinematics were made using Canva, as I had a pretty clear idea of what I wanted my site to look like. [Canva](<https://www.canva.com/>) is a easy and free online graphic tool that allows you to create a wide range of visual content.

**Desktop view for:**
- Homepage
- Movie Page

<details close>
    <summary>Desktop Home Page Wireframe</summary>  
    <img src="documentation/wireframe/Canva_Homepage.png">  
</details>

<details close>
    <summary>Desktop Movie Page Wireframe</summary>  
    <img src="documentation/wireframe/Canva_Moviepage.png">  
</details>

During the implementation stage for my movie page, I found I did not like the look of just a plain white background for where the movie information will be, I feel it made the site look incomplete, so I experimented with a few different shades of blue, red and green until I found a colour I liked best and went best with my idea. 

### Database Schema - Entity Relationship Diagram for ZoroCinematics
![ERD Image](documentation/wireframe/erd.png)  
*Database Schema (ERD) for ZoroCinematics displaying relationships between feature components saved within the database*

This Entity Relationship Diagram (ERD) was generated using an [ERD AI Generator](<https://www.eraser.io/diagramgpt>). It illustrates how each feature interacts with each other and their relationsip with the postgreSQL database. Using Django's User Model, and Django AllAuth to carry out all user authentication, a user_id is created when the user registers with their username. This allows users to be able to leave a review on their chosen movie. For future development, a Profile feature will be added so users can customise their own profile page and users can follow each others page if they like their reviews. 

By impletmenting the use of the Admin, the Admin can remove a User and their data completely through the additon of on_delete=models.CASCADE through the use of the user_id. However, a user can only remove the reviews they posted on the site, but they cannot delete their account completely. I hope to add this feature in the next version.

### Security
ZoroCinematics implements a number of security measures to protect user data. I implemented the following features:

**Django AllAuth**
This handles the user registration and authentication, providing:
- Secure user registration and login
- Password hashing and storage
- Authentication backends configuration
- URL routing for authentication views

**Defensive Design**
I incorporated defensive design principles to enhance user experience and security:
- Redirection of unauthenticated users to login page
- Confirmation modals for actions like editing reviews
- Comprehensive testing and validation of all features

**CSRF Protection**

Cross-Site Request Forgery (CSRF) tokens are included in all forms to prevent leaving the site vulnerable to attackers who may steal user data.

### Features and User Access
During the planning of the site I knew I wanted unregistered users to be able to access the site and see all the movies available. Here is a breakdown of the sites accessibility for registered and unregistered users:

| Feature   | Unregistered User | Registrated User |
|-----------|-------------------|-----------------|
|Home Page	|       Visible	    |     Visible|
|Movie Page|	Visible|	Visible|
|Review Page|	Visible|	Visible|
|Leave a review|	Not available|	Available and editable|
|Leave a rating|	Not available|	Available and editable|

## CRUD Functionality

ZoroCinematics provides registered users to be able to Create, Read, Update and Delete their reviews.
Here are the features for my CRUD functionality:

| Feature   | Create |  Read   	|   Update |	Delete|
|-----------|--------|----------|----------|--------|
|Review|	Yes |	Yes|	Yes|	Yes|
|Rating|	Yes| Yes|	Yes|	Yes|


## Future Features
- **User Profile:** Implement a user profile page where they can add a profile image, cover image and a bio and it will also have their most recent reviews.
- **Follow:** Gives users the ability to follow other users if they like the type of movies they review.
- **Search:** Be able to also search by reviewer name.
- **Genres:** Implement a list_display so users can quick search by genres, recently released, and best rated.
- **Social Media:** Allow users to be able to share their reviews via different social media platforms.
- **Profile link:** Allows users to be able to share a link of their profile page to friends and family so they can follow them.
- **TV-Shows:** add a feature where you can click between movies or tv-shows called ZoroVision for tv-shows. 

These enhancements aim to improve user experience, increase engagement, and expand ZoroCinematics beyond a movie review site.

## Technologies and languages used
- HTML
- CSS
- JavaScript
- Python
- [Django](<https://djangoproject.com/>) was used as the python framework for the site.
- PostgreSQL for database management.
- [Github](<https://github.com/>) used for online storage of codebase and Projects tool.
- VS Code used as an IDE for development
- [Heroku](<https://heroku.com/>) was used to host the ZoroCinematics website.

## Libraries and framework
- Bootstrap v5.3.x
- Django v5.1.7
- Django AllAuth v0.57.2
- Whitenoise v5.3.0

All libraries and framework is available in the [requirements.txt](<https://github.com/LorealCI/ZoroCinematics/blob/main/requirements.txt>) file.

## Tools and Programs
- [Canva](<https://www.canva.com/>) for project design planning.
- [Short Pixel](<https://shortpixel.com>) to convert images from JPG to WEBP.
- [ERD AI Generator](<https://www.eraser.io/diagramgpt>) to generate an ERD.