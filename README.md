# Antonio Portillo's explanation of how to test the service

## Installation and deployment
After downloading the repository, we place ourselves from our terminal in the folder where the Dockerfile is located and 
then use the following commands.
- docker build -t fever .
- docker run -d --name fever -p 8080:8080 fever:latest
- After deploying the service in a docker container, from any browser. Access from this url to the service, in order to test it from OpenApi/Swagger.
- http://localhost:8080/docs#

## Explanation of design decision making
Python is used to design the solution for this service, but in a typed way, in order to better define the interfaces and to better see the response and input between layers.

The hexagonal architecture, better defined as port and adapters, has been used. In order to be able to use the FastAPI library completely decoupled from our interactors/use cases.

I have defined domain entities and value objects in order to be able to represent the business concepts defined in the technical test. This facilitates the understanding between the business and the technical part, and to be able to validate all the primitives that can be used in the service.

The repository pattern has been used to abstract from the provider data format and to be able to use whatever library or tool is necessary for it. In the same way that it has been used to be able to abstract from where event data is persisted, from previous calls.

In short, TDD has been used for the design of the main interactor/use case. DDD has been used for the definition of domain entities, domain services and other artefacts in this bound context. And port and adapters to completely decouple our infrastructure layer (FastApi, Json File, Aiohttp, etc), from our application and domain layer.

I have opted for FastApi for API exposure, because of the easy integration with typing, the easy exposure of OpenApi and the easy use of dependency inversion.

In order to explain everything in much more detail and to be able to answer any questions you may have. We can have a call to discuss design and implementation with me at any time.

I have worked in many teams applying devops philosophy. I have prepared a Dockerfile to prepare the image with everything needed automatically, in order to be able to deploy it in a Docker container. I have chosen this, instead of using a makefile, because although I know the tool, it is quite old. I'm more comfortable doing it this way, and I think you'll find it just as easy.

In order to test the endpoint, I have made sure that the formats of the two query parameters have the format indicated in the example swagger. It is necessary to use this format "2017-07-21T17:32:28Z", as the interactor validates that the data type is correct.

# Fever code challenge

Hello! Glad you are on this step of the process. We would like to see how you are doing while coding and this exercise
tries to be a simplified example of something we do on our daily basis.

At Fever we work to bring experiences to people. We have a marketplace of events from different providers that are
curated and then consumed by multiple applications. We work hard to expand the range of experiences we offer to our customers.
Consequently, we are continuosly looking for new providers with great events to integrate in our platforms. 
In this challenge, you will have to set up a simple integration with one of those providers to offer new events to our users.

Even if this is just a disposable test, imagine when coding that somebody will pick up this code an maintain it on
the future. It will be evolved, adding new features, adapting existent ones, or even removing unnecessary functionalities.
So this should be conceived as a long term project, not just one-off code.

## Evaluation
We will value the solution as a whole, but some points that we must special attention are:
- How the proposed solution matches the given problem.
- Code style.
- Consistency across the codebase.
- Software architecture proposed to solve the problem.
- Documentation about decisions you made.

## Tooling
- Use Python 3 unless something different has been told.
- You can use any library, framework or tool that you think are the best for the job.
- To provide your code, use the master branch of this repository.

## Description
We have an external provider that gives us some events from their company, and we want to integrate them on the Fever
marketplace, in order to do that, we are developing this microservice.

##### External provider service
The provider will have one endpoint:

https://provider.code-challenge.feverup.com/api/events

Where they will give us their list of events on XML. Every time we fetch the events,
the endpoint will give us the current events available on their side. Here we provide some examples of three different
calls to that endpoint on three different consecutive moments.

Response 1
https://gist.githubusercontent.com/sergio-nespral/82879974d30ddbdc47989c34c8b2b5ed/raw/44785ca73a62694583eb3efa0757db3c1e5292b1/response_1.xml

Response 2
https://gist.githubusercontent.com/sergio-nespral/82879974d30ddbdc47989c34c8b2b5ed/raw/44785ca73a62694583eb3efa0757db3c1e5292b1/response_2.xml

Response 3
https://gist.githubusercontent.com/sergio-nespral/82879974d30ddbdc47989c34c8b2b5ed/raw/44785ca73a62694583eb3efa0757db3c1e5292b1/response_3.xml

As you can see, the events that aren't available anymore aren't shown on their API anymore.

##### What we need to develop
Our mission is to develop and expose just one endpoint, and should respect the following Open API spec, with
the formatted and normalized data from the external provider:
https://app.swaggerhub.com/apis-docs/luis-pintado-feverup/backend-test/1.0.0

This endpoint should accept a "starts_at" and "ends_at" param, and return only the events within this time range.
- We should only receive the available events (the sell mode is online, the rest should be ignored)
- We should be able to request this endpoint and get events from the past (events that came in previous API calls to the provider service since we have the app running) and the future.
- The endpoint should be fast in hundred of ms magnitude order, regardless of the state of other external services. For instance, if the external provider service is down, our search endpoint should still work as usual.

Example: If we deploy our application on 2021-02-01, and we request the events from 2021-02-01 to 2022-07-03, we should
see in our endpoint the events 291, 322 and 1591 with their latest known values. 

## Requirements
- The service should be as resource and time efficient as possible.
- The Open API specification should be respected.
- Use PEP8 guidelines for the formatting
- Add a README file that includes any considerations or important decision you made.
- If able, add a Makefile with a target named `run` that will do everything that is needed to run the application.

## The extra mile
With the mentioned above we can have a pretty solid application. Still we would like to know your opinion, either 
directly coded (if you want to invest the time) or explained on a README file about how to scale this application
to focus on performance. The examples are small for the sake of the test, but imagine that those files contains
thousands of events with hundreds of zones each. Also consider, that this endpoint developed by us, will have peaks
of traffic between 5k/10k request per second.

## Feedback
If you have any questions about the test you can contact us, we will try to reply as soon as possible.

In Fever, we really appreciate your interest and time. We are constantly looking for ways to improve our selection processes,
our code challenges and how we evaluate them. Hence, we would like to ask you to fill the following (very short) form:

https://forms.gle/6NdDApby6p3hHsWp8

Thank you very much for participating!