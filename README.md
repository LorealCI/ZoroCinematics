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
- [Project Planning](#project-planning)
   - [Strategy Plane](#strategy-plane)
   - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
   - [MoSCoW Prioritisation](#moscow-prioritisation)
- [User Stories](#user-stories)
- [Scope Plane](#scope-plane)
- [Structural Plane](#structural-plane)
 - [Skeleton and Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
    - [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
    - [Security](#security)
- [Features and user access](#features-and-user-access)
- [CRUD Functionality](#crud-functionality)
- [Future features](#future-features)
- [Technologies and languages used](#technologies-and-languages-used)
- [Libraries and framework](#libraries-and-framework)
- [Tools and programs](#tools-and-programs)
- [Deployment](#deployment)
   - [Create a new workspace in your IDE](#create-a-new-workspace-in-your-ide)
   - [Creating your repo](#creating-your-repo)
   - [Creating a new project](#creating-a-new-project)
   - [Creating a new app](#creating-a-new-app)
   - [Heroku deployment](#heroku-deployment)
- [AI Implemation](#ai-implementation)
   - [Code creation](#code-creation)
   - [Debugging](#debugging)
   - [Performance and UX Optimization](#performance-and-ux-optimization)
   - [Overall Impact](#overall-impact)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

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

User Story 1: Search for Movies
As a user,
I want to use a search bar to find movies,
so that I can quickly locate the movie I am interested in reviewing or learning about.

User Story 2: Log In and Log Out
As a user,
I want to log in and log out of my account, so that I can access personalized features like leaving reviews or requesting movies.

User Story 3: View Movie Details
As a user,
I want to view a page with general information about a chosen movie, so that I can learn more about the movie before deciding to watch or review it.

User Story 4: Leave a Review
As a user,
I want to leave a review for a movie, so that I can share my thoughts and opinions with others.

User Story 5: Star Rating System
As a user,
I want to give a star rating to a movie, so that I can provide a quick and visual representation of my opinion.

User Story 6: Edit or Delete Reviews
As a user,
I want to edit or delete my reviews, so that I can update or remove my feedback if needed.


User Story 7: Request a Movie
As a user,
I want to fill out a form to request a movie that is not yet on the site, so that I can suggest adding movies I want to review or learn about.

User Story 8: Responsive Design
As a user,
I want the website to be responsive on all devices, so that I can have a seamless experience whether I’m on a phone, tablet, or desktop.

User Story 9: View Trending Movies
As a user,
I want to see a list of trending movies on the homepage, so that I can discover popular movies to watch or review.

User Story 10: View and Manage My Profile
As a user,
I want to view and manage my profile, so that I can update my personal information and see my submitted reviews.

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

### Wireframes
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

## Deployment
### Create a new workspace in your IDE
To set up a Django project you should:
1. Open your file explorer and locate your Projects folder (the folder with all your projects in)
2. Inside the projects folder, create a new folder and name your project **remember to use underscores for Python project names**
3. Open VS Code, select File > Open Folder and then select the new project folder you just created
### Creating your repo
4. Then go to GitHub and create a new repo and create a unique repository name based on your project. (You can use the same name as the folder you created to be consistent.) Then click create repository. (You do not need to add a .README file)
5. Copy the commands provided by GitHub in the 'create a new repository on the command line'
6. Back in VS Code, in the main menu, click on the three dots > Terminal > New Terminal, then paste the commands into the terminal and hit Enter
7. Then go back into GitHub and refresh the repository to check that the new README file is visible on your GitHub page
8. Go back into VS Code and start up your virtual environment using the Command Palette. In the search bar add an > symbol then click Python: Create Environment, then click Venv and your Python version. **Remember to check whether you need to use python or python3 in upcoming steps and lessons by checking the version linked to each with --version.**
9. Create a .gitignore file then add .venv/ inside that file
### Creating a new project
10. Type the following command in the terminal to install the Django Python package, ```pip3 install Django~=4.2.1``` or any Django version you want (check [Django Project](<https://www.djangoproject.com/>) for the latest release)
11.	Once the package is installed, add it to the requirements.txt file with the following command, ```pip3 freeze --local > requirements.txt```
12.	In the terminal, create the new project and call it whatever you want in the current directory. **Important: Remember that the shortcut to refer to the current directory is a single dot . at the end of the command.**
```django-admin startproject zorocinematics .```
### Creating a new app
13.	To make the app, we use the manage.py file. In the terminal, type: ```python manage.py startapp blog``` (Remember to check whether you need to use Python or Python3) Check the explorer panel to see the new blog app directory has been created.
14.	In settings.py add 'blog',  to the list of installed apps
15. Create a superuser for the project to allow Admin access ```python manage.py createsuperuser```
16. Migrate the changes with the command: ```python manage.py migrate```
17. An env.py file must be created to store all protected data such as the DATABASE_URL and SECRET_KEY. These may be called upon in your project's settings.py file. The env.py file must be added to your .gitignore file so that your important, protected information is not pushed to public viewing on GitHub
18. Create a file called Procfile for Heroku deployment and type: web: gunicorn ems.wsgi
### Heroku Deployment
1. Log in to [Heroku](<https://heroku.com/>) or create an account if you are a new user
2. Once logged in, in the Heroku Dashboard, navigate to the 'New' button in the top, right corner, and select 'Create New App'
3. Enter your chosen app name and choose your region then click 'Create App'
4. In the Deploy tab, click on the 'Settings', scroll to find the 'Config Vars' section and click on 'Reveal Config Vars'. Here you will enter KEY:VALUE pairs for the app to run successfully
5. Add the heroku host name '.herokuapp.com' to the ALLOWED_HOSTS in you settings.py file
6. Go to the 'Deploy' tab and choose GitHub as the Deployment method and login
7. Search for the repository name, select the branch that you would like to build from, and connect it via the 'Connect' button
8. Go back to VS Code and add in some code then git add, commit and push it back to GitHub
9. You can then go to Heroku and click the deploy tab then click 'Deploy Branch'
10. Once the app has finished building you can click the 'View' button to bring you to your deployed site

## AI Implementation
### Code creation
AI tools (co-pilot) facilitated in a quick codebase of ZoroCinematics core features such as the search bar, the trending section, the star rating feature and the colourful borders. I also used question-answer prompts to help resolve specific challenges in implementing my star rating feature and the average all rating feature. I made sure to ask Co-pilot to break down and explain any code I did not yet understand.

### Debugging
AI interventions were crucial in resolving errors in the reviews section, particularly with the star rating features not showing up as intended. AI walked me through and helped fix the code to ensure I achieved my desired outcome. I also used co-pilot to help debug my issue with my edit button feature which helped me to create a form using AJAX so users can edit their reviews seemlessly.

### Performance and UX Optimization
AI-driven improvements enhanced the application's speed. The user interface was optimized for responsiveness across all devices, ensuring it is accessible for everyone.

### Overall Impact
AI tools streamlined the development of ZoroCinematics essential features, allowing focus on creating an inclusive and user-friendly movie review site. Efficiency gains were notable in faster debugging of the rating feature and comprehensive testing of the CRUD functionality for user reviews. The main challenge was adapting AI-generated code to fit my specific requirements, which I resolved by using specific targeted prompts and manual adjustments, which ultimately enhanced my websites inclusivity and usability.

## Credits
Here are the following sites that aided in my learning and completion of this project: 
- [Code Institutes](<https://codeinstitute.net/>) for my overall content learning and the blog walkthrough.
- Django Docs
- Bootstrap
- [Youtube video](<https://youtu.be/Reu0hHbis5w?si=KerGmLPT-SB98i2j>) for my trending movies.
- [How to build a django movie review app](<https://blog.devgenius.io/lets-build-a-movie-review-django-app-47658f8e3751>) I used this to help with my base code.
- [Stack Overflow](<https://stackoverflow.com/>) to help with certain coding features.
- [Freepik](<https://www.freepik.com/>) for the default image for movies that did not have an image
- [TMDB API Database](<https://developer.themoviedb.org/docs/getting-started>) I used this to import all the movies and the movie information onto the site.

## Acknowledgements
- Thank you to my facilitator Dillon Mccaffery for his positive support, guidance and advice.
- Huge thanks to my fellow students and friends, and Code Institute's Slack community for keeping positive the energy up.
- Thank you to God for helping me push through when things got hard.
- And last but not least thank you to my snack draw for keeping me going!






