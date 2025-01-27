# Nourish
![Nourish header](assets/images/header-nourish.png)

## Introduction 

Nourish is an attractive and user-friendly web application built to share and discover delicious recipes. The site allows authorised users to log in and publish recipes to Nourish, and allows site visitors to browse recipes for that all-too-needed meal inspo. This Full Stack Individual Capstone Project marks the culmination of everything learnt while studying at the Code Institute. Nourish combines and demonstrates:

* Frontend Development: HTML, CSS, JavaScript
* Backend Development: Django web framework
* Database Management: Django
* Agile Methodology: Project planning and tracking using Agile principles
* Version Control: Git & GitHub
* AI Integration: Exploring the potential of AI tools in the development process.

<a href="https://nourish-recipes-0c552fcf97d0.herokuapp.com/" target="_blank">View the live project here.</a>

## UX Design

### Site Owner’s Goal

The site owner's goal is to build a user-friendly online platform that inspires and excites users to try new recipes from a range of creators. Nourish will foster a sense of community through user interactions, such as recipe reviews and feedback, to create a site that users will want to keep coming back to.

Whilst Nourish provides users with a curated collection of delicious recipes, the site will also foster a sense of community through user interactions, such as recipe reviews and feedback. Nourish will use HTML, CSS, JavaScript, and Python to create a site that users will want to keep coming back to.

### User Stories

The full user stories for this project as well as their acceptance criteria and tasks can be found in the <a href="https://github.com/users/katee145/projects/13" target="_blank">project board</a>. Below are the user-stories that were considered essential to making the minimum viable product:

* As a site visitor, I want to be able to access the recipe website on multiple devices (desktop, mobile, tablet) so that I can use it anytime, anywhere.
* As a recipe website administrator, I want to be able to easily add, edit, and delete recipes so that I can keep the content fresh and up-to-date.
* As a recipe website administrator, I want to be able to moderate user-generated content so that I can ensure the quality and appropriateness of reviews and comments.
* As a site visitor, I want to be able to easily browse and find recipes so that I can discover new and delicious dishes.
* As a user with dietary restrictions, I want to be able to filter recipes so that I can easily find recipes that are suitable for my needs.
* As a user looking for useful recipes, I want to be able to view detailed recipe information so that I can easily follow the instructions and understand the ingredients.
* As someone who has used a recipe, I want to be able to contribute to the recipe website by submitting my comments as feedback after making a recipe.

### Access Control

| Access                            | Superuser | Staff user | Signed in user | Signed out user |
|-----------------------------------|-----------|------------|----------------|-----------------|
| Can view comments on a recipe     | Y         | Y          | Y              | Y               |
| Can comment on a recipe           | Y         | Y          | Y              | N               |
| Can edit their own comment on a recipe | Y     | Y          | Y              | N               |
| Can delete their own comment on a recipe | Y     | Y          | Y              | N               |
| Can log in to the admin panel     | Y         | Y          | N              | N               |
| Can manage users in admin panel   | Y         | N          | N              | N               |
| Can manage posts in admin panel   | Y         | Y          | N              | N               |
| Can manage comments in admin panel| Y         | Y          | N              | N               |


### User Flow Diagram
![User flow diagram](assets/images/user-flow-diagram-nourish.png)

### Wireframes

...

<details><summary>Homepage</summary>

![Wireframe](assets/images/homepage-wireframes-mobile.png)
![Wireframe](assets/images/homepage-wireframes-desktop.png)
</details>

<details><summary>About</summary>

![Wireframe](assets/images/about-wireframes-mobile.png)
![Wireframe](assets/images/about-wireframes-desktop.png)
</details>

<details><summary>Recipe</summary>

![Wireframe](assets/images/recipe-wireframes-mobile.png)
![Wireframe](assets/images/recipe-wireframes-desktop.png)
</details>

<details><summary>Errors</summary>

![Wireframe](assets/images/errors-wireframes--mobile.png)
![Wireframe](assets/images/errors-wireframes-desktop.png)
</details>

<details><summary>Account</summary>

![Wireframe](assets/images/account-wireframes-mobile.png)
![Wireframe](assets/images/account-wireframes-desktop.png)
</details>

### Branding
![Branding slide for nourish](assets/images/branding-nourish.png)

#### Fonts

