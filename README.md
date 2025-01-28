# Nourish
![Nourish header](assets/images/header-nourish.png)

## Introduction 

Nourish is an attractive and user-friendly web application built to share and discover delicious recipes. The site allows authorised users to log in and publish recipes to Nourish, and allows site visitors to browse recipes for that all-too-needed meal inspo. This Full Stack Individual Capstone Project marks the culmination of everything learnt while studying at the Code Institute. Nourish combines and demonstrates:

- **Frontend Development**: HTML, CSS, JavaScript
- **Backend Development**: Python, Django framework
- **Database Management**: PostgreSQL, integrated through Django ORM
- **Agile Methodology**: Project planning and tracking using Agile principles
- **Version Control**: Git & GitHub
- **Deployment**: Heroku
- **AI Integration**: Harnessing AI tools in the development process

<a href="https://nourish-recipes-0c552fcf97d0.herokuapp.com/" target="_blank">View the live project here.</a>

## UX Design

### Site Owner’s Goal

The Nourish site owner's goal is to create a user-friendly online platform that inspires users to explore the joy of cooking and discover new recipes for every occasion. Nourish aims to be more than just a recipe collection—it will foster a sense of community by enabling users to connect, share feedback, leave reviews, and swap cooking tips.

The site will be built using HTML, CSS, JavaScript, Python, and the Django framework to create a site that users will want to keep coming back to. It will focus on fostering connections between food enthusiasts while showcasing the site’s core values: sharing good food and great ideas.

### User Stories

The full user stories for this project, along with their acceptance criteria and tasks, can be found on the <a href="https://github.com/users/katee145/projects/13" target="_blank">project board</a>. Below are the user stories deemed essential to achieving the minimum viable product (MVP):

* As a site visitor, I want to be able to access the recipe website on multiple devices (desktop, mobile, tablet) so that I can use it anytime, anywhere.
* As a recipe website administrator, I want to be able to easily add, edit, and delete recipes so that I can keep the content fresh and up-to-date.
* As a recipe website administrator, I want to be able to moderate user-generated content so that I can ensure the quality and appropriateness of reviews and comments.
* As a site visitor, I want to be able to easily browse and find recipes so that I can discover new and delicious dishes.
* As a user with dietary restrictions, I want to be able to filter recipes so that I can easily find recipes that are suitable for my needs.
* As a user looking for useful recipes, I want to be able to view detailed recipe information so that I can easily follow the instructions and understand the ingredients.
* As someone who has used a recipe, I want to be able to contribute to the recipe website by submitting my comments as feedback after making a recipe.

### Access Control

The table below outlines access control for each user type, covering both the site’s front end and admin panel:

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

The user flow diagram illustrates how unauthorised (non-staff) users navigate the site. For simplicity, it assumes the user begins by deciding whether they have an account. In practice, many users will land directly on a specific recipe page they are searching for.

![User flow diagram](assets/images/user-flow-diagram-nourish.png)

### Branding
![Branding slide for nourish](assets/images/branding-nourish.png)

#### Fonts

This project uses 'Bowlby One' for headings and 'Open Sans' for body text. Both fonts are sourced from Google Fonts and there is a backup of 'sans-serif' applied on the site.

#### Colour Palette

The colour palette for Nourish was carefully selected to align with the brand's purpose as a recipe site. The colours ensure a user-friendly experience, balancing attractiveness with accessibility standards.

<details><summary>View</summary>

![Nourish colour palette](assets/images/colour-palette-nourish.png)
</details>

#### Imagery

All photography used on the Nourish site, including recipe images and staff photos, was sourced from Unsplash, ensuring high-quality visuals that align with the site’s aesthetic.

The brand logo was designed using Canva, carefully crafted to complement the site’s overall branding and color palette, reinforcing a cohesive and appealing identity.

<details><summary>View</summary>

![Nourish logo](assets/images/logo-nourish.png)
</details>

### Wireframes
The wireframes for the Nourish site were created using Canva to visually map out the layout and design for both mobile and desktop screens. These wireframes served as a foundational guide for the site’s development, ensuring a consistent and user-friendly interface across devices.

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

### Responsiveness

Nourish is designed to be fully responsive across all device sizes, ensuring an optimal user experience whether accessed on mobile, tablet, or desktop. The design follows a mobile-first approach, based on the hypothesis that the majority of users browse recipes on their smartphones.

To achieve this, the layout adapts seamlessly to different screen sizes using a combination of Bootstrap's grid system and Flexbox, applied strategically to maintain consistency and usability across devices.

![Website on multiple device sizes](assets/images/responsiveness-nourish.png)

## Agile

The development of the Nourish project followed Agile methodology, focusing on iterative improvements, flexibility, and user-centered design. The project was broken down into 'must have', 'should have' and 'could have' functionality to determine which features would deliver a functional minimum viable product (MVP).

A <a href="https://github.com/users/katee145/projects/13" target="_blank">GitHub Project Board</a> was used to effectively plan, track, and manage tasks, with cards representing user stories, acceptance criteria, and sub-tasks. The board utilised the columns 'Backlog', 'To Do', 'In Progress', and 'Done' to provide a clear visual representation of progress throughout the project.

