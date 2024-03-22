# TESTING

Back to [Silly Talks README](https://github.com/Nathisaraujo/project4/blob/main/README.md)

# TABLE OF CONTENTS

* [CODE VALIDATION](<#code-validation>)
    * [HTML](<#html>) 
    * [CSS](<#css>) 
    * [Python](<#python>) 

* [RESPONSIVENESS](<#responsivess>) 

* [BROWSER COMPATIBILITY](<#browser-compatibility>) 

* [LIGHTHOUSE](<#lighthouse>) 

* [MANUAL TESTING](<#manual-testing>)

* [DEFENSIVE PROGRAMMING](<#defensive-programming>) 

* [USER STORY TESTING](<#user-story-testing>) 

# CODE VALIDATION

## Html 
Ensured that all HTML code adheres to the standards set by the W3C Markup Validation Service.

![html validation](/readme-images/html.png)

## Css
Validated all CSS code using the W3C CSS Validation Service to ensure compliance with CSS standards.

![css validation](/readme-images/css.png)

## Python
Validated all Python Files using CI Python Linter to ensure code quality and adherence to PEP 8 guidelines.

![python validation](/readme-images/Python.png)

# RESPONSIVENESS

Tested the responsiveness of the website across various screen sizes, including desktop, tablet, and mobile devices. Ensured that the layout and content adjust appropriately to different screen resolutions.

| Device | Comments | Pass/Fail |
| --- | --- | --- | 
| Samsung Galaxy A54 | Displays and functions correctly  | PASS |
| Samsung Galaxy S8+ | Displays and functions correctly  | PASS |
| iPhone SE | Displays and functions correctly  | PASS |
| iPad Air | Displays and functions correctly  | PASS |

- Desktop

![desktop responsiveness](/readme-images/desktop.png)

- Tablet

![tablet responsiveness](/readme-images/tablet.png)

- Mobile

![mobile responsiveness](/readme-images/mobile.png)

# BROWSER COMPATIBILITY
Tested the website on different web browsers to ensure consistent functionality and appearance across all major browsers.

| Browser | Comments | Pass/Fail |
| --- | --- | --- | 
| Google Chrome | Displays and functions correctly  | PASS |
| Mozilla Firefox | Displays and functions correctly  | PASS |
| Microsoft Edge | Displays and functions correctly  | PASS |
| Opera | Displays and functions correctly  | PASS |
| Samsung Internet | Displays and functions correctly  | PASS |

# LIGHTHOUSE
Used Lighthouse, an automated tool integrated into web browsers or available as a Chrome extension, to assess the website's performance, accessibility, best practices, and SEO. Addressed any issues or recommendations provided by Lighthouse.

![lighthouse validation](/readme-images/lighthouse.png)

# MANUAL TESTING
Conducted thorough manual testing of all features and functionalities of the website, including navigation, forms, buttons, links, and interactive elements. Ensured that all aspects of the website work as expected and are user-friendly.

## Home Page
| Section | Test |Pass/Fail |
| --- | --- |--- |
| **Navbar (not logged)** | Click on "Silly Talks" | PASS |
|  | Click on "Register" | PASS |
|  | Click on "Login" | PASS |
| **Navbar (logged)** | Click on "Profile" | PASS |
|  | Click on "Logout" | PASS |
| Read more stories button | Click on it | PASS |
| Start the silliness?register button (logged or not) | Click on it | PASS |
| Contribution form | Send a request | PASS |

## Silly Talks Page
| Section | Test |Pass/Fail |
| --- | --- |--- |
| Search Bar | Search something and be redirected to search bar page | PASS |
|  Post Cards | See title, excerpt, author, date and vote counter | PASS |
|  | Click on the card title and be redirected to post detail page  | PASS |
| Pagination | Click on any pagination button | PASS |


## Search Bar Page
| Section                   | Test                                      | Pass/Fail |
| -------------------------| ------------------------------------------| --------- |
| List of Found Posts      | Search for a keyword in the search bar    | PASS      |
| No Results Found Message | Verify message when no results are found  | PASS      |
| Header with Searched Word| Confirm "Search Results for [keyword]" header is displayed | PASS      |
| Go Back Button            | Click on the button to return to the previous page | PASS      |

## Post Detail Page
| Section                                             | Test                                                             | Pass/Fail |
| --------------------------------------------------- | ----------------------------------------------------------------- | --------- |
| **If User is Not Logged In**                        |                                                                   |           |
| See Page Content                                    | Verify that the title, excerpt, author, date, and comments are displayed | PASS      |
| Click on "See the Whole Silliness Here"             | Confirm that the collapsible button shows the full post content | PASS      |
| "Login" or "Signup" Buttons for Voting or Commenting | Click on the buttons and ensure redirection to the respective pages | PASS      |
| **If User is Logged In**                            |                                                                   |           |
| Click on Vote Buttons                               | Verify voting functionality: Not Silly, Silly, More Information | PASS      |
| Comment                                             | Leave a comment on the post                                      | PASS      |
| **If User is Logged In and is the Author of the Post** |                                                                 |           |
| Manage Posts                                        | See Edit and Delete buttons for own posts                         | PASS      |
| Edit Post                                           | Click on "Edit" post and be redirected to the Edit Post page      | PASS      |
| Confirm Post Edition                                | Verify changes are reflected after editing and saving             | PASS      |
| Delete Post                                         | Click on "Delete" post and be redirected to the Delete Post page  | PASS      |
| Confirm Post Deletion                               | Verify post is deleted after confirmation                         | PASS      |
| **If User is Logged In and is the Author of the Comment** |                                                               |           |
| Manage Comments                                     | See comments awaiting admin approval and Edit/Delete options      | PASS      |
| Edit Comment                                        | Click on "Edit" comment and ensure the comment field is prepopulated for editing | PASS      |
| Confirm Comment Edition                             | Verify changes are reflected after editing and saving             | PASS      |
| Delete Comment                                      | Click on "Delete" comment and confirm deletion via popup          | PASS      |
| Confirm Comment Deletion                            | Verify comment is deleted after confirmation                      | PASS      |


## Register and Login Pages

- **Register**

| Section        | Test                                                           | Pass/Fail |
| -------------- | -------------------------------------------------------------- | --------- |
| Details   | Users can fill out the form with their personal details       | PASS      |
| Errors    | Users are notified if any field is filled out incorrectly      | PASS      |
| Signup    | Clicking on the signup button redirects users to the profile page | PASS      |
| Sigin button   | If the user already have an account, he will be redirected to the login page | PASS      |
| Go Back Button            | Click on the button to return to the previous page | PASS      |

- **Login**

| Section                   | Test                                      | Pass/Fail |
| -------------------------| ------------------------------------------| --------- |
| Details      | User can fill out the form with his username and password | PASS      |
| Errors | Users will be notified if any space is filled incorrectly  | PASS      |
| Login | Clicking on the login button redirects users to the profile page | PASS      |
| Sigup button   | If the user doesn't have an account, he will be redirected to the signup page | PASS      |
| Go Back Button            | Click on the button to return to the previous page | PASS      |

- **Logout**

| Section                   | Test                                      | Pass/Fail |
| -------------------------| ------------------------------------------| --------- |
| Sigout      | Clicking on the login button redirects users to the home page | PASS      |
| Go Back Button            | Click on the button to return to the previous page | PASS      |

## Profile Page

- **Main profile**

| Section                   | Test                                      | Pass/Fail |
| -------------------------| ------------------------------------------| --------- |
| Profile image      | Users can see their profile picture | PASS      |
| Fallback image            | If the user doesn't have any profile picture, a fallback image will appear | PASS      |
| User details            | The user can see his details listed | PASS      |
| User Statistics button          | if the user clicks on this button, it'll appear a table with numbers of all of his interactions | PASS      |


- **New Post** 

| Section           | Test                                                | Pass/Fail |
| ----------------- | --------------------------------------------------- | --------- |
| Form          | Users can fill out the form and submit their stories | PASS      |
| Errors       | Users are notified if any field is filled out incorrectly | PASS      |
| Submit buttons | Users receive a confirmation popup after submitting the form, and are redirected to the manage posts page | PASS      |
| Characters    | The form restricts users from exceeding the maximum number of characters per field | PASS      |
| Go Back Button| Clicking the button navigates users back to the previous page | PASS      |

- **Manage Posts**

| Section           | Test                                                | Pass/Fail |
| ----------------- | --------------------------------------------------- | --------- |
| Published Posts          | Users see all the published posts they have | PASS      |
| Drafts       | Users can see a list of drafts they sent for approval | PASS      |
| Click on posts | Users can click on the title to be redirected to the respective page | PASS      |
| Go Back Button| Clicking the button navigates users back to the previous page. | PASS      |

- **Edit personal information**

| Section                   | Test                                      | Pass/Fail |
| -------------------------| ------------------------------------------| --------- |
| Form      |  Users can fill out the form and update their profile  | PASS      |
| Errors       | Users are notified if any field is filled out incorrectly | PASS      |
| Save      |  Users can click on the save button and they will be redirected to the profile page| PASS      |
| Go Back Button            | Click on the button to return to the previous page | PASS      |

- **Activity**

| Section           | Test                                                | Pass/Fail |
| ----------------- | --------------------------------------------------- | --------- |
| List of Posts   | Users can see all posts he interacted by voting or commenting | PASS      |
| Click on posts | Users can click on the title to be redirected to the respective page | PASS      |
| Go Back Button| Clicking the button navigates users back to the previous page. | PASS      |


# DEFENSIVE PROGRAMMING
Implemented defensive programming techniques to handle unexpected inputs, edge cases, and error conditions gracefully. Utilized exception handling, input validation, and error messages to enhance the robustness and reliability of the code.

![password error](/readme-images/senha.png)
![messages](/readme-images/msg.png)


# USER STORY TESTING
Tested the website against user stories and acceptance criteria defined during the development process. Verified that all user stories are successfully implemented and that users can accomplish their intended tasks seamlessly.

| User Story           | Test                                                | Pass/Fail |
| ----------------- | --------------------------------------------------- | --------- |
| **[Send anonymous stories](https://github.com/Nathisaraujo/silly-talks-blog/issues/6)**   | As a blog user I can fill the home page gorm so that I can give send my stories without being logged |       |
|   | The users can give name, email, title and the content of the story on the form at the bottom of the main page |   PASS    |
|   | The user can send stories without logging in |   PASS    |
|   | The admin will receive a post request for approval |   PASS    |
| **[Home page](https://github.com/Nathisaraujo/silly-talks-blog/issues/13)** | As a Site User, I can access the website home page and I can understand how the website is about and how it works. |       |
|   | When the website is accessed, the information about it is loaded. |   PASS    |
| **[View content of the post](https://github.com/Nathisaraujo/silly-talks-blog/issues/3)** |As a blog user I can click on the post I'm interested in on the "talks" page so that I can see the post text, the likes, and the comments |       |
|   | A detailed view of the post is seen when a blog post title is clicked on. |   PASS    |
| **[Comment/Vote on posts](https://github.com/Nathisaraujo/silly-talks-blog/issues/5)** | As a blog user I can comment and/or vote on posts when I'm logged in so that I can give my opinion about the discussed topic|       |
|   | As a blog user, I'll send my comment for approval |   PASS    |
|   | Then my contribution is posted |   PASS    |
|   | As a blog user, I can vote on posts |   PASS    |
| **[Modify or delete a comment on a post](https://github.com/Nathisaraujo/silly-talks-blog/issues/8)** | As a blog user I can modify or delete a comment on a post so that I can choose how to be involved |       |
|   | When the users are logged in, they can modify their comment |   PASS    |
|   | When the users are logged in, they can delete their comment |   PASS    |
| **[See list of posts](https://github.com/Nathisaraujo/silly-talks-blog/issues/2)** | As a site user I can click on the "start talking" button so that I can see the list of posts |       |
|   | When the users clicks on the "start talking" button on the home page, they will be redirected to the "talks" page, where they can see the list of posts |   PASS    |
| **[Account Registration](https://github.com/Nathisaraujo/silly-talks-blog/issues/4)** | As a blog user I can sign up or log in so that I can comment and/or like posts |       |
|   | The users can register an account by giving full name, email, DOB, username and password. |   PASS    |
|   | Then the user can log in |   PASS    |
|   | Then the user can comment and/or like posts |   PASS    |
| **[Manage Posts](https://github.com/Nathisaraujo/silly-talks-blog/issues/16)** | As a blog user I can login in my profile so that I can manage my posts |       |
|   | As a logged-in user, I can add a post |   PASS    |
|   | As a logged-in user, I can delete a post |   PASS    |
|   | As a logged-in user, I can edit a post |   PASS    |
| **[See user activity](https://github.com/Nathisaraujo/silly-talks-blog/issues/18)** | As a blog user I can log in so that I can see my activity |       |
|   | As a logged-in user, I can see which posts I voted for when I click on User Activity |   PASS    |
|   | As a logged-in user, I can see which posts I commented on when I click on User Activity |   PASS    |
|   | As a logged-in user, I can see how many votes, posts, and comments I have in my user's statistics |   PASS    |
| **[Edit profile information](https://github.com/Nathisaraujo/silly-talks-blog/issues/17)** | As a blog user I can log in so that I can edit, add or delete my personal information |       |
|   | As a blog user, I can edit my profile information |   PASS    |
|   | As a blog user, I can delete my profile information |   PASS    |
|   | As a blog user, I can add information to my profile |   PASS    |
| **[Add a post](https://github.com/Nathisaraujo/silly-talks-blog/issues/19)** | As a logged user I can send a post request so that my story will be published on the website |       |
|   | As a logged user I can go to my profile and click on the post page |   PASS    |
|   | As a logged user I can send my story through the "add a post" page form |   PASS    |
| **[Edit and Delete posts](https://github.com/Nathisaraujo/silly-talks-blog/issues/20)** | As a logged user I can edit and delete posts so that I have the control of my posts |       |
|   | As a logged user, I can click on my post and edit its information. |   PASS    |
|   | As a logged user, I can click on my post and delete it. |   PASS    |
| **[Create Drafts](https://github.com/Nathisaraujo/silly-talks-blog/issues/10)** | As a blog admin I can draft posts so that I can finish writing the content later |       |
|   | Given a logged in admin, they can save a draft blog post |   PASS    |
|   | Then they can finish the content at a later time |   PASS    |
| **[Review Collaboration Requests](https://github.com/Nathisaraujo/silly-talks-blog/issues/15)** | As an admin I can store collaboration requests in the database so that I can review them. | PASS      |
|   | the site admin will receive stories for post-collaboration. |   PASS    |
|   | the site admin will be able to mark requests as "read" to control the posts flow. |   PASS    |
| **[Approve comments](https://github.com/Nathisaraujo/silly-talks-blog/issues/11)** | As a blog admin I can approve or disapprove comments so that I can filter out objectionable comments |       |
|   | Given a logged in blog admin, they can approve a comment |   PASS    |
|   | Given a logged in blog admin, they can disapprove a comment |   PASS    |
| **[Admin post management](https://github.com/Nathisaraujo/silly-talks-blog/issues/9)** | As a blog admin I can create, read, update and delete posts so that I can manage my blog content |       |
|   | When the blog admins are logged in, they can: Create a blog post, update a blog post and delete a blog post|   PASS    |


# KNOWN BUGS

When I was writing the README file I tried to signup to get some errors messages for printing and documenting and I was surprised with the following error:

![known bug](/readme-images/error.png)

I didn't understand what it meant as I tested everything and it was working fine. I started testing different usernames to test and found out that a username only with numbers were working. I decided to ask for tutor assistance but when I tried to show him, it was working fine again. So he advised me to report this on the readme file.

![tutor assistance](/readme-images/tutor.png)