This project used 'Bowlby One' as the heading font and 'Open Sans' as the body font. Both of these fonts are available via Google Fonts and there is a backup of 'sans-serif' applied on the site.

#### Colour Palette

The colour palette for Nourish was carefully selected to align with the brand's purpose as a recipe site. The colours ensure a user-friendly experience with both attractiveness and meeting accessibility standards.

![Nourish colour palette](assets/images/colour-palette-nourish.png)

#### Imagery

...
![Nourish logo](assets/images/logo-nourish.png)

### Responsiveness

...

![Website on multiple device sizes](assets/images/responsiveness-nourish.png)

## Agile

## Data Model/ERD

![Entity relationship diagram](assets/images/erd--nourish.png)

## Features
### Existing Features

#### Navigation

...

<details><summary>View</summary>

![Navigation bar](assets/images/navbar.png)
</details>

#### Login Notice

...

<details><summary>View</summary>

![Login notice](assets/images/login-notice-1.png)
![Login notice](assets/images/login-notice-2.png)
</details>

#### Masthead

...

<details><summary>View</summary>

![Masthead](assets/images/masthead.png)
</details>

#### Search

...

<details><summary>View</summary>

![Search bar](assets/images/searchbar.png)
![No search results](assets/images/no-search-results.png)
</details>

#### Recipe Cards

...

<details><summary>View</summary>

![Recipe cards](assets/images/recipe-cards.png)
</details>

#### Navigation buttons

...

<details><summary>View</summary>

![Navigation buttons](assets/images/prev-next-buttons.png)
</details>

#### Recipe

...

<details><summary>View</summary>

![Recipe page](assets/images/recipe.png)
</details>

#### Comments

...

<details><summary>View</summary>

![Comments](assets/images/comments.png)
![Comments](assets/images/comments-2.png)
</details>

#### Notification

...

<details><summary>View</summary>

![Notification](assets/images/notification.png)
</details>

#### About

...

<details><summary>View</summary>

![About](assets/images/about.png)
</details>

#### 404

...

<details><summary>View</summary>

![404](assets/images/404.png)
</details>

#### Login

...

<details><summary>View</summary>

![Login](assets/images/signin.png)
</details>

#### Logout

...

<details><summary>View</summary>

![Logout](assets/images/signout.png)
</details>

#### Register

...

<details><summary>View</summary>

![Register](assets/images/signup.png)
</details>

### Future Changes

* Flagging inappropriate comments
* Notification that you comment has been approved 
* Save recipesand have a profile 

## Built With

* ...

## AI Implementation and Orchestration

### Use Cases and Reflections:

...

- **Code Creation:** 
  - ...
  - ...

- **Debugging:** 
  - ...

- **Performance and UX Optimization:** 
  - ...

- **Automated Unit Testing:**
  - ...

### Overall Impact:
...

## Deployment

- **Platform:** Heroku
- **High-Level Deployment Steps:** 
  1. Clone the repository
  2. Set up the Heroku environment with a PostgreSQL database.
  3. Configure environment variables for sensitive data (e.g., secret keys).
  4. Deploy using Heroku Git or GitHub integration.
- **Verification and Validation:**
  - Tested the deployed application against the development environment for consistent functionality and design.
  - Verified accessibility using tools such as Lighthouse and manual testing.
- **Security Measures:**
  - Sensitive data is stored in environment variables.
  - DEBUG mode is disabled in the production environment to enhance security.

<a href="https://nourish-recipes-0c552fcf97d0.herokuapp.com/" target="_blank">View the live project here.</a>

## Testing

...

### Manual Testing

| Browser          | Functioning? (Y/N) | Responsive? (Y/N) |
|------------------|--------------------|-------------------|
| Google Chrome    | Y                  | Y                 |
| Safari           | Y                  | Y                 |
| Bing             | Y                  | Y                 |
| Microsoft Edge   | Y                  | Y                 |
| Firefox Mozilla  | Y                  | Y                 |
| Opera GX         | Y                  | Y                 |


#### Test Scope

Manual testing was carried out on the website to ensure full functionality. I have focused on specifically the ability to comment then edit and delete your own comment, and the risk. The following was identified as the potential risks given the scope of the site. 

#### Risk testing

The following were identified as risks:
<details><summary>Regisering with a username that is already taken</summary>

