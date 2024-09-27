# GAMER'S VAULT

[Link to a live site](https://gamers-vault-72a0e73da873.herokuapp.com/)

![Responsive view of mixology master website](/docs/images/gamers-vault-responsive.png)

# Introduction to Gamer's Vault: A Full-Stack E-Commerce Platform for Gaming Equipment

Welcome to my fourth project, part of the Code Institute Full Stack Development Course. The aim of this project is to develop a fully functional, full-stack e-commerce web application using Django.

**Gamer's Vault** offers a seamless shopping experience for gaming enthusiasts, featuring user registration for personalized account management and wishlist creation. Registered users can write product reviews to assist others in making informed decisions. The site ensures secure purchasing and provides easy order inquiries for enhanced customer support. Additionally, the guest checkout option allows non-registered users to make purchases without needing an account, providing flexibility and convenience.

## UXD – User Experience Design

A user experience designer, Jesse James Garrett, introduced five UX design elements in his book The Elements of User Experience.
In the book, he explains the steps of user experience projects and what UX designers should consider at each stage.
This is where most of my planning process steps came from.

The 5 planes of UX are as below:

- The Strategy Plane
- The Scope Plane
- The Structure Plane
- The Skeleton Plane
- The Surface Plane

## The Strategy Plane

### Creator Goals

As the creator of this e-commerce platform, my primary goals are:

1. **Provide a Seamless Shopping Experience:** I aim to create a user-friendly and visually appealing platform that allows customers to easily browse, search, and purchase gaming peripherals such as keyboards, mice, and headsets.

2. **Cater to Gaming Enthusiasts:** I want to build a platform that caters specifically to gaming enthusiasts by offering high-quality products and detailed descriptions to help users make informed purchasing decisions.

3. **Offer Customization and Personalization:** Through features like Wishlist and Product Reviews, I plan to offer users a more personalized shopping experience, allowing them to save their favorite items and share their feedback on purchases.

4. **Ensure Secure and Efficient Transactions:** Security and efficiency are paramount, so I aim to implement a reliable and secure payment system that protects user data and ensures smooth transactions.

5. **Create a Scalable and Maintainable Platform:** I strive to build a platform that is not only scalable to accommodate growth but also maintainable, with clean code and a solid structure for future upgrades and features.

6. **Engage and Retain Users:** By providing features like product reviews and a Wishlist, I aim to engage users and encourage repeat visits, fostering a community of gaming enthusiasts around the platform.

### User Stories

#### Guest User

1. **As a Guest User,** I want to easily browse gaming keyboards, mice, and headsets so that I can find products that interest me.

2. **As a Guest User,** I want to search for specific gaming peripherals by name, brand, or type so that I can quickly find the items I’m looking for.

3. **As a Guest User,** I want to view detailed product descriptions, including specifications and high-quality images, so that I can make an informed purchasing decision.

4. **As a Guest User,** I want to add products to my cart and check out without needing to create an account, so that I can make a quick purchase.

5. **As a Guest User,** I want to see customer reviews and ratings for products so that I can understand the experiences of others before buying.

6. **As a Guest User,** I want to be able to sign up for an account.

#### Registered User

1. **As a Registered User,** I want to log in securely so that I can access my account and previous orders.

2. **As a Registered User,** I want to add products to my Wishlist so that I can save items I'm interested in for future reference.

3. **As a Registered User,** I want to view and edit my profile information, including my shipping address and payment methods, so that I can easily manage my account.

4. **As a Registered User,** I want to leave reviews and ratings for products I've purchased so that I can share my experience with other users.

5. **As a Registered User,** I want to view my order history so that I can easily reorder items or track my past purchases.

6. **As a Registered User,** I want to be able to remove items from my Wishlist if I no longer desire them, so that I can keep my Wishlist up to date.

## The Scope Plane 

The planning process allowed me to prioritize the implementation of features based on their importance to my user stories, enabling me to identify which ones could be completed within the given deadline and which ones would need to be postponed for later implementation.

### Features implemented upon webpage release:

1. **User Registration and Login**:  
   Users can create an account to manage their shopping experience and access additional features.

2. **Wishlist Creation**:  
   Logged-in users can curate a personalized wishlist of their favorite gaming products, making it easy to keep track of what they want.

3. **Product Reviews**:  
   Registered users can share their opinions on products by writing reviews, helping fellow gamers make informed purchasing decisions.

4. **Secure Purchasing**:  
   Users can seamlessly purchase gaming equipment directly from the platform, all while enjoying a secure and reliable shopping experience.

5. **Order Inquiries**:  
   Users can easily contact the shop regarding their orders, enhancing customer support and satisfaction.

6. **Guest Checkout**:  
   Guests can browse and purchase products without creating an account, ensuring a smooth and hassle-free shopping experience.

7. **Shopping Basket**:  
   Users can easily add products to their shopping basket for checkout, streamlining the purchasing process.

8. **Search Bar**:  
   Users can quickly find products using the search functionality, making navigation fast and easy.

9. **User Dashboard**:  
   Registered users can access a dashboard to view their order history and manage their account.

10. **Product Filter**:  
    Users can filter products based on criteria like price, category, and brand to find what they need faster.

11. **Product Categories**:  
    Products are organized into categories, allowing users to browse specific types of products efficiently.


### Features planned to implement later:

- **Two-step authentication**
- **Live chat**
- **Q&A Forum**

*Above decisions have been made based on the below table.*

| Feature         | Feasibility | Importance |
| --------------- |:-----------:|:----------:|
| Registration    |      5      |     5      |
| Two-step auth.  |      4      |     3      |
| Wishlist        |      5      |     5      |
| Product reviews |      5      |     5      |
| Contact         |      5      |     4      |
| Live chat       |      3      |     2      |
| Secure purch.   |      5      |     5      |
| Basket          |      5      |     5      |
| Search bar      |      5      |     5      |
| User dashboard  |      5      |     4      |
| Product filter  |      5      |     4      |
| Product cat.    |      5      |     5      |


## The Structure Plane

### Colors:

`#000`:

- Body
- Footer links
- Navbar icons
- Navbar font color
- Checkout toast button

![#000 Hex Color](/docs/images/000.PNG)

`#FAFAFA`:

- All font colors around the page

![#FAFAFA Hex Color](/docs/images/fafafa.PNG)

`#44D62C`:

- Navbar background
- Category tags on product cards and product detail pages
- Rating on product cards and product detail pages
- Buttons
- Horizontal rules (hr tags)
- Footer background
- Free delivery banner - toast

![#44D62C Hex Color](/docs/images/44d62c.PNG)

`#333333`:

- Delivery banner background
- 'Up' button (to take user back to the top of the page)

![#333333 Hex Color](/docs/images/333333.PNG)

`rgba(50, 50, 50, 0.8)` :

- Toast background

`rgba(23, 162, 184, .85)` :

- Loading overlay 

`#F39C12` :

- Quotation marks

![#F39C12 Hex Color](/docs/images/f39c12.PNG)

`#DCDCDC` :

- Blockquote footer font

![#DCDCDC Hex Color](/docs/images/dcdcdc.PNG)

**Bootstrap Colors** : 

`#DEE2E6` :

![#DEE2E6 Hex Color](/docs/images/dee2e6.PNG)

- borders

`#FFFFFF` :

- icons
- font

![#FFFFFF Hex Color](/docs/images/ffffff.PNG)

`#28A745` :

- header font in 'success' toast

![#28A745 Hex Color](/docs/images/28a745.PNG)

`#17A2B8` :

- header font in 'info' toast

![#17A2B8 Hex Color](/docs/images/17a2b8.PNG)

`#DC3545` :

- header font in 'error' toast
- font
- wishlist icon

![#DC3545 Hex Color](/docs/images/dc3545.PNG)

`#FFC107` :

- header font in 'warning' toast

![#FFC107 Hex Color](/docs/images/ffc107.PNG)

### Fonts:

**Roboto** :

The decision to use the Roboto font from Google as the primary typeface was driven by its popularity and user-friendly design. Roboto offers excellent readability across different screen sizes, ensuring an optimal user experience for everyone interacting with the content.

**Oswald** :

The Oswald font was chosen for the logo due to its bold and distinctive appearance, which effectively enhances brand recognition. Its modern, condensed design conveys a sense of professionalism while maintaining clarity and readability across various sizes and platforms. Oswald’s strong, clean lines help the logo stand out, making it both memorable and visually striking. This choice ensures that the brand identity is consistent and impactful, whether displayed on large banners or smaller digital screens.

**Helvetica** :

The decision to use the Helvetica font for Stripe elements was made to ensure a clean, modern, and professional appearance. As a widely used and highly legible typeface, Helvetica aligns well with Stripe’s emphasis on trust, security, and user experience. Its neutrality complements the minimalist design of payment forms, ensuring the focus remains on the transaction process.


**Images** :

Images for this project has been downloaded from : 

- [Amazon](https://www.amazon.co.uk/ref=nav_logo)
- [GSMA](https://www.gsma.com/)

**More information in credits section.**

### Database :

I decided to use **retalional database** in my project.

A **relational database**  is used for several reasons that align with the structure and needs of your application:

1. **Data Integrity**: Relational databases enforce constraints such as `ForeignKey`, `Unique`, and `Not Null`, which ensure data consistency. For example, the `Order` model's relationship with the `UserProfile` ensures that every order is tied to a valid user.

2. **Relationships Between Models**: The models have relational structures. The `ForeignKey` fields, such as those between `Order` and `OrderLineItem` or `Product` and `Subcategory`, allow efficient mapping of relationships, which is a core feature of relational databases.

3. **ACID Compliance**: Relational databases typically ensure atomicity, consistency, isolation, and durability, meaning transactions (like order creation and payment processing) are reliable and safe from data corruption.

4. **Normalization**: Data is organized to minimize redundancy. For instance, user information is stored in a separate `UserProfile` table instead of repeating it for every order.

5. **Structured Querying**: SQL (Structured Query Language) enables complex queries, including `JOIN`s and aggregations, which are necessary to fetch related data across models (e.g., retrieving all `OrderLineItem`s for an `Order`).

---

#### *DATABASE SCHEMA* :

The schema for each model, detailing the structure and relationships, is presented below.

#### 1. **User Model (Django Default)**

The default Django `User` model handles authentication and includes fields such as `username`, `password`, and `email`. I extended its functionality using the `UserProfile` model.

---

#### 2. **UserProfile Model**

**Table Name**: `user_profile`

**Description**: This table stores additional user information, primarily related to delivery details and order history, to extend the functionality of the default Django `User` model.

| Field                  | Data Type            | Nullable | Constraints       | Foreign Key          |
|------------------------|----------------------|----------|-------------------|----------------------|
| id                     | Integer (Auto)       | No       | Primary Key       |                      |
| user_id                | Integer              | No       | Unique            | FK to `User`          |
| default_full_name       | Varchar(100)         | Yes      |                   |                      |
| default_phone_number    | Varchar(20)          | Yes      |                   |                      |
| default_street_address1 | Varchar(80)          | Yes      |                   |                      |
| default_street_address2 | Varchar(80)          | Yes      |                   |                      |
| default_town_or_city    | Varchar(40)          | Yes      |                   |                      |
| default_county          | Varchar(80)          | Yes      |                   |                      |
| default_postcode        | Varchar(20)          | Yes      |                   |                      |
| default_country         | Country (ISO Code)   | Yes      |                   |                      |

---

#### 3. **Order Model**

**Table Name**: `order`

**Description**: This table stores individual orders placed by users, including user details, delivery costs, and the total amount for each order.

| Field                  | Data Type            | Nullable | Constraints       | Foreign Key              |
|------------------------|----------------------|----------|-------------------|--------------------------|
| id                     | Integer (Auto)       | No       | Primary Key       |                          |
| order_number           | Varchar(32)          | No       | Unique, Editable  |                          |
| user_profile_id        | Integer              | Yes      |                   | FK to `UserProfile`      |
| full_name              | Varchar(50)          | No       |                   |                          |
| email                  | Varchar(254)         | No       |                   |                          |
| phone_number           | Varchar(20)          | No       |                   |                          |
| country                | Country (ISO Code)   | No       |                   |                          |
| postcode               | Varchar(20)          | No       |                   |                          |
| town_or_city           | Varchar(40)          | No       |                   |                          |
| street_address1        | Varchar(80)          | No       |                   |                          |
| street_address2        | Varchar(80)          | Yes      |                   |                          |
| county                 | Varchar(80)          | Yes      |                   |                          |
| date                   | DateTime             | No       | Auto Add          |                          |
| delivery_cost          | Decimal (6,2)        | No       | Default = 0       |                          |
| order_total            | Decimal (10,2)       | No       | Default = 0       |                          |
| grand_total            | Decimal (10,2)       | No       | Default = 0       |                          |
| original_bag           | Text                 | Yes      |                   |                          |
| stripe_pid             | Varchar(254)         | Yes      |                   |                          |

---

#### 4. **OrderLineItem Model**

**Table Name**: `order_line_item`

**Description**: This table stores individual items associated with an order, linking the order to specific products and tracking quantity and price per item.

| Field                  | Data Type            | Nullable | Constraints       | Foreign Key              |
|------------------------|----------------------|----------|-------------------|--------------------------|
| id                     | Integer (Auto)       | No       | Primary Key       |                          |
| order_id               | Integer              | No       |                   | FK to `Order`            |
| product_id             | Integer              | No       |                   | FK to `Product`          |
| quantity               | Integer              | No       | Default = 0       |                          |
| lineitem_total         | Decimal (6,2)        | No       | Editable=False    |                          |

---

#### 5. **Product Model**

**Table Name**: `product`

**Description**: This table stores product information including pricing, descriptions, and relationships with categories and subcategories.

| Field                  | Data Type            | Nullable | Constraints       | Foreign Key              |
|------------------------|----------------------|----------|-------------------|--------------------------|
| id                     | Integer (Auto)       | No       | Primary Key       |                          |
| category_id            | Integer              | Yes      |                   | FK to `Category`         |
| subcategory_id         | Integer              | Yes      |                   | FK to `Subcategory`      |
| sku                    | Varchar(254)         | Yes      |                   |                          |
| name                   | Varchar(254)         | No       |                   |                          |
| description            | Text                 | No       |                   |                          |
| price                  | Decimal (6,2)        | No       |                   |                          |
| rating                 | Decimal (6,2)        | Yes      |                   |                          |
| image_url              | Varchar(1024)        | Yes      |                   |                          |
| image                  | Image                | Yes      |                   |                          |

---

#### 6. **Category Model**

**Table Name**: `category`

**Description**: This table stores information about product categories, which are used to organize products.

| Field                  | Data Type            | Nullable | Constraints       | Foreign Key              |
|------------------------|----------------------|----------|-------------------|--------------------------|
| id                     | Integer (Auto)       | No       | Primary Key       |                          |
| name                   | Varchar(254)         | No       |                   |                          |

---

#### 7. **Subcategory Model**

**Table Name**: `subcategory`

**Description**: This table stores information about product subcategories, each of which is linked to a parent category.

| Field                  | Data Type            | Nullable | Constraints       | Foreign Key              |
|------------------------|----------------------|----------|-------------------|--------------------------|
| id                     | Integer (Auto)       | No       | Primary Key       |                          |
| category_id            | Integer              | No       |                   | FK to `Category`         |
| name                   | Varchar(254)         | No       |                   |                          |

---

#### 8. **ProductReview Model**

**Table Name**: `product_review`

**Description**: This table stores user reviews for products, including ratings, review content, and user information.

| Field                  | Data Type            | Nullable | Constraints       | Foreign Key              |
|------------------------|----------------------|----------|-------------------|--------------------------|
| id                     | Integer (Auto)       | No       | Primary Key       |                          |
| product_id             | Integer              | Yes      |                   | FK to `Product`          |
| user_id                | Integer              | Yes      |                   | FK to `User`             |
| title                  | Varchar(254)         | No       |                   |                          |
| rating                 | Integer              | No       |                   |                          |
| content                | Text                 | No       |                   |                          |
| added_on               | DateTime             | No       | Auto Add          |                          |

---

#### 9. **Wishlist Model**

**Table Name**: `wishlist`

**Description**: This table stores products that have been added to a user's wishlist.

| Field                  | Data Type            | Nullable | Constraints       | Foreign Key              |
|------------------------|----------------------|----------|-------------------|--------------------------|
| id                     | Integer (Auto)       | No       | Primary Key       |                          |
| user_id                | Integer              | No       |                   | FK to `User`             |
| product_id             | Integer              | No       |                   | FK to `Product`          |
| added_on               | DateTime             | No       | Auto Add          |                          |

---

#### 10. **ContactQuery Model**

**Table Name**: `contact_query`

**Description**: This table stores queries or contact messages submitted by users or guests. Queries can be related to general issues or specific orders.

| Field                  | Data Type            | Nullable | Constraints       | Foreign Key              |
|------------------------|----------------------|----------|-------------------|--------------------------|
| id                     | Integer (Auto)       | No       | Primary Key       |                          |
| user_id                | Integer              | Yes      |                   | FK to `User`             |
| name                   | Varchar(100)         | No       |                   |                          |
| email                  | Varchar(254)         | No       |                   |                          |
| query_type             | Varchar(20)          | No       | Default = 'General'|                         |
| order_id               | Integer              | Yes      |                   | FK to `Order`            |
| message                | Text                 | No       |                   |                          |

---

#### Relationship :

- **UserProfile** links to **User** (One-to-One).
- **Order** links to **UserProfile** (Many-to-One).
- **OrderLineItem** links to **Order** and **Product** (Many-to-One for each).
- **Product** links to **Category** and **Subcategory** (Many-to-One).
- **ProductReview** links to **Product** and **User** (Many-to-One for each).
- **Wishlist** links to **User** and **Product** (Many-to-One for each).
- **ContactQuery** links to **User** and **Order** (Many-to-One for each).