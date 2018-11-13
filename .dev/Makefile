make_env:
	sudo apt-get -y update; \
	sudo apt-get -y dist-upgrade; \
	sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
	libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
	xz-utils tk-dev; \
	sudo apt-get -y install python3.6; \
	sudo apt-get -y install apt-transport-https \
    						ca-certificates \
    						curl \
    						software-properties-common; \
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -; \
	sudo apt-key fingerprint 0EBFCD88; \
	sudo add-apt-repository \
   		"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   		$$(lsb_release -cs) \
   		stable"; \
	sudo apt-get -y update; \
	sudo apt-get -y install docker-ce; \
	sudo apt-get -y install postgresql postgresql-contrib; \
	sudo apt-get -y install zsh; \
	chsh -s `which zsh`; \
	init 6

make_oh_my_zsh:
	sudo apt -y install git; \
	curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh
	exit

make_pyenv:
	curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash; \
	echo 'export PATH=$$HOME/.pyenv/bin:$$PATH' >> ~/.zshrc; \
	echo 'eval "$$(pyenv init -)"' >> ~/.zshrc; \
	echo 'eval "$$(pyenv virtualenv-init -)"' >> ~/.zshrc; \
	exit

workspace_pyenv_get_version:
	pyenv install 3.6.6; \
	pyenv global 3.6.6; \

workspace_make_path:
	echo 'PATH=$$PATH:$(shell pwd)/bin' >> ~/.zshrc

workspace_make_aws_config:
	mkdir ~/.aws; \
	cp -f ./config ~/.aws/config
	cp -f ./credential ~/.aws/credential
