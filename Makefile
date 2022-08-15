IMAGE ?= "simpleapp:0.5"

app/setup-venv:
	@echo '+ Setting up venv'
	@python3 -m venv venv
	@. ./venv/bin/activate && pip install -r requirements.txt
	# @. ./venv/bin/activate && flask run
	
app/build-docker:
	@echo '+ Building docker image $(IMAGE)'
	@docker build . -t $(IMAGE)

app/run-docker: app/build-docker
	@echo '+ Running docker image on port 5000'
	@docker run -it -p5000:5000 $(IMAGE)