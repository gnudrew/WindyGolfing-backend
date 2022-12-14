# Windy Golfing
This project demonstrates a data-intensive RESTful web application managing an asynchronous, distributed computation cluster, built around a Monte Carlo simulation that seeks to quantify agent skill at hitting a target within a dynamical system. In this case, the agents are golfers and the dynamical system is the wind. The wind's speed and direction can vary over time based on the wind generator model used, thus setting the golfing environment. For example, wind generators can include a perfectly calm day (no wind), wind that oscillates predictably, and wind whose velocity evolves chaotically as modeled by a Lorenz attractor (https://en.wikipedia.org/wiki/Lorenz_system). Golfer skill is modeled by probability functions that determine swing timing as well as initial velocity delivered to the ball. For a given skill function, swings are sampled many times to establish a distribution of ball trajectories with golfer performance measured by the resulting distribution of ball distance from the final target.

## The stack
* **Database**: *Postgres* (as the RDB), *Azure Blob Storage* (to hold sim data), *RabbitMQ* (task broker), *Redis* (task result backend & cacheing)
* **Monte Carlo simulation**: built with *numpy* and *pandas* in a *Jupyter* sandbox 
* **Backend**: *Django Rest Framework* (web API) and *Celery* (for asynchronous, distributed tasks ... mainly simulator trials)
* **Frontend**: *Vue.js* with *TailwindCSS*
* **Visualization**: *Highcharts*