![Risk testing](assets/images/sign-up-validation-4.png)
</details>

<details><summary>Registering with an insecure password</summary>

![Risk testing](assets/images/sign-up-validation-4.png)
</details>

<details><summary>Unauthorised users accessing admin panel</summary></summary>

![Risk testing](assets/images/admin-access.png)
</details>

<details><summary>Unauthorised users accessing user permissions</summary>

![Risk testing](assets/images/staff-admin-access.png)
</details>

<details><summary>Risk of being able to edit delete other peoples comments</summary>

![Risk testing](assets/images/user-edit-comment-2.png)
</details>

<details><summary>Risk of being able to submit and/or edit an empty comment</summary>

![Risk testing](assets/images/empty-comment-1.png)
![Risk testing](assets/images/edit-empty-comment.png)
</details>

#### Comment functionality
The journey of wanting to comment, creating an account, to commenting then editng and deleting
Risk of being able to comment not logged in
Risk of being able to post an empty comment

<details><summary>User is not signed into an account so cannot submit a comment on a recipe</summary> 

![Comment testing](assets/images/comment-test-0.png)
</details>

<details><summary>User is able to create an account when: they have a unique username, they have a secure password, they have entered the same password, all required fields are complete</summary> 

![Comment testing](assets/images/comment-test-1.png)
</details>

<details><summary>User is notified of their login</summary> 

![Comment testing](assets/images/comment-test-2.png)
</details>

<details><summary>User can submit a comment on a recipe</summary> 

![Comment testing](assets/images/comment-test-3.png)
</details>

<details><summary>User is notified that their comment is awaiting approval</summary> 

![Comment testing](assets/images/comment-test-4.png)
</details>

<details><summary>Admin can view new user account</summary> 

![Comment testing](assets/images/comment-test-5.png)
</details>

<details><summary>User has no admin permissions</summary> 

![Comment testing](assets/images/comment-test-6.png)
</details>

<details><summary>Admin and staff can approve user's comment</summary> 

![Comment testing](assets/images/comment-test-7.png)
</details>

<details><summary>User can view and edit comment once approved</summary> 

![Comment testing](assets/images/comment-test-8.png)
</details>

<details><summary>User is notified that their comment has been updated</summary> 

![Comment testing](assets/images/comment-test-9.png)
</details>

<details><summary>User can delete their comment</summary> 

![Comment testing](assets/images/comment-test-10.png)
</details>

<details><summary>User is notified that their comment has been deleted</summary> 

![Comment testing](assets/images/comment-test-11.png)
</details>

<details><summary>User's comment has been deleted</summary> 

![Comment testing](assets/images/comment-test-12.png)
</details>

<details><summary>Admin can delete user's account</summary> 

![Comment testing](assets/images/comment-test-13.png)
</details>

### External Testing and Validation

#### HTML
<details><summary>Homepage</summary>

![HTML testing](assets/images/home.html%20logged%20out.png)
</details>

<details><summary>About</summary>

![HTML testing](assets/images/about.html%20logged-out.png)
</details>

<details><summary>Recipe</summary>

![HTML testing](assets/images/recipe.html%20loggedin%20with%20comments.png)
</details>

<details><summary>No search results</summary>

![HTML testing](assets/images/search.html%20logged%20out.png)
</details>

<details><summary>404</summary>

![HTML testing](assets/images/404.html%20logged%20out.png)
</details>

<details><summary>Logout</summary>

![HTML testing](assets/images/logout.html%20logged%20in.png)
</details>

<details><summary>Login</summary>

![HTML testing](assets/images/login.html%20logged-out.png)
</details>

<details><summary>Register</summary>
Contains errors from allauth base

![HTML testing](assets/images/register.html%20logged%20out.png)
</details>


#### CSS
<details><summary>CSS Validation</summary>

![CSS testing](assets/images/css-validation-nourish.png)
</details>

<details><summary>CSS Warnings</summary>

![CSS warning](assets/images/css-warnings-nourish.png)
</details>

#### JavaScript
<details><summary>JSHint</summary>

![JS testing](assets/images/js-hint-nourish.png)
</details>

#### Python
<details><summary>admin.py</summary>

![Python testing](assets/images/admin.py.png)
</details>

<details><summary>apps.py</summary>

![Python testing](assets/images/apps.py.png)
</details>

