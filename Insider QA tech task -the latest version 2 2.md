### 1. Describe the steps for comprehensively testing of a pencil with an eraser on one end. Cases for all types of testing (such as functional, usability, performance, load, stress, security, etc.) are expected here.

#### Preconditions: let's assume it's a simple pencil with an eraser and it's made of wood, since no additional information is specified.

#### Functional testing:
 - Make sure that the pencil can draw.
 - Make sure the pencil can draw through a carbon paper.
 - Make sure that the pencil writes smoothly, the lines are even and do not leave smudges.
 - The lead does not break or crumble directly during drawing.
 - Make sure that the pencil can draw not only on paper but also on but on alternative materials (cardboard, wood, walls, or floor (relevant for construction work).
 - Check whether the eraser erases notes/sketches and does not smear or make it “dirty”.
 - During and after sharpening, the lead did not break its integrity.
 - During and after sharpening, the pencil does not break or crumble.
 - The sharpened pencil is successfully functioning (you can write, sketch, draw).

#### Usability Testing
- Is it comportable to hold a pencil? 
- Does it not slip, nor does it fall out when using it?
- Does it squeak while writing or does it write quietly?
- How useful is the eraser on the end of the pencil?
- The body shape is round, triangular, or hexagonal.
- Pencil sharpens easily with a pencil sharpener.

#### Security Testing
 - Can I get hurt with a pencil (scratched, cut when sharpening)?
 - Is it safe to give a pencil to a child? There are “safe” types of pencils (for example, special “children” pencils, often with a triangular body) that can be given to children without fear (of course, depending on age, general development, and characteristics of the child).
 - Is the pencil safe for people with disabilities (eg visually impaired)? E.g. a pencil with a round body can pose a serious problem for a visually impaired person when rolled under a table. For the visually impaired the use of pencils with a hexagonal or triangular barrel is more appropriate.

#### Load Testing
- Let’s check the behavior of the pencil when you press the pencil lead on the paper. Make sure the pencil won’t break.
- Pull the pencil lead. It must not come out of the body.
- Tap the pencil on the table several times. The lead should not crumble or break, fall out of the body, or crack.
- After use, the eraser does not leave crumbs, does not fall out; the ferrule does not bend or leave marks or scratches on paper and hands. 

#### Stress Testing
- Drop the pencil on the floor a couple of times and check whether the lead breaks or crumbles. The pencil body must not be damaged.
- Try to bend the pencil: will it break or not?
- Chew on a pencil. It’s advisable that the end of the pencil stays not “eaten”. Many manufacturers pay special attention to this point.
- Place the pencil in water, then dry it. It should be possible to use it normally for drawing / writing as before.
- Place the pencil in the freezer for a while to freeze it. It should be possible to use it normally for drawing / writing as before.
- Use the eraser to rigorously to erase notes / sketches. The eraser head should not wear off quickly.

#### Performance Testing
- Check that the pencil lead does not wear off, nor does it thin quickly while drawing / writing.
- Check that the eraser head does not wear off quickly while erasing notes / sketches written by the pencil.

### 2. On the Main page of https://www.hepsiburada.com/ you can see the different Recommendations section with different products. These sections are also shown on Product Detail and Cart pages. What are these product suggestions, what is the rule for listing these products and showing them to the user? Full analysis is expected here.

Product suggestions are served with the help of the recommendation algorithms. In this case, the product recommendations are made based on site bestsellers and general site data on products and visitors listing the products which are popular on the website. Seasonal products are also analyzed and taken into account, e.g. the "bikini" section. These products are fetched using the algorithm for anaylyzing the most purchased products during a season. E.g. the most sold items in summer are beach essentials, including beach towels, swimsuits, beach toys, sunglasses, flip-flops, and waterproof bags. The most viewed products are also presented and they can be viewed under the "Şu an çok bakılıyor" section. There are also bestsellers of the week, which are served in the "Haftanın çok satanları" section. In addition to that, the premium offers are shown in the "Premium fırsatları" section. 

The description of the other product recommentations sections:

 - "Popüler ürünlerden seçtik": shows products popular on the website based on general site data on products and visitors.
 - "En Avantajlı Ürünler": shows products which have the best price with regard to the quality / price ratio including promotions.
 - "Süper Fiyat, Süper Teklif": shows products with the lowest prices including discounts and promotions.
 - "Popüler ürünlerden seçtik": this seems like a bug as this section gets duplicated twice: https://app.screencast.com/KhnJDJJwXUhIR
 - "Herkes bu ürünlerin peşinde": shows products which are the most needed based on general site data on products and visitors.
 - product categories ("Bikini", "Runner", "Giyim", "Çanta") list products, which are the most purchased on the website based on general site data on products and visitors.
 - "Popüler kategorilere özel indirimler": shows special discounts on popular product categories.
 - "Günlük ihtiyaçlarda çok satanlar": shows the best sellers of daily essensitals.

### 3. Automate the scenario below:
1. Visit https://useinsider.com/ and check Insider home page is opened or not.
2. Select “Company” menu in navigation bar, select “Careers” and check Career page, its Locations, Teams and Life at Insider blocks are opened or not.
3. Go to https://useinsider.com/careers/quality-assurance/, click “See all QA jobs”, filter jobs by Location - Istanbul, Turkey and department - Quality Assurance, check presence of jobs list.
4. Check that all jobs’ Position contains “Quality Assurance”, Department contains “Quality Assurance”, Location contains “Istanbul, Turkey”.
5. Click “View Role” button and check that this action redirects us to Lever Application form page.

- Test case should be written using any programming language and framework (Python or Java + Selenium would be preferable).
- No BDD (Cucumber, Quantum, Codeception, etc.) frameworks are allowed.
- Screenshot should be taken If test fails one of steps.
- Test case should be able to run in Chrome and Firefox browsers and ensure that the browser is parametrically changeable.
- Test code should fully meet POM requirements.

Please see the "README.md" file for information.

### 4. Test Automation - API
Using “pet” endpoints from https://petstore.swagger.io/ write CRUD operations API tests with positive and negative scenarios.

#### Positive scenarios

##### 200 OK: 

curl -X 'POST' \
  'https://petstore.swagger.io/v2/pet' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 23,
  "category": {
    "id": 4,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 7,
      "name": "monkey"
    }
  ],
  "status": "available"
}'


