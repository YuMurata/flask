FROM centos:centos7
ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
RUN yum update -y && \
    yum install -y gcc zlib-devel bzip2 bzip2-devel readline readline-devel sqlite sqlite-devel openssl openssl-devel git libffi-devel && \
    curl https://bootstrap.pypa.io/get-pip.py | python && \
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc