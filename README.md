# Merchant Competition Scraper


## Getting Started


### Prerequisites

Check the package.json files for start scripts and dependencies. For this project, you just need two commands:

```
npm install
```

If NPM does not work, you can try using [YARN](https://yarnpkg.com) and running:

```
yarn install
```

This will install all the dependencies defined in the package.json file



## Development/Production

### Access


### Docker


#### Dockerfile and Docker-Compose

I follow this person's pattern on creating the development instance: https://github.com/nezhar/wordpress-docker-compose

The [docker-compose.yml](docker-compose.yml) file contains the settings I used, some notes:
* For the wp-data folder, I used a db dump sql file from https://damcms.roidna.com** to seed the development's MySQL instance
* For the wp-app folder, I already created a docker image of the damcms instance and should already populate with preinstalled themes and plugins

#### Gotchas
* WP Migrate DB will allow a smoother transition, the plugin will find and replace URLs and File Paths
* The following commands will help with the file permissions, there are easier ways to automate, but I was fed up with my shell scrips not running inside the docker containers

```
sudo chmod -R 777 wp-content #Fixes permission outside of docker container
```
```
docker exec -t -i my_instance_name /bin/bash; #Access docker container
usermod -u 1000 www-data #Give RW access to user 1000
```

## Deployment


## Running the tests
Tests are written for JEST and Enzyme
```
yarn test
```
```
npm run test
```


## Styling Guide
Airbnb Javascript style guide utilized - https://github.com/airbnb/javascript

## Built With
* [React](https://reactjs.org/) - A JavaScript library for building user interfaces
* [NodeJS](https://nodejs.org/en/) - JavaScript networking and package management
* [Docker](https://www.docker.com/) - Cloud container technology used for building and shipping applications
* [PM2](http://pm2.keymetrics.io/) - A Complete feature set for production environment, built with a worldwide community of developers and enterprises
* [Semantic UI](https://react.semantic-ui.com) - UI Framework built with React components
* [WP-API](https://github.com/WP-API/node-wpapi) - A NodeJS library used to interact with Wordpress REST API

## Troubleshooting
There is some caching weirdness that Wordpress utlizies that messes with CORS, simply perform a hard reload and clear cache.
<p align='center'>
    <img src='https://i.imgur.com/IiRI6In.png'>
</p>
<p align='center'>
    <em>Chrome</em>
</p>

## To Do
* Complete Pages link
* Save stitched picture to Express backend and then save to Wordpress CMS
* Enable Watchtower to listen for any new docker images
* Unit testing for Wordpress instance

## Authors
* **Evan Chen** - *Initial work* - [evanchen7](https://github.com/evanchen7)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Original SASS/SCSS by ROI-DNA [ROI-DNA](https://www.roidna.com/)