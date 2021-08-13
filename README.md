# turbo_fast_app
FourthBrain's AI/MLE May 2021 Cohort - FastAPI backend for turbofan engine failure app

# Run FastAPI on Docker
1. Install Docker on your machine: [Get Docker](https://docs.docker.com/get-docker/])
2. Build a docker image specified in this repo. First go to root of repo `/turbofan_fast_app` and run command: `docker build . -t turbofan_be`. Replace `turbofan_be` with any tag you would like.
3. To run the FastAPI server, run this command: `docker run --name turbo_fast -p 80:80 turbofan_be`. Note `turbo_fast` is the name of the docker image and `turbofan_be` is the container's tag from step 2.
4. See more docker runtime options here: [FastAPI Docker](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)
