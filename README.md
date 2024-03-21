# Silly Talks

Developer: Nathalia de Araujo Silva

![Responsive Design Screenshot](/readme-images/inicial.png)

Silly Talks is a platform where users share stories to receive feedback on whether they're silly or serious, aiming to allow people to vent in a fun way and get impartial opinions.

Link para live website

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
    * [Django Apps](<#django-apps>)
    * [Models, views and forms](<#models-views-and-forms>)
    * [Agile](<#agile>)

* [Techonologies Used](<#technologies-used>)
    * [Languages](<#languages>)
    * [Libraries and Programs](<#libraries-and-programs>)

* [TESTING](<#testing>)
    * [Code Validation](<#code-validation>)
    * [Manual Testing](<#manual-testing>)

* [DEPLOYMENT](<#deployment>)
    
* [CREDITS](<#credits>)
	* [Colleagues](<#colleagues>)
	* [Websites](<#websites>)

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

![Responsive Design Screenshot](/readme-images/lobster.png)

2. **"DM Serif Display"**, a serif font, is employed for post titles, the welcome message, and text prompting user interaction such as voting. The objective is to craft attention-grabbing titles, distinct from the rest of the page, reminiscent of the aesthetic of a printed newspaper headline.

![Responsive Design Screenshot](/readme-images/DM-Serif-Display.png)

3. **"Comfortaa"**, another sans-serif font, is utilized for body text and is consistently applied across the entire website. Its purpose is to foster an ambiance of relaxation and approachability, ensuring that the site maintains an informal and friendly tone."

![Responsive Design Screenshot](/readme-images/comfortaa.png)

## Color Scheme

In [color theory](https://www.colorpsychology.org/pink/), pink is often associated with feelings of hope and sensitivity. It represents a soft and nurturing energy, evoking a sense of optimism and renewal. Pink is believed to inspire hope in difficult times and convey a gentle sensitivity towards emotions and experiences. Its presence can symbolize a comforting reassurance, reminding us that brighter days are ahead and encouraging us to approach challenges with a compassionate heart.

Despite the main color being pink, the entire website adopts a white color scheme for a cleaner look. Additionally, we've included shades of purple to enhance certain elements, and shades of gray for buttons such as "back" and "delete," as well as for some box borders.

Pictures from [Coolors](https://coolors.co/)

**White:**
- #F9FAFC: Background, footer text, body background

![Responsive Design Screenshot](/readme-images/branco.png)

**Purple:**
- #693d69: Nav link
- #630d5c: Nav title, pagination active, button form text
- #630d5c79: Message border
- #3d013a: Footer background, vote buttons, post card information
- #2f2738: Post list title, post link, pagination text

![Responsive Design Screenshot](/readme-images/roxo.png)

**Pink:**
- #dba2d836: Comments background
- #dba2d8: Message background, button background, pagination background
- #f9d1f7: Post list
- #c27bbcc0: Input borders, container borders, index post cards, home page cards

![Responsive Design Screenshot](/readme-images/rosa.png)

**Gray:**
- #6c757d: Pagination border, comment border, pagination disabled

![Responsive Design Screenshot](/readme-images/cinza.png)

**Home page Linear-gradient:**
- rgba(248,249,250), - F8F9FA
- rgba(182, 131, 224, 0.377), - B683E0
- rgba(255, 0, 140, 0.336), - FF008C
- rgb(255, 255, 255) - FFFFFF

![Responsive Design Screenshot](/readme-images/gradient.png)

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

![Responsive Design Screenshot](/readme-images/navigation.png)

**- Navigation Bar Structure:** The navigation bar was constructed using Bootstrap, ensuring a responsive and user-friendly design. 
**- Branding:** Positioned in the left corner, the navigation bar prominently displays the name of the website, ensuring easy identification and branding consistency.
**- User Authentication Indicator:** Located in the right corner, the navigation bar provides a clear indication of the user's authentication status, offering seamless navigation  
and personalized experiences.
**- Interactive Elements:** All elements within the navigation bar exhibit interactivity, dynamically changing color upon hovering, enhancing user engagement and intuitiveness.
**- Useful Links:** The navigation bar includes convenient links to access key pages such as [Silly Talks](<#silly-talks-page>) and the [register and login page](<#register-and-login>), facilitating streamlined navigation and user journey..

![Responsive Design Screenshot](/readme-images/navlogged.png)

**- User Authentication Feedback:** When logged in, the user will receive personalized feedback in the form of a message displayed in the right corner, stating "You are logged in as -username-," providing a clear indication of their authentication status and enhancing user experience.
**- Enhanced Navigation Options:** Additionally, when logged in, the navigation bar will dynamically update to include convenient shortcuts to access the user's [profile page](<#profile>) and the [logout](<#logout>) functionality, ensuring seamless navigation and quick access to essential features.

**- Welcome message**

![Responsive Design Screenshot](/readme-images/landing.png)

- The landing page features a welcoming message that encapsulates the essence of the website and introduces visitors to its core concepts and ideas.

**- Website explanation**

![Responsive Design Screenshot](/readme-images/explain.png)

- Directly beneath the welcome message, the website provides further insight into its core concepts and ideas, offering visitors a deeper understanding of its purpose and objectives.
- Positioned on the left side, visitors can explore a selection of published stories, showcasing the diverse range of content available on the platform and providing inspiration for potential contributions.
- On the right side, a detailed explanation of the voting system is presented, empowering users with an understanding of how they can engage with and contribute to the community-driven platform.
- The Font Awesome items are animated to uphold the relaxed atmosphere of the site, enhancing user engagement and adding a touch of dynamism to the browsing experience.
- When the user is logged in, a "Read More Stories" button appears, redirecting to the [Silly Talks page](<#silly-talks-page>), while for non-logged-in users, it directs to a [registration page](<#register>), encouraging seamless navigation tailored to user authentication status.

**- Call to register**

![Responsive Design Screenshot](/readme-images/chamando.png)

- Directly below the website explanation, on the left side, a prominent box invites users to register, enabling them to participate in voting, commenting, and activity tracking features. 
- Upon logging in, the button transforms to "Start the Silliness," directing users to the Silly Talks page, fostering engagement and interaction within the community.

**- Collaboration form**

![Responsive Design Screenshot](/readme-images/contribua.png)

- Positioned on the right side, the site encourages users to anonymously share their stories by completing a form, fostering a sense of inclusivity and encouraging user-generated content.

**- Footer**

![Responsive Design Screenshot](/readme-images/footer.png)

- The footer is elegantly minimalistic, showcasing the website's social media links. 
- Additionally, it features a message indicating its educational purpose, ensuring transparency and fostering trust with users.

### Silly Talks Page

![Responsive Design Screenshot](/readme-images/index.png)

- The Silly Talks page presents a comprehensive list of posts available on the website, offering users easy access to a wealth of content.
- Additionally, it features a convenient [search bar](<#search-bar-page>), allowing users to quickly find posts related to specific topics or keywords.
- Each post card includes essential details such as its text, excerpt, author, and creation date, providing users with valuable context before engaging with the content.
- Furthermore, the post card prominently displays a vote count, enabling users to gauge the popularity of each post across different categories without needing to open it.
- To enhance user experience and navigation, pagination functionality is seamlessly integrated, ensuring smooth browsing through multiple pages of posts.

### Search Bar Page

![Responsive Design Screenshot](/readme-images/procura.png)

- The search bar page showcases a curated list of posts closely related to the user's search query, facilitating efficient content discovery.
- Clicking on a post redirects the user to its dedicated page, allowing for a deeper exploration of the content.
- For added convenience, users can initiate a new search by simply clicking the "New Search" button, ensuring a seamless search experience.

![Responsive Design Screenshot](/readme-images/cade.png)

- In the event of no search results, users are presented with a clear and informative message, ensuring transparency and guiding them to explore alternative options.

### Post page

![Responsive Design Screenshot](/readme-images/post.png)

- Clicking on a post redirects the user to a dedicated post page, where the title of the post is prominently displayed at the center of the page.
- Below the title, users find the post's excerpt, providing a concise overview of its content.
- Further down, users can view information about the author and the post's creation date.

![Responsive Design Screenshot](/readme-images/colapse.png)

- By clicking on "See the Whole Silliness Here," users can expand a collapsible section to reveal the full content of the post.

![Responsive Design Screenshot](/readme-images/comentario.png)

- For non-logged-in users, comments are visible, accompanied by a message prompting them to log in or register to vote or comment.

![Responsive Design Screenshot](/readme-images/votos.png)

![Responsive Design Screenshot](/readme-images/comente.png)

- Logged-in users have access to voting buttons and counters, as well as a comment box to engage with the post.

![Responsive Design Screenshot](/readme-images/autor_comentario.png)

- If the user is the author of the comment, they will see edit and delete buttons for their own comments.

![Responsive Design Screenshot](/readme-images/post_author.png)

- Similarly, if the user is the author of the post, they will see edit and delete buttons for the post itself.

### Register and Login

![Responsive Design Screenshot](/readme-images/login.png)

- The register page features a user-friendly interface where users can easily choose a username, enter their email, and create a password.
- Detailed instructions are provided in the password field, ensuring users understand the requirements for creating a secure password.
- For existing users, a convenient link is available to redirect them to the login page, streamlining the authentication process.

![Responsive Design Screenshot](/readme-images/senha.png)

- In case of invalid data input, clear and informative error messages are displayed, guiding users to correct any mistakes and successfully complete the registration process.

### Logout

![Responsive Design Screenshot](/readme-images/signout.png)

- In case of invalid data input, clear and informative error messages are displayed, guiding users to correct any mistakes and successfully complete the registration process.

### Profile

![Responsive Design Screenshot](/readme-images/profile.png)

- Upon logging in or registering, users are automatically redirected to their profile page, ensuring a seamless entry into the platform.
- The profile page's navigation bar is persistently displayed across all profile pages, providing easy access to navigation options.
- Users have access to view their personal details, facilitating control over their account information.

![Responsive Design Screenshot](/readme-images/estatistica.png)

- Clicking on the collapsible button reveals a table displaying user statistics, offering insights into activity and engagement.

![Responsive Design Screenshot](/readme-images/ninguem.png)

- In the absence of a user-uploaded profile picture, a placeholder image is displayed, ensuring a visually consistent experience.

### New Post

![Responsive Design Screenshot](/readme-images/addpost.png)

- Clicking on "Post - New Post" redirects the user to an "Add Post" page, streamlining the process of creating new content.
- On the "Add Post" page, users can submit a new post request by providing the title, excerpt, and content, facilitating seamless content creation.
- After submitting the new post, users are automatically redirected to the "Manage Posts" page, providing immediate access to review and manage their posts.

### Manage Posts

![Responsive Design Screenshot](/readme-images/manage.png)

- The "Manage Post" page showcases all posts created by the user, presenting essential details such as the title, author, date of submission, and excerpt.
- Users can easily access individual posts by clicking on their titles, seamlessly redirecting them to the respective post pages for further engagement.
- Additionally, the page features a dedicated section listing drafts, providing visibility into posts awaiting approval and enabling users to monitor and manage their content effectively.

![Responsive Design Screenshot](/readme-images/nodraft.png)

- If the user doesn't have any posts or drafts, a message will be displayed to inform them of this, ensuring clarity.

### Edit Profile

![Responsive Design Screenshot](/readme-images/editar.png)

- Users have the ability to edit their profile information within the "Edit" tab, providing a convenient way to update their details.
- Upon saving the changes, users are automatically redirected to the [profile page](<#profile>), ensuring a smooth and seamless transition while confirming the successful update of their information.

### Activity

![Responsive Design Screenshot](/readme-images/atividade.png)

- Clicking on the "Activity" tab will reveal a comprehensive list of the user's voting activity and comments, providing visibility into their engagement on the platform.
- If the user has not voted or commented in a specific category, a message will be displayed, ensuring transparency and guiding them to explore other areas of the platform.
- Each item in the post list includes the title, author, and excerpt, allowing users to quickly identify posts of interest. Clicking on any item redirects the user to the respective post page for further exploration.

### General

![Responsive Design Screenshot](/readme-images/msg.png)

- Users will receive notifications for every action performed on the website, ensuring they stay informed and engaged with updates and changes.

![Responsive Design Screenshot](/readme-images/button.png)

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
* Explains databse
prints

## Workflow
* Explain workflow
prints

## Django App
* Explains audience
prints

## Models, Views and Forms
* Explain each thing
prints

## Agile
* Explain agile
prints

# TECHNOLOGIES USED

## Languages
* Explains each one in list

## Libraries and Programs
* Explain each one and try to add the pictures

# TESTING

## Code Validation
* Colocar print de cada um?

## Manual Testing
* ver o que tem 

# DEPLOYMENT

* Explicar essa merda

# CREDITS

## Colleagues
* lista de projetos que me inspirei

## Websites
* pegar do treco de documentation