<details><summary>asgi.py</summary>

![Python testing](assets/images/asgi.py.png)
</details>

<details><summary>forms.py</summary>

![Python testing](assets/images/forms.py.png)
</details>

<details><summary>models.py</summary>

![Python testing](assets/images/models.py.png)
</details>

<details><summary>settings.py</summary>

![Python testing](assets/images/settings.py.png)
</details>

<details><summary>tests.py</summary>

![Python testing](assets/images/tests.py.png)
</details>

<details><summary>config/urls.py</summary>

![Python testing](assets/images/config%20urls.py.png)
</details>

<details><summary>nourish_home/urls.py</summary>

![Python testing](assets/images/nourish_home%20urls.py.png)
</details>

<details><summary>views.py</summary>

![Python testing](assets/images/views.py.png)
</details>

<details><summary>wsgi.py</summary>

![Python testing](assets/images/wsgi.py.png)
</details>

#### Lighthouse
<details><summary>Homepage: Desktop</summary>

![Lighthouse testing](assets/images/home%20lighthouse%20desktop.png)
</details>

<details><summary>Homepage: Mobile</summary>

![Lighthouse testing](assets/images/home%20lighthouse%20mobile.png)
</details>

<details><summary>About: Desktop</summary>

![Lighthouse testing](assets/images/about%20lighthouse%20desktop.png)
</details>

<details><summary>About: Mobile</summary>

![Lighthouse testing](assets/images/about%20lighthouse%20mobile.png)
</details>

<details><summary>Recipe: Desktop</summary>

![Lighthouse testing](assets/images/recipe%20lighthouse%20desktop%20logged%20in.png)
</details>

<details><summary>Recipe: Mobile</summary>

![Lighthouse testing](assets/images/recipe%20lighthouse%20mobile%20logged%20in.png)
</details>

<details><summary>No search results: Desktop</summary>

![Lighthouse testing](assets/images/search%20lighthouse%20desktop.png)
</details>

<details><summary>No search results: Mobile</summary>

![Lighthouse testing](assets/images/search%20lighthouse%20mobile.png)
</details>

<details><summary>404: Desktop</summary>

![Lighthouse testing](assets/images/404%20lighthouse%20desktop.png)
</details>

<details><summary>404: Mobile</summary>

![Lighthouse testing](assets/images/404%20lighthouse%20mobile.png)
</details>

<details><summary>Logout: Desktop</summary>

![Lighthouse testing](assets/images/signout-lighthouse-desktop.png)
</details>

<details><summary>Logout: Mobile</summary>

![Lighthouse testing](assets/images/signout-lighthouse-mobile.png)
</details>

<details><summary>Login: Desktop</summary>

![Lighthouse testing](assets/images/signin%20lighthouse%20desktop.png)
</details>

<details><summary>Login: Mobile</summary>

![Lighthouse testing](assets/images/signin%20lighthouse%20mobile.png)
</details>

<details><summary>Register: Desktop</summary>

![Lighthouse testing](assets/images/signup%20lighthouse%20desktop.png)
</details>

<details><summary>Register: Mobile</summary>

![Lighthouse testing](assets/images/signup%20lighthouse%20mobile.png)
</details>

#### WAVE Accessibility
Redundant links were flagged
<details><summary>Homepage</summary>

![WAVE testing](assets/images/home%20wave%20logged-out.png)
</details>

<details><summary>About page</summary>

![WAVE testing](assets/images/about%20wave%20%20logged-out.png)
</details>

<details><summary>Recipe page</summary>

![WAVE testing](assets/images/recipe%20wave%20logged%20in%20comments.png)
</details>

<details><summary>No search results page</summary>

![WAVE testing](assets/images/search%20wave%20logged-out.png)
</details>

<details><summary>404 page</summary>

![WAVE testing](assets/images/404%20wave%20logged-out.png)
</details>

<details><summary>Logout page</summary>

![WAVE testing](assets/images/logout%20wave%20logged%20in.png)
</details>

<details><summary>Login page</summary>

![WAVE testing](assets/images/login%20wave%20logged-out.png)
</details>

<details><summary>Register page</summary>

![WAVE testing](assets/images/register%20wave%20logged-out.png)
</details>

## Credits
### Code
* ...

### Content
* ...

### Media
* ...

