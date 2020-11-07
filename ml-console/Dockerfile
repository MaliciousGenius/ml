FROM ubuntu:latest

# apt conf
ENV DEBIAN_FRONTEND=noninteractive

# apt update & upgrade
RUN apt update --quiet ; \
    apt upgrade --quiet --yes ;

# configure deb-backend
RUN echo "debconf debconf/frontend select noninteractive" | debconf-set-selections ; \
    dpkg-reconfigure --frontend=noninteractive debconf ; \
    # do not exclude man pages & other documentation
    rm /etc/dpkg/dpkg.cfg.d/excludes ;

# install some the packages to full system provision
RUN apt install --quiet --yes --no-install-recommends \
        ca-certificates \
        apt-transport-https \
        software-properties-common \
        apt-utils \
        gnupg ;

# locale
RUN apt install --quiet --yes --no-install-recommends \
        locales language-pack-ru-base ;
ENV LANG="ru_RU.UTF-8" \
    LANGUAGE="ru_RU.UTF-8" \
    LC_ALL="ru_RU.UTF-8" \
    LC_CTYPE="ru_RU.UTF-8"
RUN sed -i "s/^[^#]*ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/g" /etc/locale.gen ; \
    sed -i "s/^[^#]*en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/g" /etc/locale.gen ; \
    echo $LANGUAGE >> /etc/default/locale ; \
    echo $LC_ALL >> /etc/default/locale ; \
    locale-gen ; \
    update-locale LANG=$LANG LC_ALL=$LC_ALL LANGUAGE=$LANGUAGE ; \
    dpkg-reconfigure --frontend=noninteractive locales ;

# time
RUN apt install --quiet --yes --no-install-recommends \
        tzdata ;
ENV TIMEZONE="Europe/Moscow"
RUN echo $TIMEZONE > /etc/timezone ; \
    ln -sf /usr/share/zoneinfo/$TIMEZONE /etc/localtime ; \
    dpkg-reconfigure --frontend=noninteractive tzdata ;

# python 3
RUN apt install --quiet --yes --no-install-recommends \
        python3-minimal python3 python3-dev python3-doc python3-examples ;

# tools
RUN apt install --quiet --yes --no-install-recommends \
        bash bash-completion \
        curl wget \
        tar unzip bzip2 xz-utils \
        make \
        inetutils-ping \
        ansible ;

# utils
RUN apt install --quiet --yes --no-install-recommends \
        mc htop iotop \
        clickhouse-client kafkacat ;

# clearnup apt
RUN apt autoremove --yes ; \
    apt clean ; \
    rm -rf /var/lib/apt/lists/* ;
