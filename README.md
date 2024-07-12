# Silly Talks

Developer: [Nathalia de Araujo Silva](https://www.linkedin.com/in/nathaliaaraujosilva/)

![home page print](/readme-images/inicial.png)

Silly Talks is a platform where users share stories to receive feedback on whether they're silly or serious, aiming to allow people to vent in a fun way and get impartial opinions.

Deployed website: [Go to Silly Talks](https://sillytalks-d90cef26c5c7.herokuapp.com/)

# CONTENT

* [OBJECTIVES](<#objectives>)

* [DESIGN](<#design>)
    * [Typography](<#typography>)
    * [Color Scheme](<#color-scheme>)

* [USER EXPERIENCE](<#user-experience>)
    * [Audience](<#audience>)
    * [User Stories](<#user-stories>)

* [FEATURES](<#features>)
    * [Existing Features](<#existing-features>)
        * [Home page](<#home-page>)
        * [Silly Talks Page](<#silly-talks-page>)
        * [Register](<#register>)
        * [Profile](<#profile>)
    * [Future Features](<#future-features>)

* [LOGIC](<#logic>)
    * [Database](<#database>)
    * [Workflow](<#workflow>)
         * [Agile](<#agile>)
    * [Django Apps](<#django-apps>)
        * [Blog App](<#blog-app>)
        * [Home App](<#home-app>)
        * [Profiles App](<#profiles-app>)

* [Techonologies Used](<#technologies-used>)
    * [Languages](<#languages>)
    * [Libraries and Programs](<#libraries-and-programs>)

* [TESTING](<#testing>)

* [DEPLOYMENT](<#deployment>)

* [UPDATE - JULY 2024](<#update---july-2024>)
    
* [CREDITS](<#credits>)

# OBJECTIVES

Silly Talks is a website inspired by the ["AITA" community](https://www.reddit.com/r/AmItheAsshole/) on Reddit. Users can share their stories, and everyone will judge whether they find them silly. 

The site aims to allow people to share their problems in a more fun way so that impartial third parties can give their opinion. We often think the grass is greener on the other side and don't know how many people go through the same thing or how many have different problems. It's a community to help people vent and also understand that everyone has problems. 

Since the site's intention is to help people facing a problem, all posts and comments require approval from the administrator. Non-logged-in users can submit their stories through the homepage form, and the administrator will post them later. We included this option so that we have stories on the site even if the person doesn't feel comfortable registering at the moment. Registered users can request a post, comment (subject to approval), and vote on the problem. The site offers 3 voting options: not silly, silly, and more information.

- **NOT SILLY:** Your problem is more serious than you think. Seek help! - We inform the author of the story that their problem is serious and they need to seek help (from family, friends, or professionals).

- **SILLY:** It's really silly, you're fine! - We inform the user that the problem is trivial and that everything will be okay.

- **MORE INFORMATION:** Give us more details so we can judge better! - We inform the user that we need more information to assess their problems.

# DESIGN

The primary objective of our website is to deliver a visually appealing and user-friendly experience, characterized by a clean and engaging design. The focus lies in providing users with just the right amount of informative content essential for comprehending the website's functionality. The approach is deliberately minimalist, as we strive to avoid overwhelming users with unnecessary information or distracting elements that may detract from their overall experience.

## Typography
The fonts have been sourced from the [Google Fonts library](https://fonts.google.com/), each selected with the intention of cultivating a relaxed atmosphere on the website while imbuing it with its own distinct meaning.

The site utilizes three different fonts:

1. **"Lobster"**, a sans-serif font, is exclusively reserved for the page title. This choice aims to emulate a handwritten appearance, imparting a sense of personalization and warmth to the site.

![Lobster Font](/readme-images/lobster.png)

2. **"DM Serif Display"**, a serif font, is employed for post titles, the welcome message, and text prompting user interaction such as voting. The objective is to craft attention-grabbing titles, distinct from the rest of the page, reminiscent of the aesthetic of a printed newspaper headline.

![DM Serif Display Font](/readme-images/DM-Serif-Display.png)

3. **"Comfortaa"**, another sans-serif font, is utilized for body text and is consistently applied across the entire website. Its purpose is to foster an ambiance of relaxation and approachability, ensuring that the site maintains an informal and friendly tone."

![Comfortaa Font](/readme-images/comfortaa.png)

## Color Scheme

In [color theory](https://www.colorpsychology.org/pink/), pink is often associated with feelings of hope and sensitivity. It represents a soft and nurturing energy, evoking a sense of optimism and renewal. Pink is believed to inspire hope in difficult times and convey a gentle sensitivity towards emotions and experiences. Its presence can symbolize a comforting reassurance, reminding us that brighter days are ahead and encouraging us to approach challenges with a compassionate heart.

Despite the main color being pink, the entire website adopts a white color scheme for a cleaner look. Additionally, we've included shades of purple to enhance certain elements, and shades of gray for buttons such as "back" and "delete," as well as for some box borders.

Pictures from [Coolors](https://coolors.co/)

**White:**
- #F9FAFC: Background, footer text, body background

![white colour scheme](/readme-images/branco.png)

**Purple:**
- #693d69: Nav link
- #630d5c: Nav title, pagination active, button form text
- #630d5c79: Message border
- #3d013a: Footer background, vote buttons, post card information
- #2f2738: Post list title, post link, pagination text

![purple colour scheme](/readme-images/roxo.png)

**Pink:**
- #dba2d836: Comments background
- #dba2d8: Message background, button background, pagination background
- #f9d1f7: Post list
- #c27bbcc0: Input borders, container borders, index post cards, home page cards

![pink colour scheme](/readme-images/rosa.png)

**Gray:**
- #6c757d: Pagination border, comment border, pagination disabled

![gray colour scheme](/readme-images/cinza.png)

**Home page Linear-gradient:**
- rgba(248,249,250), - F8F9FA
- rgba(182, 131, 224, 0.377), - B683E0
- rgba(255, 0, 140, 0.336), - FF008C
- rgb(255, 255, 255) - FFFFFF

![gradient colour scheme](/readme-images/gradient.png)

# USER EXPERIENCE

## Audience
This a platform for individuals to share their challenges in a lighthearted manner, inviting impartial perspectives from the community. It's a safe space where users can express themselves knowing they're not alone in their struggles. With every post and comment carefully moderated, we ensure a supportive environment for all. Whether the users are seeking advice or simply want to share your story, our site encourages open dialogue and empathy. 

## User Stories
**- EPIC 1 - Home page**
- [Send anonymous stories](https://github.com/Nathisaraujo/silly-talks-blog/issues/6)
As a blog user I can fill the home page gorm so that I can give send my stories without being logged

- [Home page](https://github.com/Nathisaraujo/silly-talks-blog/issues/13)
As a Site User, I can access the website home page and I can understand how the website is about and how it works.

**- EPIC 2 - Silly Talks page**
- [See list of posts](https://github.com/Nathisaraujo/silly-talks-blog/issues/2)
As a site user I can click on the "start talking" button so that I can see the list of posts

- [View content of the post](https://github.com/Nathisaraujo/silly-talks-blog/issues/3)
As a blog user I can click on the post I'm interested in on the "talks" page so that I can see the post text, the likes, and the comments

**- EPIC 3 - Logged-in user page**
- [Comment/Vote on posts](https://github.com/Nathisaraujo/silly-talks-blog/issues/5)
As a blog user I can comment and/or vote on posts when I'm logged in so that I can give my opinion about the discussed topic

- [Modify or delete a comment on a post](https://github.com/Nathisaraujo/silly-talks-blog/issues/8)
As a blog user I can modify or delete a comment on a post so that I can choose how to be involved

**- EPIC 4 - Register**
- [Account Registration](https://github.com/Nathisaraujo/silly-talks-blog/issues/4)
As a blog user I can sign up or log in so that I can comment and/or like posts

**- EPIC 5 - Porfile Page**
- [Manage Posts](https://github.com/Nathisaraujo/silly-talks-blog/issues/16)
As a blog user I can login in my profile so that I can manage my posts

- [See user activity](https://github.com/Nathisaraujo/silly-talks-blog/issues/18)
As a blog user I can log in so that I can see my activity

- [Edit profile information](https://github.com/Nathisaraujo/silly-talks-blog/issues/17)
As a blog user I can log in so that I can edit, add or delete my personal information

- [Add a post](https://github.com/Nathisaraujo/silly-talks-blog/issues/19)
As a logged user I can send a post request so that my story will be published on the website

- [Edit and Delete posts](https://github.com/Nathisaraujo/silly-talks-blog/issues/20)
As a logged user I can edit and delete posts so that I have the control of my posts

**- EPIC 6 - Porfile Page**
- [Create Drafts](https://github.com/Nathisaraujo/silly-talks-blog/issues/10)
As a blog admin I can draft posts so that I can finish writing the content later

- [Review Collaboration Requests](https://github.com/Nathisaraujo/silly-talks-blog/issues/15)
As an admin I can store collaboration requests in the database so that I can review them.

- [Approve comments](https://github.com/Nathisaraujo/silly-talks-blog/issues/11)
As a blog admin I can approve or disapprove comments so that I can filter out objectionable comments

- [Admin post management](https://github.com/Nathisaraujo/silly-talks-blog/issues/9)
As a blog admin I can create, read, update and delete posts so that I can manage my blog content


# FEATURES

## Existing Features

### Home Page

**- Navigation**

![Navigation bar](/readme-images/navigation.png)

- **Navigation Bar Structure:** The navigation bar was constructed using Bootstrap, ensuring a responsive and user-friendly design. 
- **Branding:** Positioned in the left corner, the navigation bar prominently displays the name of the website, ensuring easy identification and branding consistency.
- **User Authentication Indicator:** Located in the right corner, the navigation bar provides a clear indication of the user's authentication status, offering seamless navigation and personalized experiences.
- **Interactive Elements:** All elements within the navigation bar exhibit interactivity, dynamically changing color upon hovering, enhancing user engagement and intuitiveness.
- **Useful Links:** The navigation bar includes convenient links to access key pages such as [Silly Talks](<#silly-talks-page>) and the [register and login page](<#register-and-login>), facilitating streamlined navigation and user journey..

![Navigation bar logged](/readme-images/navlogged.png)

- **User Authentication Feedback:** When logged in, the user will receive personalized feedback in the form of a message displayed in the right corner, stating "You are logged in as -username-," providing a clear indication of their authentication status and enhancing user experience.
- **Enhanced Navigation Options:** Additionally, when logged in, the navigation bar will dynamically update to include convenient shortcuts to access the user's [profile page](<#profile>) and the [logout](<#logout>) functionality, ensuring seamless navigation and quick access to essential features.

**- Welcome message**

![landing page](/readme-images/landing.png)

- The landing page features a welcoming message that encapsulates the essence of the website and introduces visitors to its core concepts and ideas.

**- Website explanation**

![website explanation](/readme-images/explain.png)

- Directly beneath the welcome message, the website provides further insight into its core concepts and ideas, offering visitors a deeper understanding of its purpose and objectives.
- Positioned on the left side, visitors can explore a selection of published stories, showcasing the diverse range of content available on the platform and providing inspiration for potential contributions.
- On the right side, a detailed explanation of the voting system is presented, empowering users with an understanding of how they can engage with and contribute to the community-driven platform.
- The Font Awesome items are animated to uphold the relaxed atmosphere of the site, enhancing user engagement and adding a touch of dynamism to the browsing experience.
- When the user is logged in, a "Read More Stories" button appears, redirecting to the [Silly Talks page](<#silly-talks-page>), while for non-logged-in users, it directs to a [registration page](<#register>), encouraging seamless navigation tailored to user authentication status.

**- Call to register**

![register box](/readme-images/chamando.png)

- Directly below the website explanation, on the left side, a prominent box invites users to register, enabling them to participate in voting, commenting, and activity tracking features. 
- Upon logging in, the button transforms to "Start the Silliness," directing users to the Silly Talks page, fostering engagement and interaction within the community.

**- Collaboration form**

![contribution form](/readme-images/contribua.png)

- Positioned on the right side, the site encourages users to anonymously share their stories by completing a form, fostering a sense of inclusivity and encouraging user-generated content.

**- Footer**

![footer](/readme-images/footer.png)

- The footer is elegantly minimalistic, showcasing the website's social media links. 
- Additionally, it features a message indicating its educational purpose, ensuring transparency and fostering trust with users.

### Silly Talks Page

![index.html list of posts](/readme-images/index.png)

- The Silly Talks page presents a comprehensive list of posts available on the website, offering users easy access to a wealth of content.
- Additionally, it features a convenient [search bar](<#search-bar-page>), allowing users to quickly find posts related to specific topics or keywords.
- Each post card includes essential details such as its text, excerpt, author, and creation date, providing users with valuable context before engaging with the content.
- Furthermore, the post card prominently displays a vote count, enabling users to gauge the popularity of each post across different categories without needing to open it.
- To enhance user experience and navigation, pagination functionality is seamlessly integrated, ensuring smooth browsing through multiple pages of posts.

### Search Bar Page

![Search bar page](/readme-images/procura.png)

- The search bar page showcases a curated list of posts closely related to the user's search query, facilitating efficient content discovery.
- Clicking on a post redirects the user to its dedicated page, allowing for a deeper exploration of the content.
- For added convenience, users can initiate a new search by simply clicking the "New Search" button, ensuring a seamless search experience.

![No results found](/readme-images/cade.png)

- In the event of no search results, users are presented with a clear and informative message, ensuring transparency and guiding them to explore alternative options.

### Post page

![Post detail page](/readme-images/post.png)

- Clicking on a post redirects the user to a dedicated post page, where the title of the post is prominently displayed at the center of the page.
- Below the title, users find the post's excerpt, providing a concise overview of its content.
- Further down, users can view information about the author and the post's creation date.

![Collapsable button read more](/readme-images/colapse.png)

- By clicking on "See the Whole Silliness Here," users can expand a collapsible section to reveal the full content of the post.

![comments](/readme-images/comentario.png)

- For non-logged-in users, comments are visible, accompanied by a message prompting them to log in or register to vote or comment.

![votes](/readme-images/votos.png)

![add a comment](/readme-images/comente.png)

- Logged-in users have access to voting buttons and counters, as well as a comment box to engage with the post.

![comment author](/readme-images/autor_comentario.png)

- If the user is the author of the comment, they will see edit and delete buttons for their own comments.

![Post author](/readme-images/post_author.png)

- Similarly, if the user is the author of the post, they will see edit and delete buttons for the post itself.

### Register and Login

![Login page](/readme-images/login.png)

- The register page features a user-friendly interface where users can easily choose a username, enter their email, and create a password.
- Detailed instructions are provided in the password field, ensuring users understand the requirements for creating a secure password.
- For existing users, a convenient link is available to redirect them to the login page, streamlining the authentication process.

![invalid password](/readme-images/senha.png)

- In case of invalid data input, clear and informative error messages are displayed, guiding users to correct any mistakes and successfully complete the registration process.

### Logout

![signout page](/readme-images/signout.png)

- In case of invalid data input, clear and informative error messages are displayed, guiding users to correct any mistakes and successfully complete the registration process.

### Profile

![profile page](/readme-images/profile.png)

- Upon logging in or registering, users are automatically redirected to their profile page, ensuring a seamless entry into the platform.
- The profile page's navigation bar is persistently displayed across all profile pages, providing easy access to navigation options.
- Users have access to view their personal details, facilitating control over their account information.

![user statistics](/readme-images/estatistica.png)

- Clicking on the collapsible button reveals a table displaying user statistics, offering insights into activity and engagement.

![fallback image](/readme-images/ninguem.png)

- In the absence of a user-uploaded profile picture, a placeholder image is displayed, ensuring a visually consistent experience.

### New Post

![add a post page](/readme-images/addpost.png)

- Clicking on "Post - New Post" redirects the user to an "Add Post" page, streamlining the process of creating new content.
- On the "Add Post" page, users can submit a new post request by providing the title, excerpt, and content, facilitating seamless content creation.
- After submitting the new post, users are automatically redirected to the "Manage Posts" page, providing immediate access to review and manage their posts.

### Manage Posts

![manage posts page](/readme-images/manage.png)

- The "Manage Post" page showcases all posts created by the user, presenting essential details such as the title, author, date of submission, and excerpt.
- Users can easily access individual posts by clicking on their titles, seamlessly redirecting them to the respective post pages for further engagement.
- Additionally, the page features a dedicated section listing drafts, providing visibility into posts awaiting approval and enabling users to monitor and manage their content effectively.

![no post results found](/readme-images/nodraft.png)

- If the user doesn't have any posts or drafts, a message will be displayed to inform them of this, ensuring clarity.

### Edit Profile

![edit profile personal information](/readme-images/editar.png)

- Users have the ability to edit their profile information within the "Edit" tab, providing a convenient way to update their details.
- Upon saving the changes, users are automatically redirected to the [profile page](<#profile>), ensuring a smooth and seamless transition while confirming the successful update of their information.

### Activity

![user activity](/readme-images/atividade.png)

- Clicking on the "Activity" tab will reveal a comprehensive list of the user's voting activity and comments, providing visibility into their engagement on the platform.
- If the user has not voted or commented in a specific category, a message will be displayed, ensuring transparency and guiding them to explore other areas of the platform.
- Each item in the post list includes the title, author, and excerpt, allowing users to quickly identify posts of interest. Clicking on any item redirects the user to the respective post page for further exploration.

### General

![messages](/readme-images/msg.png)

- Users will receive notifications for every action performed on the website, ensuring they stay informed and engaged with updates and changes.

![goback button](/readme-images/button.png)

- Throughout the website, users will find convenient "Go Back" buttons, offering a quick and intuitive way to navigate back to the previous page, enhancing the overall user experience.

## Future Features

In the future, this website will include the following features:

- **Enhanced user interaction:** Users will have the ability to view each other's profile pages, fostering a sense of community and connection.
- **Improved post management:** Users can delete or edit draft posts, providing greater control and flexibility over their content creation process.
- **Password recovery functionality:** A "Forgot My Password" feature will be implemented, enabling users to regain access to their accounts securely.
- **Expanded engagement options:** Users will be able to like comments, facilitating appreciation and acknowledgment of valuable contributions.
- **Enhanced comment functionality:** Users can reply to other comments, encouraging meaningful discussions and interactions within the community.
- **Private messaging capability:** Users will have the option to reply to posts privately, establishing a direct channel of communication with the post author for more personal exchanges.

# LOGIC

## Database
A database diagram (ERD) was generated using Django Extensions.

You can see the documentation I've followed [here.](https://www.linkedin.com/pulse/generate-database-diagramerd-django-extensions-automatically-srujan-s/)

![database schema](/readme-images/database.png)

## Workflow

I've crafted a comprehensive workflow detailing the functionality of every feature on the website. This detailed roadmap elucidates the user journey from registration to navigation, post creation, engagement, and profile management. By mapping out each step and interaction, users can seamlessly navigate the platform with clarity and ease. This workflow serves as a guiding beacon, ensuring that every aspect of the website operates harmoniously, fostering a seamless and intuitive user experience from start to finish.

![first workflow](/readme-images/workflow1.jpeg)

![second workflow](/readme-images/workflow2.jpeg)

### Agile
In this project, I've implemented the Agile methodology to ensure dynamic and iterative development cycles. By breaking tasks into manageable sprints, we maintain flexibility and adaptability, responding efficiently to evolving requirements. 

## Django Apps

I've structured the project into three distinct Django apps, each serving a specific purpose. This deliberate organization ensures clarity and maintainability throughout the development process. By compartmentalizing functionality into separate apps, we enhance modularity and streamline collaboration. This approach fosters a clear understanding of the project's architecture and facilitates efficient development, testing, and deployment workflows.

Models represent our data structure, Views handle the presentation logic, and Forms manage user input. These components interact harmoniously: Models define the database schema, Views render the data for user interaction, and Forms facilitate data entry and validation. Together, they form the core of our application, ensuring efficient data management and seamless user experience.

### Blog App

- **Models**
1. Post - The Post model serves as the backbone for all blog posts within the system. It encapsulates crucial details such as the title, author, content, creation date, update date, excerpt and status of each post. This first part was all from the Code Instute's I Think Therefore I Blog template. Additionally, I included some objects that tracks user interactions through like, silly, and more information votes, as well as its respectives counters. Property methods num_likes, num_silly, and num_more calculate the respective vote counts for each post, enhancing user engagement metrics.

2. Comment - The Comment model was 100% Code Instute's I Think Therefore I Blog template. fIt facilitates the storage of individual comments associated with specific posts and users. Each comment includes the post it's related to, the author who submitted it, the content body, approval status, and creation timestamp. This model ensures efficient organization and retrieval of user-generated content, fostering interaction and discourse within the blogging community.

- **Views**
1. Post List - it retrieves published posts from the database and displays them paginated on the index.html template. It ensures only published posts are displayed to users and provides a context of object_list containing a list of published posts.

2. Post Detail - it retrieves details of a specific post based on the provided slug. It handles comment submission and rendering, displaying the post's content, associated comments, and related user interactions such as voting. Additionally, it provides a comment form for users to submit new comments.

3. Comment Edit - it allows users to edit their comments. It retrieves the post associated with the comment and the comment itself, then updates the comment based on user input. After editing, users are redirected to the post detail page.

4. Comment Delete - it permits users to delete their comments. It verifies the user's authorization to delete the comment and removes it from the database if the user is the author. Users are then redirected to the post detail page.

5. Post Vote - it handles voting on posts, enabling users to mark posts as not silly, silly, or in need of more information. It processes user preferences and updates post vote counts accordingly, ensuring accurate representation of user opinions on each post.

6. Search - The search_view function allows users to search for specific posts based on provided query terms. It retrieves posts containing the query term in their title or excerpt and renders the search results to the user.

- **Forms**
1. Comment Form - it serves as a form for users to submit comments on posts within the website. It is designed to interact with the Comment model.


### Home App

- **Models**
1. Collaboration Request - The CollaborateRequest model model was made following Code Instute's I Think Therefore I Blog template. I only added the title field so the users can send what title they want to use. It stores collaboration requests, capturing sender details like name and email, along with request specifics such as title and message content. Additionally, a flag is included to indicate whether the request has been posted. This model facilitates the management of collaboration inquiries on the website, enabling administrators to review, process, and mark requests as posted.

- **Views**
1. Home - it renders the home.html template, which includes a collaboration form. Upon receiving a POST request with valid form data, the collaboration request is saved, and a success message is displayed using Django's messaging framework. The view initializes an instance of the CollaborateForm, which is passed to the template context for rendering. This view serves as the entry point for users to submit collaboration requests through the website's homepage.

- **Forms**
1. Collaboration Form - it allows users to submit collaboration requests anonymously by providing their name, email, title, and message. It inherits from Django's ModelForm and is associated with the CollaborateRequest model, specifying the fields to be included in the form. Additionally, it includes a crispy-bootstrap5 FloatingField for enhanced form rendering. This form facilitates the submission of collaboration requests through the website's collaboration feature.

### Profiles App

This app was designed and created by me, without the support of any Code Institute's walkthrough. Some parts of the code were inspired in my colleague, which I credit [here](<#credits>)

- **Models**
1. User Profile - The UserProfile model stores user profiles, containing fields for bio, profile picture, birth date, location, registration date, and gender. It includes a one-to-one relationship with the built-in User model from Django, ensuring each user has a unique profile. The bio field allows users to provide additional information about themselves, while the picture field utilizes CloudinaryField for storing profile pictures. Other fields such as birth_date, location, registration_date, and gender provide additional user details. This model enhances user interaction and personalization within the website.

- **Views**
1. Profile - it renders the user profile page with user-specific information, including user statistics such as the count of posts authored, comments made, and votes received on posts. It retrieves the UserProfile instance associated with the provided username and passes relevant context to the profile.html template.

2. Add Post - it allows authenticated users to add a new post, rendering the add_post.html template with the PostForm instance. Upon successful submission, a success message is displayed, and the user is redirected to their post list.

3. Edit Post - it enables authenticated users to edit their own posts. It renders the update_post.html template with the PostForm instance pre-populated with the post's current data. After successfully updating the post, a success message is shown, and the user is redirected to the post detail page.

4. Delete Post - it permits authenticated users to delete their own posts. It renders the delete_post.html template and handles post deletion upon confirmation. After successful deletion, a success message is displayed, and the user is redirected to their post list.

5. Manage Posts - it provides authenticated users with a way to manage their posts by displaying a list of posts and drafts authored by the user. It passes the user's posts and drafts as context to the manage_posts.html template.

6. User activity - it showcases user activity by displaying the posts on which the user has voted or commented. It retrieves posts voted as silly, not silly and more information, and commented posts associated with the user and passes them as context to the user_activity.html template.

7. Edit Profile - it allows authenticated users to edit their profile information. It renders the edit_profile.html template with the UserProfileForm instance pre-filled with the user's current profile data. Upon successful profile update, a success message is shown, and the user is redirected to their profile page.

- **Forms**
1. Post Form - it allows users to add and edit blog posts by providing a title, excerpt, and content. It ensures that the length of the title does not exceed 200 characters and the excerpt does not exceed 500 characters, truncating them if necessary. This form enhances the user experience by simplifying the process of creating and updating blog posts.

2. User Profile Form - it enables users to update their profiles, including their bio, birth date, location, gender, and profile picture. It provides a convenient interface for users to manage their personal information. Additionally, it includes validation to limit the length of the bio to 255 characters, ensuring consistency and preventing excessive text input. This form enhances user interaction and customization within the website.

# TECHNOLOGIES USED

## Languages
- **HTML:** structure the content of web pages.

- **CSS:** style HTML elements.

- **JavaScript:** create interactive and dynamic features.

- **Python:** is used with the Django framework to handle server-side logic and data manipulation.

## Libraries and Programs:

- **Frameworks and Packages:**
    - **Django:** a high-level Python web framework that simplifies the process of building web applications.

    - **Crispy Forms:** Crispy Forms is a Python package used to style Django forms, making them more visually appealing and user-friendly.

    - **Bootstrap5:** front-end framework for building responsive and mobile-first websites.

    - **Cloudinary:** cloud-based image and video management service.

    - **Allauth:** is a Django package that provides authentication, registration, and account management functionality for Django applications

    - **Bootstrap Datepicker:** Django package that integrates the Bootstrap Datepicker Plus plugin with Django forms, allowing to add date and time picker widgets to their forms with ease.
    
    - **Password Validators:** a Django package that provides a set of customizable password validators for enforcing password strength requirements, such as minimum length, uppercase letters, digits, symbols, etc.

    - **Gunicorn:** a WSGI HTTP server for running Python web applications, providing a fast and scalable solution for serving web requests in production environments.

    - **Whitenoise:** a Python library for serving static files efficiently.

    - **PyGraphviz:** a Python library used for working with Graphviz, to generate the ERD.

- **Database:**
    - **ElephantSQL:** a PostgreSQL database service hosted in the cloud.

    - **SQLite:** database management system used as a local database during development.

- **Tools and Platforms:**

    - **Gitpod:** cloud-based integrated development environment (IDE) used for coding.

    - **Git and GitHub:** track changes in project files.

    - **Heroku:** cloud-based platform as a service (PaaS) that enables deployment and management.

    - **Google Developer Tools:** web development and debugging tools built into the Google Chrome browser.

- **Design and Styling:**

    - **Summernote:** rich text editor that provides an easy-to-use interface for formatting and styling text in web applications.

    - **Fontawesome:** a library of scalable vector icons.

    - **Google Fonts:** a collection of open-source fonts hosted by Google. 

    - **Coolors:** Coolors is a color scheme generator.

    - **LucidChart:** diagramming tool used for creating flowcharts.

    - **Canva:** a graphic design platform used for creating visual content.

- **Validators:**

    - **Code Institute Python Linter:** Python.

    - **W3C Validator:** HTML and CSS.

    - **JS Hint:** JavaScript.

# TESTING

Refer to the [TESTING.MD](https://github.com/Nathisaraujo/project4/blob/main/TESTING.md)

# DEPLOYMENT

## Deployment to Heroku

### Heroku Setup:
1. **Create a New App:** log in to Heroku and create a new app.
2. **Configure Settings:** in the settings tab of your Heroku app dashboard, set config vars for 
 production:
    - DATABASE_URL 
    - SECRET_KEY
    - CLOUDINARY_URL
3. **Add Buildpack:** Include a Python buildpack in the settings tab to install necessary dependencies.

### Deploying
1. **Install Gunicorn:** In Gitpod, install Gunicorn using "pip3 install gunicorn" and freeze it into requirements.txt.
2. **Create Procfile:** Specify the web dyno command in a Procfile.
3. **Disable Collectstatic:** Temporarily disable collectstatic to prevent serving static files during deployment.
4. **Commit and Push:** Commit changes to GitHub and push them to Heroku for deployment. Heroku automatically detects changes in the repository and triggers the deployment process.

## Forking
Forking allows you to freely experiment with changes without affecting the original repository.

1. **Create a Fork:** Visit the GitHub repository and click on 'Fork' to create a copy of the repository under your account. 
2. **Customize Fork:** Customize the fork as needed before creating it. You can modify the fork's settings, description, and other details to suit your requirements.

## ElephantSQL
1. **Create New Instance:** Log in to ElephantSQL and select 'Create New Instance'. 
2. **Plan Selection:** Choose a plan, input your details, and review the instance configuration. 
3. **Select Region:** Choose a region for hosting the database, such as EU-West-1 (Ireland). 
4. **Database URL:** After instance creation, copy the DATABASE_URL provided for use in the project. This URL contains connection details necessary for Django to communicate with the ElephantSQL database.

## Cloning Repository
Cloning creates a local copy of the repository on your machine, allowing you to work on the codebase locally.

1. **Copy Repository Link:** Copy the repository link from GitHub.
2. **Clone Repository:** Use Git commands to clone the repository to your local environment.
3. **Set Up Environment:** Enter your workspace, set up a virtual environment, install dependencies from requirements.txt, and create an env.py file. 
4. **Configuration:** Modify settings.py and other necessary files to match your environment and configurations. Update settings.py with database connection details, secret keys, and other environment-specific configurations.

## Cloudinary
The CLOUDINARY_URL contains authentication and configuration details required for Django to interact with the Cloudinary service.

1. **Log in to Cloudinary:** Access your Cloudinary account through the web interface.
2. **Retrieve Cloudinary URL:** Copy your CLOUDINARY_URL for use in storing static and media files.

# UPDATE - JULY 2024

On July 2024 I made the following updates taking into consideration the assessments criterias:

## User Stories 

While working to complete my project and learning Django basics, I mistakenly created issues in a private repository. I used the Kanban board, but since it was linked to the private repository, the issues couldn't be seen. I've now transferred them to the correct public repository. Each issue shows its original creation date during my fourth project.

I apologize for the oversight caused by my focus on deadlines, bug fixing, and learning. I'll ensure to use Agile practices with Github correctly in the future.

## Post 

Previously, when a user submitted a post, it entered a draft status. Upon admin approval, it appeared in the user's profile but didn't update to "approved," causing a 500 error when accessed. I've fixed this in the commit "fixed post status issue" and added comments titled "Fixing assessments error" for easy reference. After testing, everything appears to work correctly now.

# CREDITS

- The "I Think Therefore I Blog" project by Code Institute played a crucial role in my learning journey. It provided invaluable insights and knowledge, significantly contributing to my project development.

- **Debugging and Error Resolution:** When encountering issues with the like button implementation, I utilized various resources for assistance, including tutoring sessions, browser developer tools, and ChatGPT.

- I used [ChatGPT](https://chat.openai.com/) to help me throughout the project, leveraging its capabilities in various ways:
    - **Error Understanding and Debugging:** ChatGPT assisted me in comprehending complex errors and provided insights to debug the code effectively.
    - **Typo Detection:** I employed ChatGPT to identify any typos present in my code or documentation files.
    - **Vocabulary and Grammar Enhancement:** ChatGPT helped refine the vocabulary and grammar in my project documentation, ensuring clarity as English is not my first language.

    - **Specific Use Cases:**
        - **Customizing Allauth Text:** When faced with the task of customizing Allauth text, ChatGPT provided guidance on the necessary steps and best practices.

            ![chatgpt customize allauth](/readme-images/1.png)

        - **JS Assistance:** Due to  my limited proficiency in JavaScript, I sought ChatGPT's advice on implementing a 'go back' button, which it efficiently provided.

            ![chatgpt goback buttons](/readme-images/2.png)

        - **Fixing User Total Votes Issue:** I had an issue related to user_total_votes in profile views. It was returning some random numbers. It offered insightful suggestions, enabling me to address the problem effectively and tailor the solution to my specific requirements.

            ![chatgpt user statistics](/readme-images/3.png)

- **Email Field Configuration:** To set the email field as required in Django Allauth, I found a helpful solution on [Stack Overflow](https://stackoverflow.com/questions/23956288/django-all-auth-email-required).

- **Implementing Like Button:** I learned how to add a like button by watching a tutorial on YouTube. [YouTube](https://www.youtube.com/watch?v=xqFM6ykQEwo).

- **Email Verification with Social Accounts:** I followed multiple video tutorials to understand how to implement email verification with social accounts:
    - [Video 1](https://www.youtube.com/watch?v=RyB_wdEZhOw&t=40s)
    - [Video 2](https://www.youtube.com/watch?v=NG48CLLsb1A)
    - [Video 3](https://www.youtube.com/watch?v=GQySb3W2feo)

- **Code Collaboration:** A friend shared his code with me, which greatly aided in completing the like button feature. [JustBlog](https://github.com/gioZAK/justblog).

- **Profile Page Development:** To enhance the profile page functionality, I referred to various online resources:
    - [Dev.to Article](https://dev.to/earthcomfy/django-user-profile-3hik)
    - [Blog Tutorial](https://dontrepeatyourself.org/post/django-blog-tutorial-part-3-users-authentication/#profile-page)
    - [YouTube Tutorial](https://www.youtube.com/watch?v=zb4fIvtn4tY)

- **Django Password Validators:** For implementing Django password validators, I consulted the official documentation available [here](https://pypi.org/project/django-password-validators/#:~:text=Validator%20checks%20if%20the%20password,are%20stored%20in%20a%20database.).

- **Post Views Enhancement:** I referred to a project I found on LinkedIn, by [Eleanor Bucke](https://github.com/eleanorbucke21/PP4/), which made the Bawarchi Khana Website.

To craft this README, I referred to the following projects found on LinkedIn:

1. **[The Groomers Network Website by Helen Murugan](https://github.com/helenmurugan/the-groomers-network/)**

2. **[Inspiring Young Writers by Georgina Carlisle](https://github.com/GeorginaCarlisle/inspiring-young-writers/)**