Regular reviews and retrospectives were conducted throughout to evaluate progress and prioritise next tasks to deliver the site within the allotted time frame.

## Entity Relationship Diagram
The Entity Relationship Diagram (ERD) below outlines the relationships between the site's models.

![Entity relationship diagram](assets/images/erd--nourish.png)

## Features

### Existing Features

#### Navigation

The navigation bar is present on all pages, featuring the Nourish title on the left, which links to the homepage. The title remains visible even on smaller screen sizes. The rest of the navigation options collapse into a Bootstrap-built dropdown menu. Links to Home and About behave as expected, while the user's login status determines whether they see Register/Login or Logout as options.

<details><summary>View</summary>

![Navigation bar](assets/images/navbar.png)
</details>

#### Login Notice

A permanent login notice is displayed below the navigation bar, informing users of their current status. If logged in, the notice displays the username for clarity and personalisation.

<details><summary>View</summary>

![Login notice](assets/images/login-notice-1.png)
<br>

![Login notice](assets/images/login-notice-2.png)
</details>

#### Masthead

The masthead displays the Nourish brand name prominently across the screen with the tagline: "Recipes that make you feel good". The font size dynamically adjusts based on screen size to ensure responsiveness.

<details><summary>View</summary>

![Masthead](assets/images/masthead.png)
</details>

#### Search

The search bar is a core feature of the site, allowing users to filter recipes. It provides a dropdown of suggested categories such as vegan, meat, and budget eats, while also supporting keyword searches, including specific ingredients. If no results match, users are shown a page with alternative suggestions. The search bar clears automatically when clicked and prevents empty submissions with validation.

<details><summary>View</summary>

![Search bar](assets/images/searchbar.png)
![No search results](assets/images/no-search-results.png)
</details>

#### Notification

A notification system provides instant feedback at the top of the page (both homepage and recipe page) when a user completes an action, such as logging in, logging out, submitting a comment, editing a comment, or deleting a comment. These notifications ensure that users are aware of successful interactions.

<details><summary>View</summary>

![Notification](assets/images/notification.png)
</details>

#### Recipe Cards

Recipe cards are displayed on the homepage, showing eight recipes per page. The layout adapts to screen size, varying from four cards per row to one per row on smaller devices. Each card features an image, recipe title, and categories. Hovering over the title or image causes responsive animations, and clicking redirects users to the recipe details page.

<details><summary>View</summary>

![Recipe cards](assets/images/recipe-cards.png)
</details>

#### Pagination

The homepage features Prev and Next buttons for navigating between pages of recipes. These buttons only appear when applicable—Next is hidden on the last page, and Prev is hidden on the first. Buttons include hover animations for improved user experience.

<details><summary>View</summary>

![Navigation buttons](assets/images/prev-next-buttons.png)
</details>

#### Recipe

Each recipe page includes a title, categories, description, preparation time, cook time, servings, image, ingredients, and instructions. Recipes are added via the admin panel which ensures all fields are completed. A placeholder image is provided for recipes without a custom image that displays on both the recipe page and homepage.

<details><summary>View</summary>

![Recipe page](assets/images/recipe.png)
</details>

#### Comments

At the bottom of each recipe page is a fully functional comment section. Users can see all existing comments, along with the author's name and the date and time of submission. If no comments are available, the message "Be the first to comment!" is displayed. Logged-out users are prompted to log in to leave a comment. Logged-in users can submit, edit, or delete their comments. Form validation prevents the submission of empty comments.

<details><summary>View</summary>

![Comments](assets/images/comments.png)
![Comments](assets/images/comments-2.png)
</details>

#### About

The About page introduces the site and its purpose. It features the brand logo prominently at the top, followed by a "Meet the Team" section that displays team member photos, names, and bios.

<details><summary>View</summary>

![About](assets/images/about.png)
</details>

#### 404

If a user navigates to a non-existent page, they are shown a custom 404 error message with a link back to the homepage for easy navigation.

<details><summary>View</summary>

![404](assets/images/404.png)
</details>

#### Login

The login page allows users with existing accounts to sign in using their username and password. Both fields are required, and users are notified if any details are missing or incorrect.

<details><summary>View</summary>

![Login](assets/images/signin.png)
</details>

#### Logout

The logout page confirms that the user wants to log out by displaying a confirmation button with hover animations for visual feedback.

<details><summary>View</summary>

![Logout](assets/images/signout.png)
</details>

#### Register

The register page allows users to create an account by entering a unique username and a strong password. Form validation and allauth integration ensures all required fields are completed correctly, with error messages displayed for any invalid input.

<details><summary>View</summary>

![Register](assets/images/signup.png)
</details>

### Future Features

