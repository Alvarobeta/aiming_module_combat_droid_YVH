# The exercise

Create an endpoint that will send a POST request to /radar with the information about its surroundings. The module about to develop must return which are the visible target's coordinates that must be attacked.

An example body would be: `{"protocols":["avoid-mech"], "scan":[{"coordinates":{"x":0,"y":40},"enemies":{"type":"soldier","number":10}}]}`

- protocols: Protocol or list of protocols to be used to determine which of the following points should be attacked first.
- scan: List of points extracted from the vision module, which is an array of points with the number of targets of that position, and the following subvalues:
  - coordinates: `x` and `y` coordinates of the point.
  - enemies: Enemy `type` and number `number`. The possible values of type will be: `soldier` and `mech`.

  - (optional) allies : Number of allies in that position. If this value is not present, means that there are no allies in the area.

The response must contain the `x` and `y` coordinates of the next point to destroy.
An example of a response body for the above example would be: `{"x":0, "y":40}`
That way, our combat droid YVH would know which item to destroy next.
To determine which is the next item to destroy, we must take into account which are the requested protocols, and act according to their rules. protocols requested, and act according to their rules.

## Available protocols

- closest-enemies: The closest point where there are enemies should be prioritized.
- furthest-enemies: The furthest point where there are enemies should be prioritized.
- assist-allies: Priority should be given to the points where there is an ally.
- avoid-crossfire: No point where there is an ally should be attacked.
- prioritize-mech: A mech should be attacked if found. If not, any other type of target will be valid.
- avoid-mech: No mech type enemy should be attacked.

It is important to note that several protocols may be provided in the request. As an example, if received the `closest-enemies` and `assist-allies protocols`, we should look for the closest point that has allies present.
In any case, protocols compatible with each other will be provided. It can't be assumed that the module will receive, for example, `closest-enemies` and `furthest-enemies` protocols in the same request.
Finally, it is important to note that targets at a distance of more than 100m are considered too far away to be attacked and should therefore be ignored.

# Getting started

## Prerequisites
- [Docker](https://docs.docker.com/docker-for-mac/install/) 
- [Docker Compose](https://docs.docker.com/compose/) 
- make command

## How to run the app
```bash
make up
```
This command will expose the app under `http://localhost:8888/`

In the URL `http://localhost:8888/docs` you have a Swagger UI with the API documentation. There you'll have a link with the OpenAPI in json format.

In the URL `http://localhost:8888/redoc` you have a [ReDoc](https://github.com/Redocly/redoc) living.

And of course, under `http://localhost:8888/radar` it's the required endpoint 😀.

## How run the tests

```bash
make tests
```

## How to run the configured linters
```bash
make lint
```

## How to autoformat the code
```bash
make format
```
