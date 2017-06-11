# cucco-api

Oh, [cucco](https://github.com/davidmogar/cucco). Such a great friend! That little chicken know how to do its job, right?

The only problem is that it's hard to have the patience to tame it. And here is where this project comes handy. This simple library will connect users with an efficient cucco so everybody can normalize their texts easily.

## You're intriguing me and I wish to know a bit more...

Sure! :chicken:

This API exposes every single cucco normalization function so you can reach it easy. Three endpoints categories can be found:

* **common**: Available to any user.
* **private**: Endpoints requiring authentication.
* **public**: Unauthenticated rate limited endpoints.

## What the heck is an endpoint?

An endpoint is a route to which you can send a request. The next sections show all the routes exposed by cucco-api grouped by category.

### Common
| Endpoint                | Method    | Rate limit          | Authentication |
| ----------------------- |:---------:| ------------------- |:--------------:|
| api/status              | GET       |                     |                |

### Private

| Endpoint                | Method    | Rate limit          | Authentication |
| ----------------------- |:---------:| ------------------- |:--------------:|
| api/private/accents     | GET, POST |                     | Yes            |
| api/private/characters  | GET, POST |                     | Yes            |
| api/private/emails      | GET, POST |                     | Yes            |
| api/private/emojis      | GET, POST |                     | Yes            |
| api/private/hyphens     | GET, POST |                     | Yes            |
| api/private/normalize   | GET, POST |                     | Yes            |
| api/private/punctuation | GET, POST |                     | Yes            |
| api/private/stopwords   | GET, POST |                     | Yes            |
| api/private/symbols     | GET, POST |                     | Yes            |
| api/private/urls        | GET, POST |                     | Yes            |
| api/private/whitespaces | GET, POST |                     | Yes            |

### Public

| Endpoint                | Method    | Rate limit          | Authentication |
| ----------------------- |:---------:| ------------------- |:--------------:|
| api/public/accents      | GET, POST | 30 request per hour | No             |
| api/public/characters   | GET, POST | 30 request per hour | No             |
| api/public/emails       | GET, POST | 30 request per hour | No             |
| api/public/emojis       | GET, POST | 30 request per hour | No             |
| api/public/hyphens      | GET, POST | 30 request per hour | No             |
| api/public/normalize    | GET, POST | 10 request per hour | No             |
| api/public/punctuation  | GET, POST | 30 request per hour | No             |
| api/public/stopwords    | GET, POST | 10 request per hour | No             |
| api/public/symbols      | GET, POST | 30 request per hour | No             |
| api/public/urls         | GET, POST | 30 request per hour | No             |
| api/public/whitespaces  | GET, POST | 30 request per hour | No             |

### Cucco allows to personalize the normalizations. Can I do the same with the API?

As a matter of fact yes, you can. The API admits the same parameters that cucco admit so the way to use it is really similar.

To know more about how to use the API you can visit [documentation.cucco.io](documentation.cucco.io).
