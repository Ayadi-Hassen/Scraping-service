
# Facebook Scraping service

Scrape Facebook public pages


## Instalation

Clone the project

```bash
  git clone https://github.com/Ayadi-Hassen/Scraping-service

```
Go to the project directory

```bash
  cd Scraping-service
```

Run project using Docker

```bash
  docker-compose up
```


## API Reference

#### Collect facebook posts

```http
  POST /fb/posts
```
Request Body
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `page_name` | `string` | **Required**. Name of the facebook page  |
| `pages` | `integer` | **Required**. Number of pages to scrap |

Collected posts will be saved in mongodb database

## Run Locally

Clone the project

```bash
  git clone https://github.com/Ayadi-Hassen/Scraping-service

```

Go to the project directory

```bash
  cd Scraping-service
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
```


## Running Tests

To run tests, run the following command

```bash
  pytest
```


## Want to help
If you like this application, please star this repository.

If you create an app using this application, please mention this repository.

If you want to contribute to this application, feel free to create a pull request.
## Authors

- [@hassenayadi](https://github.com/Ayadi-Hassen)
- [LinkedIn](https://www.linkedin.com/in/hassen-ayadi-8534661ba/)