curl -X 'PUT' \
  'https://petstore.swagger.io/v2/pet' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 23,
  "category": {
    "id": 5,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 8,
      "name": "dog"
    }
  ],
  "status": "available"
}'


curl -X 'GET' \
  'https://petstore.swagger.io/v2/pet/23' \
  -H 'accept: application/json'


curl -X 'DELETE' \
  'https://petstore.swagger.io/v2/pet/23' \
  -H 'accept: application/json'

#### Negative scenarios

##### 404 Not found:
curl -X 'GET' \
  'https://petstore.swagger.io/v2/pet/23' \
  -H 'accept: application/json'

curl -X 'GET' \
  'https://petstore.swagger.io/v2/user/user1%22' \
  -H 'accept: application/json'

curl -X 'POST' \
  'https://petstore.swagger.io/v2/pet/323' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'name=toney&status=duck'


curl -X 'DELETE' \
  'https://petstore.swagger.io/v2/pet/23' \
  -H 'accept: application/json'

  curl -X 'DELETE' \
  'https://petstore.swagger.io/v2/store/order/3424234234' \
  -H 'accept: application/json'

  ##### 500 Internal Server Error:

curl -X 'POST' \
  'https://petstore.swagger.io/v2/user/createWithList' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ "id": 23,
  "category": {
    "id": 5,
    "name": "string"
  } 
    }'

curl -X 'POST' \
  'https://petstore.swagger.io/v2/user/createWithArray' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
  {
    "username": "string",
  }
]'

  ##### 400 Bad Request:

  curl -X 'POST' \
  'https://petstore.swagger.io/v2/user/createWithList' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d ''\''{ "id": 23,
  "category": {
    "id": 5,
    "name": "string"
  } 
    }'\'''

curl -X 'POST' \
  'https://petstore.swagger.io/v2/user/createWithList' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d ''\''{ "id": 23,

    }'\'''