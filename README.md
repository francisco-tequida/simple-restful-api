
# Running project locally
```
> git clone git@github.com:francisco-tequida/simple-restful-api.git
> cd simple-restful-api
> docker-compose up -d --build
```
**Note:** Some files (like entrypoint.sh) might need to change EOL from CRLF to LF to run properly on Windows environments. Linux environments may require to add exec mode to some files (like entrypoint.sh, :( chmod +x entrypoint.sh)

# User types and restrictions
The *admin* users can create/update/delete/retrive other users or admins and can create/update/delete/retrive products as well. The following data is valid for an admin user.
```
username: admin
password: admin
```

*Registered* users can only retrive information from products. The following data is valid for a registered user.

```
username: user
password: user
```

Non registered users or *anonymous* users can request paths as **/api/products/** and **/api/products/\<slug\>/**

# Documentation
This project implements the [OpenAPI](https://spec.openapis.org/oas/v3.1.0) specification via [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/). You can find it by navigating to http://127.0.0.1:8000/swagger on your browser once the project is running.

# Testing API
Inside *tests* folder you will find the [Postman](https://www.postman.com/) [collection](https://www.postman.com/collection/) and [environment](https://learning.postman.com/docs/sending-requests/managing-environments/) used to test this API.

Most paths require [Bearer](https://swagger.io/docs/specification/authentication/bearer-authentication/) authorization. You can get a JWT token by querying to **/api/token/** with a valid username/password as the ones mentioned in the **User types and restrictions** section.

# Containerization
Both, **API** and **BD** run as services, so, docker compose is recommended. 

# Notification system
This project uses [**SendGrid**](https://sendgrid.com/) as notification system.

> You need to create an [**API KEY**](https://docs.sendgrid.com/ui/account-and-settings/api-keys) and add it to the env variables.

> You need a [**Verified Sender Address**](https://docs.sendgrid.com/ui/sending-email/senders) and add it to the env variables.

> You need a [**Dynamic Template ID**](https://docs.sendgrid.com/ui/sending-email/how-to-send-an-email-with-dynamic-transactional-templates) and add it to the env variables. The minimum variables expected to be found inside the templeta are: *prev_sku*, *curr_sku*, *prev_name*, *curr_name*, *prev_price*, *curr_price*, *prev_brand*, *curr_brand*

# Proposal for the future
> We can break the monolithic application into services. Each application would be a service.

> From every service we can create an image and upload it to a cloud image registry.

> From every image we could create a kubernetes service loadbalancing the total amount of requests.
