# Boutique Ado Milestone Project

This e-commerce website is a final project that concludes 'Full Stack Frameworks With Django' module and 'Full Stack Software Development' program provided by Canadian Business College.

## UX

This project is an online store that inherits most of the best practices used by hundreds of online stores all-around the Internet.

### User Stories

- As a user, I want to have the ability to search through all items in a store and add them to my shopping bag.
- As a user, I want to be able to modify the quantity of items in my bag as well as remove them from the bag.
- As a user, I want to register and save my info, so my future shopping process is faster.
- As a registered user, I want to add items to my Wishlist, so I can buy them later.
- As a user, I want to be able to use an online store on devices with different screen resolution.

## Features

- All products are conveniently sorted by categories, also user can sort them by price and by rating.
- Users can register an account and save their info, as well as add items to a wishlist.
- Searchbar makes it easier to find needed product.
- Guest users can checkout without registration.
- A convenient message system informs users about most of their actions (add to/remove from bag/wishlist, sign out, etc.).
- Responsive design makes it easy to use the store on both mobile and desktop devices.
- Stripe payment system provides safe checkout for credit card users.

## Features left to implement

- Set up a loyalty system that can be used to conduct purchases
- Ability to use coupon codes to reduce purchase price
- Automatic tax calculation based on location
- Implement social media account creation on All Auth
- Integrate a live chat bot for inquiries before purchase
- Set up a ticketing system for returns and post purchase issues
- Integrate voice command functionality

## Technologies Used
- HTML
- CSS
- JavaScript
- Jquery
- Python
- Django
- Bootstrap
- Heroku
- Amazon Web Services (AWS) 
- GitHub
- GitPod

## Testing

Most of the testing was done manually during development process with the help of Google Chrome Inspect Element Tool.
One of the interesting issues I discovered during the testing process was related to Django messages framework.
I assigned a very high z-index for messages, so they appear on top of all other elements. But after I closed a message I was unable to click on 'my profile' in dropdown menu. Actually, I was unable to click on anything that was covered by the message, because when I closed the message, it disappeared visually, but technically it just became transparent and it was still covering other elements. It took me a long time to figure out what???s going on and how to solve this issue, but finally I've decided to add an 'onClick' event to the button, so it makes the webpage reload.
Special thanks to [Very Academy](https://www.youtube.com/channel/UC1mxuk7tuQT2D0qTMgKji3w) YouTube channel that helped me to implement wishlist functionality.
There are still few minor issues I'll have to solve in the future.<br/>
To make a wishlist functionality I've added one more field to the Product model form.<br/>
![model](/pics/model.jpg)
<br/>But when I went to 'Product Management' page I've noticed that a new field appeared.<br/>
![product](/pics/product.jpg)
<br/> It's happening because the form is automatically generated via for loop in html.<br/>
![html](/pics/html.jpg)
<br/> Hopefully I will find a solution in the nearest future.
<br/> Also I will need to write custom CSS for country field in checkout form, as for now it cuts off country name filled in.<br/>
![country](/pics/country.jpg)

## Deployment

The online store was deployed on Heroku and can be found via following link: https://glib-django.herokuapp.com

