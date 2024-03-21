# Silly Talks

Developer: Nathalia de Araujo Silva

main page print

Silly Talks is a platform where users share stories to receive feedback on whether they're silly or serious, aiming to allow people to vent in a fun way and get impartial opinions.

Link para live website

# CONTENT

* [OBJECTIVES](<#objectives>)

* [DESIGN](<#design>)
    * [Typography](<#typography>)
    * [Color Scheme](<#color-scheme>)

* [USER EXPERIENCE](<#user-experience-ux>)
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
2. **"DM Serif Display"**, a serif font, is employed for post titles, the welcome message, and text prompting user interaction such as voting. The objective is to craft attention-grabbing titles, distinct from the rest of the page, reminiscent of the aesthetic of a printed newspaper headline.
3. **"Comfortaa"**, another sans-serif font, is utilized for body text and is consistently applied across the entire website. Its purpose is to foster an ambiance of relaxation and approachability, ensuring that the site maintains an informal and friendly tone."


Prints das fontes

## Color Scheme

In [color theory](https://www.colorpsychology.org/pink/), pink is often associated with feelings of hope and sensitivity. It represents a soft and nurturing energy, evoking a sense of optimism and renewal. Pink is believed to inspire hope in difficult times and convey a gentle sensitivity towards emotions and experiences. Its presence can symbolize a comforting reassurance, reminding us that brighter days are ahead and encouraging us to approach challenges with a compassionate heart.

Despite the main color being pink, the entire website adopts a white color scheme for a cleaner look. Additionally, we've included shades of purple to enhance certain elements, and shades of gray for buttons such as "back" and "delete," as well as for some box borders.

Pictures from [Coolors](https://coolors.co/)

**White:**
- #F9FAFC: Background, footer text, body background

**Purple:**
- #693d69: Nav link
- #630d5c: Nav title, pagination active, button form text
- #630d5c79: Message border
- #3d013a: Footer background, vote buttons, post card information
- #2f2738: Post list title, post link, pagination text

**Pink:**
- #dba2d836: Comments background
- #dba2d8: Message background, button background, pagination background
- #f9d1f7: Post list
- #c27bbcc0: Input borders, container borders, index post cards, home page cards

**Gray:**
- #6c757d: Pagination border, comment border, pagination disabled

**Home page Linear-gradient:**
- rgba(248,249,250), - F8F9FA
- rgba(182, 131, 224, 0.377), - B683E0
- rgba(255, 0, 140, 0.336), - FF008C
- rgb(255, 255, 255) - FFFFFF

Foto com as cores lado a lado

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
	Explicar tudo que contém
    Colocar Prints

### Silly Talks Page
	Explicar tudo que contém
    Colocar Prints

### Register
    Explicar tudo que contém
    Colocar Prints

### Profile
	Explicar tudo que contém
    Colocar Prints

## Future Features
* Explain each user stories by points

Foto geral com todos cumpridos

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