- **Enhanced Comment Moderation**: Add functionality to flag inappropriate edits in comments or require admin approval for comment edits to maintain the integrity of published comments.
- **Comment Approval Notifications**: Notify users via email or on-site messages when their comments are approved and published.
- **User Profiles**: Create profile pages for registered users where they can save and manage favorite recipes for easy access.
- **Seasonal Spotlight**: Highlight recipes with seasonal ingredients on the homepage to encourage users to cook with fresh, in-season produce.
- **Advanced Search Filters**: Expand search functionality to include additional filters, such as preparation time, cook time, or specific cuisines.

## AI Implementation and Orchestration

Throughout this project, AI was an invaluable tool that helped streamline development and complemented the manual steps I took alongside.

### Use Cases and Reflections:

- **Code Creation:** 
  - AI was key in generating recipes, titles, instructions, and names, which sped up the process of building content for the site.
  - Reflection: While AI provided creative outputs, I refined the content to match the tone and goals of the project, ensuring a cohesive user experience.

- **Debugging:** 
  - AI helped debug issues by analysing warning messages and offering solutions or explanations. By inserting problematic code and describing the issue, the AI provided effective troubleshooting strategies.
  - Reflection: This iterative debugging process improved my understanding of error-handling and problem-solving, as I had to evaluate and adapt the AI's suggestions to fit the project.

- **Performance and UX Optimisation:** 
  - AI provided initial suggestions for media queries and breakpoints which I then manually adjusted for a truly responsive design. By testing the site across different devices, I refined the appearance and functionality.
  - Reflection: While AI contributed to speeding up the process, fine-tuning responsiveness was a manual effort, reinforcing my understanding of CSS and media queries.

- **Automated Unit Testing:**
  - AI helped to define the test scope that was required for this project. This process identified risks over functionality such as form validation. The test process was then completed manually.
  - Reflection: AI was valuable in helping me focus on key areas like input validation. This process improved my understanding of testing and the potential of automated testing.

### Overall Impact:

The use of AI tools in this project greatly improved efficiency, allowing me to focus on higher-level decisions and manual debugging. However, AI was used as a supportive partner rather than a replacement for my skills. Each suggestion was subject to critical evaluation and refined to meet the project’s unique needs.

This process not only improved my technical abilities but also my problem-solving and decision-making skills. The experience emphasised the importance of embracing new technologies as tools to enhance development.

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

### Testing Scope

The testing focused on the core functionalities of the site, addressing the most common risks and ensuring full functionality.

#### Browser Testing

Manual testing was conducted across a variety of widely-used browsers to ensure both full functionality and responsiveness of the site.

| Browser          | Functioning? (Y/N) | Responsive? (Y/N) |
|------------------|--------------------|-------------------|
| Google Chrome    | Y                  | Y                 |
| Safari           | Y                  | Y                 |
| Bing             | Y                  | Y                 |
| Microsoft Edge   | Y                  | Y                 |
| Firefox Mozilla  | Y                  | Y                 |
| Opera GX         | Y                  | Y                 |

#### Risk Testing

Key risks were identified, including duplicate usernames, insecure passwords, unauthorised admin access, and the ability to post empty comments. Each was subject to manual unit testing to ensure proper security and functionality.

<details><summary>Regisering with a username that is already taken</summary>

![Risk testing](assets/images/sign-up-validation-4.png)
</details>

<details><summary>Registering with an insecure password</summary>

![Risk testing](assets/images/sign-up-validation-4.png)
</details>

<details><summary>Unauthorised users accessing admin panel</summary>

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

#### Comment Functionality

I documented the end-to-end validation of comment CRUD functionality, from account creation to comment submission, editing, and deletion. This ensured that each step worked correctly and was user-friendly.

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

The project underwent external testing and validation for HTML, CSS, JavaScript, Python, Lighthouse, and WAVE accessibility. Errors and warnings are explained where applicable.

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
The HTML validation errors on the registration page are a result of using allauth.

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
The undefined variable is a result of using Bootstrap library.

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
<details><summary>Homepage</summary>

![WAVE testing](assets/images/home%20wave%20logged-out.png)
</details>

<details><summary>About</summary>

![WAVE testing](assets/images/about%20wave%20%20logged-out.png)
</details>

<details><summary>Recipe</summary>

![WAVE testing](assets/images/recipe%20wave%20logged%20in%20comments.png)
</details>

<details><summary>No search results</summary>

![WAVE testing](assets/images/search%20wave%20logged-out.png)
</details>

<details><summary>404</summary>

![WAVE testing](assets/images/404%20wave%20logged-out.png)
</details>

<details><summary>Logout</summary>

![WAVE testing](assets/images/logout%20wave%20logged%20in.png)
</details>

<details><summary>Login</summary>

![WAVE testing](assets/images/login%20wave%20logged-out.png)
</details>

<details><summary>Register</summary>

![WAVE testing](assets/images/register%20wave%20logged-out.png)
</details>

## Credits

### Code

* The initial GitHub repository was created using the Code Institute template.
* The foundational code, including CRUD functionality, the comment model, and general inspiration for the blog-like features, was adapted from Code Institute's 'Codestar' project.

### Content
* AI generated

### Media
* Canva
* Unsplash

## Acknowledgements

A huge thank you to the Code Institute staff team for their support throughout, in particular Dillon, Roo, and John.