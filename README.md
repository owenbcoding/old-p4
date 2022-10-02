# Devstories
Devstories basically a blog site for developers where developers can share their projects and talk about their skills and comment and like each others posts
For some reason the Responsive image didnt work properly 

link: https://app-devstories.herokuapp.com/

# Project Four - Devstories

### Intention
My intension for this project was to make a blog site for any developer who whises to blog about their journey or projects they are working on the and discuss things about them in the comment section 

### Features I aimed to achieve with this project:
 -  I aimed to achive a nice easy to navigate site with minimal effort 
 -  I aimed the site to be driven more towards developers who wish to blog 
 -  I aimed to bring in more people and people who are new to tech and want to learn more.

# How To Navigate The Website
 
 - You start on the home page looking at the blog posts. Then at the top left you have name Home Link Register link and login link.
 - Once you are logged in you can view the blogs and comment and like the posts and you can click the new post link that should bring you to a creat post page.
 - You should be able to add an image to your post and post it to the home page on the site.
 - Users will also have ability to delete or edit their posts

# Planning 
Devstories - Balsamiq Wireframe

- Desktop View 

![BalsamiqWireframes_I87Zo05LXd](https://user-images.githubusercontent.com/43074374/187065389-3ba38110-1f69-4041-8ec6-23006f2d83b0.png)

- Mobile View

![BalsamiqWireframes_04pnexitYF](https://user-images.githubusercontent.com/43074374/187065475-6c22e79e-b841-4a0b-b634-b6352800cb6b.png)


## Github - User Project Kanban Board

### Start of Project
![chrome_beY8TXdeB9](https://user-images.githubusercontent.com/43074374/186406278-f5c1bbcf-76e2-4b87-b6e1-fe1304930136.png)

### End of Project
![chrome_cXbi0HPwZd](https://user-images.githubusercontent.com/43074374/186414153-fd56c2e6-3afc-4883-a6f1-40476e13d0fa.png)

# UX

User Stories: 
As a guest I would like to be able to:
 
 - Register an account using username, email, and password.
 - View a List of the current blogs on the home page.
 - Will be able to read the detailed version of the blog.
 - Will be to view comments and likes on a post.

As a user I would like to be able to:

 - Login into my account.
 - blog about their own devevelopment projects.
 - edit delete and create my own content on a blog.
 - Comment and like a post that you like.

As a admin I need to be able to: 

 - Manage the list of users who sign up to the site.
 - Approve users comments on the website.
 - Post a blog about the site or projects.

# Website Design

## Design

## Logic

Devstories - Database Schema

(Database Schema Image)
Before I started to code this project I created a Diagram Entity Relationship - Database Schema using dbdiagram.
I created this to easier understand the database models that I was going to create for this project.

![image](https://user-images.githubusercontent.com/43074374/187066336-94946348-b08e-4b25-b9db-3a320d31719b.png)

# Existing Features
# Navbar
### Navbar links: 
 - The Nav bar consists of 3 main links and a caption on the far right

![chrome_AgcrCwMR6o](https://user-images.githubusercontent.com/43074374/186414631-7e98ef47-4a63-4fc2-bbb7-e89b0c3f5e34.png)


## Start Screen

 - The start screen consists of the main home page with the blogs and navigation if the user is not authenticated

![chrome_V5XHjyvmhb](https://user-images.githubusercontent.com/43074374/186414883-a1a9f4bb-e5b8-4638-a4ea-4bc2e034dc8d.png)

### Not authenticated:
 - what it loooks like if the user is not authenticated

![chrome_ZcfXgV6qxZ](https://user-images.githubusercontent.com/43074374/186425288-8bd55366-63c7-479e-9a0e-ae2ac7f585bf.png)

### Authenticated:
 - what it looks like if the user is authenticated

![chrome_HsAF9staQK](https://user-images.githubusercontent.com/43074374/187064149-8ba81b23-d252-40c6-8660-5ee8079708e4.png)

### Footer:
![chrome_pyyN8XexhH](https://user-images.githubusercontent.com/43074374/186425816-be8616ef-4f8d-467c-a967-3ae0ffc9b799.png)

## User:
### Register account:
- This is where a user registers their account

![chrome_uQllWik7Nl](https://user-images.githubusercontent.com/43074374/186416028-22e858f5-696a-4dde-b0d6-cd6bc37a7463.png)


### Login to account:
- This is where a user logs into their account

![chrome_71qSONu2yd](https://user-images.githubusercontent.com/43074374/187064285-5cd41954-4937-4859-8c9b-c3d8459cc91d.png)

### Logout:
![chrome_HsAF9staQK](https://user-images.githubusercontent.com/43074374/187064149-8ba81b23-d252-40c6-8660-5ee8079708e4.png)

## Blog Details, authenticated and creator of:
![chrome_IK7ymkU4U9](https://user-images.githubusercontent.com/43074374/186421214-30fd9ed5-2f9e-40f0-9c05-87445de404dc.png)

## Post Blog 

- Creat a blog post 

![chrome_PqWuIjNyMD](https://user-images.githubusercontent.com/43074374/187066816-1f719079-08c0-4b36-9b71-04a5cb8de07b.png)

# Future Features

- For Future Features I tend to be adding memebers and user profile images so people can add their profile picture.
- I also tend to make a friends list so developers can add eachother on site and message eachother about their projects.

# Technologies Used
- HTML / Django Templates: I used the html templates for django to generate and render the pages.

- Django Framwork: Full stack framework.

- Python backgend: I used python to manage the backend for the website.

- Bootstrap: I used Boostrap for the styling and responsiveness.

- Postgres SQL: I used PosgresSql for the database.

- Cloudinary: I used cloudinary for storing the images on the site.

- Github: I used github to backup my code.

- Heroku: I used herkou to deploy and launch my website.

# Testing

- For testing I created a user and used that to login and everything seem to work perfectly
- I also made some test comments and approved them from the admin page that django has
- For Basic CRUD opperations I was able to use the admin data base for approving comments creating posts and deleteing posts as shown below

- A user signing in

![image](https://user-images.githubusercontent.com/43074374/187066893-bfb7adc4-8215-4e47-9d10-879ee5a29160.png)

- Successfull login

![image](https://user-images.githubusercontent.com/43074374/187066941-37346a2f-d3b4-4122-a044-9fd3d114648b.png)

- Registered Users

![image](https://user-images.githubusercontent.com/43074374/187066986-958afc89-a895-4cbc-a822-3926446b4901.png)

- Approved Comments

![image](https://user-images.githubusercontent.com/43074374/187067054-4e469878-25e1-46b7-9991-be09b36bdac4.png)

- Posts added by admin

![image](https://user-images.githubusercontent.com/43074374/187067088-9f972ae8-157c-4859-8034-f77125933e4c.png)


# Bugs

- Bug 1

# Unfixed Bugs
- Bug 1
The first bug I found was the likes not be able to show when I liked on a post but it seemed to work for the comments as you can see the zero next to the comments icon
![chrome_OODnVDh7pt](https://user-images.githubusercontent.com/43074374/186948199-266c2740-731d-47f8-afd1-b080760aba79.png)


# Credit 
### Media
As For the media: 
The first image is from my own website.

For the second image I want to thank my team on Hostsapling for letting me take a picture of our site Im working on with them

For the Third Image I want to thank the graphic designer I am working with on a web 3 project with and his site I am working on


### Inspiration for this project
Code Institute - I took inspiration to this project from the Code Institute videos of I Think Therefore I Blog

### Help from Stack Overflow
I got alot of help from stack overflow using it to help answer questions or problems I had during the projects development

 - Django all auth docs https://django-allauth.readthedocs.io/en/latest/installation.html : I also used all auth docs to help me with authentication during the project
 - Djang docs https://www.djangoproject.com/ 

 - Code Institute for the project starter files : https://github.com/Code-Institute-Solutions/django-blog-starter-files
# Deployment

## GitHub:

## GitHub & Gitpod
For this project I used Code Institutes Python template that can be found here https://github.com/Code-Institute-Org/python-essentials-template.

Steps to create a new repository in Github:

Sign in or sign up to GitHub https://github.com/home.
When you have done that, you will see "new" up in the left corner. Like this: Screenshot new repository button github
Select in the dropdown menu under Repository template if you for example would like to use the template provided by Code Institute that I did for this project. If you don't see it in the dropdown menu click this link to get to the one provided by Code Institute and click Use this template to the left of the green Gitpod button.
When you have done that, give the repository a name. Leave it public if you want anyone on the internet to see your repository (I always do).
Click create repository.
Remember to use the commit commands that I explained above so your hard work doesn't get lost if anything happens to Gitpod.

## Heroku
For Hosting on Heroku Follow these steps  

Go to your Apps in your heroku profile

![chrome_hmeiK7pB4i](https://user-images.githubusercontent.com/43074374/187060903-ac072171-ea8f-4530-848f-cb9554f5fbb5.png)

Then go to this page and select the github button 
  
![chrome_NQv83MFCsa](https://user-images.githubusercontent.com/43074374/187060942-fa6d611e-7a60-48e7-a31b-d883557c955b.png)

Then on the same page make sure your on the proper branch of your repo and click the deploy button 

![chrome_jlcavSzU8z](https://user-images.githubusercontent.com/43074374/187061047-406a900c-f2b8-4b5b-864f-8b3de3721e64.png)




